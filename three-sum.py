import operator

def solution(numbers, target_sum):
    myhash = {}
    added = []
    numbers.sort()
    atual = []
    for x in range(len(numbers) - 2):
        for y in range(x + 1, len(numbers) - 1):
            for z in range(y + 1, len(numbers)):
                atual = [x, y, z]
                atual.sort()
                if (x + y + z) not in myhash:                    
                    added.append(atual)
                    myhash[x + y + z] = [[x, y, z]]
                else:
                    if (atual not in added):
                        myhash[x + y + z].append([x, y, z])

    try:  
        return sorted(myhash[target_sum])
    except KeyError:
        return []


def solution_oficial(numbers, target_sum):
    result = []
    for i in range(len(numbers) - 2):
        first = numbers[i]
        for j in range(i + 1, len(numbers) - 1):
            second = numbers[j]
            for k in range(j + 1, len(numbers)):
                third = numbers[k]
                if first + second + third == target_sum:
                    result.append(sorted([first, second, third]))
    return result


def solution_oficial_2(numbers, target_sum):
    result = []
    sorted_numbers = list(sorted(numbers))
    
    for current in range(len(numbers)):
        left_pointer = current + 1
        right_pointer = len(numbers) - 1

        while left_pointer < right_pointer:
            pointers_sum = sorted_numbers[current] + sorted_numbers[left_pointer] + sorted_numbers[right_pointer]
            if pointers_sum < target_sum:
                left_pointer += 1
            elif pointers_sum > target_sum:
                right_pointer -= 1
            else:
                result.append([sorted_numbers[current], 
                       sorted_numbers[left_pointer], sorted_numbers[right_pointer]])

                left_pointer += 1
                right_pointer -= 1
    return result



import unittest

class WSTests(unittest.TestCase):    
    def test_solution(self):
        self.assertEqual(
            [[-8, 3, 5], [-6, 1, 5], [-8, 2, 6]],
            solution_oficial([12, 3, 1, 2, -6, 5, -8, 6], 0)
        )

# unittest.main()


teste = [ [1, 2], [3, 4] ]

print(teste)

teste.append([1, 2])


print(teste)