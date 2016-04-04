#!/usr/bin/python
# reports to elasticsearch information about installed packages
# Usage:
# python es-reporter.py
import sys
import rpmglob
import rpminfo


def process(installedPackages):
    for p in installedPackages:
        rpminfo.queryInfo(p)

if __name__ == '__main__':
    installed = rpmglob.query_glob(sys.argv[1])
    process(installed)
