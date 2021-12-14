# Dada uma string codificada, retorne a string decodificada.
# s = "2[a]3[bc]", retornará "aabcbcbc".
# s = "3[a2[c]]", retornará "accaccacc".
# s = "2[abc]3[cd]ef", retornará "abcabccdcdcdef".

# 2[a]    3[bc]


# arrStrings = ["2[a]3[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]

class Pilha:
    def __init__(self, nr_repetidor, ds_string, arrPilha):
        # print(ds_string)
        self.nr_repetidor = nr_repetidor
        self.ds_string = ds_string
        self.arrPilha = arrPilha
    def setString(self, ds_string):
        self.ds_string = ds_string
    def imprimir(self):
        for i in range(0, self.nr_repetidor):
            print(self.ds_string)

class ProcessPilha:
    def __init__(self):
        self.arrPilhaCompleta = []

    def ehInteiro(self, ds_string):                
        # print(ds_str_atual)
        try:
            nr_inteiro = int(ds_string)
        except ValueError:
            nr_inteiro = -1

        # eh um numero
        if nr_inteiro > 0:
            return True
        return False

    def buscaInteiro(self, ds_string):
        for nr_index, ds_char in enumerate(ds_string):
            if (self.ehInteiro(ds_char)):
                return self.retornarPilha(
                    int(ds_char),
                    ds_string[(nr_index + 1):]
                )
    
    # vamos buscar se tem um fechador ou inteiro
    def buscaFechador(self, ds_string):
        for nr_index, ds_char in enumerate(ds_string):
            if (self.ehInteiro(ds_char) == True):
                return False
            if (ds_char == "]"):
                return True

    # retorna uma pilha montada
    def retornarPilha(self, nr_repetidor, ds_string):
        if (self.buscaFechador(ds_string) == True):
            return Pilha(
                nr_repetidor,
                ds_string,
                []
            )           
        else:
            return self.buscaInteiro(ds_string)

    def printPilha(self):
        print(self.arrPilhaCompleta)

class Decodifica:
    def __init__(self):
        self.ds_texto = ""
        self.arrPilha = []
        
    def decodificar(self, ds_string):
        nr_repetidor = 0
        ds_string_pilha = ""

        for nr_char, ds_char in enumerate(ds_string):
            if (ds_char == "["):
                nr_repetidor = int(ds_string[nr_char-1])
                ds_string_pilha = ""
                objPilha = Pilha(
                    nr_repetidor,
                    "",
                    []
                )
                self.arrPilha.append(objPilha)
            if (ds_char == "]"):
                objPilha = self.arrPilha.pop()
                objPilha.setString(ds_string_pilha)
                objPilha.imprimir()
                ds_string_pilha = ""
            #  qualquer coisa diferente vira string da pilha
            if (ds_char != "[" and ds_char != "]"):
                ds_string_pilha = ds_string_pilha + ds_char
        if len(ds_string_pilha) > 0:
            print(ds_string_pilha)
            
            
            


# for nr_pos_string, ds_str_atual in enumerate(ds_string):
arrStrings = [
    # "2[a]3[bc]",
    "2[abc]3[cd]ef"
    # "3[a2[c]]"
]



for ds_texto in arrStrings:
    objDecodifica = Decodifica()
    objDecodifica.decodificar(ds_texto)    