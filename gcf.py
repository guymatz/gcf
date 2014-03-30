#!/usr/bin/env python

import sys

if len(sys.argv) < 3:
	print "Please enter two numbers to find their GCF"
	exit(1)

num1 = sys.argv[1]
num2 = sys.argv[2]

def gcf(num1, num2):
	# Sadie said to find prime factors
	num1_pfs = find_prime_factors(num1)
	num2_pfs = find_prime_factors(num2)

        # She then said to find their common factors
	cfs = find_common_factors(num1_pfs, num2_pfs)

	# And then finally multiply the common factors
	return multiply_common_factors(cfs)

def find_prime_factors(num):
	pass

def find_common_factors(num1_pfs, num2_pfs):
	pass

def multiply_common_factors(cfs):
	pass

print gcf(num1, num2)
