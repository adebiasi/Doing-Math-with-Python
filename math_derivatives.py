Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sympy import Limit, Symbol, S
>>> x = Symbol('x')
>>> Limit(1/x, x, S.Infinity)
Limit(1/x, x, oo, dir='-')
>>> l = Limit(1/x, x, S.Infinity)
>>> l.doit()
0
>>> Limit(1/x, x, 0, dir='-').doit()
-oo
>>> from sympy import Symbol, Limit
>>> t = Symbol('t')
>>> St = 5*t**2 + 2*t + 8
>>> t1 = Symbol('t1')
>>> delta_t = Symbol('delta_t')
>>> St1 = St.subs({t: t1})
>>> St1_delta = St.subs({t: t1 + delta_t})
>>> Limit((St1_delta-St1)/delta_t, delta_t, 0).doit()
10*t1 + 2
>>> t = Symbol('t')
>>> St = 5*t**2 + 2*t + 8
>>> Derivative(St, t)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    Derivative(St, t)
NameError: name 'Derivative' is not defined
>>> from sympy import Derivative
>>> Derivative(St, t)
Derivative(5*t**2 + 2*t + 8, t)
>>> Derivative(St, t).doit()
10*t + 2
>>> d.doit().subs({t:1})
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d.doit().subs({t:1})
NameError: name 'd' is not defined
>>> d = Derivative(St, t)
>>> d.doit().subs({t:1})
12
>>> from sympy import Integral, Symbol
>>> x = Symbol('x')
>>> k = Symbol('k')
>>> Integral(k*x, x).doit()
k*x**2/2
>>> Integral(k*x, (x, 0, 2)).doit()
2*k
>>> 