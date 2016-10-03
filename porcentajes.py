#!/usr/bin/python
# -- coding: utf-8 --
"""
>>> calcularPorcentaje(50,50)
Porc. Hombres 50.00 Porc. Mujeres 50.00

>>> calcularPorcentaje(55,45)
Porc. Hombres 55.00 Porc. Mujeres 45.00

>>> calcularPorcentaje('cincuenta',50)
Datos invalidos
"""


class porcentajes(object):

    def calcularPorcentaje(self, hombres, mujeres):

        try:
            hombres = float(hombres)
            mujeres = float(mujeres)
            total = hombres + mujeres
            porcHom = float((hombres * 100) / total)
            porcMuj = float((mujeres * 100) / total)
            return "Porc. Hombres %.2f Porc. Mujeres %.2f" % (porcHom, porcMuj)
        except Exception:
            return "Datos invalidos"
