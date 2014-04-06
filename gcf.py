#!/usr/bin/env python

import sys
import math

if len(sys.argv) < 3:
  print "Please enter two numbers to find their GCF"
  exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

def gcf(num1, num2):
  # Sadie said to find prime factors
  num1_pfs = find_prime_factors(num1)
 #print "PFs for num1 = ", num1_pfs
  num2_pfs = find_prime_factors(num2)
 #print "PFs for num2 = ", num2_pfs

  # She then said to find their common factors
  cfs = find_common_factors(num1_pfs, num2_pfs)
 #print "CFs num2 = ", cfs

  # And then finally multiply the common factors
  return multiply_common_factors(cfs)

def is_prime(num):
  if num in [2,3]:
    return True
  max_num = int(math.ceil(math.sqrt(num)))
  #print "Max of %i for %i" % (max_num, num)
  for n in range(2,max_num+1):
    #print "Checking if %i divides %i" % (n, num)
    if num % n == 0:
      #print "returning False"
      return False
  #print "returning True"
  return True

def find_prime_factors(num):
  pfs = []
  n = 2
  while num > 1:
    if num % n != 0:
      n += 1
      continue
    if is_prime(n):
      #print "%i is prime" % n
      pfs.append(n)
      num = num / n
      n = 2
   #print "num = ", num, ", n = ", n
  return pfs

def find_common_factors(num1_pfs, num2_pfs):
  cfs = []
  # Loop trough prime factors of num1.  If num_pfs has that
  # prime factor, then it's common
  for n in num1_pfs:
    for i in range(0,len(num2_pfs)):
      if n == num2_pfs[i]:
        cfs.append(n)
        #  I need to get rid of this common factor, so i'll just set it to 1
        num2_pfs[i] = 1
  return cfs

def multiply_common_factors(cfs):
  total = 1
  for n in cfs:
    total = total * n
  return total

print gcf(num1, num2)


# vim: ts=2 expandtab sw=2 sts=2
