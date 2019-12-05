'''
programa para reforzar la utilizacion de ciclos
'''
listado_nombre = []
listado_numero = []

respuesta = 's'

# se repetira mientras la variable respuesta sea 's'
while respuesta == 's':
    nombre = input('Ingrese nombre:')
    numero = int(input('Ingrese numero de telefono: '))

    
    respuesta_seguir_ingresando = input('Desea ingresar otro contaco s/n: ')
    # Este while fuerza al usuario a ingresar solo 's' o 'n'
    while respuesta_seguir_ingresando not in ['s', 'n']:
        respuesta_seguir_ingresando = input('Desea ingresar otro contaco s/n: ')
    
    respuesta = respuesta_seguir_ingresando
    
    listado_nombre.append(nombre)
    listado_numero.append(numero)


print('Listado: ')

# generamos un rango a partir del largo de la lista de nombres
for i in range(len(listado_nombre)):
    print('----')
    print(listado_nombre[i])
    print(listado_numero[i])
