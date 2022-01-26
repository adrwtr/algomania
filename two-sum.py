# A solucao deve estar implementada dentro da função abaixo.
# Dica: Você pode criar outras funções e classes se quiser mas esta é a função principal que será usada.

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

print([4, 1, 2, -2, 11, 15, 1, -1, -6, -4], 9)