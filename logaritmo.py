"""
Test de primalidad con algoritmo del logaritmo discreto.
Algoritmo paso-enano, paso-gigante.
"""

"""
Pasos del algortimo:
 0.- Comprobamos que no tenemos a, b sean distintos de 0 y que p sea primo (utilizaremos el algoritmo utilizado anteriormente).
 1.- Calculamos el primer número más pequeño que sqrt(p-1)
 2.- Calculamos una lista: b*a^i donde i va hasta s-1.
 3.- Calculamos una lista: a^s*i donde i va hasta s-1.
 4.- Calculamos intersección de ambas listas:
    4.1.- Si la intersección está vacía, el número no se puede calcular. Devolvemos false.
    4.2.- Si no está vacía: calculamos los índices de la listas.
5.- Calculamos x como: x = is-j. Siendo i=indice(n,lista_punto_2), j=indice(n,lista_punto_3).
"""
from Miller_Rabin import Miller_Rabin1

# Función para calcular el módulo de forma eficiente.
def exp_mod(a,b,p):
    
    sol=1
    while b > 0:
        if b%2 == 1:
            sol = (sol * a) % p
        a= (a*a) % p
        b=b//2
        
        
    return sol

# Función para calcular el primer número menor que sqrt(p-1).
def techo(p):
    s = 1

    while( s**2 < (p-1) ):
        s = s+1
    
    return s

# Función para calcular la solución del algoritmo discreto.
def algoritmo_discreto(a,b,p):
    if(a == 0 or b == 0):
        print("Introduzca valores diferentes a 0")
        return False
    
    # Comprobación de que p es un número primo.
    if not Miller_Rabin1(p,10):
        return False

    # Calculamos techo.
    s = techo(p)
    
    # Calculamos listas.
    L = [exp_mod(a,s*i,p) for i in range(s)]
    l = [b*exp_mod(a,i,p) % p for i in range(s)]

    # Calculamos la intersección de las listas.
    intersection = list(set(L) & set(l))

    # Comprobamos que la intersección no está vacía.
    if not intersection:
        print("No hay intersección")
        return False
    
    # Calculamos índices.
    i = L.index(intersection[0])
    j = l.index(intersection[0])

    x = i*s - j
    x = (x+p) % p

    return x


# Algunos ejemplos.
#print(algoritmo_discreto(5,13,37))
#print(algoritmo_discreto(0,13,37))
#print(algoritmo_discreto(3,4,19))
#print(algoritmo_discreto(7,11,19))


import time

#print("----------------------------------------")
#print("Soluciones Práctica:")
#print("----------------------------------------")

# Función medir los tiempos de ejecución.
def medirTiempos(args =  list(),miller_rabin=False):
    if( not miller_rabin ):
        init_time = time.time()
        algoritmo_discreto(args[0],args[1],args[2])
        finish_time = time.time()
        elapsed_time = finish_time-init_time
    else:
        init_time = time.time()
        Miller_Rabin1(args[0],args[1])
        finish_time = time.time()
        elapsed_time = finish_time-init_time
    
    return elapsed_time 


#print(medirTiempos(6,50628,57347))

