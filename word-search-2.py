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
        self.arrBoard = []
        self.arrPrimeiraLetra = []

    def solution(self, board, word):
        primeira_letra = word[0]
        self.arrBoard = self.transformarBoard(board)
        self.arrPrimeiraLetra = self.procura_primeira_letra(self.arrBoard, primeira_letra)

        if len(word) == 1 and len(self.arrPrimeiraLetra) >= 1:
            return True

        return self.buscarLetras(self.arrPrimeiraLetra, word[1:], self.arrBoard)
    
    def buscarLetras(self, arrPrimeiraLetra, palavra, arrBoard):   
        arrFinal = []
        arrEncontradas = []

        for primeira_letra, primeira_linha, primeira_coluna in arrPrimeiraLetra:
            # arrEncontradas = []

            for letra_atual in palavra:
                for board_letra, board_linha, board_coluna in arrBoard:

                    direita = letra_atual == board_letra and primeira_linha == board_linha and (primeira_coluna + 1) == board_coluna
                    esquerda = letra_atual == board_letra and primeira_linha == board_linha and (primeira_coluna - 1) == board_coluna
                    cima = letra_atual == board_letra and (primeira_linha - 1) == board_linha and primeira_coluna == board_coluna
                    baixo = letra_atual == board_letra and (primeira_linha + 1) == board_linha and primeira_coluna == board_coluna
                    
                    arrEncontradas.append([primeira_letra, letra_atual, board_linha, board_coluna, (direita or esquerda or cima or baixo)])

                    if (direita or esquerda or cima or baixo) == True:
                        primeira_linha = board_linha
                        primeira_coluna = board_coluna
                    
            
        for letra_atual in palavra:
            achou = False
            
            for primeira_letra, teste_atual, board_linha, board_coluna, verdade in arrEncontradas:
                if letra_atual == teste_atual and verdade == True:
                    achou = True

            if achou == False:
                return False
            
        return True  


    def transformarBoard(self, board):
        arrBoard = []
        for (nr_linha, arrLinha) in enumerate(board):
            for (nr_coluna, ds_letra) in enumerate(arrLinha):
                arrBoard.append([ds_letra, nr_linha, nr_coluna])

        return arrBoard

    def procura_primeira_letra(self, arrBoard, letra):
        arrPrimeiraLetra = []

        for arrValores in arrBoard:
            if (arrValores[0] == letra):
                arrPrimeiraLetra.append(arrValores)
        
        return arrPrimeiraLetra



import unittest

class WSTests(unittest.TestCase):    
    def test_transforma(self):
        obj = MySolution()

        board_test = [
          ['A','B'],  
          ['S'] 
        ]

        self.assertEqual(
            [
                ['A', 0, 0],
                ['B', 0, 1],
                ['S', 1, 0]
            ],
            obj.transformarBoard(board_test)
        )

    def test_primera_letra(self):
        obj = MySolution()

        board_test = [
          ['A','B'],  
          ['S', 'S'] 
        ]

        self.assertEqual(
            [
                ['S', 1, 0],
                ['S', 1, 1],
            ],

            obj.procura_primeira_letra(
                obj.transformarBoard(board_test), 
                'S'
            )
        )

    def test_solution(self):
        obj = MySolution()

        # board_test = [
        #   ['A','B'],  
        #   ['S', 'S'] 
        # ]

        # self.assertEqual(
        #     True,
        #     obj.solution(
        #         board_test,
        #         'ABS'
        #     )
        # )

        # self.assertEqual(
        #     True,
        #     obj.solution(
        #         board_test,
        #         'A'
        #     )
        # )

        # self.assertEqual(
        #     True,
        #     obj.solution(
        #         board_test,
        #         'S'
        #     )
        # )

        # self.assertEqual(
        #     True,
        #     obj.solution(
        #         board_test,
        #         'BS'
        #     )
        # )

        # self.assertEqual(
        #     True,
        #     obj.solution(
        #         board_test,
        #         'SAB'
        #     )
        # )

        board = [
          ['A','B','C','E'],  
          ['S','F','C','S'],    
          ['A','D','E','E']
        ]

        # Dada a palavra = "ABCCED", retorne true.
        self.assertEqual(
            True,
            obj.solution(
                board,
                'ABCCED'
            )
        )

        # Dada a palavra = "SEE", retorne true.
        self.assertEqual(
            True,
            obj.solution(
                board,
                'SEE'
            )
        )

        # Dada a palavra = "ABCB", retorne false.
        self.assertEqual(
            False,
            obj.solution(
                board,
                'ABCB'
            )
        )

unittest.main()