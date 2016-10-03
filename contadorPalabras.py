#!/usr/bin/python
# -- coding: utf-8 --
"""
>>> contador("Que lindo dia que hace hoy")
[('hace', 1), ('hoy', 1), ('que', 2), ('dia', 1), ('lindo', 1)]

"""
class contador():

	def contador(self, string):

		try:
			contador={}
			words=string.split(" ")
			for w in words:
				w=w.lower()
				if w in contador:
					contador[w]+=1
				else:
					contador[w]=1
	   		return contador.items()
		except Exception, e:
			return "Datos invalidos"