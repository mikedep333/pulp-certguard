#!/bin/sh

set -euv

# Aliases for running commands in the pulp-worker container.
# PULP_API_POD comes from before_script.sh
PULP_CONTENT_APP_POD="$(sudo kubectl get pods | grep -E -o "pulp-content-(\w+)-(\w+)")"

CMD_API_PREFIX=$CMD_PREFIX # from before_script.sh
CMD_CONTENT_APP_PREFIX="sudo kubectl exec -i $PULP_CONTENT_APP_POD -- "

$CMD_API_PREFIX bash -c "dnf install openssl-devel -y"
$CMD_CONTENT_APP_PREFIX bash -c "dnf install openssl-devel -y"

$CMD_API_PREFIX bash -c "pip install rhsm"
$CMD_CONTENT_APP_PREFIX bash -c "pip intall rhsm"
