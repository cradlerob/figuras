#!/usr/bin/python
# -- coding: utf-8 --
"""
>>> calcularArea(-1)
3.14

"""


def calcularArea(radio):

    try:
        import math
        area = round(math.pi, 2) * (radio**2)
        print area
    except Exception, e:
        print"Datos invalidos"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
