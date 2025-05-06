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
    digitar(f"Olá, {nome}. Aqui começamos seu mundo de realidade virtual.\n"
            "Suas escolhas irão definir o seu futuro, então preste atenção...\n"
            "Ou você poderá seguir por um caminho sem volta.")

def aviso_inicial(nome):
    digitar(f"⚠️ AVISO IMPORTANTE, {nome}! Tudo o que você faz aqui afeta o mundo real.")


print("teste")