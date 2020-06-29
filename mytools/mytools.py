import json
import re
import os
import ipaddress

def read_json_file(filename):
  with open(filename, 'r') as f:
    content = json.load(f)
  return content

def read_json_str(str):
  return json.loads(str)

def valid_ip(ip):
  try:
    ipaddress.ip_address(unicode(ip))
  except ValueError:
    return False
  return True

def split_str(s):
  return re.split(r'\s+', s)

def get_config_dict(config_file):
  '''
  Parse config file like this:
  ---------
  # this is comment
  key1 = value1

  key2 = value2
  ---------
  '''
  d = {}
  with open(config_file, 'r') as f:
    for line in f:
      if line[0] == '#' or line in ('\r\n', '\n'):
        continue
      name, value = line.split('=', 1)
      d[name.strip()] = value.strip()
  return d
