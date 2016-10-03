#!/usr/bin/python
# -- coding: utf-8 --


class figuras():

    def cuadrado(lado):
        try:
            lado = float(lado)
            return lado ** 2

        except Exception:
            return 'Datos invalidos'

    def rectangulo(base, altura):
        try:
            base = abs(float(base))
            altura = abs(float(altura))
            return base * altura

        except Exception:
            return 'Datos invalidos'

    def triangulo(base, altura):
        try:
            base = abs(float(base))
            altura = abs(float(altura))
            return (base * altura) / 2

        except Exception:
            return 'Datos invalidos'

    def circulo(radio):
        try:
            radio = float(radio)
            return (radio ** 2) * 3.1416

        except Exception:
            return 'Datos invalidos'
