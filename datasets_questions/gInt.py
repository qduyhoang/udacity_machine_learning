#!/usr/bin/env python3

#Name: Duy Hoang
#Id: dqh23
#gInt.py - Gaussian integer class(numbers of the form a + bi, where a & b are integers)## Python 3.5 .2, on# 4.13 .0 - 38 - generic GNU / Linux#
class gInt:
	"""Gaussian integer.  Numbers of the form a+bi, where a & b are integers.'
	"""
	def __init__(self, a, b = 0):
		"""'Creates a gInt of the form a+bi'
		''"""   
		self.real = a
		self.imag = b

	# Pre: #-lhs and rhs must be of the same type gInt
	# - rhs must not be Null
	# - return false if preconditions are not met
	# Post: 
	# return true if the real parts and the\# imaginary are both equals# -
	# return false if either the real parts or the\# imaginary parts are not equal

	def __eq__(self, other):
		if not isinstance(self, other.__class__):
			return False
		return self.real == other.real and self.imag == other.imag

	# Post: 
	#-print out the string representation
	# in either of the forms: a + bi and a - bi
	def __str__(self):
		"""Return a string representation"""
		op = '+'
		i = self.imag
		if self.imag < 0:
		    op = '-'
		i = -i

		return '(%d%s%di)' % (self.real, op, i)

	# Pre: 
	#-rhs is of the same type as lhs: gInt
	# - rhs must not be null
	# Post: 
	# -lhs and rhs are unaffected
	# -return a gInt object representing the result\
	# of the addition
	def __add__(self, rhs):
		if not isinstance(self, rhs.__class__):
			raise Exception("Operands must be of type gInt")
		"""Return a new gInt, self + rhs"""
		r = self.real + rhs.real
		i = self.imag + rhs.imag
		return gInt(r, i)

	# Pre: 
	#-rhs is of the same type as lhs: gInt
	# - rhs must not be null
	# Post: 
	# -lhs and rhs are unaffected
	# - return a gInt object representing the result
	# of the multiplication

	def __mul__(self, rhs):
		""""    ''
		'Return a new gInt, self * rhs'
		''"""
		if not isinstance(self, rhs.__class__):
			raise Exception("Operands must be of type gInt")
		r = self.real * rhs.real - self.imag * rhs.imag
		i = self.real * rhs.imag + self.imag * rhs.real
		return gInt(r, i)

	# Post: 
	#-  return an integer representing the# result of the normalization
	def norm(self):
		"""Return real^2 + imag^2 as an int"""
		r = self.real * self.real
		i = self.imag * self.imag
		result = r + i
		return result

def test():
	""""A quick example/test function'"""
	x = gInt(3, -2)
	y = gInt(2, 5)
	z = gInt(13)
	xcopy = gInt(x.real, x.imag)
	if not x == xcopy:
		print("gInt not equal to new copy")
	else :
		print("Equal")

	print("x:", str(x))
	print("y:", str(y))
	print("z:", str(z))
	print("")

	print("norm(x):", x.norm())
	print("norm(y):", y.norm())
	print("norm(z):", z.norm())
	print("")

	print("x + y:", x + y)
	print("x * y:", x * y)
	print("")

	print("x:", str(x))
	print("y:", str(y))
	print("z:", str(z))
	print("")

	print("x + z:", x + z)
	print("x * z:", x * z)
	print("")

	print("y + z:", y + z)
	print("y * z:", y * z)
	print("")

test()