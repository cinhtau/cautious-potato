#!/usr/bin/python
# Acts like rpm -qi and lists the information of the installed package.
# Usage:
# python rpminfo.py
import sys
import subprocess


def query_info(package):
    result = '[info]\n' + subprocess.check_output(['rpm', '--query', '--info', package])
    return result

if __name__ == '__main__':
    print query_info(sys.argv[1])
