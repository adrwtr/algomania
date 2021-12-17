# Dada uma string codificada, retorne a string decodificada.
# s = "2[a]3[bc]", retornará "aabcbcbc".
# s = "3[a2[c]]", retornará "accaccacc".
# s = "2[abc]3[cd]ef", retornará "abcabccdcdcdef".

# 2[a]    3[bc]
# arrStrings = ["2[a]3[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]

# for nr_pos_string, ds_str_atual in enumerate(ds_string):
arrStrings = [
    "2[a]3[bc]",
    "2[abc]3[cd]ef",
    "3[a2[c]]"
]

class Decodifica:
    def __init__(self):
        self.arrPilha = []

    def decodificar(self, ds_texto):
        for ds_char in ds_texto:
            self.arrPilha.append(ds_char)
            if ds_char == "]":
                self.processaFechamento()
        return self.imprimirPilha()
    
    def processaFechamento(self):
        # remove fechamento
        self.arrPilha.pop()

        ds_texto_final = ""
        ds_char = self.arrPilha.pop()
        while (ds_char != "["):
            ds_texto_final = ds_char + ds_texto_final
            ds_char = self.arrPilha.pop()

        nr_repetidor = int(self.arrPilha.pop())
        ds_texto_final = ds_texto_final * nr_repetidor

        self.arrPilha.append(ds_texto_final)
    
    def imprimirPilha(self):
        ds_texto = ""
        while self.arrPilha:
            ds_texto = self.arrPilha.pop() + ds_texto
        return ds_texto

for ds_texto in arrStrings:
    objDecodifica = Decodifica()
    print(objDecodifica.decodificar(ds_texto))  
