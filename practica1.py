"""
Práctica 1 Criptografía.
Test de primalidad.
- si p es primo: a^(p-1) = 1 mod p
- si p no es primo la ecuación x^2 = 1 en Zp tiene más de dos soluciones.

Variantes a elegir:
- Logaritmo discreto.
- Factorización.
- Raíces cuadradas.
"""

candidato_a_primo = 37

"""
Si 37 es primo, sabemos que a^36 = 1.
Tenemos que descomponer 36 en una multiplicación por un número par. 36 = 9*4 = 9*2²
Ahora calculamos a^9, a^18, a^36, por lo que sabemos, si a^9, a^18 o a^36, sabemos que para que dé 1 tiene que ser una
raíz de 1. (Puede ser 1 ó -1).
a^9,a ^18, a^36 (este último no hace falta).
Trabajaremos en Z37.
Ahora elegiremos un número dentro de Z37, mejor entre 3 y el 35.
"""
a = 3
print(a)
print(a**9 % 37)
print(a**18 % 37)
a = 7
print(a)
print(a**9 % 37)
print(a**18 % 37)

print("------------------------------------------------------------")

"""
Otro ejemplo, con 105.
104 = 13+4^3.

"""
a = 8
print(a)
print(a**13 % 105)
print(a**26 % 105)
print(a**52 % 105)
a = 10
print(a)
print(a**13 % 105)
print(a**26 % 105)
print(a**52 % 105)

print("----------------------------------------------------------------")

"""
Ahora intentaremos implementar el algoritmo para comprobar si es primo,
si pasa el test, el número puede ser primo o no. Si no lo pasa, el número no es primo.
n = 561
560 = 2^4*35

El test debe comprobar si existe algún número para el cuál no existe que a^potencia_de_impar*(1 to max_pot_par-1)

Ejemplos:
a = 103 --> a^35 mod 561 = 1.
a = 95 --> a^35 mod 561 = 65 --> a^70 mod 561 = 298 --> a^140 mod 561 = 166 --> a^280 mod 561 = 67; llegados a este punto, debemos de
comprobar si x^2 = 1 en Z561.
"""

"""
Test de Miller-Rabin.
Entrada: p perteneciente a N n>2.
Salida: no es primo/
        es probable que sea primo.
            
Pasos:
1.- Escribimos p-1  como p-1 = 2^u*S, donde S es un número impar.
2.- Elegimos un número aleatorio a entre 2 y p-2
3.- Calculamos a = a^S mod p.
4.- a) Si a == 1 o a == p-1 devuelve que es probable primo --> return.
5.  Bucle  desde i = 1 hasta u-1:
    a = a^2;
    Si a == p-1 , devuelve "es probable primo".
    Si a == 1, devuelve "no es primo".
6.- Devuelve "no es primo" ( por defecto ).

No olvidarse que todas las operaciones tienen el modulo p 
"""

"""
Problema dado el número 7, 11 y 19
Existe un número X tal que 7^X = 11 mod 19
"""
    
import time
from random import randrange

def Modulo(a,b,m):
    
    sol=1
    while b > 0:
        if b%2 == 1:
            sol = (sol * a) % m
        a= (a*a) % m
        b=b//2
        
        
    return sol


def Miller_Rabin1(p, n):

    for i in range(n):
        a = randrange(3, p - 1)
        if Modulo(a,p-1,p) != 1:
            return False
    
    return True



if Miller_Rabin1(37,10):
    print("Candidato a primo")
else:
    print("No primo")

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

if Miller_Rabin2(37,[14,20]):
    print("Candidato a primo")
else:
    print("No primo")
    


# Optativa 1.
"""
Logaritmo discreto:
log7(11) mod 19
"""

"""
Otro ejemplo:
3^X = 4 mod 19.
"""

"""
loga(b)modp.
Algoritmo Giant Step, baby Step.
1.-Calculamos s >= sqrt(p-1)
2.- Calculamos b, b*a, b*a^i hasta s-1.
3.- Calculamos a⁵, a¹⁰ mod p, hasta s-1.
Solucion: si a**(t*5) = b*a**(c) --> b = t*5 - c
"""


# Optativa 2.
"""
Factorización:
- División.
- Fermat.
- (Rho) de pollard

"""

# Optativa 3.

"""
Raíces cuadradas.
p primo.
a que pertenece a Zp.
Existe r perteneciente a Zp t.q r^2 = a.
En caso afirmativo calcularlo. (Si es verdadero = 1. Si es falso = -1).
También puede darse una respuesta = 0, que se da cuando r^2 = 0.

2 en Z7

Una función que nos responda a la primera pregunta  "Simbolo de legendre" = (a/p)
(1/p) = 1
(a^2/p) = 1 (el propio a = a^2)
(a*b/p) = (a/p) * (b/p)
(2/p) = 1 si p=1 7 mod 8 o -1 si p = 3 5 mod 8

si n es impar (a/n) = "Simnbolo de Jacubi"

Si m y n son impares (m/n) = (-1)^(((m-1)*(n-1))/4) * (n/m)
(m/n) = (m%n/n)
"""



