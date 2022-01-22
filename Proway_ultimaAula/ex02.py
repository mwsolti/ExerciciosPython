def cadastra_aluno():
    nome  = input("Digite o nome do aluno: ")
    nota1 = input("Digite a nota 1: ")
    nota2 = input("Digite a nota 2: ")
    nota3 = input("Digite a nota 3: ")
    dict_aluno  =  {"nome": nome,
                    "nota1": nota1,
                    "nota2": nota2,
                    "nota3": nota3
                    }
    
    
    print (dict_aluno)
    return dict_aluno 


def caucula_media_retorna_status(dict_aluno = {}):
    nota1 = dict_aluno["nota1"]
    nota2 = dict_aluno["nota2"]
    nota3 = dict_aluno["nota3"]
    media = (float(nota1)+float(nota2)+float(nota3))/3

    if media >=7:
        stats = "Passou"
    elif media>=5:
        stats = "Recuperação"
    else:
        stats = "Reprovado"
    
    dict_med_aluno = {"nome":dict_aluno["nome"],
                      "media":media,
                      "status":stats}
    
    
    print(dict_med_aluno)
    return dict_med_aluno


def run():
    
    qt_alunos = 0
    list_alunos = []
    list_stats_alunos = []
    
    while qt_alunos <=3:
        
        qt_alunos+=1
        
        list_alunos.append(cadastra_aluno())
        
    
    for dict_aluno in list_alunos:
        list_stats_alunos.append(caucula_media_retorna_status(dict_aluno))
    
    
    for dict_status in list_stats_alunos:
        print ("------------------------------------------------------")
        print ("Aluno: " +dict_status["nome"])
        print ("Media: " +str(dict_status["media"]))
        print ("Status: " +dict_status["status"])
        print ("------------------------------------------------------")
        
    
    

run()