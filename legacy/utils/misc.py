import os
import random

def random_num(l,u):
	r = u-l
	if r == 0:
		return 0
	r = int(int.from_bytes(os.urandom(2), byteorder='little')/65536 * (r+1))
	n = l+r
	return n

def rand_pick(a):
	i = random_num(0,len(a)-1)
	return list(a)[i]
