import operator

def solution(numbers, target_sum):
    myhash = {}
    added = []
    numbers.sort()
    atual = []
    for x in numbers:
        for y in numbers:
            for z in numbers:
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

import unittest

class WSTests(unittest.TestCase):    
    def test_solution(self):
        self.assertEqual(
            [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]],
            solution([12, 3, 1, 2, -6, 5, -8, 6], 0)
        )

unittest.main()