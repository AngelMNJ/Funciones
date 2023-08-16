# FUNCION 1 #
import random
import math
import time

def numero_aleatorio(num1 = None, num2 = None):
    while True:
        if num1 is None:
            num1 = float(input("Intrese el primer numero del rango: "))
        if num2 is None:
            num2 = float(input("Ingrese el segumdo numero del rango: "))    
        numero_random = input(random.randint(num1, num2))
        print(f"Numero random: {numero_random}")
        pregunta = input('¿Desea continuar? SI/NO:')
        if pregunta == 'NO':
            num1 = None
            num2 = None
            break

def obtener_resto(dividendo = None, divisor = None):
    if dividendo is None:
        dividendo = float(input("Intrese el dividendo: "))
    if divisor is None:
        divisor = float(input("Ingrese el divisor: "))    
    resto = dividendo % divisor
    return resto
    print(f"Resto: {resto}")

def ecuacion_de_segudo_grado(a1  = None , b1  = None, c1  = None):
    if a1 is None:
        a1 = float(input("Ingrese el valor de a: "))
    if b1 is None:
        b1 = float(input("Ingrese el valor de b: "))
    if c1 is None:
        c1 = float(input("Ingrese el valor de c: "))

    raiz = b1**2-4*a1*c1
    if raiz >= 0:
        x_1 = (-b1 + math.sqrt(b1**2-4*a1*c1))/(2*a1)
        x_2 = (-b1 - math.sqrt(b1**2-4*a1*c1))/(2*a1)
        pregunta = input('La funcion es positiva, ¿Deseas sabeer el resultado? (Si/No):')
        if pregunta == 'si' or 'Si' or 'SI':
            print(f"El resultado es: {x_1} y {x_2}")
            return x_1, x_2
    else:
        print('No tiene solución')

def cuenta_atras(numero = None):
    if numero is None:
        numero = int(input("El tiempo de la cuenta atrás: "))
    for i in range(numero, 0, -1):
        time.sleep(1)
        print(i)

def sistema(a = None, b = None, c = None, d = None, e = None, f = None):
    print("     El sistema se ingresa de la siguiente forma:")
    print("ax + by = e")
    print("cx + dy = f")
    if a is None:
        a = float(input("Ingrese a: "))
    if b is None:
        b = float(input("Ingrese b: "))
    if c is None:
        c = float(input("Ingrese c: "))
    if d is None:
        d = float(input("Ingrese d: "))
    if e is None:
        e = float(input("Ingrese e: "))
    if f is None:
        f = float(input("Ingrese f: "))
    content = (b*c - d*a)
    if (b*c - d*a) != 0 and a != 0:
        y = (e*c - f*a)/content
        x = (e - b*y)/a
        print(f"La x es : {x}")
        print(f"La y es : {y}")
    else:
        print('No tiene solución')

def rufini(a3_, a2_, a1_, a0_):
    global x_1
    global x_2
    for x in range(-13, 14):
        pol = a3_*x**3 + a2_*x**2 + a1_*x + a0_
        if pol == 0:
            print(x)
            a33 = a3
            a22 = x*a3_+a2_
            a11 = x*a22+a1_
            ecuacion_de_segudo_grado(a33, a22, a11)
            break
    else:
        print(f'No se ha encontrado: {pol}')

a3 = float(input("Coeficiente a3: "))
a2 = float(input("Coeficiente a2: "))
a1 = float(input("Coeficiente a1: "))
a0 = float(input("Coeficiente a0: "))

rufini(a3, a2, a1, a0)