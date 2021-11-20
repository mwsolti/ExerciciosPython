
dict_lista = {}

#Recebe Dados
def coletor_dados_lista(item,quantidade):
    dict_lista[item] = quantidade
    return dict_lista

#Processa Dados
def processa_dados_lista_item_repetido(dict_lista, item, quantidade):
    
    #Verifica Item Duplicado
    for nome_item in dict_lista.keys():
        if (item == nome_item):
            print("Item UDplicado Encontrado")
            op = int(input(" 1 - Cancelar Item \n"
                       + "2 - Somar QUantidade dos Items DUplicados"))
            #Cancela Item
            if op == 1:
                print ("Item Cancelado")
                return
            else:
                print ("Item Somado" )        
                dict_lista[item] += quantidade
                return 
            
        else:
            return
            
    
    
    #Processa Item Zerado
def processa_dados_lista_item_zerado(dict_lista, item, quantidade):
        
       if quantidade ==0:
           print("Produto Zerado \n")
           op = int(input("Deseja Cancelar? \n"+
                      "1 - SIm \n"
                      + " 2 - Não"))
            
           if op == 1:
               print("Cancelado")
               return
           else: 
               qt_nova = int(input("Insire Uma qunatidade para este item"))
               dict_lista[item] += qt_nova
               return
            
       else:
           return
    
inicia_lista = 1
cont_seg = 0
while (inicia_lista == 1):
    item = input("Ditige o nome do Produto: ")
    quantidade = int(input("Digite a Quantidade deste Produto: "))
    
    lista_de_Produtos = coletor_dados_lista(item, quantidade)
    
    cont_seg += 1
    
    if (cont_seg  > 1):
        processa_dados_lista_item_repetido(lista_de_Produtos,item,quantidade)
        
    processa_dados_lista_item_zerado(lista_de_Produtos,item,quantidade)
    
    inicia_lista = int(input(" Deseja COntinua? \n" + 
          "1 - Sim \n"+
          "2 - Não \n"))
    

print(dict_lista)
