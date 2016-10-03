#!/usr/bin/python
# -- coding: utf-8 --


def empaquetar(lista):

    try:
        y = lista[0]
        lista_tup = []
        cont = 0
        for x in range(len(lista)):
            if lista[x] == lista[x + 1]:
                cont += 1
            else:
                lista_tup.add((lista[x - 1], cont))
                cont = 0
        return lista_tup
    except Exception, e:
        return "Datos invalidos"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
