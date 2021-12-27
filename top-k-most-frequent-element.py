# top-k-most-frequent-element

'''
Dado um array que nunca é vazio, retorne os K elementos mais frequentes do mesmo.

Exemplos
Entrada: [1, 1, 1, 3, 3, 5, 6, 7, 8, 9, 10] -> K = 2

Saída: [1, 3]

Explicação: Os 2 números mais frequentes são 1 e 3.
'''

def solution(numbers, k):
    arrContador = {}

    for nr_numero in numbers:

        # pode usar nr_numero not in arrContador ao invez do try

        try:  
            if arrContador[nr_numero] == None:
                arrContador[nr_numero] = 1
            else:
                arrContador[nr_numero] += 1
        except KeyError:
            arrContador[nr_numero] = 1
        

    arrContador = sorted(arrContador.items(), reverse=True,  key=lambda x: x[1])
    arrRetorno = []

    for (nr_key, nr_valor) in  enumerate(arrContador):
        if nr_key < k:
            arrRetorno.append(nr_valor[0])
        else:
            return arrRetorno

    return arrRetorno


# sort = {1: 25, 2: 10, 3 : 15}
# print(sort)
# print(sorted(sort, reverse=True))
# print(sorted(sort.items(), reverse=True))
# print(sorted(sort.items(), reverse=True,  key=lambda x: x[1]))
# 

import heapq

def sol_com_hashmap(numbers, k):
    hash_map = {}

    for number in numbers:
        if number not in hash_map:
            hash_map[number] = 0
        hash_map[number] += 1

    # so consegue fazer isso pois o heapq ta usando min heap 
    # e nesse caso ele ja insere ordenado
    heap = []
    for number, count in hash_map.items():
        heapq.heappush(heap, (count, number))
        if len(heap) > k:
            heapq.heappop(heap)
    
    result = []
    for pair in heap:
        result.append(pair[1])
    return result


def sol_com_dict(numbers, k):
    hash_map = {}

    for number in numbers:
        if number not in hash_map:
            hash_map[number] = 0
        hash_map[number] += 1

    freq = {}
    for number, count in hash_map.items():
        if count not in freq:
            freq[count] = []
        freq[count].append(number)

    result = []
    
    for number in reversed(range(len(numbers) + 1)):
        if number in freq:
            result.extend(freq[number])
    return result[:k]


import unittest

class ListTests(unittest.TestCase):    
    def test_normal(self):
        self.assertEqual(
            [1, 3], 
            sol_com_dict([1, 1, 1, 3, 3, 5, 6, 7, 8, 9, 10], 2)            
        )

        self.assertEqual(
            [3], 
            sol_com_dict([1, 3, 1, 3, 3, 5, 6, 3, 3, 9, 10], 1)            
        )

        self.assertEqual(
            [3, 1, 9], 
            sol_com_dict([1, 3, 1, 3, 3, 5, 6, 3, 3, 9, 9, 10], 3)            
        )

        self.assertEqual(
            [9],
            sol_com_dict([9, 9, 9, 9], 9)
        )


unittest.main()