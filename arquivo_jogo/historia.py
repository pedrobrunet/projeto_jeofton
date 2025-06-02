# play.py

import time
import os
from rich import print #importanto a biblioteca rich para formatar o textos do terminal
from rich.console import Console #importando o console dentro do modulo rich console
console = Console() #criando a variavel


# Função para limpar a tela (opcional)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para simular texto sendo digitado em vermelho
def digitar_red(texto, velocidade=0.03):
    for letra in texto:
        console.print(letra, end='', style="bold red")  
        time.sleep(velocidade)
    print()

#Função para simular texto sendo digitado em vermelho
def digitar_pink(texto, velocidade=0.03):
    for letra in texto:
        console.print(letra, end='', style="hot_pink")  
        time.sleep(velocidade)
    print()
    
# Função para simular texto sendo digitado sem cor
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