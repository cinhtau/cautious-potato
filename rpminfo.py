#!/usr/bin/python
# Acts like rpm -qi and lists the information of the installed package.
# Usage:
# python rpminfo.py
import sys
import subprocess


def queryInfo(package):
    result = '[info]\n' + subprocess.check_output(['rpm', '--query', '--info', package])
    return result

if __name__ == '__main__':
    print queryInfo(sys.argv[1])
