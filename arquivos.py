class manipula_arquivo:

  _manipula  = ''
  _nomeARquivo = ''
  _texto = ''

  def manipulaArquivo(self,nomeArquivo,manipula = 'w'):
    self._nomeARquivo = nomeArquivo
    self._manipula = manipula

    #Abaixo SOlução de contorno para evitar erro do usuari e ler arquivo inexistente
    arq = self.arquivo()
    arq.close()
  
  def setTexto(self,texto):
    self._texto = texto
  
  def arquivo(self):
    arquivo = open(self._nomeARquivo,self._manipula)
    return arquivo

  def insereTextoArquivo(self):
    if self._manipula == 'r':
      print("Você esta lendo e não gravando")
      return
    arq = self.arquivo()
    arq.writelines(self._texto)
    arq.close()
  
  def lerArquivo(self):
    arq = self.arquivo()
    listaLinhas = arq.readlines()
    arq.close()
    return listaLinhas


    
    



