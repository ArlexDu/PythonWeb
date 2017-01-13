# import logging
# import pdb
# logging.basicConfig(level = logging.INFO)
# def foo(s):
# 	n = int(s)
# 	#assert n!=0, 'n is zero!'
# 	#logging.info('n = %d' % n)
# 	pdb.set_trace()
# 	return 10/n

# def main():
# 	foo('0')

# main()

def fact(n):
	'''

	>>> fact(-1)
	Traceback (most recent call last):
	...
	ValueError

	>>> fact(1)
	1

	>>> fact(3)
	6

	'''
	if n < 1:
		raise ValueError()
	if n == 1:
		return 0
	return n * fact(n-1)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
