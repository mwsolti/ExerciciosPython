# # Criar 3 variaveis de nota, uma variavel de nome e exibir o nome e a media do aluno
# aluno = "Ciclano"
# nota_um = 7
# nota_dois = 7
# nota_tres = 7

# media = (nota_um+nota_dois+nota_tres)/3

# print (aluno + " Possui: "+str(media) + " de media")

# # If Medias
# #Aprovado >7
# #Recuperacao >=5 <7
# #Reprovado <=4

# list_med = [7,5,4]
# list_result = ["Passou","Recuperação","Reprovou"]

# cont = 0
# for x in list_med:
#   if media >= int(x):
#     print(list_result[cont])
#     break
#   cont = cont +1

# # Transformar em Dinamico
# nota1 = int(input("Digite a Nota 1: "))
# nota2 = int(input("Digite a Nota 2: "))
# nota3 = int(input("Digite a Nota 3: "))

# med = ((nota1+nota2+nota3))/3

# print("Sua media é: "+ str(med))

# if med >= 7:
#   print("Passou")
# elif med >= 5:
#   print("Recuperacao")
# else:
#   print("Reprovou")

#   # dict_turma = {'Cicado':'7,5'}

dict_turma = {}
qt_alunos = int(input("Digite a quantidade de Alunos: \n"))
qt_notas = int(input("Digite a quantidade de Notas : \n"))

cont = 0
cont2 = 0
notas  = []

while cont != qt_alunos:
  cont = cont + 1
  nome = input("Digite o Nome do Aluno "+str(cont)+ ": ")
  cont2 = 0
  notas  = []
  while cont2 != qt_notas:
    cont2 = cont2 + 1
    nota = float(input("Digite a nota "+str(cont2)+ ": "))
    notas.append(nota)
    
 # media = notas
  #print(notas)
  
  media = (sum(notas)) / qt_notas
  dict_turma[nome] = media

list_alunos = dict_turma.keys()

for aluno in list_alunos:
  print( "O aluno: " + aluno + " Possui a Media: " + str(dict_turma[aluno]))

