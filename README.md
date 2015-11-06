# Forklift

##Overview

**Forklift** is meant to be a really simple script to both build and run multiple, isolated docker continers as a single CI, and have success and fail hooks.

##Configuration
All configuration happens in a single YAML file

```
tests:
- name: "example/frontend"
  dockerfile_path: "~/path/to/first/dockerfile"
  entrypoint: "/usr/bin/run-build-a"
- name: "example/backend"
  dockerfile_path: "~/path/to/second/dockerfile"
  entrypoint: "/usr/bin/run-build-b"
success:
  script: "/run/on/sucess"
fail
  script: "run/on/fail"
  ```
  
The yaml file is a list of _tests_ with a couple of properties. Each image takes 3 arguments

1. **name** The name of the docker container you want to build and run
2. **dockerfile_path** The path to the dockerfile that configures the image you want to build and run
3. **entrypoint** The entrypoint to the docker container if you want to overwrite the existing entrypoint

Additionally, tou you can configure scripts that execute one both success and failure of the builds

* success: a path to a script to run on success of all docker build and run commands
* fail: a path to a script to run on failure of a single docker build or run command



## Running Forklift
Forklift requires that a connection to your docker VM is in your shell, and that the requisite Docker commands are in your path. For more info on setting this up, check out the [docs](http://docs.docker.com/)

Once that is setup, you can run `python forklift.py path/to/yaml/config/file.yaml`

This should begin building the docker images and running them in containers one by one. The assumption is that the containers will run the tests you need them to.

## Dependencies

* [pyyaml](http://pyyaml.org/)
* Python 2.7 or higher
* [Docker engine](http://docs.docker.com/)







