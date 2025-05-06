# play.py

import time
import os

# Função para limpar a tela (opcional)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para simular texto sendo digitado
def digitar(texto, velocidade=0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidade)
    print()

def introducao_jogo(nome):
    digitar(f"Olá, {nome}. Bem-vindo à sua nova realidade: uma cela fria e silenciosa.\n"
"Você foi preso... mas não sabe exatamente por quê.\n"
"Suas escolhas daqui em diante serão cruciais.\n"
"Cada decisão pode te levar à liberdade — ou te condenar para sempre.\n"
"Está pronta para enfrentar as sombras dessa prisão?\n")

def aviso_inicial(nome):
    digitar(f"⚠️ AVISO IMPORTANTE, {nome}!")
    digitar("Tudo o que você fizer aqui pode ter consequências inesperadas...")
    digitar("Este não é apenas um jogo. Este é um teste.")
    digitar("Um erro pode te prender aqui... para sempre.\n")
    digitar("Pressione 'Enter' para continuar")