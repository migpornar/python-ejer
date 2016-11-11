# ejercicios-02-ipppd.py
# Introducción a la Programación con Python y los Paradigmas de Datos

# Práctica 2: Introducción a Python
# =================================

import math

# -----------
# EJERCICIO 1
# -----------

# Usando como técnica principal la definición de secuencias por
# comprensión, definir las siguientes funciones:

# a) Dada una lista de números naturales, la suma de los cuadrados de los
#    números pares de la lista.

# Ejemplo:
# >>> suma_cuadrados([9,4,2,6,8,1])
# 120

def suma_cuadrados(xs):
    return sum(x**2 for x in xs if x%2 == 0)
##### no pongo corchetes para que no me genere la lista

def suma(xs)
    return sum(xs)


# b) dada una lista de números l=[a(1),...,a(n)], calcular el sumatorio de i=1
#    hasta n de i*a(i).

# ejemplo:

# >>> suma_formula([2,4,6,8,10])
# 110

def suma_formula(xs):
    return sum((i+1)*xs[i] for i in range(len(xs)))

# =============

# c) dados dos listas numéricas de la misma longitud, representado dos puntos
#    n-dimensionales, calcular la distancia euclídea entre ellos. 

# ejemplo:

# >>> distancia([3,1,2],[1,2,1])
# 2.449489742783178

def distancia (xs,ys):
    return math.sqrt(sum((x-y)**2 for x,y in zip(xs,ys)))
    
    
# ===========

# d) dada un par de listas (de la misma longitud) y una función de dos
#    argumentos, devolver la lista de los resultados de aplicar la función a
#    cada par de elementos que ocupan la misma posición en las listas de
#    entrada.


# ejemplo:

# >>> map2_mio((lambda x,y: x+y) ,[1,2,3,4],[5,2,7,9])
# [6, 4, 10, 13]

def map2_mio (f,xs,ys):
    return [f(x,y) for x,y in zip(xs,ys)]





# e) dada una lista de números, contar el número de elementos que sean múltiplos
#    de tres y distintos de cero. 

# ejemplo:

# >>> m3_no_nulos([4,0,6,7,0,9,18])
# 3

def m3_no_nulos(xs):
    return sum(x!=0 and x%3==0 for x in xs)
    ##porque el true y el false lo guarda como 1 y 0

# f) dadas dos listas de la misma longitud, contar el número de posiciones en
#    las que coinciden los elementos de ambas listas.  

# ejemplo:

# >>> cuenta_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# 3

def cuenta_coincidentes(xs,ys):
    return len([0 for x,y in zip(xs,ys) if x==y])

def cuenta_coincidentes2(xs,ys):
    return sum(x==y for x,y in zip(xs,ys))
 

    
# -----------
# ejercicio 2
# -----------
#
# 
# definir una función oculta_palabras(s) que reciba una cadena de caracteres
# (de letras minúsculas y posiblemente espacios) y devuelva la cadena de
# caracteres resultante de doblar cada consonante colocando una "o" enmedio y
# dejar el resto de caracteres igual
#
# ejemplo:
# >>> oculta_palabras("inteligencia")
# 'inontoteloligogenoncocia'
# ---------------------------------------------------------------------------
# [(x*x*x if x%3== 0 else (expr if (propiedad) else expr))]
def oculta_palabras(xs):
    lista = ""
    while xs != "":
        x = xs[0]
        if x in "aeiou ":
            lista += x
        else:
            lista += x + "o" + x
        xs = xs[1:]
    return lista
        
def oculta_palabras2(xs):
    lista = ""
    for x in xs:
        if x in "aeiou ":
            lista += x
        else:
            lista += x + "o" + x
    return lista
    
def oculta_palabras3(xs):
    lista = ""
    for c in xs:
        lista+=(c if c in "aeiou " else c+"o"+c)
    return lista
        

    
    
# -----------
# ejercicio 3
# -----------
#
# 
# definir, sin usar "slicing", una función es_palíndromo(s) que reconoce si
# una cadena s es un palíndromo o no (es decir que se lee igual de izquierda a
# dercha que de derecha a izquierda). para simplificar, supondremos que no hay
# espacios y que todas las letras son minúsculas y sin tilde. 

# ejemplos:
# >>> es_palindromo("reconocer")
# true
# >>> es_palindromo("inteligencia")
# false
# >>> es_palindromo("sometemos")
# true
# ---------------------------------------------------------------------------


def es_palindromo(xs):
    n = len(xs)
    return [] == [0 for i in range(n) if xs[n -i-1] != xs [i]]






# -----------
# ejercicio 4
# -----------
#
# 
# definir una función dibuja_caja(n) que recibiendo como entrada dos números
# naturales n y m, dibuja, usando el caracter "*", los lados de un rectángulo
# n x m 
# ejemplo:

# >>> dibuja_caja(10,6)
# **********
# *        *
# *        *
# *        *
# *        *
# **********
# -----------------------------------------------------------------------

def dibuja_caja(a,b):
    print("*"*a)
    for _ in range(b-2):
        print("*"+" "*(a-2) + "*")
    print("*"*a)




    


# -----------
# ejercicio 5
# -----------
#
# 
# antiguamente, cuando las impresoras eran matriciales y se compartían en un
# centro de trabajo, era normal que cada trabajo de impresión llevara una
# portada con dígitos de gran tamaño que indicaba el número del trabajo de
# impresión. estos dígitos estaban dibujados mediante algún carácter simple. 

# por ejemplo, lo que sigue es el número 0123456789 dibujado con asteriscos:

#   ***    *   ***   ***     *   *****  ***  *****  ***   ****  
#  *   *  **  *   * *   *   **   *     *         * *   * *   *
# *     *  *  *  *      *  * *   *     *        *  *   * *   *
# *     *  *    *     **  *  *    ***  ****    *    ***   ****
# *     *  *   *        * ******     * *   *  *    *   *     *
#  *   *   *  *     *   *    *   *   * *   * *     *   *     *
#   ***   *** *****  ***     *    ***   ***  *      ***      *

# definir una función dígitos_grandes(x) que recibiendo un número entero
# positivo, lo escriba por pantalla usando dígitos grandes. por ejemplo:


# >>> dígitos_grandes(8)
#   *** 
#  *   *
#  *   *
#   *** 
#  *   *
#  *   *
#   *** 
# >>> dígitos_grandes(4)
#     *  
#    **  
#   * *  
#  *  *  
#  ******
#     *  
#     *  

# indicación:

# puede ser de utilidad tener definidas las siguientes listas, que almacenan
# las distintas líneas que sirven para dibujar cada dígito grande:
 
cero = ["  ***  ", 
        " *   * ", 
        "*     *", 
        "*     *", 
        "*     *", 
        " *   * ", 
        "  ***  "]

uno = [" * ", 
       "** ", 
       " * ", 
       " * ", 
       " * ", 
       " * ", 
       "***"]

dos = [" *** ", 
       "*   *", 
       "*  * ", 
       "  *  ", 
       " *   ", 
       "*    ", 
       "*****"]

tres = [" *** ", 
        "*   *", 
        "    *", 
        "  ** ", 
        "    *", 
        "*   *", 
        " *** "]

cuatro = ["   *  ", 
          "  **  ", 
          " * *  ", 
          "*  *  ", 
          "******", 
          "   *  ", 
          "   *  "]

cinco = ["*****", 
         "*    ", 
         "*    ", 
         " *** ", 
         "    *", 
         "*   *", 
         " *** "]

seis = [" *** ", 
        "*    ", 
        "*    ", 
        "**** ", 
        "*   *", 
        "*   *", 
        " *** "]

siete = ["*****", 
         "    *", 
         "   * ", 
         "  *  ", 
         " *   ", 
         "*    ", 
         "*    "]

ocho = [" *** ", 
        "*   *", 
        "*   *", 
        " *** ", 
        "*   *", 
        "*   *", 
        " *** "]

nueve = [" ****", 
         "*   *", 
         "*   *", 
         " ****", 
         "    *", 
         "    *", 
         "    *"]


# ---------------------------------------------------------------------------

def digitos_grandes(n):
    listanum = str(n)
    lista = []
    for x in listanum:
        if x == "0":
            lista += [cero]
        elif x == "1":
            lista += [uno]
        elif x == "2":
            lista += [dos]
        elif x == "3":
            lista += [tres]
        elif x == "4":
            lista += [cuatro]
        elif x == "5":
            lista += [cinco]
        elif x == "6":
            lista += [seis]
        elif x == "7":
            lista += [siete]
        elif x == "8":
            lista += [ocho]
        elif x == "9":
            lista += [nueve]
    for i in range(7):
        stracum = ""
        for j in range(len(listanum)):
            stracum += lista[j][i] + " "
        print(stracum)

digitos = [cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve]

def digitos_grandes2(n):
    sn = str(n)
    for fila in range(7):
        linea = ""
        for digito in sn:
            linea += " " + digitos[int(digito)][fila]
        print(linea)
    

# -----------
# ejercicio 6
# -----------
#
# 
# definir una función aspa(a,c) que recibiendo un número natural a (impar y
# mayor que 2) y una cadena de caracteres c (de longitud 1), dibuja por
# pantalla una cruz en forma de aspa construida con el carácter dado c, con
# una altura de a líneas. definir la función de manera que el primer argumento
# se pueda dar con la clave "caracter" y el segundo argumento sea "o" por
# defecto.

# ejemplos:

# >>> aspa(7)
# o     o
#  o   o
#   o o
#    o
#   o o
#  o   o
# o     o
# >>> aspa(21,caracter="x")
# x                   x
#  x                 x
#   x               x
#    x             x
#     x           x
#      x         x
#       x       x
#        x     x
#         x   x
#          x x
#           x
#          x x
#         x   x
#        x     x
#       x       x
#      x         x
#     x           x
#    x             x
#   x               x
#  x                 x
# x                   x
# -------------------------------------------------------------------------------

####para que tenga argumentos de funciones por defecto
def aspa(a,c="o"):
    ran = a//2
    for i in range(ran):
        char = i*" " + c + (a-2*(i+1))*" " + c
        print(char)
    print(ran*" "+c)
    for i in range(ran):
        char = (ran - i -1)*" " + c + (1+2*i)*" " + c
        print(char)
    print()


# -----------
# ejercicio 7
# -----------


# definir la siguiente función usando comprensión. dadas dos listas de la
# misma longitud, devolver un diccionario que tiene como claves las posiciones
# en las que coinciden los elementos de ambas listas, y como valor de esas
# claves, el elemento coincidente.

# ejemplos:

# >>> dic_posiciones_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# {1: 2, 3: 8, 4: 9}
# >>> dic_posiciones_coincidentes([2,8,1,2,1,3],[1,8,1,2,1,6])
# {1: 8, 2: 1, 3: 2, 4: 1}

def dic_posiciones_coincidentes(xs,ys):
    return {i:xs[i] for i in range(len(xs)) if xs[i] == ys[i]}

### tambien se puede usar enumerate
def dic_posiciones_coincidentes2(xs,ys):
    return {i:x for i,(x,y) in enumerate(zip(xs,ys)) if x == y}

# -----------
# ejercicio 8
# -----------
#
# supongamos que recibimos un diccionario cuyas claves son cadenas de
# caracteres de longitud uno y los valores asociados son números enteros 
# entre 0 y 50. 
# definir una función histograma_horizontal(d), que recibiendo un diccionario 
# de ese tipo, escribe un histograma de barras horizontales asociado, 
# como se ilustra en el siguiente ejemplo:  

# >>> d1={"a":5,"b":10,"c":12,"d":11,"e":15,"f":20,
#         "g":15,"h":9,"i":7,"j":2}
# >>> histograma_horizontal(d1)
# a: *****
# b: **********
# c: ************
# d: ***********
# e: ***************
# f: ********************
# g: ***************
# h: *********
# i: *******
# j: **
#
# nota: imprimir las barras, de arriba a abajo, en el orden que determina la
#         función "sorted" sobre las claves 
# ---------------------------------------------------------------------------

def histograma_horizontal(dic):
    for (l,n) in sorted(dic.items()):
        print(l + ": "+ n*"*") 

### usando la funcion format

def histograma_horizontal2(dic):
    for k,v in sorted(dic.items()):
        print("{}: {}".format(k,"*"*v))

# ------------
# ejercicio 9
# ------------
# con la misma entrada que el ejercicio anterior, definir una función
# histograma_vertical(d) que imprime el mismo histograma pero con las barras
# en vertical. 

# ejemplo:

# >>> d2={"a":5,"b":7,"c":9,"d":12,"e":15,"f":20,"g":15,"h":9,"i":7,"j":2}
# >>> histograma_vertical(d2)
#           *         
#           *         
#           *         
#           *         
#           *         
#         * * *       
#         * * *       
#         * * *       
#       * * * *       
#       * * * *       
#       * * * *       
#     * * * * * *     
#     * * * * * *     
#   * * * * * * * *   
#   * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * *   
# * * * * * * * * * * 
# * * * * * * * * * * 
# a b c d e f g h i j

# >>> histograma_vertical(d2,"x")
#           x         
#           x         
#           x         
#           x         
#           x         
#         x x x       
#         x x x       
#         x x x       
#       x x x x       
#       x x x x       
#       x x x x       
#     x x x x x x     
#     x x x x x x     
#   x x x x x x x x   
#   x x x x x x x x   
# x x x x x x x x x   
# x x x x x x x x x   
# x x x x x x x x x   
# x x x x x x x x x x 
# x x x x x x x x x x 
# a b c d e f g h i j 


# >>> histograma_vertical(d2,"o",true)
#           o         
#           o         
#           o         
#           o         
#           o         
#         o o o       
#         o o o       
#         o o o       
#       o o o o       
#       o o o o       
#       o o o o       
#     o o o o o o     
#     o o o o o o     
#   o o o o o o o o   
#   o o o o o o o o   
# o o o o o o o o o   
# o o o o o o o o o   
# o o o o o o o o o   
# o o o o o o o o o o 
# o o o o o o o o o o 
# --------------------
# a b c d e f g h i j 


# nota: imprimir las barras, de izquierda a derecha, en el orden que determina la
#         función "sorted" sobre las claves 
# ---------------------------------------------------------------------------

def histograma_vertical(dic,c="*",header=false):
    lista = sorted(dic.items())
    maxi = max(dic.values())
    for nlinea in range(maxi,0,-1):
        acumlin = ""
        for _,numero in lista:
            if numero >= nlinea:
                acumlin += c + " "
            else:
                acumlin += "  "
        print(acumlin)
    acumlin = ""
    if header:
        print("--"*len(lista))
    for letra,_ in lista:
        acumlin += letra + " "
    print(acumlin)
    return

### con la funcion join: va intercalando entre ks, espacios " "

def histograma_vertical2(d):
    ks = sorted(d.keys())
    maxv = max(d.values())
    for altura in range(maxv,0,-1):
        lin=""
        for k in ks:
            lin += ("* " if d[k] >= altura else "  ")
        print(lin)
    print(" ".join(ks))
    
    
# ------------
# ejercicio 10
# ------------
#
# 
# supongamos que tenemos almacenada, usando diccionario, la información sobre
# el grupo de los alumnos de un curso. para ello, usamos como clave el nombre
# de los alumnos de un grupo y como valor el grupo que tienen asignado. 

# 1) definir una función alumnos_grupo(d) que a partir de un diccionario
# de ese tipo, devuelve otro diccionario cuyas claves son los nombres de los
# grupos y cuyo valor asignado a cada clave es la lista los alumnos que
# forman parte del grupo.

# ejemplos:

# >>> alum={"juan":"g1", "rosa":"g2"  , "joaquín":"g1"   ,"carmen":"g2"  ,"isabel":"g1" , "rocío":"g3" , "bernardo":"g3", "jesús":"g2"}
# >>> grupos=alumnos_grupo(alum)
# >>> grupos
# {'g3': ['rocío', 'bernardo'], 'g2': ['jesús', 'carmen', 'rosa'], 
#  'g1': ['isabel', 'juan', 'joaquín']}

#####################*******recheck
def alumnos_grupo(d):
    dg = dict()
    for n,g in d.items():
        if d[n] in dg:
            dg[g] += [n]
        else:
            dg[g] = [n]
    return dg
                  

# 2) definir una función nuevo_alumno(dict_n,dict_g,nombre,grupo) tal que
# supuesto que dict_n y dict_g son dos variables conteniendo respectivamente
# el grupo de cada alumno y los alumnos de cada grupo, introduce un nuevo
# alumno con su nombre y grupo, modificando adecuadamente tanto dict_n como
# dict_g. si el alumno ya está en los diccionarios, modificar el dato
# existente (en ese caso, si además el grupo que se quiere asignar no coincide
# que el que ya tiene se mostrará un mensaje de advertencia). si se asigna un
# grupo que no está dado de alta, la correspondiente entrada se debe añadir al
# diccionario de grupos.
# >>> grupos
# {'g3': ['rocío', 'bernardo'], 'g2': ['jesús', 'carmen', 'rosa'], 
#  'g1': ['isabel', 'juan', 'joaquín']}
# ejemplos:

# >>> nuevo_alumno(alum,grupos,"bernardo","g3")
# no actualizado. el alumno bernardo ya está dado de alta en el grupo g3
# >>> alum
# {'isabel': 'g1', 'jesús': 'g2', 'rocío': 'g3', 'juan': 'g1', 'carmen': 'g2', 
#  'rosa': 'g2', 'joaquín': 'g1', 'bernardo': 'g3'}
# >>> nuevo_alumno(alum,grupos,"bernardo","g1")
# el alumno bernardo ya está dado de alta. se cambia al grupo g1
# >>> alum
# {'isabel': 'g1', 'jesús': 'g2', 'rocío': 'g3', 'juan': 'g1', 'carmen': 'g2', 
#  'rosa': 'g2', 'joaquín': 'g1', 'bernardo': 'g1'}
# >>> grupos
# {'g3': ['rocío'], 'g2': ['jesús', 'carmen', 'rosa'], 
#  'g1': ['isabel', 'juan', 'joaquín', 'bernardo']}
# >>> nuevo_alumno(alum,grupos,"ana","g3")
# nuevo alumno ana. incluido en el grupo g3
# >>> nuevo_alumno(alum,grupos,"juan","g4")
# el alumno juan ya está dado de alta. se cambia al grupo g4
# >>> alum
# {'isabel': 'g1', 'jesús': 'g2', 'rocío': 'g3', 'ana': 'g3', 'juan': 'g4', 'carmen': 'g2', 
#  'rosa': 'g2', 'joaquín': 'g1', 'bernardo': 'g1'}
# >>> grupos
# {'g4': ['juan'], 'g3': ['rocío', 'ana'], 'g2': ['jesús', 'carmen', 'rosa'], 
#  'g1': ['isabel', 'joaquín', 'bernardo']}
# --------------------------------------------------------------------------

def nuevo_alumno(dicn,dicg,nombre,grupo):
    a = dicn.get(nombre)
    if a == none:
        dicn[nombre] = grupo
        dicg[grupo] += [nombre]
        print("nuevo alumno", nombre,". incluido en el grupo", grupo)
    elif grupo == a:
        print("no actualizado. el alumno", nombre, "ya está dado de alta en el grupo", grupo)
    else:
        dicn[nombre] = grupo
        if grupo in dicg:
            dicg[a] = [x for x in dicg[a] if x != nombre]
            dicg[grupo] += [nombre]
        else:
            dicg[a] = [x for x in dicg[a] if x != nombre]
            dicg[grupo] = [nombre]
        print("el alumno", nombre, "ya está dado de alta. se cambia al grupo", grupo)
    return
            

# ------------
# ejercicio 11
# ------------
#
# 
# definir, usando definición de listas por comprensión, una función
# sustituye(x,y,l) que obtiene el resultado de sustituir en l todas las
# ocurrencias (a primer nivel) de x por y.

# ejemplo:

# >>> sustituye("a","b",["q","w","a","b","a","a","c"])
# ['q', 'w', 'b', 'b', 'b', 'b', 'c']
# >>> sustituye("a","b",["q","w",["a","b"],"a","a","c"])
# ['q', 'w', ['a', 'b'], 'b', 'b', 'c']
# -----------------------------------------------------------------------

def sustituye(x,y,ls):
    return([y if x == l else l for l in ls])


# ------------
# ejercicio 12
# ------------
#
# 
# decimos que el elemento a_ij de una matriz cuadrada a es un punto de silla
# si es el máximo de los elementos de la fila i y el mínimo de los elementos
# de la columna j.  es posible probar que una matriz cuyos elementos son
# todos distintos tiene a lo sumo un único punto de silla.  
# definir una función silla que recibiendo como entrada una matriz a
# (representada mediante la lista de sus filas) con números distintos, 
# devuelva la tupla (i, j) tal que el elemento a_ij es un punto de silla de
# a. devolver false si la matriz no tiene puntos de silla. 

# ejemplos:

# >>> punto_de_silla([[1,2,3],[4,5,6],[7,8,9]])
# (0, 2)
# >>> punto_de_silla([[11,12],[14,9]])
# false
# >>> punto_de_silla([[1,4,3,2],[9,8,7,6],[5,10,11,13],[12,14,15,16]])
# (0, 1)
# -------------------------------------------------------------------------


def punto_de_silla(xss):
    n = len(xss)
    m = len(xss[0])
    for i in range(n):
        for j in range(m):
            valor = xss[i][j]
            if max(xss[i]) == valor and min([colum[j] for colum in xss]) == valor:
                return i,j
    return false
        

# ------------
# ejercicio 13
# ------------
#
# 
# definir la función mezcla(l1,l2) que recibe como argumentos dos listas
# numéricas ordenadas de menor a mayor y devuelve la mezcla ordenada de dichas
# listas.  por ejemplo: 

# >>> mezcla([3,7,8,11,13],[1,4,9,10])
# [1, 3, 4, 7, 8, 9, 10, 11, 13]
# --------------------------------------------------------------------

def mezcla(xs,ys):
    lista = []
    while (xs != [] and ys != []):
        a = xs[0]
        b = ys[0]
        if a < b:
            lista += [a]
            xs = xs[1:]
        else:
            lista +=[b]
            ys = ys[1:]
    if xs == []:
        lista += ys
    else:
        lista += xs
    return lista

### por recursion
def mezcla2(xs,ys):
    lista = []
    if (xs != [] and ys != []):
        a = xs[0]
        b = ys[0]
        if a < b:
            lista = [a]
            xs = xs[1:]
        else:
            lista =[b]
            ys = ys[1:]
    elif xs == []:
        return(lista + ys)
    else:
        return(lista + xs)
    return(lista + mezcla(xs,ys))



# ------------
# ejercicio 14
# ------------
#
# 
# en este ejercicio vamos a "comprimir" y "descomprimir" listas.

#  apartado (a).
#  definir la función compresion(l) que devuelva la lista resultante de
#  comprimir la lista l que recibe como entrada, en el siguiente sentido: 
#  * si el elemento x aparece n (n > 1) veces de manera consecutiva en l
#    sustituimos esas n ocurrencias por la tupla (n, x)
#  * si el elemento x es distinto de sus vecinos, entonces lo dejamos
#    igual
#  ejemplo:
 
#  >>> compresion([1, 1, 1, 2, 1, 3, 2, 4, 4, 6, 8, 8, 8])
#  [[3, 1], 2, 1, 3, 2, [2, 4], 6, [3, 8]]
#  >>> compresion(["a", "a", "a", "b", "a", "c", "b", "d", "d", "f", "h", "h", "h"])
#  [[3, 'a'], 'b', 'a', 'c', 'b', [2, 'd'], 'f', [3, 'h']]

#  apartado (b).
#  definir la función descompresion(l) que devuelva la lista l descomprimida,
#  suponiendo que ha sido comprimida con el método del apartado anterior.
#  ejemplo:

#  >>> descompresion([[3, 1], 2, 1, 3, 2, [2, 4], 6, [3, 8]])
#  [1, 1, 1, 2, 1, 3, 2, 4, 4, 6, 8, 8, 8]
# ----------------------------------------------------------------------------


def compresion(xs):
    elem = xs[0]
    acum = 0
    lista = []
    for x in xs:
        if x == elem:
            acum += 1
        elif acum == 1:
            lista += [elem]
            elem = x
            acum = 1
        else:
            lista += [[acum,elem]]
            elem = x
            acum = 1
    lista += [[acum,elem]]
    return lista

    
def descompresion(xs):
    lista = []
    for x in xs:
        if list == type(x):
            for _ in range(x[0]):
                lista += [x[1]]
        else:
            lista += [x]
    return lista
### uso de la funcion type
























