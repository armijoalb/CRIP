import random as rnd

def potencia(a,b,m):
    x = 1
    while( b > 0):
        if (b%2 ==1):
            x = (x*a)%m
        a = (a**2)%m
        b = b//2
    return x
def PrimalidadMillerRabin(p,lista):
    """
    Descripción: devuelve si p es posible primo o no
    Argumentos:
        p:(int)Número sobre el que se realiza el test
        n:(int)Número de veces que se realiza el test
    """
    if type(lista) is int:
        n = lista
        l_cond = False #si no es una lista lo guardamos
    elif type(lista) is list:
        n = len(lista)
        l_cond = True #Si es una lista lo guardamos
    else:
        print("Se esperaba una lista o un entero como segundo argumento")
        return False
    s = p-1
    u = 0
    while(s%2==0):
            u+=1
            s = s//2
    #Iterator almacena la potencia de 2 y s el producto de forma que p-1 = (2^u)*s
    for i in range(n):#Para cada experimento
        if l_cond:
            a = lista[i]
        else:
            a = rnd.randrange(2,p-2)#Se crea un a aleatorio
        a = potencia(a,s,p)
        if(a != 1 and a != p-1):
            probFound = False
            for j in range(1,u):
                a = potencia(a,2,p)
                if(a == p-1):
                    #print("Es probable primo porque a = -1")
                    probFound = True
                    break
                elif(a == 1):
                    #print("No es primo porque a = 1")
                    return False
                probFound = False

            if(not probFound):#Si sale del bucle(habiendo entrado en él) devuelve false
                return False
    return True
def siguientePrimoFuerte(n):
	number = n+3-(n%4)
	while(not(PrimalidadMillerRabin(number,100)) or not(PrimalidadMillerRabin((number-1)//2,100))):
		number+=4
	return number
primoFuerte = siguientePrimoFuerte(24)
print(primoFuerte)
p = 19
for i in range(1,p):
	a = i
	l = [1]
	while a != 1:
		l.append(a)
		a = (a*i)%p
	print (str(i)+": "+str(len(l)))
