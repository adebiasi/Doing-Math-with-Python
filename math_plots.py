Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x_numbers = [1, 2, 3]
>>> y_numbers = [2, 4, 6]
>>> from pylab import plot, show
>>> plot(x_numbers, y_numbers)
[<matplotlib.lines.Line2D object at 0x0000028079C413D0>]
>>> show()
>>> plot(x_numbers, y_numbers, marker='o')
[<matplotlib.lines.Line2D object at 0x0000028079C9AAF0>]
>>> show()
>>> plot(x_numbers, y_numbers, 'o')
[<matplotlib.lines.Line2D object at 0x0000028079D11250>]
>>> show()
>>> nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
>>> plot(nyc_temp, marker='o')
[<matplotlib.lines.Line2D object at 0x0000028079D7A610>]
>>> show()
>>> years = range(2000, 2013)
>>> plot(years, nyc_temp, marker='o')
[<matplotlib.lines.Line2D object at 0x000002807AB08640>]
>>> show()
>>> nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
>>> nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
>>> nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
>>> months = range(1, 13)
>>> plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
[<matplotlib.lines.Line2D object at 0x000002807A98FDC0>, <matplotlib.lines.Line2D object at 0x000002807A98A400>, <matplotlib.lines.Line2D object at 0x000002807A98A520>]
>>> show()
>>> from pylab import legend
>>> legend([2000, 2006, 2012])
<matplotlib.legend.Legend object at 0x0000028079CEAF70>
>>> show()
>>> plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
[<matplotlib.lines.Line2D object at 0x0000028079DE4040>, <matplotlib.lines.Line2D object at 0x0000028079C35160>, <matplotlib.lines.Line2D object at 0x0000028079C35A90>]
>>> show()
>>> plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
[<matplotlib.lines.Line2D object at 0x0000028079D77220>, <matplotlib.lines.Line2D object at 0x0000028079D772E0>, <matplotlib.lines.Line2D object at 0x0000028079D773A0>]
>>> legend([2000, 2006, 2012])
<matplotlib.legend.Legend object at 0x0000028079C9AD90>
>>> show()
>>> from pylab import plot, show, title, xlabel, ylabel, legend
>>> plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
[<matplotlib.lines.Line2D object at 0x000002807AB5E4C0>, <matplotlib.lines.Line2D object at 0x000002807AB5E580>, <matplotlib.lines.Line2D object at 0x000002807AB5E640>]
>>> title('Average monthly temperature in NYC')
Text(0.5, 1.0, 'Average monthly temperature in NYC')
>>> xlabel('Month')
Text(0.5, 0, 'Month')
>>> ylabel('Temperature')
Text(0, 0.5, 'Temperature')
>>> legend([2000, 2006, 2012])
<matplotlib.legend.Legend object at 0x000002807AB51400>
>>> show()
>>> 