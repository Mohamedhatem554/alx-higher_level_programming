#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lista = list(tuple_a)
    listb = list(tuple_b)

    for i in range(2):
        lista.append(0)
        listb.append(0)
    add1 = lista[0] + listb[0]
    add2 = lista[1] + listb[1]
    new_tuple = (add1, add2)
    return new_tuple
