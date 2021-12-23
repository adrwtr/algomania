

arr = []
arr.append("teste")
arr.append("teste2")

my_dict = {}
my_dict['123'] = "teste"
my_dict["456"] = "teste2"

print(my_dict)
print(my_dict['123'])

print('abc'.__hash__())


# O Two Sum é bastante comum durante entrevistas. Seu objetivo é identificar um par de números que somados batam com o valor da variável target.
# 
# Ele pode ser escrito em um algoritmo que roda no tempo O(n).
# 
# Exemplos
# Se o array é [4, 1, 2, -2, 11, 15, 1, -1, -6, -4] e o target é 9. Neste caso, seu programa deve retornar:
# 
# [-2, 11]
# 
# O motivo é bastante simples:
# 
# -2 + 11 = 9

buscar = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
myhash = {}

for i in buscar:
    for a in buscar:
        myhash[i + a] = [i, a]

print(myhash[5])


import operator

def solution(numbers, target_sum):
    myhash = {}
    for i in numbers:
        for a in numbers:
            myhash[i + a] = [i, a]

    try:  
        return sorted(myhash[target_sum])
    except KeyError:
        return []

# exemplo que nao encontra
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 12], 99)

# exemplo que encontra o valor 5
print(solution([1, 4], 5))