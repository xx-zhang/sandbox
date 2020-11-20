# CAPE - Config And Payload Extraction
# Copyright(C) 2019 Kevin O'Reilly (kevoreilly@gmail.com)
# See the file 'docs/LICENSE' for copying permission.

from __future__ import absolute_import
import os
import shutil

from lib.common.abstracts import Package

class Emotet(Package):
    """Emotet analysis package."""

    # PATHS = [
    #    ("SystemRoot", "system32"),
    # ]

    def __init__(self, options={}, config=None):
        """@param options: options dict."""
        self.config = config
        self.options = options
        self.pids = []
        self.options["unpacker"] = "1"
        self.options["injection"] = "0"

        # This depends on Emotet trends
        # so may vary or be removed
        if self.config.timeout > 10:
            self.config.timeout = 10

    def start(self, path):
        arguments = self.options.get("arguments")

        # If the file doesn't have an extension, add .exe
        # See CWinApp::SetCurrentHandles(), it will throw
        # an exception that will crash the app if it does
        # not find an extension on the main exe's filename
        if "." not in os.path.basename(path):
            new_path = path + ".exe"
            os.rename(path, new_path)
            path = new_path

        return self.execute(path, arguments, path)
