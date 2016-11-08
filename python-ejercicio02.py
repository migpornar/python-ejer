# ejercicios-02-ipppd.py
# Introducción a la Programación con Python y los Paradigmas de Datos

# Práctica 2: Introducción a Python
# =================================

import math

# -----------
# EJERCICIO 1
# -----------

# Usando como técnica principal la definición de secuencias por comprensión,
# definir las siguientes funciones:

# a) Dada una lista de números naturales, la suma de los cuadrados de los
#    números pares de la lista.

# Ejemplo:
# >>> suma_cuadrados([9,4,2,6,8,1])
# 120

def suma_cuadrados(xs):
    return sum(x**2 for x in xs if x%2 == 0)
##### NO PONGO CORCHETES PARA QUE NO ME GENERE LA LISTA




# b) Dada una lista de números l=[a(1),...,a(n)], calcular el sumatorio de i=1
#    hasta n de i*a(i).

# Ejemplo:

# >>> suma_formula([2,4,6,8,10])
# 110

def suma_formula(xs):
    return sum((i+1)*xs[i] for i in range(len(xs)))

# =============

# c) Dados dos listas numéricas de la misma longitud, representado dos puntos
#    n-dimensionales, calcular la distancia euclídea entre ellos. 

# Ejemplo:

# >>> distancia([3,1,2],[1,2,1])
# 2.449489742783178

def distancia (xs,ys):
    return math.sqrt(sum((x-y)**2 for x,y in zip(xs,ys)))
    
    
# ===========

# d) Dada un par de listas (de la misma longitud) y una función de dos
#    argumentos, devolver la lista de los resultados de aplicar la función a
#    cada par de elementos que ocupan la misma posición en las listas de
#    entrada.


# Ejemplo:

# >>> map2_mio((lambda x,y: x+y) ,[1,2,3,4],[5,2,7,9])
# [6, 4, 10, 13]

def map2_mio (f,xs,ys):
    return [f(x,y) for x,y in zip(xs,ys)]





# e) Dada una lista de números, contar el número de elementos que sean múltiplos
#    de tres y distintos de cero. 

# Ejemplo:

# >>> m3_no_nulos([4,0,6,7,0,9,18])
# 3

def m3_no_nulos(xs):
    return sum(x!=0 and x%3==0 for x in xs)
    ##PORQUE EL TRUE Y EL FALSE LO GUARDA COMO 1 Y 0

# f) Dadas dos listas de la misma longitud, contar el número de posiciones en
#    las que coinciden los elementos de ambas listas.  

# Ejemplo:

# >>> cuenta_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# 3

def cuenta_coincidentes(xs,ys):
    return len([0 for x,y in zip(xs,ys) if x==y])

def cuenta_coincidentes2(xs,ys):
    return sum(x==y for x,y in zip(xs,ys))
 

    
# -----------
# EJERCICIO 2
# -----------
#
# 
# Definir una función oculta_palabras(s) que reciba una cadena de caracteres
# (de letras minúsculas y posiblemente espacios) y devuelva la cadena de
# caracteres resultante de doblar cada consonante colocando una "o" enmedio y
# dejar el resto de caracteres igual
#
# Ejemplo:
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
# EJERCICIO 3
# -----------
#
# 
# Definir, sin usar "slicing", una función es_palíndromo(s) que reconoce si
# una cadena s es un palíndromo o no (es decir que se lee igual de izquierda a
# dercha que de derecha a izquierda). Para simplificar, supondremos que no hay
# espacios y que todas las letras son minúsculas y sin tilde. 

# Ejemplos:
# >>> es_palindromo("reconocer")
# True
# >>> es_palindromo("inteligencia")
# False
# >>> es_palindromo("sometemos")
# True
# ---------------------------------------------------------------------------


def es_palindromo(xs):
    n = len(xs)
    return [] == [0 for i in range(n) if xs[n -i-1] != xs [i]]






# -----------
# EJERCICIO 4
# -----------
#
# 
# Definir una función dibuja_caja(n) que recibiendo como entrada dos números
# naturales n y m, dibuja, usando el caracter "*", los lados de un rectángulo
# n x m 
# Ejemplo:

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
# EJERCICIO 5
# -----------
#
# 
# Antiguamente, cuando las impresoras eran matriciales y se compartían en un
# centro de trabajo, era normal que cada trabajo de impresión llevara una
# portada con dígitos de gran tamaño que indicaba el número del trabajo de
# impresión. Estos dígitos estaban dibujados mediante algún carácter simple. 

# Por ejemplo, lo que sigue es el número 0123456789 dibujado con asteriscos:

#   ***    *   ***   ***     *   *****  ***  *****  ***   ****  
#  *   *  **  *   * *   *   **   *     *         * *   * *   *
# *     *  *  *  *      *  * *   *     *        *  *   * *   *
# *     *  *    *     **  *  *    ***  ****    *    ***   ****
# *     *  *   *        * ******     * *   *  *    *   *     *
#  *   *   *  *     *   *    *   *   * *   * *     *   *     *
#   ***   *** *****  ***     *    ***   ***  *      ***      *

# Definir una función dígitos_grandes(x) que recibiendo un número entero
# positivo, lo escriba por pantalla usando dígitos grandes. Por ejemplo:


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

# INDICACIÓN:

# Puede ser de utilidad tener definidas las siguientes listas, que almacenan
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
# EJERCICIO 6
# -----------
#
# 
# Definir una función aspa(a,c) que recibiendo un número natural a (impar y
# mayor que 2) y una cadena de caracteres c (de longitud 1), dibuja por
# pantalla una cruz en forma de aspa construida con el carácter dado c, con
# una altura de a líneas. Definir la función de manera que el primer argumento
# se pueda dar con la clave "caracter" y el segundo argumento sea "o" por
# defecto.

# Ejemplos:

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

####PARA QUE TENGA ARGUMENTOS DE FUNCIONES POR DEFECTO
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
# EJERCICIO 7
# -----------


# Definir la siguiente función usando comprensión. Dadas dos listas de la
# misma longitud, devolver un diccionario que tiene como claves las posiciones
# en las que coinciden los elementos de ambas listas, y como valor de esas
# claves, el elemento coincidente.

# Ejemplos:

# >>> dic_posiciones_coincidentes([4,2,6,8,9,3],[3,2,1,8,9,6])
# {1: 2, 3: 8, 4: 9}
# >>> dic_posiciones_coincidentes([2,8,1,2,1,3],[1,8,1,2,1,6])
# {1: 8, 2: 1, 3: 2, 4: 1}

def dic_posiciones_coincidentes(xs,ys):
    return {i:xs[i] for i in range(len(xs)) if xs[i] == ys[i]}

### TAMBIEN SE PUEDE USAR ENUMERATE
def dic_posiciones_coincidentes2(xs,ys):
    return {i:x for i,(x,y) in enumerate(zip(xs,ys)) if x == y}

# -----------
# EJERCICIO 8
# -----------
#
# Supongamos que recibimos un diccionario cuyas claves son cadenas de
# caracteres de longitud uno y los valores asociados son números enteros 
# entre 0 y 50. 
# Definir una función histograma_horizontal(d), que recibiendo un diccionario 
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
# Nota: imprimir las barras, de arriba a abajo, en el orden que determina la
#         función "sorted" sobre las claves 
# ---------------------------------------------------------------------------

def histograma_horizontal(dic):
    for (l,n) in sorted(dic.items()):
        print(l + ": "+ n*"*") 

### USANDO LA FUNCION FORMAT

def histograma_horizontal2(dic):
    for k,v in sorted(dic.items()):
        print("{}: {}".format(k,"*"*v))

# ------------
# EJERCICIO 9
# ------------
# Con la misma entrada que el ejercicio anterior, definir una función
# histograma_vertical(d) que imprime el mismo histograma pero con las barras
# en vertical. 

# Ejemplo:

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


# >>> histograma_vertical(d2,"o",True)
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


# Nota: imprimir las barras, de izquierda a derecha, en el orden que determina la
#         función "sorted" sobre las claves 
# ---------------------------------------------------------------------------

def histograma_vertical(dic,c="*",header=False):
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

### CON LA FUNCION JOIN: VA INTERCALANDO ENTRE ks, ESPACIOS " "

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
# EJERCICIO 10
# ------------
#
# 
# Supongamos que tenemos almacenada, usando diccionario, la información sobre
# el grupo de los alumnos de un curso. Para ello, usamos como clave el nombre
# de los alumnos de un grupo y como valor el grupo que tienen asignado. 

# 1) Definir una función alumnos_grupo(d) que a partir de un diccionario
# de ese tipo, devuelve otro diccionario cuyas claves son los nombres de los
# grupos y cuyo valor asignado a cada clave es la lista los alumnos que
# forman parte del grupo.

# Ejemplos:

# >>> alum={"Juan":"G1", "Rosa":"G2"  , "Joaquín":"G1"   ,"Carmen":"G2"  ,"Isabel":"G1" , "Rocío":"G3" , "Bernardo":"G3", "Jesús":"G2"}
# >>> grupos=alumnos_grupo(alum)
# >>> grupos
# {'G3': ['Rocío', 'Bernardo'], 'G2': ['Jesús', 'Carmen', 'Rosa'], 
#  'G1': ['Isabel', 'Juan', 'Joaquín']}

#####################*******recheck
def alumnos_grupo(d):
    dg = dict()
    for n,g in d.items():
        if d[n] in dg:
            dg[g] += [n]
        else:
            dg[g] = [n]
    return dg
                  

# 2) Definir una función nuevo_alumno(dict_n,dict_g,nombre,grupo) tal que
# supuesto que dict_n y dict_g son dos variables conteniendo respectivamente
# el grupo de cada alumno y los alumnos de cada grupo, introduce un nuevo
# alumno con su nombre y grupo, modificando adecuadamente tanto dict_n como
# dict_g. Si el alumno ya está en los diccionarios, modificar el dato
# existente (en ese caso, si además el grupo que se quiere asignar no coincide
# que el que ya tiene se mostrará un mensaje de advertencia). Si se asigna un
# grupo que no está dado de alta, la correspondiente entrada se debe añadir al
# diccionario de grupos.
# >>> grupos
# {'G3': ['Rocío', 'Bernardo'], 'G2': ['Jesús', 'Carmen', 'Rosa'], 
#  'G1': ['Isabel', 'Juan', 'Joaquín']}
# Ejemplos:

# >>> nuevo_alumno(alum,grupos,"Bernardo","G3")
# No actualizado. El alumno Bernardo ya está dado de alta en el grupo G3
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Juan': 'G1', 'Carmen': 'G2', 
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G3'}
# >>> nuevo_alumno(alum,grupos,"Bernardo","G1")
# El alumno Bernardo ya está dado de alta. Se cambia al grupo G1
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Juan': 'G1', 'Carmen': 'G2', 
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G1'}
# >>> grupos
# {'G3': ['Rocío'], 'G2': ['Jesús', 'Carmen', 'Rosa'], 
#  'G1': ['Isabel', 'Juan', 'Joaquín', 'Bernardo']}
# >>> nuevo_alumno(alum,grupos,"Ana","G3")
# Nuevo alumno Ana. Incluido en el grupo G3
# >>> nuevo_alumno(alum,grupos,"Juan","G4")
# El alumno Juan ya está dado de alta. Se cambia al grupo G4
# >>> alum
# {'Isabel': 'G1', 'Jesús': 'G2', 'Rocío': 'G3', 'Ana': 'G3', 'Juan': 'G4', 'Carmen': 'G2', 
#  'Rosa': 'G2', 'Joaquín': 'G1', 'Bernardo': 'G1'}
# >>> grupos
# {'G4': ['Juan'], 'G3': ['Rocío', 'Ana'], 'G2': ['Jesús', 'Carmen', 'Rosa'], 
#  'G1': ['Isabel', 'Joaquín', 'Bernardo']}
# --------------------------------------------------------------------------

def nuevo_alumno(dicn,dicg,nombre,grupo):
    a = dicn.get(nombre)
    if a == None:
        dicn[nombre] = grupo
        dicg[grupo] += [nombre]
        print("Nuevo alumno", nombre,". Incluido en el grupo", grupo)
    elif grupo == a:
        print("No actualizado. El alumno", nombre, "ya está dado de alta en el grupo", grupo)
    else:
        dicn[nombre] = grupo
        if grupo in dicg:
            dicg[a] = [x for x in dicg[a] if x != nombre]
            dicg[grupo] += [nombre]
        else:
            dicg[a] = [x for x in dicg[a] if x != nombre]
            dicg[grupo] = [nombre]
        print("El alumno", nombre, "ya está dado de alta. Se cambia al grupo", grupo)
    return
            

# ------------
# EJERCICIO 11
# ------------
#
# 
# Definir, usando definición de listas por comprensión, una función
# sustituye(x,y,l) que obtiene el resultado de sustituir en l todas las
# ocurrencias (a primer nivel) de x por y.

# Ejemplo:

# >>> sustituye("a","b",["q","w","a","b","a","a","c"])
# ['q', 'w', 'b', 'b', 'b', 'b', 'c']
# >>> sustituye("a","b",["q","w",["a","b"],"a","a","c"])
# ['q', 'w', ['a', 'b'], 'b', 'b', 'c']
# -----------------------------------------------------------------------

def sustituye(x,y,ls):
    return([y if x == l else l for l in ls])


# ------------
# EJERCICIO 12
# ------------
#
# 
# Decimos que el elemento a_ij de una matriz cuadrada A es un punto de silla
# si es el máximo de los elementos de la fila i y el mínimo de los elementos
# de la columna j.  Es posible probar que una matriz cuyos elementos son
# todos distintos tiene a lo sumo un único punto de silla.  
# Definir una función silla que recibiendo como entrada una matriz A
# (representada mediante la lista de sus filas) con números distintos, 
# devuelva la tupla (i, j) tal que el elemento a_ij es un punto de silla de
# A. Devolver False si la matriz no tiene puntos de silla. 

# Ejemplos:

# >>> punto_de_silla([[1,2,3],[4,5,6],[7,8,9]])
# (0, 2)
# >>> punto_de_silla([[11,12],[14,9]])
# False
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
    return False
        

# ------------
# EJERCICIO 13
# ------------
#
# 
# Definir la función mezcla(l1,l2) que recibe como argumentos dos listas
# numéricas ordenadas de menor a mayor y devuelve la mezcla ordenada de dichas
# listas.  Por ejemplo: 

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

### POR RECURSION
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
# EJERCICIO 14
# ------------
#
# 
# En este ejercicio vamos a "comprimir" y "descomprimir" listas.

#  Apartado (a).
#  Definir la función compresion(l) que devuelva la lista resultante de
#  comprimir la lista l que recibe como entrada, en el siguiente sentido: 
#  * Si el elemento x aparece n (n > 1) veces de manera consecutiva en l
#    sustituimos esas n ocurrencias por la tupla (n, x)
#  * Si el elemento x es distinto de sus vecinos, entonces lo dejamos
#    igual
#  Ejemplo:
 
#  >>> compresion([1, 1, 1, 2, 1, 3, 2, 4, 4, 6, 8, 8, 8])
#  [[3, 1], 2, 1, 3, 2, [2, 4], 6, [3, 8]]
#  >>> compresion(["a", "a", "a", "b", "a", "c", "b", "d", "d", "f", "h", "h", "h"])
#  [[3, 'a'], 'b', 'a', 'c', 'b', [2, 'd'], 'f', [3, 'h']]

#  Apartado (b).
#  Definir la función descompresion(l) que devuelva la lista l descomprimida,
#  suponiendo que ha sido comprimida con el método del apartado anterior.
#  Ejemplo:

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
### USO DE LA FUNCION TYPE
























