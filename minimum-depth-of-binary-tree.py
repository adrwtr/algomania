# minimum-depth-of-binary-tree

def solution(root):
    contador = 1

    if root == None:
        return 0

    if root.left == None and root.right == None:
        return 0
    else:
        resultado = contadorDeep(root.left, root.right, contador, contador)
        # resultado = bsfTest(root.left, root.right)

        menor = 99
        for i in resultado:
            if i < menor:
                menor = i

        return menor
       
def contadorDeep(tree1, tree2, contador_l, contador_r):
    if tree1 != None:
       contador_l += 1
    
    if tree2 != None:
       contador_r += 1

    if (tree1 == None and tree2 == None):
        return (contador_l, contador_r)
    
    if (tree1 != None and tree2 == None):
        return contadorDeep(tree1.left, tree1.right, contador_l, contador_r)
   
    if (tree2 != None and tree1 == None):
        return contadorDeep(tree2.left, tree2.right, contador_l, contador_r)

    if (tree1.left == None and tree1.right == None and tree2.left == None and tree2.right == None):
        return (contador_l, contador_r)
    
    return contadorDeep(tree1.left, tree1.right, contador_l, contador_r) + contadorDeep(tree2.left, tree2.right, contador_l, contador_r)

class BinaryTree:
    def __init__(self):
        self.name = ''
        self.value = 0
        self.left = None
        self.right = None



def bsfTest(tree1, tree2):
    contadorl = 1
    contadorr = 1

    pilha = [(tree1, tree2)]
    while pilha:
        teste = pilha.pop(0)

        continualeft = None
        continualeft1 = None
        continuaright = None
        continuaright1 = None

        if (teste[0] != None):
            contadorl += 1
        
        if (teste[1] != None):
            contadorr += 1

        if (teste[0] == None):
            return (contadorl, contadorr)
            
        if (teste[1] == None):
            return (contadorl, contadorr)

        if (teste[0] != None and teste[0].left != None):
            continualeft = teste[0].left

        if (teste[0] != None and teste[0].right != None):
            continuaright = teste[0].right

        if (teste[1] != None and teste[1].left != None):
            continualeft1 = teste[1].left

        if teste[1] != None and (teste[1].right != None):
            continuaright1 = teste[1].right
               
        if (continualeft != None or continualeft1 != None):
            pilha.append([continualeft, continualeft1])

        if (continuaright != None or continuaright1 != None):    
            pilha.append([continuaright, continuaright1])
           

    return (contadorl, contadorr)




arvoreZero = BinaryTree()
arvoreZero.name = "zero"
arvoreZero.value = 0
arvoreZero.left = None
arvoreZero.right = None

arvore9 = BinaryTree()
arvore9.name = "arvore9"
arvore9.value = 9

arvore20 = BinaryTree()
arvore20.name = "arvore20"
arvore20.value = 20

arvore15 = BinaryTree()
arvore15.name = "arvore15"
arvore15.value = 15

arvore1 = BinaryTree()
arvore1.name = "arvore1"
arvore1.value = 3
arvore1.left = arvoreZero
arvore1.right = arvoreZero 

arvoreNoneR = BinaryTree()
arvoreNoneR.name = "arvoreNoneR"
arvoreNoneR.value = 1
arvoreNoneR.left = arvore1
arvoreNoneR.right = None 


arvore2 = BinaryTree()
arvore2.name = "arvore2"
arvore2.value = 3
arvore2.left = arvore1
arvore2.right = arvore1 


arvoreNoneRR = BinaryTree()
arvoreNoneRR.name = "arvoreNoneRR"
arvoreNoneRR.value = 2
arvoreNoneRR.left = arvore2
arvoreNoneRR.right = arvoreNoneR 


arvore3 = BinaryTree()
arvore3.name = "arvore3"
arvore3.value = 3
arvore3.left = arvore2
arvore3.right = arvore2

arvore4 = BinaryTree()
arvore4.name = "arvore4"
arvore4.value = 4
arvore4.left = arvore3
arvore4.right = arvore2

arvore5 = BinaryTree()
arvore5.name = "arvore5"
arvore5.value = 5
arvore5.left = arvore2
arvore5.right = arvore3

arvore6 = BinaryTree()
arvore6.name = "arvore6"
arvore6.value = 6
arvore6.left = arvore3
arvore6.right = arvore1

arvore7 = BinaryTree()
arvore7.name = "arvore7"
arvore7.value = 7
arvore7.left = arvore1
arvore7.right = arvore3


arvore8 = BinaryTree()
arvore8.name = "arvore8"
arvore8.value = 3
arvore8.left = arvoreZero
arvore8.right = arvore1
# [3, 9, 20, None, None, 15, 7]



arvore9 = BinaryTree()
arvore9.name = "arvore9"
arvore9.value = 3
arvore9.left = arvoreNoneR
arvore9.right = arvore1

# [3, 9, 20, 2, None, 15, 7]



import unittest

class LinkedListTests(unittest.TestCase):    
    def test_normal(self):
        self.assertEqual(
            0, 
            solution(arvoreZero)            
        )

        self.assertEqual(
            2,
            solution(arvore1)
        )

        self.assertEqual(
            3,
            solution(arvore2)
        )

        self.assertEqual(
            4,
            solution(arvore3)
        )
      
        self.assertEqual(
            4,
            solution(arvore4)
        )

        self.assertEqual(
            4,
            solution(arvore5)
        )

        self.assertEqual(
            3,
            solution(arvore6)
        )

        self.assertEqual(
            3,
            solution(arvore7)
        )

        self.assertEqual(
            3,
            solution(arvoreNoneRR)
        )

        self.assertEqual(
            2,
            solution(arvore8)
        )

        self.assertEqual(
            3,
            solution(arvore9)
        )
       


unittest.main()