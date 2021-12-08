nr_numero = 10
vl_float = 12.2
ds_string = "minha variavel"
sn_boolean = False
ds_concatenar = ds_string + " " + str(nr_numero)
ds_enter = "\n"
ds_interpolacao = "meu valor {$vl_float}"
dois, valores = "teste", "outro"

arrNumeros = [10, 20, 50]

arrValores = [1, 2, 3, 4, 5]

arrString = ["adriano", "waltrick"]

print(nr_numero)
print(ds_enter)

print(vl_float)
print(ds_enter)

print(ds_string)
print(ds_enter)

# forma de mostrar boolean na tela
print(sn_boolean)
print(ds_enter)

print(ds_concatenar)
print(ds_enter)

print(ds_interpolacao)
print(ds_enter)

# arrays
print(arrNumeros)
print(ds_enter)

print(arrString)
print(ds_enter)

print(dois, valores)
print(ds_enter)

# nao faz a quebra de linha e imprime com um espaço ao final
print(1, end=' ')
print(2, end=' ')
print(3, end=' ')
print(ds_enter)
