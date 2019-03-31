#!/usr/bin/env bash

echo "${secure}" | docker login --username="${REGISTRY_USER}" --password-stdin
docker push "${REGISTRY_USER}"/"${REPO}":latest