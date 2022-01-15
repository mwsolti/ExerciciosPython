
class regraGmae():

    def qt_letras_total_erro(self):
        return 6


    def palavra_padrao(self):
        return "Abacate" 

        
class processa_forca():

    def coleta_palavra(self):
        reg = regraGmae()
        return reg.palavra_padrao().lower()
    
    def tamanho_palavra(self):
        q1t_letras = len(self.coleta_palavra())
        return q1t_letras
    
    def acertou(self,letra, qt_acertos = 0 ,qt_erros = 0, letras_list = []):
        
        qt_letras_palavra = self.coleta_palavra().count(letra)

        if letra in letras_list:
            qt_erros +=1
            print("Você Já Digitou esta Letra Candango!")
            self.bonequixa(qt_erros)
            letra = input("Digite outra letra")

            if qt_erros == regraGmae().qt_letras_total_erro():
                print("Você Perdeu O Game")
                return

            self.acertou(letra,qt_acertos,qt_erros,letras_list)        

        else:

            print(self.tamanho_palavra())
            #print((qt_acertos))

            if qt_letras_palavra > 0:
                qt_acertos += qt_letras_palavra
                print(qt_acertos)
                print("Acertou Mizeravi")
            else:
                qt_erros += 1
                print("Errou Tio!")
                self.bonequixa(qt_erros)
            
            if qt_acertos == self.tamanho_palavra():
                print ("Você Ganhou o Game")
                return
            
            elif qt_erros == regraGmae().qt_letras_total_erro():
                print("Você Perdeu O Game")
                return

            else:
                letras_list.append(letra)
                letra = input("Digite outra letra")
                self.acertou(letra,qt_acertos,qt_erros,letras_list) 




    def bonequixa(self,qt_erros):
        txt = ""

        if qt_erros ==1 :
            txt = "    0    "
        elif qt_erros ==2:
            txt = "    0    \n"
            txt +="    |    "
        elif qt_erros ==3:
            txt = "    0    \n"
            txt +="   -|    "
        elif qt_erros ==4:
            txt = "    0    \n"
            txt +="   -|-   "
        elif qt_erros ==5:
            txt = "    0    \n"
            txt +="   -|-   \n"
            txt +="   /     "
        elif qt_erros ==6:
            txt = "    0    \n"
            txt +="   -|-   \n"
            txt +="   / \   "
        
        print(txt)




    


        


    




