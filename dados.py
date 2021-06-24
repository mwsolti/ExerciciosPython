from arquivos import manipula_arquivo

class dadosCadastro():

  def criaDicionario(self):
    dicCadastro = {}

    arquivo = manipula_arquivo()
    arquivo.manipulaArquivo('chaves.txt','r')
    listaChaves = arquivo.lerArquivo()
 
    arquivo.manipulaArquivo('valores.txt','r')

    controleValor = 0

    listaValores = arquivo.lerArquivo()

    for chv in listaChaves :
      dicCadastro[chv] = listaValores[controleValor] 
      controleValor += 1
            
    return dicCadastro
    

  def cadastro(self):
    arquivo = manipula_arquivo()
    arquivo.manipulaArquivo('cadastro.txt','r')
    listaCadastro = arquivo.lerArquivo()
    dicCadastro = {}
    for item in listaCadastro:
      listaItem = item.split(':')
      dicCadastro.update({listaItem[0]:listaItem[1]})

    return dicCadastro


    
