#!/usr/bin/python
# -- coding: utf-8 --
"""
>>> calculaTotal(1000)
1150

>>> calculaTotal(1000.0)
1150.0

>>> calculaTotal(-100)
-115

>>> calculaTotal('mil')
Error: dato invalido

>>> calculaTotal(1000)
1150

"""


class tienda():

    def calculaTotal(self, total):
        try:
            suma = (total * 15) / 100
            suma = suma + total
            return suma
        except Exception, e:
            return "Error: dato invalido"
