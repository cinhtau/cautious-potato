#!/usr/bin/python
# Acts like rpm -qa and lists the names of all the installed packages.
# Usage:
# python rpmqa.py
import rpm

ts = rpm.TransactionSet()
mi = ts.dbMatch()

for h in mi:
    print "%s-%s-%s" % (h['name'], h['version'], h['release'])
