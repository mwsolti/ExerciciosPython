from proc import regraGmae,processa_forca


def coleta_letra():
    letra = input("Digite Uma Letra Que Exista na Palavra: ")
    return(letra)

def run():
    proc_game = processa_forca()
    proc_game.acertou(coleta_letra())


run()