arrNumeros = [1, 2, 3, 4]
arrStrings = ['teste', 'hello', 'world']
arrDesordem = [8, 1, 2, 6, 34]

print(arrNumeros)
print(arrStrings)

# elementos
print(arrNumeros[0])
print(arrNumeros[1])
print(arrNumeros[-1]) # acessa ultimo elemento
print(arrNumeros[1:3])

for idx, val in enumerate(arrDesordem):
    print(idx, val)

# qtd valores
print(len(arrNumeros))

# ordena o array
print(sorted(arrDesordem))

print(arrDesordem)

# ordena o array nele mesmo
arrDesordem.sort()
print(arrDesordem)

# insere no array - lento
arrNumeros.insert(0, 0)
print(arrNumeros)

# insere ao final do array
arrNumeros.append(5)
print(arrNumeros)

# min e max
print(min(arrNumeros))
print(max(arrNumeros))


# remover item (nao é pelo indice)
# este metodo é lento pois faz um shift dos elementos
arrNumeros.remove(3)
print(arrNumeros)

# solução para remover rapido
arrNumeros[1] = None # ou null
print(arrNumeros)


# trabalhando com busca em arvore
import bisect

print(arrDesordem)

# vai retornar a posicao q se encontra o 8
print(
    bisect.bisect(arrDesordem, 8)
)

# insere mantendo a ordenacao
bisect.insort(arrDesordem, 22)

print(arrDesordem)


# diferenca entre copia e referencia
arrReferencia = arrDesordem
arrCopia = list(arrDesordem)

arrDesordem.append(100)

print(arrDesordem)
print(arrReferencia)
print(arrCopia)


# estruturas de dados
# como listas tem copias diferentes

lista1 = [{'nome' : 'Adriano', 'codigo' : 1}]
lista2 = lista1

lista1[0]['nome'] = "Joao"

print(lista1)
print(lista2)

import copy
lista3 = copy.deepcopy(lista1)

lista1[0]['nome'] = "Pedro"

print(lista1)
print(lista2)
print(lista3)


# troca de elemntos na mesma linha
print(arrNumeros)
arrNumeros[0], arrNumeros[1] = arrNumeros[1], arrNumeros[0]
print(arrNumeros)
