"""
Created on Thu May 10 16:23:56 2018

@author: juanm
"""

from math import ceil, floor
bits = [0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1]

#PRIMER POSTULADO
#En todo período, la diferencia entre el número de unos y el número de ceros debe ser a lo sumo uno.

def Primer_pos(seq):
    # Contamos el número de unos
    n_unos, n_bits = sum(seq), len(seq)
    # Si la longitud de la secuencia es 0
    if n_bits % 2 == 0:
        # a la fuerza tienen que ser iguales
        # num_ceros y num_unos
        return n_bits // 2 == n_unos
    else:
        n2_bits = n_bits / 2
        return ceil(n2_bits) == n_unos or floor(n2_bits) == n_unos

    
Primer_pos(bits)


from itertools import groupby
from collections import Counter

#SEGUNDO POSTULADO
#En un periodo, el número de rachas de longitud 1 debe ser el doble al número de rachas de longitud 2,
# y este a su vez, el doble de rachas de longitud 3, etc.

# Esta función calcula el número de rachas de longitud k en la secuencia seq      
def Segundo_pos(seq):
    while seq[0] == seq[-1]:
        seq.append(seq.pop(0))
        
    # obtenemos todas las rachas posibles que existen en la secuencia
    runs = [list(g) for k, g in groupby(seq)]
    # y contamos el número de rachas que hay para cada longitud
    count = Counter(map(lambda x: len(x), runs))
    # comprobamos si se cumple que #runs(k+1) == runs(k)
    for i in range(1, len(count)):
        if count[i] != count[i+1]:
            if not count[i] == 2*count[i+1]: # en el caso de que el siguiente elemento
                return False                 # no sea 1/2 veces más pequeño
        else:
            if not count[i] >= count[i+1] :
                return False
    else:
        # si todo va bien, devolvemos True
        return True

Segundo_pos(bits)

from numpy import bitwise_xor, nonzero

#TERCER POSTULADO
#La distancia de Hamming entre dos secuencias diferentes, obtenidas mediante desplazamientos circulares
# de un periodo, debe ser constante

def rotate(seq, length):
    seq = [seq[-1]] + seq[:length-1]

def Tercer_pos(seq):
    length, rotated_seq = len(seq), seq
    rotate(rotated_seq, length)
    # Calculamos la distancia hamming como un xor entre
    # ambas cadenas, y contamos los bits no nulos
    norm = len(bitwise_xor(seq, rotated_seq).nonzero()[0])
    for i in range(1, length):
        rotate(rotated_seq, length)
        if norm != len(bitwise_xor(seq, rotated_seq).nonzero()[0]):
            return False
    else:
        return True

Tercer_pos(bits)


def Golomb(seq):
    if all(seq):
        return False
    else:
        rules = [Primer_pos, Segundo_pos, Tercer_pos]
        return all(map(lambda x: rules[x](seq), range(3)))
    
Golomb(bits)