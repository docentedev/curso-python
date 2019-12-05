import sys

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b


## LLamar funcion dependiendo parametros

if len(sys.argv) == 4:
    operacion = sys.argv[1]
    numero_1 = float(sys.argv[2])
    numero_2 = float(sys.argv[3])

    if operacion == 'suma':
        print(suma(numero_1, numero_2))
    elif operacion == 'resta':
        print(resta(numero_1, numero_2))
    elif operacion == 'multiplicacion':
        print(multiplicacion(numero_1, numero_2))
    elif operacion == 'division':
        print(division(numero_1, numero_2))

else:
    print('Error en los paramatros')
    print('Ejemplo = calculadora.py suma 1 10')