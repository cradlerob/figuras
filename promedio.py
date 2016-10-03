#!/usr/bin/python
# -- coding: utf-8 --
"""
>>> calcularPromedio([5.5,5,4])
Reprobado

>>> calcularPromedio([10,10,10])
Aprobado

"""
class promedio():

	def calcularPromedio(self,parciales):

		try:
			if len(parciales) == 3:
				suma = 0.0
				for x in parciales:
					x = float(x)
					suma += x
				suma = suma / 3
				if suma < 6:
					return "Reprobado"
				else:
					return "Aprobado"
			else:
				return "Deben ser 3"
			
		except Exception, e:
			print"Datos invalidos"