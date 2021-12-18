
def cad_aluno():
    dict_cad = {}
    nome = input("Digite o Nome do Aluno: ")

    return nome 

def cad_notas(nome_aluno):
    dict_notas = {}
    list_notas = []
    nota1 = int(input("Digite a Nota 1: "))
    nota2 = int(input("Digite a Nota 2: "))
    nota3 = int(input("Digite a Nota 3: "))
    list_notas.append(nota1)
    list_notas.append(nota2)
    list_notas.append(nota3)

    dict_notas[nome_aluno] = list_notas

    return dict_notas