# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 13:32:46 2018

@author: Whiestar
"""
import Protocolos as prot
from random import randint
from hashlib import sha256

def DSS_sign_document(document, public_key, private_key):
    
    #Obtenemos las claves publicas
    with open(public_key, 'r') as f:
        p, q = int(f.readline()), int(f.readline())
        α, y = int(f.readline()), int(f.readline())
     
    #Obtenemos la clave privata
    with open(private_key, 'r') as f:
        x = int(f.readline())
    
    # Obtenemos el resumen del mensaje con SHA2
    with open(document, 'rb') as f:
        h_m = int(sha256(f.read()).hexdigest(), 16)
        
    # Seleccionamos un k aleatorio de manera:  2 <= k <= q - 2
    k = randint(2, q - 2)
    
    # Calculamos r = (α^k mod p) mod q
    r = (prot.potenciamodular(α, k, p)) % q
    
    # Calculamos k^-1 mod q
    inv_k = prot.inverso(k, q)
    
    # Calculamos s =  (h(m) + x*r) * k^-1 mod q
    s = ((h_m + x*r) * inv_k) % q
    
    #Guardamos la firma
    with open("DSS_firma_"+document, 'w') as f:
        f.write(str(r) + "\n" + str(s))

DSS_sign_document("DSStexto.txt", "DSS_KEY.pub", "DSS_KEY")