#!/usr/bin/python

import optparse
import sys
import yaml
import os
from subprocess import call


USAGE = """%prog CONFIG_PATH
Run isolated tests as docker containers.
CONFIG_PATH    Path to the yaml file of docker containers to run."""

def main(config_path):
  print config_path
  fail = False
  with open(config_path, 'r') as stream:
    config = yaml.load(stream)
    print config
    for test in config['tests']:
      build = "docker build -t {} {}".format(test['name'], test['dockerfile_path'])
      print build
      os.system(build)
      command = "docker run"
      if 'entrypoint' in test:
        command = "{} -ti --entrypoint={}".format(command, test['entrypoint'])
      command = "{} {} -s".format(command, test['name'])
      print command
      # try:
      exit_status = os.system(command)
      print "exit status {}".format(exit_status)
      if exit_status != 0:
        fail = True
        if 'fail' in config:
          os.system(config['fail']['script'])
          break
        else:
          print "TESTS FAILED at {}".format(test['name'])
          break
    if 'success' in config and fail == False:
      os.system(config['success']['script'])
      return
  return

if __name__ == '__main__':
  sys.dont_write_bytecode = True
  parser = optparse.OptionParser(USAGE)
  options, args = parser.parse_args()
  if len(args) < 1:
    print 'Error: At least 1 argument required.'
    parser.print_help()
    sys.exit(1)
  CONFIG_PATH = args[0]
  main(CONFIG_PATH)