dicPessoa ={'Nome':'',
            'Sobrenome':'',
            'Idade':''}

dicEndereco = { 'Rua':'',
                'Bairro':'',
                'Cidade':'',
                'Estado':''}


listaChavesPessoa = dicPessoa.keys()
listaCHavesEndereco = dicEndereco.keys()

for chv in listaChavesPessoa:
  dado = input("Digite o "+chv+": ")
  dicPessoa[chv] = dado

for chv in listaCHavesEndereco:
  dado = input("Digite o "+chv+": ")
  dicEndereco[chv] = dado
 

dicCadastro = {}
# Fusão Dicionarios
dicCadastro.update(dicPessoa)
dicCadastro.update(dicEndereco)

arquivo = open('cadastro.txt', 'w')

listaCHavesCadastro = dicCadastro.keys()

for item in listaCHavesCadastro:
  # Chave : Valor \n
  linhaArquivo = " "+item+" : "+dicCadastro.get(item) +" \n"
  arquivo.write(linhaArquivo)

arquivo.close()


#writelines

#readlines

lerARquivo = open('cadastro.txt', 'r')

for linha in lerARquivo:
  print(linha)


'''

listaARquivo =['Cont linha 1','2',''3]


'''


