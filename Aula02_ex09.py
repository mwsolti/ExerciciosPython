list_nomes = ["Ana","João","Juriscleido","Roberto","Ana"," Juriscleido","Tião","Jagunço","Juriscleida","Juriscleido","Roberto","Ana"," Juriscleido","Tião","Jagunço","Juriscleida","Juriscleido","Roberto","Ana"," Juriscleido","Tião","Jagunço","Juriscleida","Juriscleido","Roberto","Ana"," Juriscleido","Tião","Jagunço","Juriscleida","João","Juriscleido","Roberto","Ana"," Juriscleido","João","Juriscleido","Roberto","Ana"," Juriscleido","João","Juriscleido","Roberto","Ana"," Juriscleido","João","Juriscleido","Roberto","Ana"," Juriscleido"]

list_repetidos = []
list_conters= []

for nome in list_nomes:

    if nome not in list_repetidos:
        list_repetidos.append(nome)
        list_conters.append(list_nomes.count(nome))
    elif list_nomes.count(nome) == 1:
        list_repetidos.append(nome)
        list_conters.append(list_nomes.count(nome))

cont = 0
total = len(list_nomes)
for conter in list_conters:
    percent = (conter/total)*100
    print("O Nome: "+ list_repetidos[cont]+ " Repete: "+ str(conter)
    + " Vezes e representa: "+str(percent)+"% de um total de: "+str(total))

    cont +=1
