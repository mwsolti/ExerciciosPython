def solucaoAnagrama1(s1,s2):
    umalista = list(s2)

    pos1 = 0
    aindaOK = True
    cont_anagram = 0
    while pos1 < len(s1) and aindaOK:
        pos2 = 0
        encontrado = False
        while pos2 < len(umalista) and not encontrado:
            if s1[pos1] == umalista[pos2]:
                encontrado = True
                cont_anagram +=1
            else:
                pos2 = pos2 + 1

        if encontrado:
            umalista[pos2] = None
        else:
            aindaOK = False

        pos1 = pos1 + 1

    return cont_anagram

print(solucaoAnagrama1('abcd','dcba'))
