#!/usr/bin/env python

import os
from AR import AccuRev, ARWorkspace, ARException

STREAMS_FILE = '/home/user/streams.txt'
ACCUREV_WS_PATH = '/home/user/ar'
ACCUREV_WS_PATTERN = 'opengrok_'
ACCUREV_USER= 'user'
ACCUREV_PWD = 'pass'

ar = AccuRev()
ar.login(ACCUREV_USER, ACCUREV_PWD)

with open(STREAMS_FILE, 'r') as streams_file:
    streams = [s.rstrip() for s in streams_file.readlines()]

for stream in streams:
    print "*"*10 + stream + "*"*10
    try:
        ws = ARWorkspace(ACCUREV_WS_PATTERN + stream)
        ws.update()
    except ARException:
        ws = ARWorkspace()
        ws.name = ACCUREV_WS_PATTERN + stream
        ws.location = os.path.join(ACCUREV_WS_PATH, ACCUREV_WS_PATTERN + stream)
        ws.stream = stream
        ws.create()
        ws = ARWorkspace(ACCUREV_WS_PATTERN + stream)
        ws.update()
