# historia.py

from historia import introducao_jogo, aviso_inicial, digitar, limpar_tela # Importando funções de historia.py


def main():
    #limpar tela
    limpar_tela()

    #tela de inicio
    digitar("\n=== VOCÊ FOI PRESO ===")

    # Aqui você pega o nome do jogador
    nome = input("Digite o nome do seu personagem: ")

    #limpar tela
    limpar_tela()

    # Chamando a função que vai mostrar a introdução
    introducao_jogo(nome)

    # Chamando a função que vai mostrar o aviso
    aviso_inicial(nome)


#conseguir fazer a separação para gente organizar melhor o codigo so que estava dando erro, A IA falou que faltava essa...
# "proteção", não entendi muito bem essa parte. irei ver melhor!:
if __name__ == "__main__":
    main()


