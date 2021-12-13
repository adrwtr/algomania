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



# for nr_pos_string, ds_str_atual in enumerate(ds_string):
arrStrings = ["2[a]3[bc]"]
objProcessar = ProcessPilha()

for ds_texto in arrStrings:
    objProcessar.buscaInteiro(ds_texto)
    objProcessar.printPilha()