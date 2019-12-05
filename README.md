# Curso React


## Comentarios
- Los comentarios en el código, dan claridad a lo programado
- No afectan al código

```python

# comentario de una linea

'''
Comentario
multi
linea
'''

```

## Variables

Las variables deben:
- Ser de una sola palabra
- Escritas en minúscula
- Para separar palabras, utilizar guion bajo

`nombre_de_variable`
`listado_elementos`

## Ejecución de Python

- Por consola
    - En Windows, abrir consola
    - En mac y linux, abrir terminal

    Escribir `python`, esto nos permite ingresar directamente código Python en la consola

- Desde un archivo
    - Deben ser llamados siguiendo las reglas de una variable y terminar con `.py`, por ejemplo: `mi_programa.py`, `script_de_calculo.py`
    - Luego se debe en consola o terminal, según corresponda, escribir
    `python archivo.py` y presionar enter

## Tipos de datos

Los tipos más simples de datos son:
- Enteros
`9`, `54656`, `-134`
- booleanos
`True`, `False`
- Flotantes
`567.456475`,`-34535.345345`
- String
`'Mi texto de ejemplo'` `'Hola Mundo'`
- listas
`[1,2,3,4,5]`, `['texto', 'b', '12']`
- tuplas
`(1,2,3,4,5)`, `('texto', 'b', '12')`
- Diccionarios
`{ 'id': 1, 'name': 'Pepe' }`

## Ingresar datos por el usuario

- por argumentos `python archivo.py argumento1 argumento2`
    - Los argumentos se pueden obtener con

```python
import sys
argumento_1 = sys.argv[1]
```
Recordad que `argv`, es una lista y que el índice `0`, corresponde al nombre del archivo

- Por input, recordar que todo lo ingresado por input se debe transformar en el tipo de dato requerido, pues todo lo que ingrese será `string`.

```python
nombre = ('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
```

## Cilos

### while
```python
i = 0

while i < 10:
    print(i)
    i += 1
```

### for
```python
listado_caracteres = ['a', 'b', 'c', 'd']

for c in listado_caracteres:
    print(c)
```

## funciones
```python

def sumar(a, b):
    return a + b

def sumar_parametro_defecto(a, b = 12):
    return a + b

sumar(12, 13)

sumar_parametro_defecto(1)


```