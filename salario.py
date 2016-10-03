#!/usr/bin/python
# -- coding: utf-8 --
"""
>>> calcularAumento(100.1)
nuevo Salario 125.125
"""
class salario():

	def calcularAumento(self,salario):

		try:

			nuevoSalario=salario+((salario*25)/100)
			return "nuevo Salario " + str(nuevoSalario) 
		except Exception, e:
			return "Datos invalidos"