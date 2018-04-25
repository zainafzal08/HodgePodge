import os

def randomNum(l,u):
	r = u-l
	n = l+int(r * (int.from_bytes(os.urandom(2), byteorder='little')/65536))
	return n

def pick(a):
	i = randomNum(0,len(a)-1)
	return a[i]
