# historia.py

from historia import introducao_jogo, aviso_inicial, digitar, limpar_tela, nivel_um, digitar_red, digitar_pink # Importando funções de historia.py

def main():
    limpar_tela()
    #tela de inicio
    texto = "=== VOCÊ FOI PRESO ==="
    digitar_red(texto)
    # Aqui você pega o nome do jogador
    nome = input("Digite o nome do seu personagem: ")
    #limpar tela
    limpar_tela()
    # Chamando a função que vai mostrar a introdução
    introducao_jogo(nome)
    # Chamando a função que vai mostrar o aviso
    aviso_inicial(nome)
    #tela nivel 1
    limpar_tela()
    digitar_pink("\n=== NÍVEL 1 ===")
    nivel_um(nome)



#Usando if __name__ == "__main__":, você garante que o 
#código dentro dele só execute se você rodar python play.py
#diretamente.
if __name__ == "__main__":
    main()


