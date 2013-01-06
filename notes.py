#!/usr/bin/env python3
import sys

rate = int(sys.argv[1])

for i in range(0,128):
	freq = 440*2**((i-69)/12)
	leng = 0.5 * rate / freq
	print("NOTE(" + str(int(leng+0.5)) + ")")
