#!/usr/bin/python
# reports to elasticsearch information about installed packages
# Usage:
# python es-reporter.py
import sys
import rpmglob

if __name__ == '__main__':
    rpmglob.query_glob(sys.argv[1])
