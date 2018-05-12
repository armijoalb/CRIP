"""
Funciones que implementan operaciones bit a bit con valores en Z2[x].
    - O exclusivo (XOR)
    - suma booleana. (OR)
    - producto booleano. (AND)
"""
# Operaciones a nivel de bit.
def bit_xor(bit_1, bit_2):
    return bit_1 ^ bit_2

def bit_and(bit_1,bit_2):
    return bit_1 & bit_2

def bit_or(bit_1,bit_2):
    return bit_1 | bit_2

# Operaciones con cadenas de bits.
def bitwise_xor(cad_1,cad_2):
    return [bit_xor(cad_1[i],cad_2[i]) for i in range(len(cad_1))]

def bitwise_or(cad_1,cad_2):
    return [bit_or(cad_1[i],cad_2[i]) for i in range(len(cad_1))]

def bitwise_and(cad_1, cad_2):
    return [bit_and(cad_1[i],cad_2[i]) for i in range(len(cad_1))]

def even_cads(cad_1,cad_2):
    if(len(cad_1) < len(cad_2)):
        print("first case")
        cad_1.extend([0]*(len(cad_2)-len(cad_1)))
    elif( len(cad_1) > len(cad_2)):
        print()
        cad_2.extend([0]*(len(cad_1)-len(cad_2)))
    else:
        print("iguales")
    
    return [cad_1, cad_2]
