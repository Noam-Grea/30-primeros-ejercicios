# Ejercicio 1 
# str contene la frase y print la imprima por pantalla
def ejercicio1():
    str = "Hola, ya se imprimir frases"
    print(str)

# Ejercicio 2
# ent contene el entero y print le imprima por pantalla
def ejercicio2():
    ent = 273
    print(ent)

# Ejercicio 3
# dec contene el decimal y print le imprima por pantalla
def ejercicio3():
    dec = 5.3
    print(dec)

# Ejercicio 4
# sum contene la soma de 1234 y 532 y print la imprima por pantalla
def ejercicio4():
    sum = 1234+532
    print(sum)

# Ejercicio 5
# rest contene la rest de 1234 y 532 y print la imprima por pantalla
def ejercicio5():
    rest = 1234-532
    print(rest)

# Ejercicio 6
# mult contene la multiplicacion de 1234 y 532 y print la imprima por pantalla
def ejercicio6():
    mult = 1234*532
    print(mult)

# Ejercicio 7
# div contene la division de 1234 entre 532 y print la imprima por pantalla
def ejercicio7():
    div = 1234-532
    print(div)

# Ejercicio 8
# i toma los valores enteras de 0 a 2 y print imprima por pantalla los i+1 
def ejercicio8():
    for i in range(3):
        print(i+1)

# Ejercicio 9
# i toma los valores enteras de 0 a 8 y print imprima por pantalla los i+1 
def ejercicio9():
    for i in range(9):
        print(i+1)

# Ejercicio 10
# i toma los valores enteras de 0 a 9999 y print imprima por pantalla los i+1 
def ejercicio10():
    for i in range(10000):
        print(i+1)

# Ejercicio 11
# i toma los valores enteras de 5 a 10 y print imprima por pantalla los i 
def ejercicio11():
    for i in range(5,11):
        print(i)

# Ejercicio 12
# i toma los valores enteras de 5 a 15 y print imprima por pantalla los i 
def ejercicio12():
    for i in range(5,16):
        print(i)

# Ejercicio 13
# i toma los valores enteras de 5 a 15000 y print imprima por pantalla los i 
def ejercicio13():
    for i in range(5,15001):
        print(i)

# Ejercicio 14
# en la bucle while i se incrementa de uno y print imprima hola por pantalla hasta que i=200
def ejercicio14():
    i=1
    while i<=200:
        print("hola")
        i=i+1

# Ejercicio 15
# i contene los 30 primeros numeros naturales y cuad su cuadrado, print imprima por pantalla los cuadrados
def ejercicio15():
    for i in range(1,31):
        cuad=i**2
        print(cuad)

# Ejercicio 16
# i toma los valores de los 20 primeros numero naturales sin el 1 y en cada iteracion de la bucle el programa multiplica res con i
def ejercicio16():
    res=1
    for i in range(2,21):
        res=res*i
    print(res)

# Ejercicio 17
# res es la soma de los cuadrados de los i primeros numeros naturales y en cada iteracion de la bucle el cuadrado de i es adicionado a res
def ejercicio17():
    res = 0
    for i in range(1,101):
        res=res+i**2
    print(res)

# Ejercicio 18
# num es el numero entero ingreso por el utilizador y i toma los valores de los 100 numero siguientes
def ejercicio18(num):
    for i in range((num+1),(num+101)):
        print(i)

# Ejercicio 19
# euro es el decimal ingreso por el utilizador, tazo es el tazo de conversion entre euros y dolares y dolares es la cantidad correspondiente en dolares  
def ejercicio19(euro):
    tazo = 1.08
    dolares = euro*tazo
    print(dolares)

# Ejercicio 20
# x y son la altura y anchura ingresadas por el utilizador y area es la area del rectangulo xy
def ejercicio20(x, y):
    area=x*y
    print(area)

# Ejercicio 21
# x y son los dos numeros y el if compara los dos
def ejercicio21(x, y):
    if x < y:
        print("x : ",x," es el menor, y : ",y," es el mayor ")
    else:
        print("y : ",y," es el menor, x : ",x," es el mayor ")

# Ejercicio 22
# x es el numero entero y por todos los numeros menores el if verifica si son impares
def ejercicio22(x):
    for i in range(x):
        if i%2==1:
            print(i)
    
# Ejercicio 23
def ejercicio23(x,y):
    d=y
    r=x%y
    # r es el resto de la division de x entre y
    while r!=0:
        # el algoritmo se acaba cuando r=0
        div=d
        # div es la valor de d
        d=r
        r=div%r
        # d toma la valor de r y r el resto de la division entre d y r
    print(d)

# Ejercicio 24
def ejercicio24(a, b, c):
    discr = b**2 - 4*a*c
    #disr es el discriminante de la ecuacion
    
    # el if verifica si el discriminante es positivo, negativo o cero
    if discr < 0:
        print("la ecuacion no tiene soluciones")
    elif discr == 0:
        # calcul de la unica solucion
        x = -b / (2 * a)
        print("la ecuacion tiene una solucion: x = ",x,)
    else:
        # calcul de las dos soluciones 
        x1 = (-b + discr**0.5) / (2 * a)
        x2 = (-b - discr**0.5) / (2 * a)
        print("la ecuacion tiene dos soluciones: x1 = ",x1," y x2 = ",x2,)


# Ejercicio 25
def factorial(n):
    if n == 0:
        # factorial de 0 es 1
        return 1
    else:
        return n * factorial(n - 1)
        # llamada recursiva donde n se multiplica con factorial de n-1

def ackermann(x, y):
    
    if x == 0:
        return y + 1
    # si x = 0 la función retorna y + 1
    elif x > 0 and y == 0:
        return ackermann(x - 1, 1)
    # si x > 0 y y = 0 la función calcula A(x-1, 1)
    else:
        return ackermann(x - 1, ackermann(x, y - 1))
    # llamada recursiva donde la función calcula A(x-1, A(x, y-1))

# Ejercicio 26
def ejercicio26(a,b,c):
    menor=min(a,b,c)
    # min calcula el menor entre a, b y c
    mayor=max(a,b,c)
    # max calcula el mayor entre a, b y c
    print("el mayor es ",mayor,"y el menor es ",menor)

# Ejercicio 27
def ejercicio27():
    while True:
        temp_far=float(input("temperatura fahrenheit : "))
        if temp_far == 999:
            break
        else:
            temp_cel = (temp_far-32)*(5/9)
            print("temperatura celcius",temp_cel)

ejercicio27()