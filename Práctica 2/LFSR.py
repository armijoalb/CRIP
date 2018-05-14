"""
Implementación de un algoritmo que genera cadenas pseudoaleatorias con un LFSR a partir de una semilla y un polinomio de grado |s|-1.
El algoritmo tiene los siguientes parámetros:
    - Un polinomio representado por una cadena de 1s y 0s en cada posición.
    - Una semilla, de la misma longitud que dicho polinomio.
    - El número de bits que se quieren generar.

En cada momento, se genera el siguiente bit a partir del polinomio de la siguiente forma. Llamaremos S_i al bit en la posición i;
llamaremos a X_z al coeficiente z del polinomio, que va desde 0 hasta n, donde n es el grado de dicho polinomio. De esta manera:
    - S_i = X_n*S_(i-1) + X_(n-1)*S_(i-2) + ... + X_0*S(i-n-1).

De forma matricial, el cálculo sería:
 polinomio * S[i-grado(polinomio)-1: i-1]
"""

def grado(polinomio=list()):
    return len(polinomio)-1

def multiply(polinomio=list(),salida=list(),modulo=2):
    lista = [polinomio[i]*salida[i] for i in range(0,len(polinomio))]
    return sum(lista) % 2


def LFSR(polinomio=[1,0,0,1],semilla=[1,0,1,1],longitud=3):
    if(len(polinomio) != len(semilla)):
        return semilla

    inicio = len(semilla)
    grad = grado(polinomio)

    salida = semilla

    for i in range(inicio, inicio+longitud):
        salida.append(multiply(polinomio,salida[i-grad-1:i]))


    return salida

#print("Prueba algoritmo LFSR")
#print(LFSR(polinomio=[1,0,1,0],semilla=[1,0,0,1],longitud=17))


