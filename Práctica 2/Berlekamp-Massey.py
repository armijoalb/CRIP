# -*- coding: utf-8 -*-
"""
Created on Fri May 11 12:39:28 2018

@author: juanm
"""
from LFSR import LFSR
def Berlekam_Massey(sequence):
    print('secuencia: ', sequence)
    n_bits = len(sequence)
    F, G = [0]*n_bits, [0]*n_bits
    F[0], G[0] = 1,1
    
    for i in range(n_bits):
        if sequence[i] == 1:
            k = i
            break
    if k+1 < n_bits:    
        F[k+1] = 1
    
    l, a, b, r = k+1, k, 0, k+1
    aux = [0]
    while r < n_bits:
        
        #Calculamos la discrepancia
        d = sum([(F[i]*sequence[i+r-l]) for i in range(l + 1)])%2
        #print('r: ', r, 'l: ', l, 'a: ', a, 'b: ', b, 'F: ', F, 'G: ', G, 'd: ', d, '2l>r: ', 2*l>r)
        if d == 0:
            b = b + 1
        if d == 1:
            if 2*l > r:
                for i in range(l+1):
                    if i+(b-a) >= 0:
                        F[i] = (F[i] + G[i+(b-a)])%2
                b = b + 1
                
            if 2*l <= r:
                #print(F)
                aux = F[:]
                #Desplazamos una unidad a la derecha aux
                #aux.insert(0,0)
                for i in range(r+l):
                    if i+(a-b) >= 0:
                        F[i] = (aux[i+(a-b)] + G[i])%2
                    else:
                        F[i] = G[i]
                #Devolvemos aux a su valor anterior
                
                #aux.pop(0)
                l = r - l + 1
                G = aux[:]
                a = b
                b = r - l + 1
                #print('es menor')
        r = r + 1
        #print('aux: ', aux)

    
    return l, F

bits = LFSR([1,0,0,1,0,1,1,0], [1,1,1,1,1,1,1,1],1000)              
bits2 = LFSR([1,0,0,0,0,1],[1,0,0,1,0,0],1002)
from Funciones import bitwise_xor,bitwise_and,bitwise_or
bit_x = bitwise_or(bits,bits2)
l, F = Berlekam_Massey(bit_x)
print('Complejidad Lineal : ', l,'Polinomio :', F)
