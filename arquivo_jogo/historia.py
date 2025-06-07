
# play.py

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
    input("Pressione 'Enter' para continuar")

def aviso_inicial(nome):
    limpar_tela()
    digitar(f"⚠️  AVISO IMPORTANTE, {nome}!")
    digitar("As decisões que você tomar a partir de agora influenciarão diretamente sua trajetória.")
    digitar("Não há escolhas certas ou erradas — apenas consequências.")
    digitar("Pense com calma. Avalie os riscos.")
    input("Pressione 'Enter' para continuar")

def nivel_um(nome):
    limpar_tela()
    digitar("[NÍVEL 1] - O Despertar")
    digitar("Você desperta em uma cela úmida e mal iluminada. O ar é pesado, e tudo ao seu redor parece estranho.")
    digitar("As lembranças da noite anterior voltam aos poucos: a polícia arrombando sua porta, gritos, confusão...")
    digitar("Acusado(a) de um crime que não cometeu, você agora está atrás das grades — e uma coisa é certa: não pretende permanecer aqui.")
    digitar("Primeira Escolha: O que fazer ao acordar?")
    digitar("A - Investigar a cela \nB - Chamar por alguém \nC - Esperar em silêncio")
    escolha_nivel_um(nome)

def escolha_nivel_um(nome):
    digitar("[NÍVEL 1] - O Despertar")
    while True:
        escolha = input("Digite sua escolha (A/B/C): ").strip().upper()
        if escolha == 'A':
            investigacao_cela(nome)
            break
        elif escolha == 'B':
            reacao_chamado(nome)
            break
        elif escolha == 'C':
            observar_ambiente(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def reacao_chamado(nome):
    limpar_tela()
    digitar("[NÍVEL 2] - O Grito Atrai Atenção")
    digitar("Você grita por ajuda, e o som ecoa pelo corredor. Momentos depois, passos se aproximam e um guarda para em frente à sua cela.")
    digitar("Ele te olha com uma expressão de tédio e irritação.")
    digitar(f"Guarda: 'Qual o problema, {nome}? Quer mais tempo aqui?'")
    digitar("Como você responde?")
    digitar("A - Tentar acalmar o guarda e pedir informações\nB - Desafiar o guarda e exigir seus direitos")

    while True:
        escolha = input("Escolha (A/B): ").strip().upper()
        if escolha == 'A':
            interagir_guarda(nome)
            break
        elif escolha == 'B':
            conflito_guarda(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def observar_ambiente(nome):
    limpar_tela()
    digitar("[NÍVEL 2] - O Silêncio Revelador")
    digitar("Você decide esperar em silêncio, observando atentamente o ambiente ao seu redor.")
    digitar("O tempo passa lentamente. Você percebe padrões nos sons, nos horários das rondas dos guardas e na iluminação que entra pela pequena fresta.")
    digitar("De repente, você ouve uma conversa abafada vinda da cela vizinha.")
    digitar("O que você faz?")
    digitar("A - Tentar ouvir a conversa da cela vizinha\nB - Focar na rotina dos guardas e buscar uma oportunidade")

    while True:
        escolha = input("Escolha (A/B): ").strip().upper()
        if escolha == 'A':
            ouvir_conversa_cela(nome)
            break
        elif escolha == 'B':
            observar_rotina_guarda(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def investigacao_cela(nome):
    limpar_tela()
    digitar("[NÍVEL 2] - A Descoberta")
    digitar("Você decide investigar a cela.")
    digitar("Passa os dedos pelas rachaduras nas paredes e examina a cama enferrujada.")
    digitar("Atrás de um tijolo solto, encontra um bilhete amassado.")
    digitar_pink("[i]“Confie em ninguém. A saída está sob seus pés.”[/i]")
    digitar("Você sente o chão tremer levemente... algo está escondido ali.")
    digitar("A - Cavar discretamente \nB - Esconder o bilhete e esperar\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            cavar_saida(nome)
            break
        elif escolha == 'B':
            esperar_depois_bilhete(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def cavar_saida(nome):
    limpar_tela()
    digitar("[NÍVEL 3] - Túnel Secreto")
    digitar("Com uma colher enferrujada escondida sob o colchão, você começa a cavar.")
    digitar("Horas se passam. Finalmente, um túnel apertado se revela.")
    digitar("Você rasteja por ele até encontrar uma grade solta que leva aos esgotos.")
    digitar("Antes de entrar, um outro prisioneiro o intercepta. Ele diz que quer ajudar, mas parece instável.")
    digitar("A - Deixar ele vir junto\nB - Ameaçar e seguir sozinho\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            companheiro_esgoto(nome)
            break
        elif escolha == 'B':
            conflito_esgoto(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def companheiro_esgoto(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - Traição nas Sombras")
    digitar("Vocês seguem juntos, mas a tensão cresce. Ele desconfia de você, e você dele.")
    digitar("Em uma encruzilhada, ele tenta trair você e te empurra na água.")
    digitar("Você reage, luta por sua vida e o empurra contra a parede. Ele cai inconsciente.")
    digitar("Ferido, você segue sozinho pela galeria oculta.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def conflito_esgoto(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - Confronto Imprudente")
    digitar("Você empurra o prisioneiro e segue sozinho pelos esgotos.")
    digitar("Ele grita, alertando guardas por vingança. Alarmes disparam.")
    digitar("Você corre desesperadamente até cair em uma câmara subterrânea.")
    digitar("Lá, encontra um velho guarda desacordado com crachá e arma.")
    digitar("A - Usar o crachá para abrir portas\nB - Pegar a arma e se defender\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            usar_cracha(nome)
            break
        elif escolha == 'B':
            pegar_arma(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def usar_cracha(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Identidade Falsa")
    digitar("Você passa por portas trancadas, mas o crachá ativa sensores que alertam sobre sua localização.")
    digitar("Uma equipe de segurança é enviada para te deter.")
    digitar("Você precisa improvisar e se esconder na ventilação.")
    digitar("Enquanto rasteja, escuta conversas suspeitas sobre um programa de controle mental com prisioneiros.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def pegar_arma(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Armadilha Letal")
    digitar("A arma está sem munição. Foi uma armadilha.")
    digitar("O guarda acorda e ativa o alarme. Você é cercado e recapturado.")
    digitar_red("FIM DE JOGO: Você foi recapturado e será transferido para um setor de segurança máxima.")

def esperar_depois_bilhete(nome):
    limpar_tela()
    digitar("[NÍVEL 3] - Espera Estratégica")
    digitar("Você guarda o bilhete e finge dormir. Um guarda entra para inspeção e você nota que ele carrega um molho de chaves solto no cinto.")
    digitar("Você pode tentar se aproximar dele em outro momento e usar isso a seu favor.")
    digitar("A - Tentar uma distração para pegar as chaves\nB - Observar mais para encontrar uma rotina do guarda\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            distracao_chaves(nome)
            break
        elif escolha == 'B':
            observar_rotina_para_chaves(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def interagir_guarda(nome):
    limpar_tela()
    digitar("[NÍVEL 3] - Persuasão na Cela")
    digitar("Você tenta acalmar o guarda, explicando sua inocência e pedindo informações sobre o motivo da sua prisão.")
    digitar("Ele parece ligeiramente surpreso com sua calma, mas se mantém cauteloso.")
    digitar(f"Guarda: 'Inocente? Todos dizem isso. Mas o que você está fazendo aqui então?'")
    digitar("Ele parece um pouco curioso. Você sente que pode conseguir algo dele.")
    digitar("A - Oferecer algo em troca de ajuda (se tiver algo de valor)\nB - Tentar convencê-lo de sua inocência com mais detalhes\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            oferecer_suborno(nome)
            break
        elif escolha == 'B':
            argumentar_inocencia(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def conflito_guarda(nome):
    limpar_tela()
    digitar("[NÍVEL 3] - Desafio Perigoso")
    digitar("Você desafia o guarda, exigindo seus direitos e reclamando da prisão injusta.")
    digitar("A face do guarda endurece. Ele se aproxima da cela e te encara.")
    digitar(f"Guarda: 'Direitos? Aqui, seus direitos são ficar calado e obedecer! Quer problemas, {nome}?'")
    digitar("Ele saca o cassetete, pronto para usar a força.")
    digitar("A - Recuar e tentar acalmar a situação\nB - Provocá-lo ainda mais, buscando uma reação exagerada\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            recuar_conflito(nome)
            break
        elif escolha == 'B':
            provocar_guarda(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def ouvir_conversa_cela(nome):
    limpar_tela()
    digitar("[NÍVEL 3] - Sussurros Misteriosos")
    digitar("Você se aproxima da parede e tenta ouvir a conversa da cela vizinha.")
    digitar("Os sons são abafados, mas você consegue distinguir algumas palavras-chave: 'transferência', 'plano', 'agora'.")
    digitar("Parece que os prisioneiros vizinhos estão planejando algo ou prestes a serem movidos.")
    digitar("Você pode tentar se comunicar ou usar essa informação a seu favor.")
    digitar("A - Bater na parede e tentar uma comunicação silenciosa\nB - Ignorar a conversa e focar na sua própria fuga\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            comunicar_vizinho(nome)
            break
        elif escolha == 'B':
            ignorar_e_observar(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def observar_rotina_guarda(nome):
    limpar_tela()
    digitar("[NÍVEL 3] - Padrões de Segurança")
    digitar("Você foca na rotina dos guardas. Depois de um tempo, percebe que um guarda em particular sempre faz uma ronda com um atraso de alguns minutos em um determinado horário.")
    digitar("Isso cria uma pequena janela de oportunidade na qual a ala da sua cela fica brevemente sem supervisão direta.")
    digitar("O que você faz com essa informação?")
    digitar("A - Preparar uma distração para essa janela de tempo\nB - Buscar uma ferramenta para arrombar algo na cela durante essa janela\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            preparar_distracao(nome)
            break
        elif escolha == 'B':
            buscar_ferramenta_cela(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def distracao_chaves(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - O Roubo da Chave")
    digitar("Você tenta criar uma distração, tossindo alto e derrubando sua caneca. O guarda se vira para repreendê-lo(a).")
    digitar("Rapidamente, você estende a mão e tenta pegar o molho de chaves em seu cinto.")
    digitar("A - Pegar as chaves e correr\nB - Tentar disfarçar se o guarda perceber\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            correr_com_chaves(nome)
            break
        elif escolha == 'B':
            limpar_tela()
            digitar("[NÍVEL 5] - Quase Pego(a)")
            digitar("Você tenta disfarçar, mas o guarda percebe sua intenção. Ele te olha desconfiado, mas decide não fazer uma confusão maior. 'Fique na linha', ele diz, e se afasta.")
            input("Pressione 'Enter' para continuar.")
            galeria_oculta(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def observar_rotina_para_chaves(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - Padrão do Guarda")
    digitar("Você decide não agir impulsivamente e passa mais tempo observando o guarda. Percebe que, a cada duas rondas, ele para para beber água em um bebedouro próximo, deixando as chaves penduradas por um instante.")
    digitar("É um risco, mas uma oportunidade clara.")
    digitar("A - Tentar pegar as chaves no momento certo\nB - Usar o momento para investigar a cela novamente (com mais calma)\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            pegar_chaves_bebedouro(nome)
            break
        elif escolha == 'B':
            investigar_cela_novamente_c4(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def oferecer_suborno(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - A Oferta Tentadora")
    digitar("Você revela que tem um pequeno objeto de valor (um relógio, um anel, etc.) que conseguiu esconder e oferece ao guarda em troca de uma 'ajuda' para sair.")
    digitar("Os olhos do guarda brilham com a possibilidade. Ele pega o objeto e o examina, pensativo.")
    digitar("Guarda: 'Interessante... O que você quer, exatamente?'")
    digitar("A - Pedir para ele 'esquecer' sua cela destrancada na próxima ronda\nB - Pedir informações sobre uma rota de fuga segura\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            cela_destrancada_suborno(nome)
            break
        elif escolha == 'B':
            informacao_rota_suborno(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def argumentar_inocencia(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - Retórica na Prisão")
    digitar("Você persiste, fornecendo detalhes convincentes sobre sua inocência, sobre onde estava e o que fazia na noite do crime.")
    digitar("O guarda ouve, sua expressão mudando de tédio para uma leve dúvida.")
    digitar("Guarda: 'Hmm... sua história é um pouco diferente da que ouvi. Mas eu sou apenas um guarda. Há um oficial de interrogatório que vem amanhã. Talvez ele te ouça.'")
    digitar("O guarda se afasta, visivelmente pensativo.")
    digitar("A - Tentar convencer outro guarda a te ajudar\nB - Se preparar para o interrogatório de amanhã\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            tentar_outro_guarda(nome)
            break
        elif escolha == 'B':
            preparar_interrogatorio(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def recuar_conflito(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - Recuo Estratégico")
    digitar("Você recua, levantando as mãos em sinal de paz. O guarda ainda está irritado, mas baixa um pouco o cassetete.")
    digitar("Guarda: 'É bom mesmo. Fique na sua, ou as coisas vão piorar para você.'")
    digitar("Ele se afasta, mas agora você está em sua lista negra. Ele te observará mais de perto.")
    digitar("Você precisa encontrar uma forma de sair sem ser detectado ou enfrentar esse guarda novamente.")
    digitar("A - Procurar por uma ferramenta ou item que ele tenha deixado cair\nB - Esperar pela troca de turno e tentar a sorte com outro guarda\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            procurar_item_guarda(nome)
            break
        elif escolha == 'B':
            esperar_troca_turno(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def provocar_guarda(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - Provocação Perigosa")
    digitar("Você decide provocá-lo ainda mais, esperando que ele reaja de forma exagerada e cometa um erro.")
    digitar("Guarda: 'Ah, é assim? Quer brincar, é?'")
    digitar("Ele abre a porta da cela, entra furioso e te empurra contra a parede. Mas ao fazer isso, ele deixa cair sua arma (um spray de pimenta) e o rádio.")
    digitar("A - Pegar o spray de pimenta e incapacitá-lo\nB - Pegar o rádio e tentar pedir ajuda externa ou alertar a prisão\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            usar_spray_pimenta(nome)
            break
        elif escolha == 'B':
            digitar_red("FIM DE JOGO: Sua tentativa com o rádio alertou a todos. Você foi encurralado(a) e recapturado(a) sem chance.")
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def comunicar_vizinho(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - Comunicação Secreta")
    digitar("Você bate na parede com um padrão específico. Depois de um tempo, a batida é respondida. É um prisioneiro experiente.")
    digitar("Através de um código de batidas e sussurros, vocês trocam informações. Ele diz que há um túnel antigo de contrabando que leva para fora, mas ele está bloqueado por escombros.")
    digitar("Ele também menciona que a chave para limpar a passagem está com um guarda específico, conhecido por ser negligente.")
    digitar("A - Pedir ajuda para o prisioneiro na limpeza do túnel\nB - Focar em distrair o guarda negligente para pegar a chave\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            limpar_tunel_ajuda(nome)
            break
        elif escolha == 'B':
            digitar_red("FIM DE JOGO: O guarda negligente não era tão negligente assim. Você foi pego(a) tentando roubar e acabou em segurança máxima.")
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def ignorar_e_observar(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - Observação Silenciosa")
    digitar("Você decide ignorar a conversa e focar na sua própria fuga, prestando atenção em tudo ao redor.")
    digitar("Durante a troca de turnos, você percebe que um dos guardas mais velhos, ao se despedir, joga um maço de cigarros e um isqueiro no lixo do corredor.")
    digitar("Isso é contra as regras da prisão, mas o guarda parece não se importar. É uma pequena oportunidade para criar um desvio.")
    digitar("A - Tentar pegar o isqueiro para criar uma distração (fumaça/fogo)\nB - Ignorar e buscar uma rota de fuga menos arriscada\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            pegar_isqueiro_distracao(nome)
            break
        elif escolha == 'B':
            buscar_rota_menos_risco(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def preparar_distracao(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - A Arte da Distração")
    digitar("Você usa um pedaço de pano da sua coberta e alguns restos de comida para criar um pequeno 'barulho' ou 'cheiro' suspeito perto da grade da sua cela.")
    digitar("Quando o guarda passa com seu atraso habitual, a distração funciona! Ele para para investigar o barulho, se afastando do seu posto por um momento.")
    digitar("Isso cria uma janela de oportunidade para você agir.")
    digitar("A - Tentar arrombar a fechadura da sua cela rapidamente\nB - Usar o momento para rastejar para fora da cela por uma fresta no chão\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            arrombar_fechadura(nome)
            break
        elif escolha == 'B':
            rastejar_fresta_chao(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def buscar_ferramenta_cela(nome):
    limpar_tela()
    digitar("[NÍVEL 4] - Ferramenta Improvável")
    digitar("Você procura algo na cela que possa servir de ferramenta durante a janela de atraso do guarda.")
    digitar("Atrás do vaso sanitário, encontra um pedaço de metal afiado, provavelmente de um antigo encanamento. É pequeno, mas pode ser útil.")
    digitar("No momento exato do atraso do guarda, você se posiciona para usar a ferramenta.")
    digitar("A - Usar o pedaço de metal para tentar serrar as grades da cela\nB - Usar o pedaço de metal para tentar forçar a fechadura da cela\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            digitar_red("FIM DE JOGO: O som das grades foi sua ruína. Você foi pego(a) e seus esforços foram em vão.")
            break
        elif escolha == 'B':
            forcar_fechadura_metal(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def correr_com_chaves(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - A Fuga da Chave")
    digitar("Você consegue pegar as chaves! O guarda percebe e grita, mas você corre pelo corredor, abrindo a porta da cela vizinha para distraí-lo.")
    digitar("O alarme soa, mas você tem uma vantagem. Você se joga em uma escadaria de serviço e desce rapidamente.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def pegar_chaves_bebedouro(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Chaves do Guarda")
    digitar("No momento exato em que o guarda se distrai no bebedouro, você age rapidamente e pega o molho de chaves. Ele não percebe nada.")
    digitar("Com as chaves em mãos, você sente um poder inesperado. Agora, as portas da prisão não são mais um obstáculo intransponível.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def investigar_cela_novamente_c4(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Novas Pistas na Cela")
    digitar("Com a rotina do guarda em mente, você volta a investigar a cela com mais calma. Atrás da pia, você encontra um pequeno compartimento escondido que guarda um mapa rudimentar da prisão.")
    digitar("O mapa tem algumas rotas secretas marcadas e um bilhete com o nome de um contato externo.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def cela_destrancada_suborno(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - A Porta Entreaberta")
    digitar("O guarda sorri, pegando o objeto de valor. 'Certo, prisioneiro. Acho que posso ter um 'esquecimento' na minha próxima ronda.'")
    digitar("Quando ele volta, a cela está de fato destrancada. Você respira fundo e sai cuidadosamente, movendo-se pelas sombras do corredor.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def informacao_rota_suborno(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Informação Valiosa")
    digitar("O guarda, após pegar seu suborno, sussurra um mapa mental de uma rota de manutenção raramente usada, que leva a uma galeria subterrânea.")
    digitar("Ele te dá direções precisas sobre como encontrar a entrada e o horário em que ela estará menos vigiada.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def tentar_outro_guarda(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Nova Tentativa de Ajuda")
    digitar("Você tenta chamar a atenção de outro guarda que parece mais simpático. Ele te escuta, mas não se compromete a ajudar diretamente.")
    digitar("No entanto, ele deixa 'cair' um jornal velho com uma seção de classificados que parece ter algumas marcações suspeitas, como um código.")
    digitar("Isso pode ser uma mensagem de alguém de fora ou uma dica para sua fuga.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def preparar_interrogatorio(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Interrogatório Amanhã")
    digitar("Você passa a noite preparando sua história e os argumentos para o interrogatório. No dia seguinte, o oficial te interroga por horas.")
    digitar("Sua história é convincente, e ele parece acreditar em parte dela. No entanto, a burocracia da prisão é lenta.")
    digitar("Você é colocado(a) de volta na cela, mas agora a vigilância sobre você é menor, pois te veem como 'menos perigoso(a)'.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def procurar_item_guarda(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Achado no Corredor")
    digitar("Após a saída do guarda irritado, você procura na área próxima à sua cela. Encontra um grampo de cabelo (ou outro item pequeno) que ele deve ter deixado cair.")
    digitar("Não é muito, mas pode ser usado para tentar forçar uma fechadura simples ou como parte de um plano maior.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def esperar_troca_turno(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Nova Ronda, Nova Sorte")
    digitar("Você espera pacificamente pela troca de turno. O novo guarda que assume a ronda é mais velho e parece menos atento.")
    digitar("Ele se encosta na parede por alguns instantes, cochilando levemente. É sua chance de agir sem ser notado por ele.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def usar_spray_pimenta(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Incapacitando o Guarda")
    digitar("Você rapidamente pega o spray de pimenta e o usa nos olhos do guarda. Ele grita e cambaleia, incapacitado temporariamente.")
    digitar("A porta da cela está aberta. Você o arrasta para dentro da cela, o tranca e corre pelo corredor, com o rádio do guarda em mãos.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def limpar_tunel_ajuda(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - O Túnel Desbloqueado")
    digitar("Você se comunica com o prisioneiro vizinho, e juntos, vocês começam a remover os escombros do túnel antigo, usando ferramentas improvisadas e um trabalho em equipe silencioso.")
    digitar("Após horas de esforço, o túnel está desobstruído. Há uma saída estreita que leva para fora dos muros da prisão.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def pegar_isqueiro_distracao(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Fumaça e Oportunidade")
    digitar("Você consegue pegar o isqueiro e um pedaço de papel. Com ele, você incendeia uma pequena pilha de lixo em uma área remota da cela, criando fumaça.")
    digitar("O alarme de fumaça dispara, e os guardas correm para investigar. O corredor da sua cela fica deserto por um tempo.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def buscar_rota_menos_risco(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - Rota Cautelosa")
    digitar("Você decide não arriscar com o isqueiro. Em vez disso, você se concentra em observar as câmeras de segurança e os pontos cegos do corredor.")
    digitar("Percebe que há uma pequena janela de tempo entre as rondas das câmeras onde você pode passar despercebido por um corredor lateral.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def arrombar_fechadura(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - A Fechadura Cedendo")
    digitar("Com a distração criada, você trabalha furiosamente na fechadura da cela. É um trabalho difícil, mas você consegue. A trava cede com um clique suave.")
    digitar("Você abre a porta e se esgueira para fora, no corredor deserto.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def rastejar_fresta_chao(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - A Fresta Oculta")
    digitar("Durante a distração, você rasteja para fora da cela por uma fresta no chão que você havia encontrado. É apertado, mas você consegue passar para um túnel de manutenção sob o corredor.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

def forcar_fechadura_metal(nome):
    limpar_tela()
    digitar("[NÍVEL 5] - A Trava Cede")
    digitar("Você usa o pedaço de metal para forçar a fechadura da cela durante a janela de oportunidade. Com um último esforço, a trava se solta com um estalo.")
    digitar("A porta da sua cela está aberta. Você sai discretamente para o corredor.")
    input("Pressione 'Enter' para continuar.")
    galeria_oculta(nome)

# --- NÍVEIS FINAIS ---

def galeria_oculta(nome):
    limpar_tela()
    digitar("[NÍVEL 6] - A Galeria Oculta")
    digitar("Você segue pela galeria úmida e encontra uma porta de manutenção antiga.")
    digitar("Com esforço, consegue abri-la e se vê em um depósito com uniformes e mapas.")
    digitar("Você está um passo mais perto da liberdade — mas o caminho ainda é longo.")
    digitar("No mapa, três rotas são marcadas: uma pelo telhado, outra pelos esgotos, e uma terceira pelo pátio.")
    digitar("A - Tentar o telhado\nB - Voltar aos esgotos\nC - Atravessar o pátio\nEscolha: ")
    while True:
        escolha = input().strip().upper()
        if escolha == 'A':
            fuga_telhado(nome)
            break
        elif escolha == 'B':
            armadilha_esgoto(nome)
            break
        elif escolha == 'C':
            fuga_patio(nome)
            break
        else:
            digitar_red("Escolha inválida. Tente novamente.")

def fuga_telhado(nome):
    limpar_tela()
    digitar("[NÍVEL 7] - Liberdade nas Alturas")
    digitar("Você escala silenciosamente pelas tubulações até o topo.")
    digitar("Evita refletores, atravessa o telhado e alcança o muro externo.")
    digitar("Com um salto arriscado, você cai em uma mata densa.")
    digitar_pink("VOCÊ CONSEGUIU! Agora está foragido, mas livre. O mundo lá fora te espera.")

def armadilha_esgoto(nome):
    limpar_tela()
    digitar("[NÍVEL 7] - A Armadilha Final")
    digitar("Você retorna aos esgotos, mas não percebe que uma armadilha foi armada pelos guardas.")
    digitar("Gás começa a vazar pelas tubulações, e você desmaia.")
    digitar_red("FIM DE JOGO: Você foi recapturado inconsciente. Não haverá segunda chance.")

def fuga_patio(nome):
    limpar_tela()
    digitar("[NÍVEL 7] - Risco no Pátio")
    digitar("Disfarçado com um uniforme de faxineiro, você atravessa o pátio como se fosse parte da equipe.")
    digitar("Troca palavras com um guarda simpático que não desconfia de nada.")
    digitar("Ao passar pelos portões principais, um caminhão de mantimentos se prepara para sair.")
    digitar("Você se esconde entre as caixas e espera. O motor ronca...")
    digitar_pink("VOCÊ ESCAPOU! Agora é hora de recomeçar, longe dos muros que te prenderam.")