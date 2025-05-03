# historia.py

from historia import introducao_jogo, aviso_inicial  # Importando funções de funcoes_historia.py


def main():
    # Aqui você pega o nome do jogador
    nome = input("Digite o nome do seu personagem: ")

    # Chamando a função que vai mostrar a introdução
    introducao_jogo(nome)

    # Chamando a função que vai mostrar o aviso
    aviso_inicial(nome)



#conseguir fazer a separação para gente organizar melhor o codigo so que estava dando erro, A IA falou que faltava essa...
# "proteção", não entendi muito bem essa parte. irei ver melhor!:
if __name__ == "__main__":
    main()


