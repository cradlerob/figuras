#!/usr/bin/python
# -- coding: utf-8 --
"""
>>> calcularPeso()
gramos=2000.00 libras=4.41 toneladas=0.00



"""


class peso():

    def calcularPeso(self, peso):

        try:
            peso = float(peso)
            gramos = peso * 1000
            libras = peso * 2.20462
            toneladas = peso / 1000
            return "g=%.2f l=%.2f t%.2f" % (gramos, libras, toneladas)
        except Exception:
            return "Datos invalidos"
