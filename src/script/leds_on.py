#!/usr/bin/python
import time
import sys

files = ["/dev/rtled0", "/dev/rtled1", "/dev/rtled2", "/dev/rtled3"]

for filename in files:
        with open(filename, 'w') as f:
            f.write("1")
