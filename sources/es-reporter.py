#!/usr/bin/python
# reports to elasticsearch information about installed packages
# Usage:
# python es-reporter.py
import sys
import rpmglob
import rpminfoparser
import json
import subprocess


def process(installed_packages):
    if installed_packages is not None:
        for p in installed_packages:
            # print p
            # if str(p).startswith('six-splunkforwarder') is not True:
            dictionary = rpminfoparser.read(p)
            if dictionary is not None:
                dictionary['environment'] = 'dev'
                json_string = encode_json(dictionary)
                send_to_elasticsearch(json_string, str(dictionary['name']))


def encode_json(dictionary):
    return json.dumps(dictionary)


def send_to_elasticsearch(jsondata, id):
    index = 'foha'
    doc_type = 'rpm'
    url = 'fo-dev:9200/' + index + '/' + doc_type + '/' + id
    subprocess.call(['curl -XPUT \'' + url + '\' -d \'' + jsondata + '\''],
                    shell=True)


if __name__ == '__main__':
    installed = rpmglob.query_glob(sys.argv[1])
    process(installed)
