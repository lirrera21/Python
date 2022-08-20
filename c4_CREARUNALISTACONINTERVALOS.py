#!/usr/bin/env python
# -*- coding: utf-8 -*-
def rango(desde, hasta, intervalo):
    numeros = []
    while desde < hasta:
        numeros.append(desde)
        desde = desde + intervalo
    return numeros


lista = rango(1, 10, 2)
print(lista)
lista = rango(1, 21, 3)
print(lista)
