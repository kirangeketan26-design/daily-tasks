#!/usr/bin/env python
"""Django's command-line entry point."""
import os
import sys

if __name__ == "__main__":
    # Tell Django which settings module contains the project configuration.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
