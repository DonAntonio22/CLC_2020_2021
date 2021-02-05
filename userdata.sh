#!/bin/bash

# Abort on all errors
set -e

# This is not production grade, but for the sake of brevity we are using it like this.
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Run the load generator
docker run -d \
  --restart=always \
  -p 8080:8080 \
  janoszen/http-load-generator:1.0.1

# Run the node exporter
docker run -d \
  --restart=always \
  --net="host" \
  --pid="host" \
  -v "/:/host:ro,rslave" \
  quay.io/prometheus/node-exporter \
  --path.rootfs=/host

