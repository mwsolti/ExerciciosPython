
list_num_fix = [1,2,3,4,5,6,7]

list_num_din = []

cont = 0

while cont <=6:
    cont +=1
    
    num = int(input("Digite um Numero: "))
    list_num_din.append(num)

#Soma da lista:

soma_din = sum(list_num_din)
soma_fix = sum(list_num_fix)

print("Soma da lista Fixa: "+str(soma_fix))
print("Soma da lista DInamica: "+str(soma_din))


#Menor Numero

print("Menor Valor na lista dinamica  é: "+str(min(list_num_din)))

print("Menor Valor na lista fixa  é: "+str(min(list_num_fix)))



#Maior Numero

print("Maior Valor na lista dinamica  é: "+str(max(list_num_din)))

print("Maior Valor na lista fixa  é: "+str(max(list_num_fix)))

