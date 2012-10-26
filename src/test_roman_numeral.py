"""
@file test_roman_numeral.py Test Roman Numeral Source File
@name Test Python Roman Numerals
@package test_roman_numeral Test Roman Numeral Class
@author Daniel Pronych
@date December 2010
@version 1.0.0

Provides a nose testing system that encapsulates Integer <--> Roman Numeral.

* Important: Requires the nose and functools packages to run the test suite.
* Note: Due to use of functools, this testing suite requires Python 2.5 and up.
"""

## @var __author__
# Script Author
__author__ = 'Daniel Pronych'
## @var __version__
# Script Release Version
__version__ = '1.0.0'

import nose

from roman_numeral import *
from nose import with_setup

from functools import partial

def setup_func():
  """Set Up Test Fixtures"""
  pass

def teardown_func():
  """Tear Down Test Fixtures"""
  pass

@with_setup(setup_func, teardown_func)
def test_integer_and_roman():
  """
  @brief Test Integer <--> Roman Numeral Conversion"""
  for i, n in [[1,'I'],[2,'II'],[3,'III'],[4,'IV'],[5,'V'],
      [8,'VIII'],[9,'IX'],[10,'X'],[30,'XXX'],[40,'XL'],[50,'L'],[80,'LXXX'], 
      [90, 'XC'],[100,'C'],[400,'CD'],[500,'D'],[900,'CM'],
      [1000,'M'],[1994,'MCMXCIV'],[2010,'MMX'],[3999,'MMMCMXCIX'], 
      [4000,'MMMM'],[5000,'(V)'],[6000,'(V)M'],[8000,'(V)MMM'],[9000,'M(X)'], 
      [10000,'(X)'],[12000,'(X)MM'],[50000,'(L)'],[90099,'(X)(C)XCIX'],
      [100000,'(C)'],[200000,'(C)(C)'],[300000,'(C)(C)(C)'],
      [400000,'(C)(D)'],[500000,'(D)'],[600000,'(D)(C)'],[700000,'(D)(C)(C)'], 
      [900000,'(C)(M)'],[1000000,'(M)']]:
      
    func = partial(check_int2roman, i,n,"I: %d should be R: %s." % (int(i), n))
    func.description = "Integer %d to Roman Numeral %s Conversion" % (int(i),n)
    yield (func, )
    func = partial(check_roman2int, n,i,"R: %s should be I: %d." % (n, int(i)))
    func.description = "Roman Numeral %s to Integer %d Conversion" % (n,int(i))
    yield (func, )

def check_int2roman(integer, numeral, description):
  """Check an Integer to a Roman Numeral Conversion
  @param integer The integer number sent for conversion.
  @param numeral The Roman Numeral string sent for conversion.
  @param description If an AssertionError occurs, output this description
  @exception AssertionError will be thrown if an invalid integer specified."""
  i = integer
  n = numeral
  assert (integer_to_roman(i) == n, description)
 
def check_roman2int(numeral, integer, description):
  """Check a Roman Numeral to Integer Conversion
  @param numeral The Roman Numeral string sent for conversion.
  @param integer The integer number sent for conversion.
  @param description If an AssertionError occurs, output this description
  @exception AssertionError will be thrown for an invalid Roman Numeral."""
  i = integer
  n = numeral
  assert (roman_to_integer(n) == i, description)

if __name__ == "__main__":
  """Runs the script tests"""
  ## @var result
  # Contains the result of the nose run command
  result = nose.run(argv=['-v','--verbose'])
  print result
