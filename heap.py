# exemplo de HEAP

arrValores = [3, 10, 4, 18, 11, 8, 9, 17, 24]

class Heap:
    def __init__(self):
        self.arr = []
        self.sn_esquerda = True
        self.nr_contador = 0

    def add(self, valor):
        if len(self.arr) == 0:
            return self.arr.append(valor)

        if self.sn_esquerda == True:
            self.sn_esquerda = False
            nr_indice = 2 * self.nr_contador + 1
            self.arr.insert(nr_indice, valor)
            self.nr_contador += 1
            return self.arr[:-1]
        
        if self.sn_esquerda == False:
            self.sn_esquerda = True
            nr_indice = 2 * self.nr_contador + 2
            self.arr.insert(nr_indice, valor)
            self.nr_contador += 1
            return self.arr[:-1]

    def print(self):
        for valor in self.arr:
            print(valor)

    def printA(self):
        for (index, valor) in enumerate(self.arr):
            if index == 0:
                print(valor)
            else:                
                nr_indice_esquerda = 2 * (index-1) + 1
                nr_indice_direita = 2 * (index-1) + 2
                espacos = " " * int(index)
                valor_esquerdo = None
                valor_direito = None

                if (len(self.arr) > nr_indice_esquerda):
                    valor_esquerdo = self.arr[nr_indice_esquerda]
                

                if (len(self.arr) > nr_indice_direita):
                    valor_direito = self.arr[nr_indice_direita]

                if (valor_esquerdo != None and valor_direito != None):
                    print(str(valor_esquerdo) + espacos + str(valor_direito))


objHeap = Heap()
for value in arrValores:
    objHeap.add(value)

objHeap.printA()
