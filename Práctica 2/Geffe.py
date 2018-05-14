"""
Implementación de un Generador de Geffe

Un Generador de Geffe crea una cadena de 0s y 1s a través de tres cadenas generadas por LFSR.
A dichas cadenas las llamaremos L1, L2 y L3 respectivamente.
A partir de dichas cadenas el Generador de Geffe crea la cadena con la siguiente operación:
cad_solucion = (L1*L2)+(L2*L3)+L3
"""

from Funciones import bitwise_and, bitwise_xor
from LFSR import LFSR

def Geffe(l1, l2, l3):
    l1l2 = bitwise_and(l1,l2)
    print("l1l2")
    print(l1l2)
    l2l3 = bitwise_and(l2,l3)
    print("l2l3")
    print(l2l3)

    cad = bitwise_xor(l1l2,l2l3)
    print("l1l2+l2l3")
    print(cad)
    cad = bitwise_xor(cad,l3)

    return cad

# Prueba de Generador de Geffe.
print("Prueba Generador de Geffe")
lfsr1 = LFSR([1,0,0,1],[1,0,1,1],15)
lfsr2 = LFSR([1,0,0,0],[0,1,1,0],15)
lfsr3 = LFSR([1,1,0,1],[1,1,0,0],15)
print("LFSR generados:")
print(lfsr1)
print(lfsr2)
print(lfsr3)
print("Cadena generada por Geffe")
geffe=Geffe(lfsr1,lfsr2,lfsr3)
print(geffe)