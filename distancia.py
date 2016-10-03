#!/usr/bin/python
# -- coding: utf-8 --
"""
>>> calcularDistancia(-10)
pies=-32.81 pulgadas=-393.70

"""


class distancia():

    def calcularDistancia(self, distancia):

        try:
            distancia = float(distancia)
            pies = distancia * 3.28084
            pulgadas = distancia * 39.3701

            return "pies=%.2f pulgadas=%.2f" % (pies, pulgadas)
        except Exception:
            return "Datos invalidos"
