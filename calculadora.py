#!/usr/bin/python
# -- coding: utf-8 --
class calculadora():
		
	def sumar(self,num1,num2):
		
		try:
			num1=float(num1)
			num2=float(num2)
			return num1+num2
		except Exception, e:
			return

		

	def restar(self,num1,num2):
		return num1-num2
