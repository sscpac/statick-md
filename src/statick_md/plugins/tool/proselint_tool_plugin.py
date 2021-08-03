"""Apply proselint tool and gather results.

The output from the tool is collected in JSON format to facilitate parsing.

Website: http://proselint.com/
Github: https://github.com/amperser/proselint
"""
import json
import logging
from typing import Any, Dict, List, Optional
import proselint

from statick_tool.issue import Issue
from statick_tool.package import Package
from statick_tool.tool_plugin import ToolPlugin


class ProselintToolPlugin(ToolPlugin):
    """Apply proselint tool and gather results."""

    def get_name(self) -> str:
        """Get name of tool."""
        return "proselint"

    def scan(self, package: Package, level: str) -> Optional[List[Issue]]:
        """Run tool and gather output."""
        if "md_src" not in package or not package["md_src"]:
            return []

        # Get output in JSON format.
        flags: List[str] = ["--json"]
        flags += self.get_user_flags(level)

        files: List[str] = []
        if "md_src" in package:
            files += package["md_src"]

        # The JSON output does not include the filename so we have to run each file
        # one at a time, and store the output along with the filename in a dictionary.
        # The filename may be added to JSON output in the future:
        # https://github.com/amperser/proselint/issues/355
        output: Dict[str, Any] = {}
        for filename in files:
            with open(filename) as fid:
                errors = proselint.tools.errors_to_json(proselint.tools.lint(fid))
                output[filename] = errors

        for key, value in output.items():
            logging.debug("%s: %s", key, value)

        if self.plugin_context and self.plugin_context.args.output_directory:
            with open(self.get_name() + ".log", "w") as fid:
                for key, value in output.items():
                    combined = key + value
                    fid.write(combined)

        issues: List[Issue] = self.parse_output(output)
        return issues

    def parse_output(self, output: Dict[str, Any]) -> List[Issue]:
        """Parse tool output and report issues."""
        issues: List[Issue] = []
        for key, value in output.items():
            data = json.loads(value)["data"]["errors"]
            for item in data:
                if (
                    "check" not in item
                    or "line" not in item
                    or "message" not in item
                    or "severity" not in item
                ):
                    logging.debug("  Found invalid proselint output: %s", item)
                    continue
                if item["severity"] == "style":
                    warning_level = "1"
                elif item["severity"] == "info":
                    warning_level = "1"
                elif item["severity"] == "warning":
                    warning_level = "3"
                elif item["severity"] == "error":
                    warning_level = "5"
                else:
                    warning_level = "3"

                issue = Issue(
                    key,
                    str(item["line"]),
                    self.get_name(),
                    item["check"],
                    warning_level,
                    item["message"],
                    None,
                )

                issues.append(issue)

        return issues
