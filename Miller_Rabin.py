# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:54:23 2018

@author: JohnAlbert
"""

"""
Test de Miller-Rabin 1.
Entrada: p perteneciente a N n>2 y un numero.
Salida: no es primo/
        es probable que sea primo.
         
Se aplica el teorema a^p-1 = 1 mod p en el cual se cumple la
funcion de heuler si mcd(a,n) = 1 entonces a^e(n) = 1 mod n
"""

def Miller_Rabin1(p, n):

    for i in range(n):
        a = randrange(3, p - 1)
        if Modulo(a,p-1,p) != 1:
            return False
    
    return True

"""
Test de Miller-Rabin 2.
Entrada: p perteneciente a N n>2 y una lista.
Salida: no es primo/
        es probable que sea primo.
            
Pasos:
1.- Escribimos p-1  como p-1 = 2^u*S, donde S es un número impar.
2.- Elegimos un número aleatorio a entre 2 y p-2
3.- Calculamos para cada a de la lista a = a^S mod p.
4.- a) Si a == 1 o a == p-1 devuelve que es probable primo --> return.
5.  Bucle  desde i = 1 hasta u-1:
    a = a^2;
    Si a == p-1 , devuelve "es probable primo".
    Si a == 1, devuelve "no es primo".
6.- Devuelve "no es primo" ( por defecto ).
7- Si se cumple que a == p-1 para todos los elementos de la lista, es un candidato a primo
"""

def Miller_Rabin2(p, n):
    
    S = p-1
    u = 0
    while (S % 2) == 0:
        u = u + 1
        S = S // 2

    primo = False
    
    for i in range(len(n)):
        a = n[i]
        primo = False
        for j in range(u):
            a = Modulo(a,2,p)
            if primo == False:
                mod = Modulo(a,S,p)
                if mod == 1 :
                    return False
                elif mod == p-1 :
                    primo = True
        if primo == False:
            return False
    
    return True