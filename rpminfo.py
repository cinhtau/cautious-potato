#!/usr/bin/python
# Acts like rpm -qi and lists the information of the installed package.
# Usage:
# python rpminfo.py
import sys

from subprocess import call

call(['rpm', '--query', '--info', sys.argv[1]])
