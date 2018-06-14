# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 17:53:07 2018

@author: Whiestar
"""

import Protocolos as prot
from hashlib import sha256

def DSS_check_sign(sign_file, document, public_key):
    
    #Obtenemos las claves publicas
    with open(public_key, 'r') as f:
        p, q = int(f.readline()), int(f.readline())
        α, y = int(f.readline()), int(f.readline())
        
        
    #Obtenemos la firma
    with open(sign_file, 'r') as f:
        r, s = int(f.readline()), int(f.readline())

    #Verificamos que los valores r y s son validos
    if not (0 < r < q or 0 < s < q):
        raise ValueError("Firma erronea.")
        
    #Calculamos w = s^-1 mod q and h(m)
    inv_s = prot.inverso(s, q)
    
    # Obtenemos el resumen del mensaje con SHA2
    with open(document, 'rb') as f:
        h_m = int(sha256(f.read()).hexdigest(), 16)
    
    
    # Calculamos u = s^-1 * h(m) mod q 
    u = (inv_s * h_m) % q
    
    # Calculamos v = r * inv_s mod q
    v = r * inv_s
    
    #Calculamos r' = (α^u * y^v mod p) mod q
    
    r2 = ((prot.potenciamodular(α,u,p) * prot.potenciamodular(y,v,p)) % p) % q
    
    # La firma es valida solo si r = r'
    return r2 == r

DSS_check_sign("DSS_firma_DSStexto.txt", "DSStexto.txt", 
               "DSS_KEY.pub")

