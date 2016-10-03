#!/usr/bin/python
# -- coding: utf-8 --


class calificaciones():

    def mostrarCalificacion(self, examenes):
        try:
            sum = 0.0
            for x in examenes:
                x = float(x)
                if x <= 10:
                    sum += x
                else:
                    return "Calificacion erronea"
            return sum / len(examenes)
        except Exception, e:
            return "Dato invalido"
