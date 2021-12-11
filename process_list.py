
class ListaCompra():

    def list_product(self):
        
        list_prod = [   {"Queijo": {"Tirol":1}}, 
                        {"Queijo":{"Pia":1}},
                        {"Macarrão":{"Orquidea":1}},
                        {"Maionese":{"Helmans":1}},
                        {"Leite":{"Pia":1}},
                        {"Mostarda":{"Hemmer":1}},
                        {"Leite":{"Tirol":1}},
                        {"Bacon":{"Celpa":1}},
                        {"Linguiça Blumenau":{"Celpa":1}},
                        
        ]

        return list_prod

    def add_list_product(self,produto,marca,quantidade,list_prod):
        dict_prod = {produto:{marca:quantidade}}
        return dict_prod


    def procees_list_prod_zero(self,produto,quantidade):
        if(quantidade == 0):
            print("Item  :" +produto+" Está Zerado \n")
            quantidade = (input("Digite um Valor Valido para o Produto"))
            self.procees_list_prod_zero(produto,quantidade)
        else:
            return quantidade


    def process_list_prod_rep(self,list_prod):
        list_key_prod = []
        for dict_produ in self.list_product():
            key_prod = list(dict_produ.keys())
            list_key_prod.append(key_prod[0])
        
        cont = 0
        for item in list_key_prod:
            qt_item_list = list_key_prod.count(item)
            if qt_item_list > 1:
                print (" Item: "+ item +" Repetido!")


    
