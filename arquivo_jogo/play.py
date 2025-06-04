from historia import limpar_tela, digitar_red, digitar_pink, digitar, introducao_jogo, aviso_inicial, nivel_um

def main():
    limpar_tela()
    digitar_red("=== VOCÊ FOI PRESO ===")
    nome = input("Digite o nome do seu personagem: ")
    limpar_tela()
    introducao_jogo(nome)
    aviso_inicial(nome)
    limpar_tela()
    digitar_pink("\n=== NÍVEL 1 ===")
    nivel_um(nome)

if __name__ == "__main__":
    main()
