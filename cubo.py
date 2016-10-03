#!/usr/bin/python
# -- coding: utf-8 --
"""
>>> calcularCubo(3)
27

"""
def calcularCubo(num):

	try:
		
		print (num ** 3)
	except Exception, e:
		print"Datos invalidos"



if __name__=="__main__":
	import doctest
	doctest.testmod()