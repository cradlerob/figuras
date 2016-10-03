#!/usr/bin/python
# -- coding: utf-8 --
"""
>>> searchstring("(Ho(la))")
'OK'
>>> searchstring(")hola(")
'WRONG'
"""


class parentesis():

    def searchstring(self, string):

        try:
            string = str(string)
            ls = []
            for x in string:
                if x == '(':
                    ls.append(x)
                elif x == ')':
                    if len(ls) == 0:

                        return 'WRONG'
                    else:
                        ls.remove(max(ls))
            if len(ls) == 0:
                return "OK"
        except Exception, e:
            return
