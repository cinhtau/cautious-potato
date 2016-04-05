#!/usr/bin/python
# Acts like rpm -q and lists the N-V-R for installed packages
# that match a given name using a glob-like syntax
#
# Usage:
# python rpmglob.py "package_fragment*"
import rpm
import sys


def query_glob(packagename):
    ts = rpm.TransactionSet()
    mi = ts.dbMatch()
    if not mi:
        print "No packages found."
    else:
        mi.pattern('name', rpm.RPMMIRE_GLOB, packagename)
        stack = []
    for h in mi:
        stack.append("%s-%s-%s" % (h['name'], h['version'], h['release']))
    return stack

if __name__ == '__main__':
    for i in (query_glob(sys.argv[1])):
        print i
