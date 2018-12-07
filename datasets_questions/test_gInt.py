#!/usr/bin/env/python3
#test_gInt - the TestCase for gInt
#Name: Duy Hoang
#Id: dqh23

#editor: tabstop=2, cols=120

import sys
import unittest
from gInt import gInt

class gIntTest(unittest.TestCase):
	def setUp( self ):
		self.g1 = gInt(1, 2)
		self.g1copy = gInt(1, 2)
		self.g2 = gInt(-1, 2)
		self.g2copy = gInt(-1, 2)
		self.g3 = gInt(1, -2)
		self.g3copy = gInt(1, -2)
		self.g4 = gInt(1)
		self.g4copy = gInt(1)
		self.notGaussianinteger = 5

	def test_equal( self ):
		self.assertEqual( self.g1, self.g1, "Gaussian integer not equal to itself" )
		self.assertEqual( self.g1, self.g1copy, "Gaussian integer not equal to identical object")
		self.assertEqual( self.g2, self.g2copy, "Gaussian integer not equal to identical object")


		self.assertNotEqual( self.g1, self.g2, "a + 2b == -a + 2b")
		self.assertNotEqual( self.g2, self.g3, "-a + 2b == a - 2b")
		self.assertNotEqual( self.g3, self.g4, "a - 2b == a")

	def test_add( self ):
		r = self.g1 + self.g2

		self.assertEqual( self.g1, self.g1copy, "left operand changes after the operation" )
		self.assertEqual( self.g2, self.g2copy, "right operand changes after the operation" )
		self.assertEqual( r, gInt(0, 4), "addition failed" )
		
		r = self.g2 + self.g3

		self.assertEqual( self.g2, self.g2copy, "left operand changes after the operation" )
		self.assertEqual( self.g3, self.g3copy, "right operand changes after the operation" )
		self.assertEqual( r, gInt(0, 0), "addition resulting in zero failed" )

		r = self.g3 + self.g4

		self.assertEqual( self.g3, self.g3copy, "left operand changes after the operation" )
		self.assertEqual( self.g4, self.g4copy, "right operand changes after the operation" )
		self.assertEqual( r, gInt(2, -2), "addition with a real integer (imaginary part = 0) failed" )

		self.assertRaises( Exception, gInt.__add__, self.g1, self.notGaussianinteger)
		self.assertRaises( Exception, gInt.__add__, self.g1, None)

	def test_mul( self ):
		r = self.g1 * self.g2

		self.assertEqual( self.g1, self.g1copy, "left operand changes after the operation" )
		self.assertEqual( self.g2, self.g2copy, "right operand changes after the operation" )
		self.assertEqual( r, gInt(-5, 0), "multiplication (real part are of opposite signs)failed" )
		
		r = self.g2 * self.g3

		self.assertEqual( self.g2, self.g2copy, "left operand changes after the operation" )
		self.assertEqual( self.g3, self.g3copy, "right operand changes after the operation" )
		self.assertEqual( r, gInt(3, 4), "multiplication (real part of left op is of opposite with that of right op) failed" )

		r = self.g3 * self.g4

		self.assertEqual( self.g3, self.g3copy, "left operand changes after the operation" )
		self.assertEqual( self.g4, self.g4copy, "right operand changes after the operation" )
		self.assertEqual( r, gInt(1, -2), "multiplication with a real integer (imaginary part = 0) failed" )

		self.assertRaises( Exception, gInt.__add__, self.g1, self.notGaussianinteger)
		self.assertRaises( Exception, gInt.__add__, self.g1, None)

	def test_norm( self ):
		self.assertEqual( self.g1, self.g1copy, "original integer changes after the operation" )
		self.assertEqual( self.g2, self.g2copy, "original integer changes after the operation" )
		self.assertEqual( self.g3, self.g3copy, "original integer changes after the operation" )
		self.assertEqual( self.g4, self.g4copy, "original integer changes after the operation" )

		self.assertEqual ( self.g1.norm() , 5, "normalization (both parts are positive) failed")
		self.assertEqual ( self.g2.norm() , 5, "normalization (real part < 0, imaginary part > 0) failed")
		self.assertEqual ( self.g3.norm() , 5, "normalization (real part > 0, imaginary part < 0) failed")
		self.assertEqual ( self.g4.norm() , 1, "normalization (imaginary part = 0) failed")

if __name__ == '__main__':
	sys.argv.append( '-v' )
	unittest.main()

