Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import Symbol
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from sympy import Symbol
ModuleNotFoundError: No module named 'sympy'
>>> pip install sympy

SyntaxError: invalid syntax
>>> from sympy import Symbol
>>> x = Symbol('x')
>>> x + x + 1
2*x + 1
>>> a = Symbol('x')
>>> a + a + 1
2*x + 1
>>> x = Symbol('x')
>>> y = Symbol('y')
>>> z = Symbol('z')
>>> from sympy import symbols
>>> x,y,z = symbols('x,y,z')
>>> s = x*y + x*y
>>> s
2*x*y
>>> expr = x**2 - y**2
>>> factor(expr)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    factor(expr)
NameError: name 'factor' is not defined
>>> from sympy import factor
>>> factor(expr)
(x - y)*(x + y)
>>> factors = factor(expr)
>>> expand(factors)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    expand(factors)
NameError: name 'expand' is not defined
>>> from sympy import expand
>>> expand(factors)
x**2 - y**2
>>> expr = x + y + x*y
>>> from sympy import pprint
>>> pprint(expr)
x⋅y + x + y
>>> expr = sympify(x**2 + 3*x + x**3 + 2*x)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    expr = sympify(x**2 + 3*x + x**3 + 2*x)
NameError: name 'sympify' is not defined
>>> from sympy import sympify
>>> expr = sympify(x**2 + 3*x + x**3 + 2*x)
>>> expr
x**3 + x**2 + 5*x
>>> solve(expr)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    solve(expr)
NameError: name 'solve' is not defined
>>> from sympy import Symbol, solve
>>> solve(expr)
[0, -1/2 - sqrt(19)*I/2, -1/2 + sqrt(19)*I/2]
>>> solve(expr, dict=True)
[{x: 0}, {x: -1/2 - sqrt(19)*I/2}, {x: -1/2 + sqrt(19)*I/2}]
>>> from sympy.plotting import plot
>>> from sympy import Symbol
>>> x = Symbol('x')
>>> plot(2*x+3)
<sympy.plotting.plot.Plot object at 0x000001C51E94F370>
>>> 