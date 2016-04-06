#!/usr/bin/python
# Acts like rpm -qi and lists the information of the installed package.
# Usage:
# python rpminfoparser.py
import sys
import ConfigParser
import io
import rpminfo


def read(package):
    result = rpminfo.query_info(package)
    if result is not None:
        return parse(result)


def parse(info):
    config = ConfigParser.RawConfigParser(allow_no_value=True)

    try:
        config.readfp(io.BytesIO(info))
        return as_dict(config)
    except AttributeError:
        return None


def as_dict(config):
    """
    Converts a ConfigParser object into a dictionary.
    """
    rpm_dict = {}
    description_found = False

    for section in config.sections():
        for key, val in config.items(section):
            if key != 'description':
                # version is internal elasticsearch field
                if key == 'version':
                    rpm_dict['app_version'] = val
                elif val is not None:
                    rpm_dict[key] = val
            else:
                description_found = True
            if description_found is True:
                # the key is the description value
                # put the description value into description
                rpm_dict['description'] = key

    return rpm_dict


if __name__ == '__main__':
    result = rpminfo.query_info(sys.argv[1])
    info = parse(result)
    if info is not None:
        dictionary = info.items()
        if dictionary is not None:
            for k, v in dictionary:
                print 'key=' + k + "/value:" + str(v)
