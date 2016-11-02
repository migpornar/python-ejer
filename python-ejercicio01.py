# ejercicios-01-ipppd.py
# Introducción a la Programación con Python y los Paradigmas de Datos

# Práctica 1: Introducción a Python
# =================================
### COMPRESION
### [(p,n) for n in range(6) for p in palabras if len(p) == n]

# -----------
# EJERCICIO 1
# -----------

# Definir una función suma(l) que recibiendo como entrada una lista l de
# números, devuelva la suma de sus elementos.

# Por ejemplo:

# >>> suma([2,4.6,3.1,2.8,5,8,9,23])
# 57.5

def suma(xs):
    n = len(xs) - 1
    i = 0
    sumatotal = 0
    while n >= i:
        sumatotal += xs[i]
        i += 1
    return sumatotal
 

## RECURSION   USO DE pop
def suma2(xs):
    if xs == []:
        return(0)
    else:
        a = xs[0]
        xs.pop(0)
        return a + suma2(xs)

### MANERA PROFESOR
       
def suma3(l):
    acum= 0
    for x in l:
        acum += x 
    return acum
        
        
# -----------
# EJERCICIO 2
# -----------

# Definir una función n_elementos_pos(l) que recibiendo como entrada una
# lista l de números enteros, devuelva el número de elementos positivos de la
# lista 

# Por ejemplo:

# >>> n_elementos_pos([-2,2,1,-3,2,5,-6,4,5,2,-8])
# 7

def n_elementos_pos(l):
    n = len(l) - 1
    i = 0
    sumatotal = 0
    while n >= i:
        if l[i] > 0:
            sumatotal += 1
        i += 1  
    return sumatotal
    
##RECURSION

def n_elementos_pos2(l):
    if l == []:
        return(0)
    elif l[0] > 0:
        l.pop(0)
        return(1 + n_elementos_pos2(l))
    else:
        l.pop(0)
        return(n_elementos_pos2(l))

##COMPRESION
def n_elementos_pos3(ls):
    return len([1 for l in ls if l>0])
        
        
# -----------
# EJERCICIO 3
# -----------

# Definir una función máximo(l) que recibiendo como entrada una lista l de
# números, devuelva el mayor de sus elementos

# Por ejemplo:

# >>> maximo([23,2,45,6,78,2,4,9,55])
# 78

def maximo(xs):
    a = xs[0]
    n = len(xs) - 1
    i = 1
    while n >= i:
        if a < xs[i]:
            a = xs[i]
        i += 1
    return a
        
### Es el menos infinito -> float("-inf")    
    
def maximo2(xs):
    m = float("-inf")
    for x in xs:
        if m < x:
            m = x
    return m

# -----------
# EJERCICIO 4
# -----------

# Definir una función suma_saltando(l,i,n) que recibiendo como entrada una lista
# números, una posición i de esa lista, y un número natural n, devuelve la
# suma de los elementos de la lista, empezanod en el i-ésimo y saltando de n
# en n. 

# Por ejemplo:

# >>> suma_saltando([2,4,3,7,8,1,2,9,4,3,2],4,3)
# 19
# >>> suma_saltando([2,4,3,7,8,1,2,9,4,3,2],2,2)
# 19
# >>> suma_saltando([2,4,3,7,8,1,2,9,4,3,2],3,2)
# 20

def suma_saltando(xs,i,n):
    return suma(xs[i::n])


# -----------
# EJERCICIO 5
# -----------

# Definir una función pos_máximo(l) que recibiendo como entrada una lista de
# números, devuelve la posición del mayor elemento de la lista.

# Por ejemplo:

# >>> pos_maximo([23,2,45,6,78,2,4,9,55])
# 4

def pos_maximo(xs):
    a = float("-inf")
    pos = 0
    n = len(xs) - 1
    i = 0
    while n >= i:
        if a < xs[i]:
            a = xs[i]
            pos = i
        i += 1
    return pos
### l.index(x) busca la posicion de x en l     
def pos_maximo2(xs):
    maxout = xs[0]
    indice = 0
    for i in range(1,len(xs)):
        if maxout < xs[i]:
            maxout = xs[i]
            indice=i
    return indice

# -----------
# EJERCICIO 6
# -----------

# Definir una función media(l) que recibiendo una lista numérica como entrada,
# devuelve la media aritmética de sus elementos 

# Por ejemplo:

# >>> media([1,2,5,2,3,6,7])
# 3.7142857142857144         

def media(xs):
    return suma(xs)/len(xs)

# -----------
# EJERCICIO 7
# -----------

# Definir una función varianza(l) que recibiendo una lista numérica como
# entrada, devuelve la varianza de ese conjunto de números

# Por ejemplo:

# >>> varianza([1,2,5,2,3,6,7])
# 4.489795918367346

# COMPRESION!!!!! >>>numbers = [ int(x) for x in numbers ]

def varianza(xs):
    med = media(xs)
    lista = [(x - med)**2 for x in xs]
    return suma(lista)/ len(xs)

# -----------
# EJERCICIO 8
# -----------

# Definir una función mediana(l) que recibiendo una lista numérica como
# entrada, devuelve la mediana de ese conjunto de números. Nota: puede ser de
# utilidad usar la función predefinida sorted(l), que ordena listas. 

# Por ejemplo:

# >>> mediana([3,1,4,2,7,8,5,3,5])
# 4
# >>> mediana([9,1,4,3,3,2,2,4,5,3,11,6])
# 3.5
#sort modifica la lista
def mediana(xs):
    xs = sorted(xs)
    n = len(xs)/2
    if n == int(n):
        return((xs[int(n-1)] + xs[int(n)])/2)
    else:
        return xs[int(n)] 
              
##Cociente entero //
## ES IMPORTANTE USAR EL ELSE, AUNQUE NO HAGA FALTA
def mediana2(xs):
    xs = sorted(xs)
    n = len(xs)//2
    if n%2 == 0:  #VER SI ES PAR
        return((xs[n-1] + xs[n])/2)
    else: 
        return xs[n]               
              

# -----------
# EJERCICIO 9
# -----------

# Definir una función cuadrados_lista(l),que recibiendo como entrada una lista
# l de números, devuelve la lista de los cuadrados de los elementos de l, en
# el mismo orden. 

# Por ejemplo:


# >>> cuadrados_lista([2,3,1,2.5,7,8/3])
# [4, 9, 1, 6.25, 49, 7.111111111111111]

def cuadrados_lista(xs):
    return [x**2 for x in xs ]

# ------------
# EJERCICIO 10
# ------------


# Definir una función prod_map(x,l) que recibiendo como entrada un número
# x y una lista de números l, devuelve la lista resultante de multiplicar cada
# elemento de l por x.

# Por ejemplo:

# >>> prod_map(2.5,[7,8.2,6,10.7,3,21])
# [17.5, 20.5, 15.0, 26.75, 7.5, 52.5]

def prod_map(n,xs):
    return [x*n for x in xs]

# EJERCICIO 11
# ------------

# Definir una función suma_vec(l,m) que recibiendo como entrada dos listas
# numéricas (de la misma longitud), devuelva la lista resultante de sumarla
# componente a componente.

# Por ejemplo:

# >>> suma_vec([8,5,4,2,7],[4,1,7,4,2])
# [12, 6, 11, 6, 9]

#USANDO INDICES
def suma_vec(xs,ys):
    return [xs[i] + ys[i] for i in range(len(xs))]

#USANDO ZIP
def suma_vec2(xs,ys):
    return [a+b for (a,b) in zip(xs,ys)]

# ------------
# EJERCICIO 12
# ------------


# Definir una función producto_escalar(l,m), que recibiendo como entrada dos
# listas numéricas de la misma longitud, devuelve su producto escalar

# Por ejemplo:

# >>> producto_escalar([2,1,3,4,2,4],[1,2,3,1,1,0])
# 19

#USANDO INDICES
def producto_escalar(xs,ys):
    return suma([xs[i] * ys[i] for i in range(len(xs))])

#USANDO ZIP
def producto_escalar2(xs,ys):
    return suma([a*b for (a,b) in zip(xs,ys)])
    

# ------------
# EJERCICIO 13
# ------------

# Definir una función covarianza(l,m) que recibiendo dos listas numéricas de
# la misma longitud, devuelve su covarianza.

# Por ejemplo:

# >>> covarianza([7,2,3,5,6,2,1],[6,1,2,4,5,1,0])
# 4.489795918367346

def covarianza (xs,ys):
    mediax = media(xs)
    mediay = media(ys)
    return suma([(a - mediax) * (b -mediay) for (a,b) in zip(xs,ys)])/len(xs)


# ------------
# EJERCICIO 14
# ------------


# Podemos representar una matriz bidimensional nxm en Python, como una lista
# que tiene n elementos que a su vez son listas de de m elementos
# numéricos. Por ejemplo, la siguiente lista de listas representa una matriz
# 4x7:  

# [[3,2,4,2,6,1,6],
#  [2,1,6,9,3,7,8],
#  [1,5,2,2,0,2,7],
#  [1,0,1,2,9,1,4]]

# Definir una función escalar_mat(x,m),que recibiendo un número x y una matriz
# m (representada como se ha indicado), devuelve la matriz que resulta de
# multiplicar cada elemento de la matriz por x. 

# Por ejemplo:

# >>> m=[[3,2,4,2,6,1,6],[2,1,6,9,3,7,8],[1,5,2,2,0,2,7],[1,0,1,2,9,1,4]]
# >>> escalar_mat(3,m)
# [[9, 6, 12, 6, 18, 3, 18], [6, 3, 18, 27, 9, 21, 24], [3, 15, 6, 6, 0, 6, 21], [3, 0, 3, 6, 27, 3, 12]]
# >>> m
# [[3, 2, 4, 2, 6, 1, 6], [2, 1, 6, 9, 3, 7, 8], [1, 5, 2, 2, 0, 2, 7], [1, 0, 1, 2, 9, 1, 4]]

def escalar_mat(x,ms):
    return [prod_map(x,ms[i]) for i in range(len(ms))]
    
####PROFESOR
#def escalar_mat2(x,m):
#    res=[]
#    for f in m:
#       resf = []
#        for e in f:    x = len(a[0])
#    y = len(b
#            resf.append(x*3)
#        res.append(resf)
#    return res
    
####PROFESOR
def escalar_mat3(x,m):
    nfilas=len(m)
    ncols=len(m[0])
    res=[]
    for i in range(nfilas):
        resf=[]
        for j in range(ncols):
            resf.append(x*m[i][j])
        resf.append(resf)
    return res
    
####PROFESOR (MANERA GUAY)
def escalar_mat4(x,m):
    return [[x*e for e in f] for f in m]
            
    
# Definir también una versión escalar_mat_destr(x,m) que devuelve lo mismo,
# pero además modifica m para que contenga lo calculado.  

# Por ejemplo:

# >>> m
# [[3, 2, 4, 2, 6, 1, 6], [2, 1, 6, 9, 3, 7, 8], [1, 5, 2, 2, 0, 2, 7], [1, 0, 1, 2, 9, 1, 4]]
# >>> escalar_mat_destr(3,m)
# [[9, 6, 12, 6, 18, 3, 18], [6, 3, 18, 27, 9, 21, 24], [3, 15, 6, 6, 0, 6, 21], [3, 0, 3, 6, 27, 3, 12]]
# >>> m
# [[9, 6, 12, 6, 18, 3, 18], [6, 3, 18, 27, 9, 21, 24], [3, 15, 6, 6, 0, 6, 21], [3, 0, 3, 6, 27, 3, 12]]

#######PARA CAMBIAR DIRECCIONES DE MEMORIA
    
def escalar_mat_destr(x,ms):
    n = len(ms)
    m = len(ms[0])
    for i in range(n):
        for j in range(m):
            ms[i][j] *= x
    return ms

# ------------
# EJERCICIO 15
# ------------


# Definir una función medias_matriz(m),que recibiendo una matriz m
# (representada como se ha indicado) cuyos elementos son números, devuelve una
# tupla con tres valores: 

# * La lista de las medias de las columnas de la matriz 
# * La lista de las medias columnas de la matriz
# * La media de todos los números de la matriz

# Por ejemplo:

# >>> medias_matriz([[1,2,5,2],[3,1,7,2],[2,1,6,1]])
# ([2.0, 1.3333333333333333, 6.0, 1.6666666666666667], [2.5, 3.25, 2.5], 2.75)



def medias_matriz(xs):
    n = len(xs)
    m = len(xs[0])
    media1 = []
    mediaacum = 0
    for j in range(m):
        for i in range(n):
            mediaacum += xs[i][j]
        media1 += [mediaacum/n]
        mediaacum = 0
    media2 = [media(x) for x in xs]
    return [media1, media2, suma(media2)/n]
    
##### PROFESOR

def medias_matriz2(m):
    nfilas = len(m)
    ncols=len(m[0])
    acum=0
    medias_filas = [0 for _ in range(ncols)]
    medias_cols = [0 for _ in range(nfilas)]
    for i in range(nfilas):
        for j in range(ncols):
            x = m[i][j]
            acum += x
            medias_filas[j] += x
            medias_cols[i] +=x
    for j in range(ncols):
        medias_filas[j] /= nfilas
    for i in range(nfilas):
        medias_cols[i] /= ncols
    return medias_filas, medias_cols, acum/(nfilas*ncols)
            
            
            
# ------------
# EJERCICIO 16
# ------------


# Definir una función producto_matrices(a,b), tal que recibiendo dos matrices
# a y b (representadas como listas de listas, tal y como se explica en el
# ejercicio anterior), devuelve la matriz resultante de multiplicar a y b
# matricialmente. Supondremos que el número de columnas de a es el mismo que
# el número de filas de b. 


# Por ejemplo:

# >>> a=[[3,1,4,5],[2,0,3,5],[1,1,4,1]]
# >>> b=[[1,2],[2,8],[4,3],[3,1]]
# >>> producto_matrices(a,b)
# [[36, 31], [29, 18], [22, 23]]

def agarracol(ms,n):
    l =[]
    for i in range(len(ms)):
        l += [ms[i][n]]
    return l

def producto_matrices(a,b):
    n = len(a)
    m = len(b[0])
    matrizprod = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrizprod[i][j] = producto_escalar(a[i],agarracol(b,j))
    return matrizprod 





# ------------
# EJERCICIO 17
# ------------
# Definir una función vocales_consonantes(s), que reciba una cadena de
# caracteres s (de letras mayúsculas) y escribe por pantalla, una a una, si
# sus letras son vocales o  consonantes.
# Ejemplo:
# >>> vocales_consonantes("INTELIGENCIA")
# I es vocal
# N es consonante
# T es consonante
# E es vocal
# L es consonante
# I es vocal
# G es consonante
# E es vocal
# N es consonante
# C es consonante
# I es vocal
# A es vocal
# ---------------------------------------------------------------------------

def vocales_consonantes(xs):
    for x in xs:
        if x in ["A","E","I","O","U"]:
            print(x, "es vocal")
        else:
            print(x, "es consonante")







# ------------
# EJERCICIO 18
# ------------
# Un número es perfecto si es la suma de todos sus divisores (excepto él
# mismo). Definir una función filtra_perfectos(n,m,p) que imprime por pantalla
# todos los números perfectos entre n y m que cumplen la condición p. Se pide
# también que se indiquen los divisores de cada número perfecto que se
# imprima. 

# Ejemplo:

# >>> filtra_perfectos(3,500, lambda x: True)
# El 6 es perfecto y sus divisores son [1, 2, 3]
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# El 496 es perfecto y sus divisores son [1, 2, 4, 8, 16, 31, 62, 124, 248]

# >>> filtra_perfectos(3,500, lambda x: (x%7==0))
# El 28 es perfecto y sus divisores son [1, 2, 4, 7, 14]
# ------------------------------------------------------------------------

def filtra_perfectos(n,m,p):
    for i in range (n, m+1):
        if p(i):
            div = [x for x in range(1,i//2+1) if i%x == 0]
            if suma(div) == i:
                print("El", i, "es perfecto y sus divisores son", div)
    return


# ------------
# EJERCICIO 19
# ------------
#

# Definir una función factoriza_primos(n), que recibiendo como entrada un número 
# natural n, cuya factorizaciçón en números primos es n=p1^e1*p2^e2*...*p_m^em,
# devueve la lista [(p1,e1),(p2,e2),...,(p_m,em)] 

# Ejemplos:

# >>> factoriza_primos(171)
# >>> [(3, 2), (19, 1)]
# >>> factoriza_primos(272250)
# [(2, 1), (3, 2), (5, 3), (11, 2)]
# >>> factoriza_primos(358695540883235472)
# [(2, 4), (3, 1), (7, 1), (83, 2), (173, 5)]

# NOTA: Hacerlo sin usar yna lista predefinida de números primos.
# SUGERENCIA: se puede hacer mediante dos bucles "while" anidados. 
# El más interno calcula el exponente de cada posible divisor del número, 
# dividiendo con ese divisor mientras sea divisible. 
# El bucle externo contendría al bucle interno
# y además iría incrementando en uno el valor de ese posible divisor.    
##### // >USO DE DOBLE BARRA ES UNA OPERACION DE DIVISION ENTRE ENTEROS,
##### NO NECESITA / QUE ES PARA FLOAT Y ES MAS COSTOSO
def factoriza_primos(n):
    avanzaprimos = 2
    listapares = []
    while n != 1:
        i = 0
        while (n%avanzaprimos == 0):
            n //= avanzaprimos
            i += 1
        if (i!=0):
            listapares += [(avanzaprimos,i)]
        avanzaprimos += 1
    return (listapares)

           









        
