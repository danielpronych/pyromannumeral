"""
@file roman_numeral.py Roman Numeral Source File
@name Python Roman Numeral
@package roman_numeral Roman Numeral Routines
@author Daniel Pronych
@date December 2010
@version 1.0.0

Roman Numeral Class Definition.
* Note: brackets are used around a Roman Numeral to support Roman
Numerals greater than 4999 since over-lines are not available."""

## @var __author__
# Script Author
__author__ = 'Daniel Pronych'
## @var __version__
# Script Release Version
__version__ = '1.0.0'

import sys

## @var __numerals
# Numerals Dictionary used for conversion by both conversion functions
__numerals = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL", 
  50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 
  1000 : "M", 4000 : 'MMMM', 5000 : '(V)', 9000 : 'M(X)', 10000 : '(X)', 
  49000 : 'M(L)', 50000 : '(L)', 90000 : '(X)(C)', 100000 : '(C)', 
  400000 : '(C)(D)', 500000 : '(D)', 900000 : '(C)(M)', 1000000 : '(M)' }

def integer_to_roman(integer):
  """
  @brief Integer to Roman Numeral Conversion Routine
  @param integer The integer number sent for conversion.
  @exception ValueError will be thrown if an invalid integer specified.
  @return string representing the Roman Numeral equivalent of input integer."""
  try:
    number = int(integer)
  except:
    raise ValueError("Input not a valid Integer: %s." % str(integer))
  # This instance does not support Roman Numerals >= 4 million
  if(number > 3999999):
    raise ValueError("Input not a valid Integer: %s." % str(integer))
  result = ""
  for v, n in sorted(__numerals.items(), reverse=True):
    while number >= v:
      result += n
      number -= v
  return result

def roman_to_integer(numeral):
  """
  @brief Roman Numeral to Integer Conversion Routine
  @param numeral The Roman Numeral string sent for conversion.
  @exception ValueError will be thrown for an invalid Roman Numeral.
  @return string representing the Roman Numeral equivalent of input numeral.
  """
  try:
    # Ensure an uppercase version of the input string is used
    roman = str(numeral).upper()
  except Exception, e:
    raise ValueError("Input not a valid Integer: %s." % str(numeral))
  result = 0
  for v, n in sorted(__numerals.items(), reverse=True):
    my_len = len(n)
    while n == roman[:my_len]:
      result += int(v)
      roman = roman[my_len:]
  # This will error if one item couldn't be converted, or no conversion match
  if len(roman) or integer_to_roman(result) != numeral.upper():
    raise ValueError("Input not a valid Integer: %s." % str(numeral))
  return result

## @var __all__
# Specifies that import * only loads the conversion functions to namespace
__all__ = ["integer_to_roman", "roman_to_integer"]

if __name__ == "__main__":
  """
  @brief Example code that utilizes both conversion routines.
  @param sys.argv[1] contains a Roman Numeral to convert to an integer.
  @param sys.argv[2] contains a integer to convert to a Roman Numeral.
  """
  if (len(sys.argv) > 2 and len(sys.argv) < 4):
    try:
      print "Integer <--> Roman Numeral Test Conversion Script"
      print "\nRoman To Integer"
      print "----------------"
      print "  Roman Numeral: %s" % str(sys.argv[1]).upper()
      try:
        print "  Integer*: %d" % roman_to_integer(sys.argv[1])
      except Exception, e:
        print "  Integer*: Invalid Roman Numeral input: %s" % sys.argv[1]
      print "\nInteger To Roman" 
      print "----------------"
      print "  Integer: %d" % int(sys.argv[2])
      try:
        print "  Roman Numeral*: %s" % str(integer_to_roman(sys.argv[2]))
      except Exception, e:
        print "  Roman Numeral*: Invalid integer input: %s" % str(sys.argv[2])
      print "\n* Indicates the calculated parameter."
    except Exception, e:
      print e
  else:
    print "Invalid parameters sent, format: script roman_numeral integer"
    print "Example: "
    print "  %s %s %d" % (sys.argv[0], 'V', 5)
