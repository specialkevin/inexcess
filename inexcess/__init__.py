import os.path
from ConfigParser import SafeConfigParser

def read_config(section):
    parser = SafeConfigParser()
    parser.read(['/etc/inexcess.conf', os.path.expanduser('~/.inexcess.conf'), os.path.expanduser('~/inexcess.conf'), 'inexcess.conf'])
    return parser.items(section)

