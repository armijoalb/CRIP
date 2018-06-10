from random import randint

def potenciamodular(a,b,m):
    p = 1
    while b > 0:
        if (b%2 == 1):
            p = (p*a)%m
        b = b//2
        a = (a*a)%m
    return p

def mcd_ex(a,b):
    (u0,u1)=(1,0)
    (v0,v1)=(0,1)
    while b > 0:
        (c,r) = (a//b, a%b)
        (u0,u1) = (u1,u0-c*u1)
        (v0,v1) = (v1,v0-c*v1)
        (a,b) = (b, a%b)
    return [a,u0,v0]

def inverso(a,n):
    u = mcd_ex(a,n)
    if u[0] == 1:
        return(u[1])
    else:
        print('No existe el inverso')
        return(0)

def mraux(u,p,a):
    if (a == 1 or a == (p-1)):
        return True
    for i in range(u-1):
        a = (a*a)%p
        if a == p-1:
            return True
        if a == 1:
            return False
    return False
    
def MillerRabin(p,n):
    if (p%2) == 0:
        #print('El numero es par')
        return False
    [u,s] = factoriza2(p-1)
    i = 0
    while i<n:
        a = randint(2,p-2)
        b = potenciamodular(a,s,p)
        i+=1
        bool = mraux(u,p,b)
        if bool == False:
            return False
    return True

def siguienteprimo(m):
    m = m + 1 - (m%2)
    primo = MillerRabin(m,50)
    while not(primo):
        m += 2
        primo = MillerRabin(m,50)
    return(m)
    


def siguienteprimofuerte(m):
    m = m + 3 - (m%4)
    primo = (MillerRabin(m,50) and MillerRabin((m-1)//2,50))
    while not(primo):
        m += 4
        primo = MillerRabin(m,50) and MillerRabin((m-1)//2,50)
    return(m)



def legendre(a,n):
    if (n%2 == 0):
        print('El segundo argumento debe ser impar')
        return(0)
    if (a > n):
        l = legendre(a%n,n)
        return(l)
    if (a == 1 or a == 0):
        return a
    if (a%2 == 0):
        e = (-1)**((n**2-1)//8)
        l = legendre(a//2,n)
        return(e*l)    
    e = (-1)**((n-1)*(a-1)//4)
    l = legendre(n%a,a)
    return(e*l)

def factoriza2(n):
    [u,s]=[0,n]
    while (s%2 == 0):
        [u,s] = [u+1,s//2]
    return([u,s])

def raiz(a,n):
    if (legendre(a,n) == -1):
        print('El numero no tiene raiz cuadrada')
        return(0)
    aux = factoriza2(n-1)
    u = aux[0]
    s = aux[1]
    m = 2
    control = True
    while control:
        if legendre(m,n)==-1:
            control = False
        m+=1
    if u == 1:
        r = potenciamodular(a,(n+1)//4,n)
        return(r)
    r = potenciamodular(a,(s+1)//2,n)
    b = potenciamodular(m,s,n)
    inv = inverso(a,n)
    for j in range (u-1):
        aux2 = (inv*r*r)%m
        aux3 = potenciamodular(aux2,2**(u-2-j),n)
        if aux3 == (n-1):
            r = (r*b)%n
        b = (b*b)%n
    return(r)

def congruencia(a,b,m):
    d = mcd_ex(a,m)
    if b%d[0] == 0:
        m1 = m//d[0]
        a1 = (d[1]*b//d[0])%m1
        return([a1,m1])
    return([0,0])

def sistema(l):
    sol = [0,1]
    for y in l:
        z = congruencia(y[0]*sol[1],(y[1]-y[0]*sol[0])%y[2],y[2])
        sol = [sol[0]+sol[1]*z[0],sol[1]*z[1]]
    return(sol)

def raizmodular(v,p,q):
    n = p*q
    u1 = raiz(v,p)
    u2 = raiz(v,q)
    r1 = sistema([[1,u1,p],[1,u2,q]])[0]
    if r1 > (n-1)//2:
        r1 = n-r1
    r2 = sistema([[1,u1,p],[1,q-u2,q]])[0]
    if r2 > (n-1)//2:
        r2 = n-r2
    return([r1,r2])
    

