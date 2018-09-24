#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os, sys
title = "Loading"
prog_max = 33

rows, columns = os.popen('stty size', 'r').read().split()
prog_width = int(columns) - 3 - len(title)
prog_width = (prog_max * int(prog_width/prog_max))

# setup toolbar
sys.stdout.write("[%s] %s" % (" " * prog_width, title))
sys.stdout.flush()
sys.stdout.write("\b" * (prog_width + len(title) + 2)) # return to start of line, after '['

for i in xrange(prog_max):
    time.sleep(0.05) # do real work here
    # update the bar
    sys.stdout.write("%s" % ("▉" * int(prog_width/prog_max)))
    sys.stdout.flush()

sys.stdout.write("\n")