import ConfigParser
import io
import rpminfo

def parse(info):
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(info))
    return as_dict(config)

def as_dict(config):
    """
    Converts a ConfigParser object into a dictionary.
    """
    dict = {}
    for section in config.sections():
        for key, val in config.items(section):
            dict[key]= val
    return dict

if __name__ == '__main__':
    result = rpminfo.queryInfo('hello_world-1.0.0-1')
    for k, v in parse(result).items():
        print 'key='+ k +"/value:" + str(v)
