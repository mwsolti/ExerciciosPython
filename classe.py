class cauculaMedia():

    def calc_media(self, nota1,nota2,nota3):
        total = nota1+nota2+nota3
        media = total/3
        return media
    
    def status(self,media):
        if media >=7:
            return "Passou"
        elif media >=5:
            return "Recuperação"
        else:
            return "Reprovou"

