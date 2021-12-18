from classe import cauculaMedia
from func import cad_aluno,cad_notas


aluno = cad_aluno()
dict_nota_aluno = cad_notas(aluno)

classe = cauculaMedia()

keys_aluno = dict_nota_aluno.keys()
value_aluno = dict_nota_aluno.values()

for list_notas in value_aluno:
    nota1 = list_notas[0]
    nota2 = list_notas[1]
    nota3 = list_notas[2]
    media = classe.calc_media(nota1,nota2,nota3)

status = classe.status(media)

for aluno in keys_aluno:
    print (""+ aluno+ " Teve media: "+str(media)+ " E ele: "+status)





