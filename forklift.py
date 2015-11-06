#!/usr/bin/python

import optparse
import sys
import yaml
import os
from subprocess import call


USAGE = """%prog DOCKER_PATH
Run isolated tests as docker containers.
DOCKER_PATH    Path to the yaml file of docker containers to run."""

def main(docker_path):
  print docker_path
  with open(docker_path, 'r') as stream:
    config = yaml.load(stream)
    print config
    for test in config:
      build = "docker build -t {} {}".format(test['name'], test['dockerfile_path'])
      print build
      os.system(build)
      command = "docker run"
      if 'entrypoint' in test:
        command = "{} -ti --entrypoint={}".format(command, test['entrypoint'])
      command = "{} {} -s".format(command, test['name'])
      print command
      os.system(command)
  pass

if __name__ == '__main__':
  sys.dont_write_bytecode = True
  parser = optparse.OptionParser(USAGE)
  options, args = parser.parse_args()
  if len(args) < 1:
    print 'Error: At least 1 arguments required.'
    parser.print_help()
    sys.exit(1)
  DOCKER_PATH = args[0]
  main(DOCKER_PATH)