#!/usr/bin/python
# Acts like rpm -qi and lists the information of the installed package.
# Usage:
# python rpminfo.py
import sys

from subprocess import call


def queryInfo(package):
    call(['rpm', '--query', '--info', package])


if __name__ == '__main__':
    queryInfo(sys.argv[1])
