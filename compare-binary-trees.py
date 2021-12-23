class BinaryTree:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None
    def add(self, valor):
        # se nao tem valor
        if (self.value == 0):
            self.value = valor
            return self
        else:
            # se ja tem valor
            # avalia se é esquerda
            if (valor % 2 == 1):
                leftAtual = self.left

                if (leftAtual == None):
                    leftAtual = BinaryTree()
                    leftAtual.value = valor
                    self.left = leftAtual
                else:
                    leftAnterior = None
                    while(leftAtual != None):
                        leftAnterior = leftAtual
                        leftAtual = leftAtual.left

                    leftAtual = BinaryTree()
                    leftAtual.value = valor
                    leftAnterior.left = leftAtual
            else:
                # se for direita
                rAtual = self.right

                if (rAtual == None):
                    rAtual = BinaryTree()
                    rAtual.value = valor
                    self.right = rAtual
                else:
                    rAnterior = None
                    while(rAtual != None):
                        rAnterior = rAtual
                        rAtual = rAtual.right

                    rAtual = BinaryTree()
                    rAtual.value = valor
                    rAnterior.right = rAtual

def solution(tree1, tree2):
    if tree1 == None and tree2 != None:
        return False
    
    if tree1 != None and tree2 == None:
        return False
    
    if tree1 == None and tree2 == None:
        return True

    if tree1.value != tree2.value:
        return False
    
    return solution(tree1.left, tree2.left) and solution(tree1.right, tree2.right)

def bsf(tree1, tree2):
    if tree1 == None and tree2 != None:
        return False
    
    if tree1 != None and tree2 == None:
        return False
    
    if tree1 == None and tree2 == None:
        return True

    pilha = [(tree1, tree2)]
    while pilha:
        teste = pilha.pop(0)
        valor1 = teste[0].value
        valor2 = teste[1].value
        
        # outra forma de escrever é
        # valor1, valor2 = pilha.pop(0)

        if (valor1 != valor2):
            return False
        
        if teste[0].left != None and teste[1].left != None:
            pilha.append([teste[0].left, teste[1].left])
        else:
            if teste[0].left != None and teste[1].left == None:
                return False
            if teste[0].left == None and teste[1].left != None:
                return False 

        if teste[0].right != None and teste[1].right != None:
            pilha.append([teste[0].right, teste[1].right])
        else:
            if teste[0].right != None and teste[1].right == None:
                return False
            if teste[0].right == None and teste[1].right != None:
                return False        

    return True

def binary_tree_from_array(arr):
    obj = BinaryTree()
    for i in arr:
        obj.add(i)
    return obj


arr1 = [1,2,3]
arr2 = [1,2,4,5,3]
arr3 = [1,2,4,5,6]

arvore1 = BinaryTree()
for i in arr1:
    arvore1.add(i)

arvore2 = BinaryTree()
for i in arr2:
    arvore2.add(i)

arvore3 = BinaryTree()
for i in arr3:
    arvore3.add(i)








import unittest

class LinkedListTests(unittest.TestCase):    
    def test_normal(self):
        self.assertTrue(
            solution(arvore1, arvore1)            
        )
        
        self.assertTrue(
            solution(arvore3, binary_tree_from_array(arr3))           
        )
     
        self.assertTrue(
            solution(BinaryTree(), BinaryTree())         
        )

        self.assertTrue(
            solution(binary_tree_from_array([]), BinaryTree())
        )

    def test_falses(self):
        self.assertFalse(
            solution(arvore1, arvore3)            
        )

        self.assertFalse(
            solution(BinaryTree(), arvore2)          
        )

        self.assertFalse(
            solution(arvore2, arvore1)          
        )

        self.assertFalse(
            solution(arvore3, arvore2)          
        )
    


    def test_normal_bsf(self):
        self.assertTrue(
            bsf(arvore1, arvore1)            
        )
        
        self.assertTrue(
            bsf(arvore3, binary_tree_from_array(arr3))           
        )
     
        self.assertTrue(
            bsf(BinaryTree(), BinaryTree())         
        )

        self.assertTrue(
            bsf(binary_tree_from_array([]), BinaryTree())
        )

    def test_falses_bsf(self):
        self.assertFalse(
            bsf(arvore1, arvore3)            
        )

        self.assertFalse(
            bsf(BinaryTree(), arvore2)          
        )

        self.assertFalse(
            bsf(arvore2, arvore1)          
        )

        self.assertFalse(
            bsf(arvore3, arvore2)          
        )


unittest.main()