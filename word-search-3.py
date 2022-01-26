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

from copy import deepcopy

class MySolution:
    def __init__(self) -> None:
        self.arrEncontrado = []
    
    def solution(self, board, word):
        if len(word) == 0:
            return False

        self.arrEncontrado = self.buscaPrimeiraLetra(board, word[0])

        if (len(self.arrEncontrado) == 0):
            return False

        boardOriginal = board[:]
        
        for arrListaInicial in self.arrEncontrado:
            board = deepcopy(boardOriginal)

            sn_encontrou = self.buscaPalavra(
                arrListaInicial,
                board,
                word
            )

            if (sn_encontrou == True):
                return True
            
        return False
   
    def buscaPrimeiraLetra(self, arrBoard, ds_letra):
        arrEncontrado = []

        for (nr_linha, arrLinha) in enumerate(arrBoard):
            for (nr_coluna, ds_letra_board) in enumerate(arrLinha):
                if ds_letra_board == ds_letra:
                    arrEncontrado.append([nr_linha, nr_coluna, ds_letra_board])
               
        return arrEncontrado
   
    def buscaPalavra(
        self,
        arrEncontrados,
        arrBoard,
        ds_word = ''
    ) :
        ds_letra = ds_word[0]

        if (ds_letra == arrEncontrados[2]):
            arrBoard[arrEncontrados[0]][arrEncontrados[1]] = 'XXX'

        if (len(ds_word) == 1):
            return True
        

        # proxima letra
        ds_letra = ds_word[1]

        arrPosibilidades = []

        for (nr_linha, arrLinha) in enumerate(arrBoard):
            for (nr_coluna, ds_letra_board) in enumerate(arrLinha):                
                if (ds_letra_board == ds_letra) :
                    # esta ao lado direito
                    #  "teste em direita

                    if (nr_linha == arrEncontrados[0] and nr_coluna == (arrEncontrados[1] + 1)):
                        arrEncontradosNovo = [
                            nr_linha, nr_coluna, ds_letra_board
                        ]

                        # concatenar retornos
                        arrPosibilidades.append([
                            nr_linha,
                            nr_coluna,
                            self.buscaPalavra(
                                arrEncontradosNovo,
                                arrBoard,
                                ds_word[1:]
                            )
                        ])                    

                    if (nr_linha == arrEncontrados[0] and nr_coluna == (arrEncontrados[1] - 1)):                        
                        arrEncontradosNovo = [
                            nr_linha, nr_coluna, ds_letra_board
                        ]

                        arrPosibilidades.append([
                            nr_linha,
                            nr_coluna,
                            self.buscaPalavra(
                                arrEncontradosNovo,
                                arrBoard,
                                ds_word[1:]
                            )
                        ])
                    


                    if (nr_linha == (arrEncontrados[0] + 1) and nr_coluna == arrEncontrados[1]):
                       
                        arrEncontradosNovo = [
                            nr_linha, nr_coluna, ds_letra_board
                        ]

                        
                        arrPosibilidades.append([
                            nr_linha,
                            nr_coluna,
                            self.buscaPalavra(
                                arrEncontradosNovo,
                                arrBoard,
                                ds_word[1:]
                            )
                        ])
                    
                    if (nr_linha == (arrEncontrados[0] - 1) and nr_coluna == arrEncontrados[1]):
                       
                        arrEncontradosNovo = [
                            nr_linha, nr_coluna, ds_letra_board
                        ]

                        
                        arrPosibilidades.append([
                            nr_linha,
                            nr_coluna,
                            self.buscaPalavra(
                                arrEncontradosNovo,
                                arrBoard,
                                ds_word[1:]
                            )
                        ])
    
        for sn_ok in arrPosibilidades:
            if (sn_ok[2] == True):
                return True
         
        return False

    def create_board(self):
        return [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ]

   

import unittest

class WSTests(unittest.TestCase):    

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

        obj = MySolution()
        self.assertEqual(
            True,
            obj.solution(obj.create_board(), "ADEESECCFBAS")
        )

        obj = MySolution()
        self.assertEqual(
            False,
            obj.solution(obj.create_board(), "AAB")
        )

        obj = MySolution()
        self.assertEqual(
            True,
            obj.solution(obj.create_board(), "ABCESEEEFS")
        )
        
unittest.main()