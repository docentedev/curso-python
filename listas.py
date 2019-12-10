from functools import reduce

lista = [['a',3], ['b', 4]]

acum = 0
for l in lista:
  acum += l[1]

print(acum)


# [3,4]
lista_numeros = [e[1] for e in lista]
print(lista_numeros)


total = reduce(lambda vant, vac : vant + vac, lista_numeros)

print('EL total es:')
print(total)

'''
l_s = ['1', '2', '3']

l_e = [int(e) for e in l_s]

print(l_e)

lista_numero = [1,2,3,4,5,6,7,8]


for i, e in enumerate(lista_numero):
  print(e)


lista_de_pares = [numero if numero%2 == 2 else None for numero in lista_numero]
print(lista_de_pares)


lista_b = []
for numero in lista_numero:
  lista_b.append(numero*numero)

print(lista_b)

print('------')
lista_c = [numero*numero for numero in lista_numero]
print(lista_c)
'''
