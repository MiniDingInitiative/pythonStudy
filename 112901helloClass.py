#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from hello import Hello
# import sys,io
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
h = Hello()
h.hello()
print(sys.path)
