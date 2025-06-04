import time
import os
from rich.console import Console

console = Console()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def digitar_red(texto, velocidade=0.03):
    for letra in texto:
        console.print(letra, end='', style="bold red")
        time.sleep(velocidade)
    print()

def digitar_pink(texto, velocidade=0.03):
    for letra in texto:
        console.print(letra, end='', style="hot_pink")
        time.sleep(velocidade)
    print()

def digitar(texto, velocidade=0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidade)
    print()

def introducao_jogo(nome):
    digitar(f"Olá, {nome}. Bem-vindo à sua nova realidade: uma cela fria e silenciosa.\n"
           "Você foi preso(a)... mas não sabe exatamente por quê.\n"
           "Suas escolhas daqui em diante serão cruciais.\n"
           "Cada decisão pode te levar à liberdade — ou te condenar para sempre.\n"
           "Está pronta para enfrentar as sombras dessa prisão?\n")

def aviso_inicial(nome):
    digitar(f"⚠️  AVISO IMPORTANTE, {nome}!")
    digitar("As decisões que você tomar a partir de agora influenciarão diretamente sua trajetória.")
    digitar("Não há escolhas certas ou erradas — apenas consequências.")
    digitar("Pense com calma. Avalie os riscos.")
    input("Pressione 'Enter' para continuar")

def nivel_um(nome):
    digitar("Você desperta em uma cela úmida e mal iluminada. O ar é pesado, e tudo ao seu redor parece estranho.")
    digitar("As lembranças da noite anterior voltam aos poucos: a polícia arrombando sua porta, gritos, confusão...")
    digitar("Acusado(a) de um crime que não cometeu, você agora está atrás das grades — e uma coisa é certa: não pretende permanecer aqui.")
    digitar("Primeira Escolha: O que fazer ao acordar?")
    digitar("A - Investigar a cela \nB - Chamar por alguém \nC - Esperar em silêncio")
    escolha_nivel_um()

def escolha_nivel_um():
    digitar("[NÍVEL 1] - O Despertar")
    while True:
        escolha = input("Digite sua escolha (A/B/C): ").strip().upper()
        if escolha == 'A':
            investigacao_cela()
            break
        elif escolha == 'B':
            chamar_por_alguem()
            break
        elif escolha == 'C':
            esperar_em_silencio()
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def investigacao_cela():
    digitar("[NÍVEL 2] - A Descoberta")
    digitar("Você decide investigar a cela.")
    digitar("Passa os dedos pelas rachaduras nas paredes e examina a cama enferrujada.")
    digitar("Atrás de um tijolo solto, encontra um bilhete amassado.")
    digitar_pink("[i]“Confie em ninguém. A saída está sob seus pés.”[/i]")
    digitar("Você sente o chão tremer levemente... algo está escondido ali.")
    escolha = input("A - Cavar discretamente \nB - Esconder o bilhete e esperar\nEscolha: ").strip().upper()
    if escolha == 'A':
        cavar_saida()
    else:
        esperar_depois_bilhete()

def cavar_saida():
    digitar("[NÍVEL 3] - Túnel Secreto")
    digitar("Com uma colher enferrujada escondida sob o colchão, você começa a cavar.")
    digitar("Horas se passam. Finalmente, um túnel apertado se revela.")
    digitar("Você rasteja por ele até encontrar uma grade solta que leva aos esgotos.")
    digitar("Antes de entrar, um outro prisioneiro o intercepta. Ele diz que quer ajudar, mas parece instável.")
    escolha = input("A - Deixar ele vir junto\nB - Ameaçar e seguir sozinho\nEscolha: ").strip().upper()
    if escolha == 'A':
        companheiro_esgoto()
    else:
        conflito_esgoto()

def companheiro_esgoto():
    digitar("[NÍVEL 4] - Traição nas Sombras")
    digitar("Vocês seguem juntos, mas a tensão cresce. Ele desconfia de você, e você dele.")
    digitar("Em uma encruzilhada, ele tenta trair você e te empurra na água.")
    digitar("Você reage, luta por sua vida e o empurra contra a parede. Ele cai inconsciente.")
    digitar("Ferido, você segue sozinho pela galeria oculta.")
    galeria_oculta()

def conflito_esgoto():
    digitar("[NÍVEL 4] - Confronto Imprudente")
    digitar("Você empurra o prisioneiro e segue sozinho pelos esgotos.")
    digitar("Ele grita, alertando guardas por vingança. Alarmes disparam.")
    digitar("Você corre desesperadamente até cair em uma câmara subterrânea.")
    digitar("Lá, encontra um velho guarda desacordado com crachá e arma.")
    escolha = input("A - Usar o crachá para abrir portas\nB - Pegar a arma e se defender\nEscolha: ").strip().upper()
    if escolha == 'A':
        usar_cracha()
    else:
        pegar_arma()

def usar_cracha():
    digitar("[NÍVEL 5] - Identidade Falsa")
    digitar("Você passa por portas trancadas, mas o crachá ativa sensores que alertam sobre sua localização.")
    digitar("Uma equipe de segurança é enviada para te deter.")
    digitar("Você precisa improvisar e se esconder na ventilação.")
    digitar("Enquanto rasteja, escuta conversas suspeitas sobre um programa de controle mental com prisioneiros.")
    galeria_oculta()

def pegar_arma():
    digitar("[NÍVEL 5] - Armadilha Letal")
    digitar("A arma está sem munição. Foi uma armadilha.")
    digitar("O guarda acorda e ativa o alarme. Você é cercado e recapturado.")
    digitar_red("FIM DE JOGO: Você foi recapturado e será transferido para um setor de segurança máxima.")

def esperar_depois_bilhete():
    digitar("[NÍVEL 3] - Espera Estratégica")
    digitar("Você guarda o bilhete e finge dormir. Um guarda entra para inspeção e você nota que ele carrega um molho de chaves solto no cinto.")
    digitar("Você pode tentar se aproximar dele em outro momento e usar isso a seu favor.")
    galeria_oculta()

def galeria_oculta():
    digitar("[NÍVEL 6] - A Galeria Oculta")
    digitar("Você segue pela galeria úmida e encontra uma porta de manutenção antiga.")
    digitar("Com esforço, consegue abri-la e se vê em um depósito com uniformes e mapas.")
    digitar("Você está um passo mais perto da liberdade — mas o caminho ainda é longo.")
    digitar("No mapa, três rotas são marcadas: uma pelo telhado, outra pelos esgotos, e uma terceira pelo pátio.")
    escolha = input("A - Tentar o telhado\nB - Voltar aos esgotos\nC - Atravessar o pátio\nEscolha: ").strip().upper()
    if escolha == 'A':
        fuga_telhado()
    elif escolha == 'B':
        armadilha_esgoto()
    else:
        fuga_patio()

def fuga_telhado():
    digitar("[NÍVEL 7] - Liberdade nas Alturas")
    digitar("Você escala silenciosamente pelas tubulações até o topo.")
    digitar("Evita refletores, atravessa o telhado e alcança o muro externo.")
    digitar("Com um salto arriscado, você cai em uma mata densa.")
    digitar_pink("VOCÊ CONSEGUIU! Agora está foragido, mas livre. O mundo lá fora te espera.")

def armadilha_esgoto():
    digitar("[NÍVEL 7] - A Armadilha Final")
    digitar("Você retorna aos esgotos, mas não percebe que uma armadilha foi armada pelos guardas.")
    digitar("Gás começa a vazar pelas tubulações, e você desmaia.")
    digitar_red("FIM DE JOGO: Você foi recapturado inconsciente. Não haverá segunda chance.")

def fuga_patio():
    digitar("[NÍVEL 7] - Risco no Pátio")
    digitar("Disfarçado com um uniforme de faxineiro, você atravessa o pátio como se fosse parte da equipe.")
    digitar("Troca palavras com um guarda simpático que não desconfia de nada.")
    digitar("Ao passar pelos portões principais, um caminhão de mantimentos se prepara para sair.")
    digitar("Você se esconde entre as caixas e espera. O motor ronca...")
    digitar_pink("VOCÊ ESCAPOU! Agora é hora de recomeçar, longe dos muros que te prenderam.")

def chamar_por_alguem():
    digitar("[NÍVEL 2] - O Grito na Cela")
    digitar("Você grita por ajuda, mas ninguém responde.")
    digitar("O silêncio é pesado e ameaçador.")
    digitar("Depois de um tempo, percebe que não adianta esperar e decide agir.")
    investigacao_cela()

def esperar_em_silencio():
    digitar("[NÍVEL 2] - O Silêncio Mortal")
    digitar("Você decide esperar em silêncio e refletir sobre a situação.")
    digitar("O tempo passa lentamente, e nada acontece.")
    digitar("Sentindo-se cada vez mais desesperado, você resolve investigar a cela.")
    investigacao_cela()
