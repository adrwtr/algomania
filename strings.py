nome = "Adriano Waltrick"
loren = "loren ipsum teste adriano hello world"

# repete os valores
repete = "A " * 10
print(repete)

# replace
print(
    loren.replace('ipsum', 'outra coisa')
)

print(
    len("teste")
)

# to upper
print(
    'adriano'.upper()
)

# indica se começa com
print(
    loren.startswith('loren')
)

# split
print(
    'test1, teste2, teste3'.split(',')
)

# todas as primeiras em maiusculas
print(loren.title())

# pega uma parte
print(loren[0:10])

# inverte a string
print(nome[::-1])

for char in reversed(range(len(nome))):
    print(nome[char])

print(','.join(nome))


novoNome = "adriano"
print(novoNome[1:])