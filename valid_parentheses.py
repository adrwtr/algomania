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

class Operadores:
    def __init__(self, ds_operador) -> None:
        self.ds_operador = ds_operador
        self.arrPilha = []
    
class Verificador:
    def __init__(self):
        self.arrPilhaInicial = []

    def verificar(self, string):
        self.__init__()

        for s in string:
            if (s in ["[", "(", "{"]):
                self.arrPilhaInicial.append(Operadores(s))
            if (s == "]"):           
                if (len(self.arrPilhaInicial) > 0 and self.arrPilhaInicial[-1].ds_operador == "[") :
                    self.arrPilhaInicial.pop()
            if (s == ")"):           
                if (len(self.arrPilhaInicial) > 0 and self.arrPilhaInicial[-1].ds_operador == "(") :
                    self.arrPilhaInicial.pop()
            if (s == "}"):           
                if (len(self.arrPilhaInicial) > 0 and self.arrPilhaInicial[-1].ds_operador == "{") :
                    self.arrPilhaInicial.pop()
        if (len(self.arrPilhaInicial) == 0):
            return True
        return False
                    
                

def solution(str_to_validate):
    objVerificador = Verificador()
    return objVerificador.verificar(str_to_validate)

arrString = [
    # "[]", # true
    # "[[]", # false
    # "[[()]]",# true
    # "[[(]]", # false
    # "((()))", # true
    # "((())", # false
    "][", # false
    "]", # false
    #"{[{{}}]}", true
    #"{{" # false
]

objVerificador = Verificador()

for s in arrString:
    print(objVerificador.verificar(s))
