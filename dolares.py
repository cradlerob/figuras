#!/usr/bin/python
# -- coding: utf-8 --
"""
>>> calcularDivisas(100,10)
Dolares 1000.00

>>> calcularDivisas(100,'diez')
Datos invalidos
>>> calcularDivisas(100,14.5)
Dolares 1450.00
>>> calcularDivisas(200.1,10.1)
Dolares 2021.01
"""


class dolares():

    def calcularDivisas(self, pesos, dolar):

        try:
            pesos = float(pesos)
            dolar = float(dolar)
            dolares = pesos * dolar
            return dolares
        except Exception:
            return "Datos invalidos"
