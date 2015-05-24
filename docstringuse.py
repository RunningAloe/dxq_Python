#!/usr/bin/python
#Filename:docstringuse.py
def MaxN(a,b):
	'''This is a function that print a bigger number.

	a and b must be integers.'''
	if (a>b):
		print a
	else:
		print b
MaxN(1,2)
print MaxN.__doc__
help(MaxN)
pydoc MaxN
