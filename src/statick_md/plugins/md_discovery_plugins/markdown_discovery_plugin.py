"""Discover Markdown files to analyze."""

from __future__ import print_function

import fnmatch
import os
from collections import OrderedDict
from typing import List, Optional

from statick_tool.discovery_plugin import DiscoveryPlugin
from statick_tool.exceptions import Exceptions
from statick_tool.package import Package


class MarkdownDiscoveryPlugin(DiscoveryPlugin):  # type: ignore
    """Discover Markdown files to analyze."""

    def get_name(self) -> str:
        """Get name of discovery type."""
        return "markdown"

    def scan(self, package: Package, level: str, exceptions: Optional[Exceptions] = None) -> None:
        """Scan package looking for Markdown files."""
        src_files = []  # type: List[str]

        for root, _, files in os.walk(package.path):
            for f in fnmatch.filter(files, "*.md"):
                full_path = os.path.join(root, f)
                src_files.append(os.path.abspath(full_path))

        src_files = list(OrderedDict.fromkeys(src_files))

        print("  {} markdown files found.".format(len(src_files)))
        if exceptions:
            original_file_count = len(src_files)  # type: int
            src_files = exceptions.filter_file_exceptions_early(package, src_files)
            if original_file_count > len(src_files):
                print(
                    "  After filtering, {} markdown files will be scanned.".format(
                        len(src_files)
                    )
                )

        package["md_src"] = src_files
