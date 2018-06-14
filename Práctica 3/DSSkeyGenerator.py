# -*- coding: utf-8 -*-
"""
Created on Sun Jun 8 13:02:20 2018

@author: Whiestar
"""

import Protocolos as prot
from random import getrandbits, randint

def generate_DSS_keys():
    # Calculamos el primo q entre 2^159 y 2^160
    q = prot.siguienteprimo(getrandbits(160))
    
    L = randint(512,1024)
    c = L - 160
    
    while c%2 != 0:
        L = randint(512,1024)
        c = L - 160
    
    #Calculamos el primo p
    p = (c*q) + 1
    
    while not prot.MillerRabin(p,50):
        c += 2
        p = (c*q) + 1
    
    # Elegimos α como un elemento de orden q
    # en Z_p 
    α = 1
    while α == 1:
        g = randint(2, p - 1)
        α = prot.potenciamodular(g, (p - 1) // q, p)
        
    # Seleccionamos el elemento x como 2 <= x <= q - 2
    # calculamos como y = α^x mod p
    x = randint(2, q - 2)
    y = prot.potenciamodular(α, x, p)
    # escribimos las claves publicas y la privada
    with open("DSS_KEY.pub", 'w') as f:
        f.write(str(p) + "\n" + str(q) + "\n" + str(α) + "\n" + str(y))
        
    with open("DSS_KEY", 'w') as f:
        f.write(str(x))
  
generate_DSS_keys()

'''
q = prot.siguienteprimo(getrandbits(160))

L = randint(512,1024)
c = L - 160

while c%2 != 0:
    L = randint(512,1024)
    c = L - 160

p = (c*q) + 1

while not prot.MillerRabin(p,50):
    print(p)
    c += 2
    p = (c*q) + 1
    
g = randint(2,p-2)

α = 1
while α == 1:
    g = randint(2, p - 2)
    α = prot.potenciamodular(g, (p - 1) // q, p)
'''

