# palindromo

arrString = ['Hello', 'teste', 'level', 'ana', 'adaada']

def solution(string):
    nova = [None] * len(string)
    teste = [None] * len(string)

    for (i, char) in enumerate(string):
        nova[len(string)-i-1] = char
        teste[i] = char

    return teste == nova


def solution2(string):
    ponteiro1 = 0
    ponteiro2 = len(string) - 1

    while ponteiro1 < ponteiro2:
        if string[ponteiro1] != string[ponteiro2]:
            return False
        else:
            ponteiro1 += 1
            ponteiro2 -= 1
    
    return True


for s in arrString:
    # print(solution(s))
    print(solution2(s))