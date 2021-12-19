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
    def printA(self, arvore):
        print(arvore.value)

        if (arvore.left != None):
            print("Para esquerda: ")
            self.printA(arvore.left)

        if (arvore.right != None):
            print("Para direita: ")
            self.printA(arvore.right)

def solution(tree):
    invert = BinaryTree(tree.value)
    invert.value = tree.value
    invert.right = tree.left
    invert.left = tree.right

    if (invert.right != None):
        invert.right = solution(invert.right)
    if (invert.left != None):
        invert.left = solution(invert.left)
    
    return invert


objArvore1 = BinaryTree()
objArvore1.value = 1

objArvore2 = BinaryTree()
objArvore2.value = 2

objArvore3 = BinaryTree()
objArvore3.value = 3

objArvore4 = BinaryTree()
objArvore4.value = 4

objArvore5 = BinaryTree()
objArvore5.value = 5

objArvore6 = BinaryTree()
objArvore6.value = 6     

objArvore6.left = objArvore5
objArvore6.right = objArvore4
objArvore5.left = objArvore3
objArvore5.right = objArvore2
# objArvore2.left = objArvore1


objArvore1.add(1)
objArvore1.add(2)
objArvore1.add(3)
objArvore1.add(4)
objArvore1.add(5)
objArvore1.add(6)
objArvore1.add(15)
objArvore1.add(16)
objArvore1.add(6)
objArvore1.add(15)
objArvore1.add(16)
# objArvore1.printA(objArvore1)

objArvore6.printA(objArvore6)

print("--------")

novo = solution(objArvore6)
novo.printA(novo)