#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
	print "Please enter two numbers to find their GCF"
	exit(1)

num1 = sys.argv[1]
num2 = sys.argv[2]
print gcf(num1, num2)
