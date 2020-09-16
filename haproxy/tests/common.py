# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.dev import get_docker_hostname, get_here

HERE = get_here()
HOST = get_docker_hostname()
ENDPOINT_PROMETHEUS = 'http://{}:8404/metrics'.format(HOST)

INSTANCE = {'use_legacy': False}
