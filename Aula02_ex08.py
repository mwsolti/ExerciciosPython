list_alunos = []
list_media = []

cont = 0

while cont != 4:
    cont += 1
    list_alunos.append(input("Digite o Nome do Aluno: "))
    list_media.append(float(input("Digite a Média do ALuno: ")))

cont = 0
for media in list_media:
    if media >=7:
        print("O ALuno: "+list_alunos[cont]+" Passou com média: "+ str(media))
    elif media >= 5:
        print("O ALuno: "+list_alunos[cont]+" está em Recuperação com média: "+ str(media))
    else:
        print("O ALuno: "+list_alunos[cont]+" Reprovou com média: "+ str(media))
    cont +=1

