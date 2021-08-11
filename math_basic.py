Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from fractions import Fraction
>>> f = Fraction(3, 4)
>>> f
Fraction(3, 4)
>>> Fraction(3, 4) + 1 + 1.5
3.25
>>> Fraction(3, 4) + 1 + Fraction(1/4)
Fraction(2, 1)
>>> a = 2 + 3j
>>> type(a)
<class 'complex'>
>>> a = complex(2, 3)
>>> a
(2+3j)
>>> type(a)
<class 'complex'>
>>> b = 3 + 3j
>>> a + b
(5+6j)
>>> a - b
(-1+0j)
>>> a.real
2.0
>>> a.imag
3.0
>>> a
(2+3j)
>>> a.conjugate
<built-in method conjugate of complex object at 0x000002211D398E50>
>>> a.conjugate()
(2-3j)
>>> abs(a)
3.605551275463989
>>> 