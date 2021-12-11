from process_list import ListaCompra


def execute():
    lista_compra = ListaCompra()
    list_prod = lista_compra.list_product()

    lista_compra.process_list_prod_rep(list_prod)

    # produto = input("Digite o Produto: ")
    # marca = input("Digite a Mzrca: ")
    # quantidade = lista_compra.procees_list_prod_zero(produto,int(input("Digite a quantidade: ")))

    # list_prod = []
    # list_prod.append(lista_compra.add_list_product(produto,marca,quantidade,list_prod))


execute()