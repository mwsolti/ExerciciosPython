palavra = 'Abacate'
palavra = palavra.lower()

comparacao =""
errou = 0
acertou = 0
qtLetras = 0

txt = "VVocê perdeu playboy ou playgirl"

for l in palavra:
  qtLetras = qtLetras + 1


while errou !=6:
  letra = input("Digite uma letra")
  qtLetrasCertas =palavra.count(letra)

  if  letra in comparacao:
    print("Você ja digitou tende novamente --> \l")

  else: 
    if qtLetrasCertas == 1:

      if letra in palavra:
        print("Acerouuuuu")
        acertou = acertou+1
        comparacao = comparacao+letra
        print (comparacao)
      else:
        print("Errouuuuu")
        errou = errou + 1
   
    
    else:
      acertou = acertou+qtLetrasCertas
      comparacao = comparacao+letra

    if acertou >= qtLetras:
       txt = "Ganhou"
       break

print(txt)
   
