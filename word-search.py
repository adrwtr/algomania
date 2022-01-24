''' 
Dado uma matriz 2D e uma palavra, identifique se esta determinada palavra está dentro da matriz.

A palavra pode ser construída a partir de letras que estão sequenciais em valores adjacentes, onde valores adjacentes são aqueles que estão horizontalmente ou verticalmente por perto.

LEMBRE-SE: a mesma letra não pode ser usada duas vezes para construir uma palavra.

board = [
          ['A','B','C','E'],  
          ['S','F','C','S'],    
          ['A','D','E','E']
        ]
Dada a palavra = "ABCCED", retorne true.
Dada a palavra = "SEE", retorne true.
Dada a palavra = "ABCB", retorne false.
'''

class MySolution:
    def __init__(self) -> None:
        self.arrEncontrados = []


    def solution(self, board, word):
        contador = 1
        linha_anterior = None
        coluna_anterior = None

        arrEncontrouPrimeira = self.procura_primeira_letra(word[0], board)

        if arrEncontrouPrimeira == False or arrEncontrouPrimeira == None:
            return False

        total_tentativas = len(arrEncontrouPrimeira)
        contador_tentativas = 1

        for tentativas in arrEncontrouPrimeira:
            # pra cada tentativa, zera o array
            self.arrEncontrados = []
            contador = 1

            for letra in word:
                arrEncontrou = None
                arrEncontrouPrimeira = None

                if letra == tentativas[0] and contador == 1:
                    arrEncontrou = tentativas
                    
                    if arrEncontrou != False:
                        self.arrEncontrados.append(
                            arrEncontrou
                        )

                        linha_anterior = arrEncontrou[1]
                        coluna_anterior = arrEncontrou[2]

                        contador = 2
                    else:
                        return False
                else:
                    # procura a direita
                    arrDireita = self.procura_na_posicao(
                        letra, 
                        linha_anterior, 
                        coluna_anterior + 1,
                        board
                    )

                    if arrDireita != False:
                        arrEncontrou = arrDireita
                        self.arrEncontrados.append(
                            arrEncontrou
                        )

                        linha_anterior = arrEncontrou[1]
                        coluna_anterior = arrEncontrou[2]
                    else:
                        arrEsquerda = self.procura_na_posicao(
                            letra,
                            linha_anterior, 
                            coluna_anterior - 1, 
                            board
                        )

                        if arrEsquerda != False:
                            arrEncontrou = arrEsquerda
                            self.arrEncontrados.append(
                                arrEncontrou
                            )

                            linha_anterior = arrEncontrou[1]
                            coluna_anterior = arrEncontrou[2]
                        else:
                            arrBaixo = self.procura_na_posicao(
                                letra, 
                                linha_anterior + 1, 
                                coluna_anterior,
                                board
                            )

                            if arrBaixo != False:
                                arrEncontrou = arrBaixo
                                self.arrEncontrados.append(
                                    arrEncontrou
                                )

                                linha_anterior = arrEncontrou[1]
                                coluna_anterior = arrEncontrou[2]
                            else:
                                arrCima = self.procura_na_posicao(
                                    letra, 
                                    linha_anterior - 1, 
                                    coluna_anterior,
                                    board
                                )

                                if (arrCima != False):
                                    arrEncontrou = arrCima
                                    self.arrEncontrados.append(
                                        arrEncontrou
                                    )

                                    linha_anterior = arrEncontrou[1]
                                    coluna_anterior = arrEncontrou[2]

                if ((arrEncontrou == False or arrEncontrou == None) and contador_tentativas >= total_tentativas):
                    return False
                else:
                    contador_tentativas = contador_tentativas + 1
            # return True
        return True
  

    def create_board(self):
        return [
          ['A','B','C','E'],  
          ['S','F','C','S'],    
          ['A','D','E','E']
        ]

    def procura_letra(self, letra, board):
        for (nr_linha, arrLinha) in enumerate(board):
            for (nr_coluna, arrColuna) in enumerate(arrLinha):
                if arrColuna == letra:
                    return [letra, nr_linha, nr_coluna]
        return False

    def procura_primeira_letra(self, letra, board):
        arrEncontrados = []

        for (nr_linha, arrLinha) in enumerate(board):
            for (nr_coluna, arrColuna) in enumerate(arrLinha):
                if arrColuna == letra:
                    arrEncontrados.append([letra, nr_linha, nr_coluna])

        if len(arrEncontrados) == 0:          
            return False
        
        return arrEncontrados


    def procura_na_posicao(self, letra, linha, coluna, board):
        # encontrou a letra no board
        try:
            if (letra == board[linha][coluna]) :
                # ok , agora vamos validar a posicao dela no encontrado
                for enc_letra, enc_linha, enc_coluna in self.arrEncontrados:
                    if enc_letra == letra and enc_linha == linha and enc_coluna == enc_coluna:
                        return False
                
                # se chegou aqui tudo bem
                return [letra, linha, coluna]
            
            return False
        except IndexError: 
            return False

obj = MySolution()

print(obj.solution(obj.create_board(), "ABC"))




import unittest

class WSTests(unittest.TestCase):    
    def test_procura_letra(self):
        obj = MySolution()

        self.assertEqual(
            ['A', 0, 0],
            obj.procura_letra('A', obj.create_board())
        )

        self.assertEqual(
            ['B', 0, 1],
            obj.procura_letra('B', obj.create_board())
        )

        self.assertEqual(
            ['F', 1, 1],
            obj.procura_letra('F', obj.create_board())
        )

        self.assertEqual(
            False,
            obj.procura_letra('X', obj.create_board())
        )

    def test_procura_na_posicao(self):
        obj = MySolution()
        
        self.assertEqual(
            False,
            obj.procura_na_posicao("X", 0, 0, obj.create_board())
        )

        obj = MySolution()
        self.assertEqual(
            False,
            obj.procura_na_posicao("B", 0, 0, obj.create_board())
        )

        obj = MySolution()
        self.assertEqual(
            False,
            obj.procura_na_posicao("B", -1, 0, obj.create_board())
        )

        obj = MySolution()
        self.assertEqual(
            False,
            obj.procura_na_posicao("B", -1, -1, obj.create_board())
        )

        obj = MySolution()
        self.assertEqual(
            ['A', 0, 0],
            obj.procura_na_posicao("A", 0, 0, obj.create_board())
        )

    def test_solution(self):
        obj = MySolution()        
        self.assertEqual(
            False,
            obj.solution(obj.create_board(), "X")
        )

        obj = MySolution()
        self.assertEqual(
            True,
            obj.solution(obj.create_board(), "A")
        )

        obj = MySolution()
        self.assertEqual(
            True,
            obj.solution(obj.create_board(), "AB")
        )

        obj = MySolution()
        self.assertEqual(
            True,
            obj.solution(obj.create_board(), "ABC")
        )

        obj = MySolution()
        self.assertEqual(
            True,
            obj.solution(obj.create_board(), "ABF")
        )

        obj = MySolution()
        self.assertEqual(
            True,
            obj.solution(obj.create_board(), "ABFD")
        )


        obj = MySolution()
        self.assertEqual(
            True,
            obj.solution(obj.create_board(), "ABFS")
        )


        obj = MySolution()
        self.assertEqual(
            True,
            obj.solution(obj.create_board(), "ABFC")
        )

        obj = MySolution()
        self.assertEqual(
            False,
            obj.solution(obj.create_board(), "ABFE")
        )
        

        obj = MySolution()
        self.assertEqual(
            True,
            obj.solution(obj.create_board(), "ABCCED")
        )

        obj = MySolution()
        self.assertEqual(
            True,
            obj.solution(obj.create_board(), "SEE")
        )

        obj = MySolution()
        self.assertEqual(
            False,
            obj.solution(obj.create_board(), "ABCB")
        )
        
unittest.main()