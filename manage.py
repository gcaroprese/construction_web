#!/usr/bin/env python
import sys
import os

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
    execute_from_command_line(sys.argv)
