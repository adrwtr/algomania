# valid parentheses

'''
Dada uma string com apenas os seguintes caracteres '(', ')', '{', '}', '[', ']' determine se uma determinada string é válida.

Uma string é considerada válida se:

Caracteres de abertura devem ser fechadas pelo mesmo tipo. Abertura devem ser fechados com uma chave correspondente. Uma string vazia é considerada válida.

Exemplos:
Entrada: '[]'
Saída: True

Entrada: '[()]'
Saída: True

Entrada: '['
Saída: False

Entrada: '[('
Saída: False

Entrada: ')[('
Saída: False
'''

class Verificador:
    def __init__(self):
        self.nr_colchete = 0
        self.nr_parentes = 0
        self.nr_chaves = 0
    
    def contarValores(self, string):
        for letra in string:
            if (letra in ["[", "]"]):
                self.nr_colchete += 1
            if (letra in ["(", ")"]):
                self.nr_parentes += 1
            if (letra in ["{", "}"]):
                self.nr_chaves += 1

    def verificar(self, string):
        self.__init__();
        print(string + " = ")
        self.contarValores(string)        
        return self.nr_colchete % 2 == 0 and self.nr_parentes % 2 == 0 and self.nr_chaves % 2 == 0 


def solution(str_to_validate):
    objVerificador = Verificador()
    return objVerificador.verificar(str_to_validate)

arrString = [
    "[]", # true
    "[[]", # false
    "[[()]]",# true
    "[[(]]", # false
    "((()))", # true
    "((())", # false
    "][",
    "{[{{}}]}"
]

objVerificador = Verificador()

for s in arrString:
    print(objVerificador.verificar(s))