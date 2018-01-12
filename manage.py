#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

    from django.core.management.commands import runserver
    runserver.Command.default_port = "8220"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
