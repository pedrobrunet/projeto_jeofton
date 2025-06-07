import tkinter as tk


class Application:
    def __init__(self):
        self.janela = tk.Tk()
        self.tela()
        self.intro()
        tk.mainloop()

    def tela(self):
        self.janela.title("Jogo de Escolhas")
        self.janela.geometry("788x588")
        self.janela.configure(background="#1a1a1a")
        self.janela.resizable(True, True)
        self.janela.maxsize(width=1520, height=900)
        self.janela.minsize(width=488, height=388)

        self.mensagem_inicial = tk.StringVar()
        self.nome_jog = tk.StringVar()
        self.boas_vindas = tk.StringVar()
        self.nome_mensagem = tk.StringVar()
        self.texto = tk.StringVar()
        self.barras = tk.StringVar()
        self.barras2 = tk.StringVar()

        self.texto_completo = ""
        self.texto_atual = ""
        self.indice_char = 0
        self.after_id = None

        self.label_boas_vindas = None

    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def linhas(self):
        linha_lat1 = tk.Frame(self.janela, bg="#a50b0b", width=1537, height=15)
        linha_lat1.place(relx=0.5, rely=0.01, anchor="center")

        linha_lat2 = tk.Frame(self.janela, bg="#a50b0b", width=1537, height=15)
        linha_lat2.place(relx=0.5, rely=0.99, anchor="center")

        linha_lat3 = tk.Frame(self.janela, bg="#a50b0b", width=15, height=1537)
        linha_lat3.place(relx=0.01, rely=0.4, anchor="e")

        linha_lat4 = tk.Frame(self.janela, bg="#a50b0b", width=15, height=1537)
        linha_lat4.place(relx=0.99, rely=0.4, anchor="w")

    def intro(self):
        self.linhas()
        self.mensagem_inicial.set(" VOCÊ FOI PRESO ")
        label_intro = tk.Label(self.janela, textvariable=self.mensagem_inicial, fg="red", bg="#1a1a1a", font=("Impact", 45, "bold"), wraplength=800, justify="left")
        label_intro.place(relx=0.5, rely=0.4, anchor="center")

        self.barras.set("═══════════════════════════════════════════════")
        label_barras = tk.Label(self.janela, textvariable=self.barras, fg="red", bg="#1a1a1a")
        label_barras.place(relx=0.5, rely=0.3, anchor="center")

        self.barras2.set("══════════════════════════════════════════════")
        label_barras2 = tk.Label(self.janela, textvariable=self.barras2, fg="red", bg="#1a1a1a")
        label_barras2.place(relx=0.5, rely=0.5, anchor="center")

        linha_decorativa = tk.Frame(self.janela, bg="#ffffff", width=390, height=2)
        linha_decorativa.place(relx=0.5, rely=0.467, anchor="center")

        botao_start = tk.Button(self.janela, text="▶ START", width=20, height=2, fg="white", bg="red", command=self.mostrar_campo_nome, font=("Consolas", 16, "bold"))
        botao_start.place(relx=0.5, rely=0.650, anchor="center")
        botao_start.bind("<Enter>", self.on_enter)
        botao_start.bind("<Leave>", self.on_leave)

        texto_inf = tk.Label(self.janela, text="Suas escolhas moldarão o caminho. Cuidado... cada decisão pode te aproximar da verdade — ou do fim.", fg="white", bg="#1a1a1a", font=("Lucida Console", 8, "italic"), wraplength=500)
        texto_inf.place(relx=0.5, rely=0.9, anchor="center")

    def on_enter(self, event):
        event.widget.config(bg="#701b1b", fg="white")

    def on_leave(self, event):
        event.widget.config(bg="red", fg="white")

    def botao_inicial(self):
        botao_volta_inicio = tk.Button(self.janela, text="Volte para tela inicial", command=self.voltar_para_inicio, font=("Helvetica", 14), bg="red", fg="white")
        botao_volta_inicio.place(relx=0.5, rely=0.9, anchor="center")

    def voltar_para_inicio(self):
        self.limpar_tela()
        self.intro()

    def mostrar_campo_nome(self):
        self.limpar_tela()
        self.botao_inicial()

        self.texto.set("⛓️ DIGITE O NOME DO SEU PERSONAGEM ⛓️")
        label_texto = tk.Label(self.janela, textvariable=self.texto, fg="red", bg="#1a1a1a", font=("Impact", 27),
                              wraplength=800, justify="center")
        label_texto.place(relx=0.5, rely=0.1, anchor="center")
        self.nome_mensagem.set("")

        fundo2 = tk.Frame(self.janela, bg="red", width=1530, height=150)
        fundo2.place(relx=0.5, rely=0.457, anchor="center")
        self.entry_nome = tk.Entry(self.janela, textvariable=self.nome_mensagem, fg="red", bg="#1a1a1a",
                                  font=("Helvetica", 14), justify="center", insertbackground="red")
        self.entry_nome.place(relx=0.5, rely=0.4, anchor="center")

        self.botao_confirmar = tk.Button(self.janela, text="Confirmar nome", command=self.pegar_nome,
                                        font=("Helvetica", 14), bg="red", fg="white")
        self.botao_confirmar.place(relx=0.5, rely=0.470, anchor="center")

    def pegar_nome(self):
        nome_digitado = self.nome_mensagem.get()
        self.nome_jogador = nome_digitado
        self.texto_completo = (f"Olá, {nome_digitado}. Bem-vindo(a) à sua nova realidade: uma cela fria e silenciosa. Você foi preso(a)... mas não sabe exatamente por quê. Suas escolhas daqui em diante serão cruciais. Cada decisão pode te levar à liberdade — ou te condenar para sempre. Está pronta para enfrentar as sombras dessa prisão?")

        if self.label_boas_vindas:
            self.label_boas_vindas.destroy()
        if hasattr(self, 'botao_proximo') and self.botao_proximo:
            self.botao_proximo.destroy()
            
            
        self.label_boas_vindas = tk.Label(self.janela, text="", fg="white", bg="#1a1a1a", font=("Courier New", 11), wraplength=700, justify="center")
        self.label_boas_vindas.place(relx=0.5, rely=0.7, anchor="center")

        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="red", fg="white", command=self.mostrar_escolha_nivel_um)
        self.botao_proximo.place(relx=0.9, rely=0.9, anchor="w")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)

        self.texto_atual = ""
        self.indice_char = 0
        self.animar_digitacao()
        
    #animação de textos
    def animar_digitacao(self):
        if self.indice_char < len(self.texto_completo):
            self.texto_atual += self.texto_completo[self.indice_char]
            self.indice_char += 1

            self.label_boas_vindas.config(text=self.texto_atual)

            velocidade = 35

            if self.texto_completo[self.indice_char - 1] in '.!?':
                velocidade = 300
            elif self.texto_completo[self.indice_char - 1] in ',;:':
                velocidade = 150

            self.after_id = self.janela.after(velocidade, self.animar_digitacao)

    def animar_digitacao_geral(self, texto_completo, label_destino, velocidade_base=70):
        self.texto_completo = texto_completo
        self.texto_atual = ""
        self.indice_char = 0
        self.label_atual = label_destino
        self.velocidade_base = velocidade_base
        self.label_atual.config(text="")
        self._processar_digitacao()
    
    def _processar_digitacao(self):
        if self.indice_char < len(self.texto_completo):
            char_atual = self.texto_completo[self.indice_char]
            self.texto_atual += char_atual
            self.indice_char += 1
            self.label_atual.config(text=self.texto_atual)
            velocidade = self.velocidade_base
        
            if char_atual in '.!?':
                velocidade = 300
            elif char_atual in ',;:':
                velocidade = 150
            elif char_atual == ' ':
                velocidade = self.velocidade_base // 2  # Espaços mais rápidos
            if self.indice_char < len(self.texto_completo):
                self.after_id = self.janela.after(velocidade, self._processar_digitacao)
        
    def mostrar_escolha_nivel_um(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 1  - O Despertar"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = "Você desperta em uma cela úmida e mal iluminada. O que deseja fazer?"
        label_texto = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label_texto.place(relx=0.5, rely=0.2, anchor="center")
        self.animar_digitacao_geral(texto, label_texto)
        
        botao_a = tk.Button(self.janela, text="A - Investigar a cela", fg="white", bg="#75010b", command=self.investigacao_cela, width=27, height=2)
        botao_a.place(relx=0.199, rely=0.6, anchor="center")

        botao_b = tk.Button(self.janela, text="B - Chamar por alguém", fg="white", bg="#75010b", command=self.chamar_por_alguem, width=27, height=2)
        botao_b.place(relx=0.500, rely=0.6, anchor="center")

        botao_c = tk.Button(self.janela, text="C - Esperar em silêncio", fg="white", bg="#75010b", command=self.observar_ambiente, width=27, height=2)
        botao_c.place(relx=0.800, rely=0.6, anchor="center")

    def investigacao_cela(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 2 - A Descoberta"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto1 = (f"{self.nome_jogador}, você começa a investigar a cela. Há rachaduras nas paredes e um pequeno buraco no chão. Passa os dedos pelas rachaduras nas paredes e examina a cama enferrujada. "
            f"Atrás de um tijolo solto, encontra um bilhete amassado. "
            f"Confie em ninguém. A saída está sob seus pés. "
            f"Você sente o chão tremer levemente... algo está escondido ali.")

        label_texto1 = tk.Label(self.janela, text=texto1, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label_texto1.place(relx=0.5, rely=0.3, anchor="center")
        self.animar_digitacao_geral(texto1, label_texto1)

        botao_cavar = tk.Button(self.janela, text="A - Cavar Saida", fg="white", bg="#75010b", command=self.cavar_saida, width=27, height=2)
        botao_cavar.place(relx=0.3, rely=0.6, anchor="center")

        botao_bilhete = tk.Button(self.janela, text="B - Esconder o bilhete e esperar", fg="white", bg="#75010b", command=self.esperar_depois_bilhete, width=27, height=2)
        botao_bilhete.place(relx=0.7, rely=0.6, anchor="center")

    def cavar_saida(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 3 - Túnel Secreto"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = (f"{self.nome_jogador}, com uma colher enferrujada escondida sob o colchão, você começa a cavar."
                 f" Horas se passam. Finalmente, um túnel apertado se revela."
                 f" Você rasteja por ele até encontrar uma grade solta que leva aos esgotos."
                 f" Antes de entrar, um outro prisioneiro o intercepta. Ele diz que quer ajudar, mas parece instável.")
        label_text_cavar = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label_text_cavar.place(relx=0.5, rely=0.3, anchor="center")
        self.animar_digitacao_geral(texto, label_text_cavar)

        botao_companheiro = tk.Button(self.janela, text="A- Deixar ele vim junto", fg="white", bg="#75010b", command= self.companheiro_esgoto, width=27, height=2)
        botao_companheiro.place(relx=0.3, rely=0.6, anchor="center")

        botao_conflito = tk.Button(self.janela, text="B- Ameaçar Ele", fg="white", bg="#75010b", command= self.conflito_esgoto, width=27, height=2)
        botao_conflito.place(relx=0.7, rely=0.6, anchor="center")

    

    def esperar_depois_bilhete(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 3 - Espera Estratégica"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = (f"{self.nome_jogador}, você guarda o bilhete e finge dormir. Um guarda entra para inspeção e você nota que ele carrega um molho de chaves solto no cinto."
                 f" Você pode tentar se aproximar dele em outro momento e usar isso a seu favor.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        

        botao_distracao_chaves= tk.Button(self.janela, text="A - Tentar uma distração\n para pegar as chaves", fg="white", bg="#75010b", command=self.distracao_chaves, width=30, height=2)
        botao_distracao_chaves.place(relx=0.3, rely=0.6, anchor="center")

        botao_observar_rotina_para_chaves= tk.Button(self.janela, text="B - Observar mais para encontrar\n uma rotina do guarda", fg="white", bg="#75010b", command=self.observar_rotina_para_chaves, width=30, height=2)
        botao_observar_rotina_para_chaves.place(relx=0.7, rely=0.6, anchor="center")
        self.animar_digitacao_geral(texto, label)
        
    def distracao_chaves(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 4 - O Roubo da Chave"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("Você tenta criar uma distração, tossindo alto e derrubando sua caneca. O guarda se vira para repreendê-lo(a)."
                 f" Rapidamente, você estende a mão e tenta pegar o molho de chaves em seu cinto.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        

        botao_correr_com_chaves= tk.Button(self.janela, text="A - Pegar as chaves e correr", fg="white", bg="#75010b", command=self.correr_com_chaves, width=27, height=2)
        botao_correr_com_chaves.place(relx=0.3, rely=0.6, anchor="center")

        botao_quase_pego= tk.Button(self.janela, text="B - Tentar disfarçar se\n o guarda perceber", fg="white", bg="#75010b", command=self.quase_pego, width=27, height=2)
        botao_quase_pego.place(relx=0.7, rely=0.6, anchor="center") 
        self.animar_digitacao_geral(texto, label)
        
    def correr_com_chaves(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - A Fuga da Chave"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("Você consegue pegar as chaves! O guarda percebe e grita, mas você corre pelo corredor, abrindo a porta da cela vizinha para distraí-lo."
        "O alarme soa, mas você tem uma vantagem. Você se joga em uma escadaria de serviço e desce rapidamente.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2)   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)
        
    def quase_pego(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - Quase Pego(a)"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        fim = ("☠️ Você tenta disfarçar, mas o guarda percebe sua intenção. Ele te olha desconfiado, mas decide não fazer uma confusão maior. 'Fique na linha', ele diz, e se afasta.")
        fim_label = tk.Label(self.janela, text=fim, font=("Impact", 17),wraplength=700, justify="left", fg="red", bg="#1a1a1a")
        fim_label.place(relx=0.5, rely=0.3, anchor="center") 
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2)   
        self.botao_proximo.place(relx=0.5, rely=0.5, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(fim, fim_label)
         
    def observar_rotina_para_chaves(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 4 - Padrão do Guarda"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("Você decide não agir impulsivamente e passa mais tempo observando o guarda. Percebe que, a cada duas rondas, ele para para beber água em um bebedouro próximo, deixando as chaves penduradas por um instante."
                 f" É um risco, mas uma oportunidade clara.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        botao_pegar_chaves_bebedouro = tk.Button(self.janela, text="A - Tentar uma distração\n para pegar as chaves", fg="white", bg="#75010b", command=self.pegar_chaves_bebedouro,  width=30, height=2)
        botao_pegar_chaves_bebedouro.place(relx=0.3, rely=0.6, anchor="center")

        botao_investigar_cela_novamente_c4= tk.Button(self.janela, text="B - Observar mais para encontrar\n uma rotina do guarda", fg="white", bg="#75010b", command=self.investigar_cela_novamente_c4, width=30, height=2)
        botao_investigar_cela_novamente_c4.place(relx=0.7, rely=0.6, anchor="center")
        self.animar_digitacao_geral(texto, label)
   
        
    def pegar_chaves_bebedouro(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - Chaves do Guarda"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("No momento exato em que o guarda se distrai no bebedouro, você age rapidamente e pega o molho de chaves. Ele não percebe nada."
        "Com as chaves em mãos, você sente um poder inesperado. Agora, as portas da prisão não são mais um obstáculo intransponível.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2)   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)
        
    def investigar_cela_novamente_c4(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - Novas Pistas na Cela"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("Com a rotina do guarda em mente, você volta a investigar a cela com mais calma. Atrás da pia, você encontra um pequeno compartimento escondido que guarda um mapa rudimentar da prisão. O mapa tem algumas rotas secretas marcadas e um bilhete com o nome de um contato externo.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2)   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)

    def companheiro_esgoto(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 4 - Traição nas Sombras"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = (f"{self.nome_jogador}, vocês seguem juntos, mas a tensão cresce. Ele desconfia de você, e você dele."
        " Em uma encruzilhada, ele tenta trair você e te empurra na água."
        " Você reage, luta por sua vida e o empurra contra a parede. Ele cai inconsciente."
        " Ferido, você segue sozinho pela galeria oculta.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2)   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)
        
    def galeria_oculta(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5  - A Galeria Oculta" #nivel 6 no terminal
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = "Você segue pela galeria úmida e encontra uma porta de manutenção antiga. Com esforço, consegue abri-la e se vê em um depósito com uniformes e mapas. Você está um passo mais perto da liberdade — mas o caminho ainda é longo. No mapa, três rotas são marcadas: uma pelo telhado, outra pelos esgotos, e uma terceira pelo pátio."
        label_texto = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label_texto.place(relx=0.5, rely=0.3, anchor="center")
        self.animar_digitacao_geral(texto, label_texto)
        botao_a = tk.Button(self.janela, text="A - Tentar o telhado", fg="white", bg="#75010b", command=self.fuga_telhado, width=27, height=2)
        botao_a.place(relx=0.199, rely=0.6, anchor="center")

        botao_b = tk.Button(self.janela, text="B - Voltar aos esgotos", fg="white", bg="#75010b", command=self.armadilha_esgoto, width=27, height=2)
        botao_b.place(relx=0.500, rely=0.6, anchor="center")

        botao_c = tk.Button(self.janela, text="C - Atravessar o pátio", fg="white", bg="#75010b", command=self.fuga_patio, width=27, height=2)
        botao_c.place(relx=0.800, rely=0.6, anchor="center")
    
    def fuga_telhado(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 6 - Liberdade nas Alturas" #nivel 7 no terminal
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = (f"{self.nome_jogador}, você escala silenciosamente pelas tubulações até o topo. Evita refletores, atravessa o telhado e alcança o muro externo. Com um salto arriscado, você cai em uma mata densa.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        fim = ("🏃 VOCÊ CONSEGUIU! Agora está foragido, mas livre. O mundo lá fora te espera.")
        fim_label = tk.Label(self.janela, text=fim, font=("Impact", 17, "bold"),wraplength=700, justify="center", fg="green", bg="#1a1a1a")
        fim_label.place(relx=0.5, rely=0.6, anchor="center")
        self.animar_digitacao_geral(fim, fim_label)

        
    def armadilha_esgoto(self): 
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 6 - A Armadilha Final" #nivel 7 no terminal
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = (f"{self.nome_jogador}, você retorna aos esgotos, mas não percebe que uma armadilha foi armada pelos guardas. Gás começa a vazar pelas tubulações, e você desmaia")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        fim = ("FIM DE JOGO: Você foi recapturado inconsciente. Não haverá segunda chance.")
        fim_label = tk.Label(self.janela, text=fim, font=("Impact", 17),wraplength=700, justify="center", fg="black", bg="red")
        fim_label.place(relx=0.5, rely=0.7, anchor="center")
        self.animar_digitacao_geral(fim, fim_label)


        
    def fuga_patio(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 6 - Risco no Pátio" #nivel 7 no terminal
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = (f"{self.nome_jogador}, Disfarçado com um uniforme de faxineiro, você atravessa o pátio como se fosse parte da equipe. Troca palavras com um guarda simpático que não desconfia de nada. Ao passar pelos portões principais, um caminhão de mantimentos se prepara para sair. Você se esconde entre as caixas e espera. O motor ronca...")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        fim = ("🏃 VOCÊ ESCAPOU! Agora é hora de recomeçar, longe dos muros que te prenderam.")
        fim_label = tk.Label(self.janela, text=fim, font=("Impact", 17),wraplength=700, justify="center", fg="green", bg="#1a1a1a")
        fim_label.place(relx=0.5, rely=0.7, anchor="center")
        self.animar_digitacao_geral(fim, fim_label)
        
    def conflito_esgoto(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 4 - Confronto Imprudente"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("Você empurra o prisioneiro e segue sozinho pelos esgotos. Ele grita, alertando guardas por vingança. Alarmes disparam. Você corre desesperadamente até cair em uma câmara subterrânea. Lá, encontra um velho guarda desacordado com crachá e arma.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.animar_digitacao_geral(texto, label)
        botao_cracha= tk.Button(self.janela, text="A - Usar o crachá para abrir portas", fg="white", bg="#75010b", command= self.usar_cracha, width=27, height=2)
        botao_cracha.place(relx=0.3, rely=0.6, anchor="center")

        botao_arma = tk.Button(self.janela, text="B - Pegar a arma e se defender", fg="white", bg="#75010b", command= self.pegar_arma, width=27, height=2)
        botao_arma.place(relx=0.7, rely=0.6, anchor="center")

    def usar_cracha(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - Identidade Falsa"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = (f"{self.nome_jogador}, Você passa por portas trancadas, mas o crachá ativa sensores que alertam sobre sua localização. Uma equipe de segurança é enviada para te deter. Você precisa improvisar e se esconder na ventilação. Enquanto rasteja, escuta conversas suspeitas sobre um programa de controle mental com prisioneiros.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)
    
    def pegar_arma(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - Armadilha Letal" 
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = (f"{self.nome_jogador}, A arma está sem munição. Foi uma armadilha. O guarda acorda e ativa o alarme. Você é cercado e recapturado.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        fim = ("FIM DE JOGO: Você foi recapturado e será transferido para um setor de segurança máxima.")
        fim_label = tk.Label(self.janela, text=fim, font=("Impact", 20),wraplength=700, justify="left", bg="#1a1a1a",fg="red")
        fim_label.place(relx=0.5, rely=0.5, anchor="center")
        self.animar_digitacao_geral(fim, fim_label)
        
    
    def chamar_por_alguem(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 2 - O Grito Atrai Atenção" 
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        
        texto = f"{self.nome_jogador}, você grita por ajuda, e o som ecoa pelo corredor. Momentos depois, passos se aproximam e um guarda para em frente à sua cela. Ele te olha com uma expressão de tédio e irritação."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        
        dialogo= (f'Guarda: "Qual o problema, {self.nome_jogador}? Quer mais tempo aqui?"\nComo você responde?')
        label1 = tk.Label(self.janela, text=dialogo, fg="#de4710", bg="#1a1a1a", font=("Impact", 14), wraplength=700, justify="left")
        label1.place(relx=0.5, rely=0.5, anchor="center")
        self.animar_digitacao_geral(dialogo, label1)


        botao_interagir_guarda= tk.Button(self.janela, text="A - Tentar acalmar o guarda \n e pedir informações", fg="white", bg="#75010b", command= self.interagir_guarda, width=37, height=2)
        botao_interagir_guarda.place(relx=0.3, rely=0.7, anchor="center")

        botao_conflito_guarda = tk.Button(self.janela, text="B - Desafiar o guarda e exigir seus direitos", fg="white", bg="#75010b", command= self.conflito_guarda, width=37, height=2)
        botao_conflito_guarda.place(relx=0.7, rely=0.7, anchor="center")
    
    def interagir_guarda(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 3 - Persuasão na Cela" 
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        
        texto = "Você tenta acalmar o guarda, explicando sua inocência e pedindo informações sobre o motivo da sua prisão. Ele parece ligeiramente surpreso com sua calma, mas se mantém cauteloso."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        
        dialogo= ('Guarda: "Inocente? Todos dizem isso. Mas o que você está fazendo aqui então?"\n Ele parece um pouco curioso. Você sente que pode conseguir algo dele.')
        label1 = tk.Label(self.janela, text=dialogo, fg="#de4710", bg="#1a1a1a", font=("Impact", 14), wraplength=650, justify="left")
        label1.place(relx=0.5, rely=0.5, anchor="center")
        
        botao_oferecer_suborno= tk.Button(self.janela, text="A - Oferecer algo em troca de\n ajuda (se tiver algo de valor)", fg="white", bg="#75010b", command= self.oferecer_suborno, width=30, height=2)
        botao_oferecer_suborno.place(relx=0.3, rely=0.7, anchor="center")

        botao_argumentar_inocencia = tk.Button(self.janela, text="B - Tentar convencê-lo de sua\n inocência com mais detalhes", fg="white", bg="#75010b", command= self.conflito_guarda, width=30,  height=2)
        botao_argumentar_inocencia.place(relx=0.7, rely=0.7, anchor="center")
        self.animar_digitacao_geral(dialogo, label1)        
        
    def conflito_guarda(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 3 - Desafio Perigoso" 
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        
        texto = "Você desafia o guarda, exigindo seus direitos e reclamando da prisão injusta. A face do guarda endurece. Ele se aproxima da cela e te encara."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        
        dialogo= (f'Guarda: "Direitos? Aqui, seus direitos são ficar calado e obedecer! Quer problemas, {self.nome_jogador}?"\n Ele saca o cassetete, pronto para usar a força.')
        label1 = tk.Label(self.janela, text=dialogo, fg="#de4710", bg="#1a1a1a", font=("Impact", 14), wraplength=700, justify="left")
        label1.place(relx=0.5, rely=0.5, anchor="center")
        
        botao_recuar_conflito= tk.Button(self.janela, text="A - Recuar e tentar acalmar a situação", fg="white", bg="#75010b", command= self.recuar_conflito, width=30, height=2)
        botao_recuar_conflito.place(relx=0.3, rely=0.7, anchor="center")

        botao_provocar_guarda = tk.Button(self.janela, text="B - Provocá-lo ainda mais, buscando\n uma reação exagerada", fg="white", bg="#75010b", command= self.provocar_guarda, width=30, height=2)
        botao_provocar_guarda.place(relx=0.7, rely=0.7, anchor="center")
        self.animar_digitacao_geral(dialogo, label1)
        
        
    def provocar_guarda(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 4 - Provocação Perigosa" 
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        
        texto = "Você decide provocá-lo ainda mais, esperando que ele reaja de forma exagerada e cometa um erro."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        
        dialogo= ('Guarda: "Ah, é assim? Quer brincar, é?" Ele abre a porta da cela, entra furioso e te empurra contra a parede. Mas ao fazer isso, ele deixa cair sua arma (um spray de pimenta) e o rádio.')
        label1 = tk.Label(self.janela, text=dialogo, fg="#de4710", bg="#1a1a1a", font=("Impact", 14), wraplength=700, justify="left")
        label1.place(relx=0.5, rely=0.5, anchor="center")
        
        botao_usar_spray_pimenta= tk.Button(self.janela, text="A - Pegar o spray de pimenta\n e incapacitá-lo", fg="white", bg="#75010b", command= self.usar_spray_pimenta, width=30, height=2)
        botao_usar_spray_pimenta.place(relx=0.3, rely=0.7, anchor="center")

        botao_digitar_red = tk.Button(self.janela, text="B - Pegar o rádio e tentar pedir ajuda\n externa ou alertar a prisão", fg="white", bg="#75010b", command= self.digitar_red, width=30, height=2)
        botao_digitar_red.place(relx=0.7, rely=0.7, anchor="center")
        self.animar_digitacao_geral(dialogo, label1)
        
    def usar_spray_pimenta(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - Incapacitando o Guarda"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("Você rapidamente pega o spray de pimenta e o usa nos olhos do guarda. Ele grita e cambaleia, incapacitado temporariamente. A porta da cela está aberta. Você o arrasta para dentro da cela, o tranca e corre pelo corredor, com o rádio do guarda em mãos.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)
    
    def digitar_red(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        texto = "FIM DE JOGO: Sua tentativa com o rádio alertou a todos. Você foi encurralado(a) e recapturado(a) sem chance."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 20), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.5, anchor="center")  
        self.animar_digitacao_geral(texto, label)
         
    def recuar_conflito(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 4 - Recuo Estratégico" 
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        
        texto = "Você recua, levantando as mãos em sinal de paz. O guarda ainda está irritado, mas baixa um pouco o cassetete."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        
        dialogo= ('Guarda: "É bom mesmo. Fique na sua, ou as coisas vão piorar para você."')
        label1 = tk.Label(self.janela, text=dialogo, fg="#de4710", bg="#1a1a1a", font=("Impact", 14), wraplength=700, justify="left")
        label1.place(relx=0.5, rely=0.4, anchor="center")
        
        texto = "Ele se afasta, mas agora você está em sua lista negra. Ele te observará mais de perto. Você precisa encontrar uma forma de sair sem ser detectado ou enfrentar esse guarda novamente."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.53, anchor="center")
        
        botao_procurar_item_guarda= tk.Button(self.janela, text="A - Procurar por uma ferramenta\n ou item que ele tenha deixado cair", fg="white", bg="#75010b", command= self.procurar_item_guarda, width=30, height=2)
        botao_procurar_item_guarda.place(relx=0.3, rely=0.7, anchor="center")

        botao_esperar_troca_turno = tk.Button(self.janela, text="B - Esperar pela troca de turno e\n tentar a sorte com outro guarda", fg="white", bg="#75010b", command= self.esperar_troca_turno, width=30, height=2)
        botao_esperar_troca_turno.place(relx=0.7, rely=0.7, anchor="center")
        
        self.animar_digitacao_geral(dialogo, label1)

        
    def procurar_item_guarda(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - Achado no Corredor"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("Após a saída do guarda irritado, você procura na área próxima à sua cela. Encontra um grampo de cabelo (ou outro item pequeno) que ele deve ter deixado cair. Não é muito, mas pode ser usado para tentar forçar uma fechadura simples ou como parte de um plano maior.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)

        
    def esperar_troca_turno(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - Nova Ronda, Nova Sorte"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("Você espera pacificamente pela troca de turno. O novo guarda que assume a ronda é mais velho e parece menos atento. Ele se encosta na parede por alguns instantes, cochilando levemente. É sua chance de agir sem ser notado por ele.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)

        
    def oferecer_suborno(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 4 - A Oferta Tentadora" 
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        
        texto = 'Você revela que tem um pequeno objeto de valor (um relógio, um anel, etc.) que conseguiu esconder e oferece ao guarda em troca de uma "ajuda" para sair. Os olhos do guarda brilham com a possibilidade. Ele pega o objeto e o examina, pensativo.'
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        
        dialogo= ('Guarda: "Interessante... O que você quer, exatamente?"')
        label1= tk.Label(self.janela, text=dialogo, fg="#de4710", bg="#1a1a1a", font=("Impact", 14), wraplength=700, justify="left")
        label1.place(relx=0.5, rely=0.5, anchor="center")
        
        botao_cela_destrancada_suborno= tk.Button(self.janela, text="A - Pedir para ele 'esquecer' sua cela\n destrancada na próxima ronda", fg="white", bg="#75010b", command= self.cela_destrancada_suborno, width=30, height=2)
        botao_cela_destrancada_suborno.place(relx=0.3, rely=0.7, anchor="center")

        botao_informacao_rota_suborno = tk.Button(self.janela, text="B - Pedir informações sobre\n uma rota de fuga segura", fg="white", bg="#75010b", command= self.informacao_rota_suborno, width=30, height=2)
        botao_informacao_rota_suborno.place(relx=0.7, rely=0.7, anchor="center")
        self.animar_digitacao_geral(dialogo, label1)
        
    def cela_destrancada_suborno(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - A Porta Entreaberta"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("O guarda sorri, pegando o objeto de valor. 'Certo, prisioneiro. Acho que posso ter um 'esquecimento' na minha próxima ronda.' Quando ele volta, a cela está de fato destrancada. Você respira fundo e sai cuidadosamente, movendo-se pelas sombras do corredor.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)
        
    def informacao_rota_suborno(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - Informação Valiosa"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("O guarda, após pegar seu suborno, sussurra um mapa mental de uma rota de manutenção raramente usada, que leva a uma galeria subterrânea. Ele te dá direções precisas sobre como encontrar a entrada e o horário em que ela estará menos vigiada.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)
        
    def observar_ambiente(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 2 - O Silêncio Revelador"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = f"{self.nome_jogador}, você decide esperar em silêncio, observando atentamente o ambiente ao seu redor. O tempo passa lentamente. Você percebe padrões nos sons, nos horários das rondas dos guardas e na iluminação que entra pela pequena fresta. De repente, você ouve uma conversa abafada vinda da cela vizinha. O que você faz?"
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        
        botao_ouvir_conversa_cela= tk.Button(self.janela, text="A - Tentar ouvir a conversa\n da cela vizinha", fg="white", bg="#75010b", command= self.ouvir_conversa_cela, width=30, height=2)
        botao_ouvir_conversa_cela.place(relx=0.3, rely=0.7, anchor="center")

        botao_observar_rotina_guarda = tk.Button(self.janela, text="B - Focar na rotina dos guardas e buscar\n uma oportunidade", fg="white", bg="#75010b", command= self.observar_rotina_guarda, width=30, height=2)
        botao_observar_rotina_guarda.place(relx=0.7, rely=0.7, anchor="center")
        self.animar_digitacao_geral(texto, label)

    def ouvir_conversa_cela(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 3 - Sussurros Misteriosos"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = f"Você se aproxima da parede e tenta ouvir a conversa da cela vizinha. Os sons são abafados, mas você consegue distinguir algumas palavras-chave: 'transferência', 'plano', 'agora'. Parece que os prisioneiros vizinhos estão planejando algo ou prestes a serem movidos. Você pode tentar se comunicar ou usar essa informação a seu favor."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        
        botao_comunicar_vizinho= tk.Button(self.janela, text="A - Bater na parede e tentar uma\n comunicação silenciosa", fg="white", bg="#75010b", command= self.comunicar_vizinho, width=30, height=2)
        botao_comunicar_vizinho.place(relx=0.3, rely=0.7, anchor="center")

        botao_ignorar_e_observar = tk.Button(self.janela, text="B - Ignorar a conversa e focar na\n sua própria fuga", fg="white", bg="#75010b", command= self.ignorar_e_observar, width=30, height=2)
        botao_ignorar_e_observar.place(relx=0.7, rely=0.7, anchor="center")
        self.animar_digitacao_geral(texto, label)

    def comunicar_vizinho(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 4 - Comunicação Secreta" 
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        
        texto = "Você bate na parede com um padrão específico. Depois de um tempo, a batida é respondida. É um prisioneiro experiente. Através de um código de batidas e sussurros, vocês trocam informações. Ele diz que há um túnel antigo de contrabando que leva para fora, mas ele está bloqueado por escombros. Ele também menciona que a chave para limpar a passagem está com um guarda específico, conhecido por ser negligente."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        
        botao_limpar_tunel_ajuda = tk.Button(self.janela, text="A - Pedir ajuda para o\n prisioneiro na limpeza do túnel", fg="white", bg="#75010b", command= self.limpar_tunel_ajuda, width=30, height=2)
        botao_limpar_tunel_ajuda.place(relx=0.3, rely=0.7, anchor="center")

        digitar_red2 = tk.Button(self.janela, text="B - Focar em distrair o guarda \nnegligente para pegar a chave", fg="white", bg="#75010b", command= self.digitar_red2, width=30, height=2)
        digitar_red2.place(relx=0.7, rely=0.7, anchor="center")
        self.animar_digitacao_geral(texto, label)

    def digitar_red2(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        texto = "FIM DE JOGO: O guarda negligente não era tão negligente assim. Você foi pego(a) tentando roubar e acabou em segurança máxima."
        label = tk.Label(self.janela, text=texto, fg="black", bg="red", font=("Impact", 20), wraplength=700, justify="center")
        label.place(relx=0.5, rely=0.5, anchor="center")
        self.animar_digitacao_geral(texto, label)  
        
    def limpar_tunel_ajuda(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - O Túnel Desbloqueado"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = "Você se comunica com o prisioneiro vizinho, e juntos, vocês começam a remover os escombros do túnel antigo, usando ferramentas improvisadas e um trabalho em equipe silencioso. Após horas de esforço, o túnel está desobstruído. Há uma saída estreita que leva para fora dos muros da prisão."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)
                
    def ignorar_e_observar(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 4 - Observação Silenciosa"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = "Você foca na rotina dos guardas. Depois de um tempo, percebe que um guarda em particular sempre faz uma ronda com um atraso de alguns minutos em um determinado horário. Isso cria uma pequena janela de oportunidade na qual a ala da sua cela fica brevemente sem supervisão direta."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        
        botao_pegar_isqueiro_distracao= tk.Button(self.janela, text="A - Tentar pegar o isqueiro para\n criar uma distração (fumaça/fogo)", fg="white", bg="#75010b", command= self.pegar_isqueiro_distracao, width=30, height=2)
        botao_pegar_isqueiro_distracao.place(relx=0.3, rely=0.7, anchor="center")

        botao_buscar_rota_menos_risco = tk.Button(self.janela, text="B - Ignorar e buscar uma rota\n de fuga menos arriscada", fg="white", bg="#75010b", command= self.buscar_rota_menos_risco, width=30, height=2)
        botao_buscar_rota_menos_risco.place(relx=0.7, rely=0.7, anchor="center")
        self.animar_digitacao_geral(texto, label)

    def buscar_rota_menos_risco(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - Rota Cautelosa"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = "Você decide não arriscar com o isqueiro. Em vez disso, você se concentra em observar as câmeras de segurança e os pontos cegos do corredor. Percebe que há uma pequena janela de tempo entre as rondas das câmeras onde você pode passar despercebido por um corredor lateral."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)

    def pegar_isqueiro_distracao(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - Fumaça e Oportunidade"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = "Você consegue pegar o isqueiro e um pedaço de papel. Com ele, você incendeia uma pequena pilha de lixo em uma área remota da cela, criando fumaça. O alarme de fumaça dispara, e os guardas correm para investigar. O corredor da sua cela fica deserto por um tempo."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)

    def observar_rotina_guarda(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 3 - Padrões de Segurança"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = "Você foca na rotina dos guardas. Depois de um tempo, percebe que um guarda em particular sempre faz uma ronda com um atraso de alguns minutos em um determinado horário. Isso cria uma pequena janela de oportunidade na qual a ala da sua cela fica brevemente sem supervisão direta."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        
        botao_preparar_distracao= tk.Button(self.janela, text="A - Preparar uma distração para\n essa janela de tempo", fg="white", bg="#75010b", command= self.preparar_distracao, width=33, height=2)
        botao_preparar_distracao.place(relx=0.3, rely=0.7, anchor="center")

        botao_buscar_ferramenta_cela = tk.Button(self.janela, text="B - Buscar uma ferramenta para arrombar\n algo na cela durante essa janela", fg="white", bg="#75010b", command= self.buscar_ferramenta_cela, width=33, height=2)
        botao_buscar_ferramenta_cela.place(relx=0.7, rely=0.7, anchor="center")
        self.animar_digitacao_geral(texto, label)   
    
    def buscar_ferramenta_cela(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 4 - Ferramenta Improvável" 
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = "Você procura algo na cela que possa servir de ferramenta durante a janela de atraso do guarda. Atrás do vaso sanitário, encontra um pedaço de metal afiado, provavelmente de um antigo encanamento. É pequeno, mas pode ser útil. No momento exato do atraso do guarda, você se posiciona para usar a ferramenta."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        digitar_red3 = tk.Button(self.janela, text="A - Usar o pedaço de metal para\n tentar serrar as grades da cela", fg="white", bg="#75010b", command= self.digitar_red3, width=30, height=2)
        digitar_red3.place(relx=0.3, rely=0.7, anchor="center")
        botao_limpar_tunel_ajuda = tk.Button(self.janela, text="B - Usar o pedaço de metal para\n tentar forçar a fechadura da cela", fg="white", bg="#75010b", command= self.forcar_fechadura_metal, width=30, height=2)
        botao_limpar_tunel_ajuda.place(relx=0.7, rely=0.7, anchor="center")
        self.animar_digitacao_geral(texto, label)

    def forcar_fechadura_metal(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - A Trava Cede"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("Você usa o pedaço de metal para forçar a fechadura da cela durante a janela de oportunidade. Com um último esforço, a trava se solta com um estalo. A porta da sua cela está aberta. Você sai discretamente para o corredor.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)

    def digitar_red3(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        texto = ("FIM DE JOGO: O som das grades foi sua ruína. Você foi pego(a) e seus esforços foram em vão.")
        label = tk.Label(self.janela, text=texto, fg="black", bg="red", font=("Impact", 20), wraplength=700, justify="center")
        label.place(relx=0.5, rely=0.5, anchor="center")
        self.animar_digitacao_geral(texto, label) 
           
    def preparar_distracao(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 4 - A Arte da Distração"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = "Você usa um pedaço de pano da sua coberta e alguns restos de comida para criar um pequeno 'barulho' ou 'cheiro' suspeito perto da grade da sua cela. Quando o guarda passa com seu atraso habitual, a distração funciona! Ele para para investigar o barulho, se afastando do seu posto por um momento. Isso cria uma janela de oportunidade para você agir."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        botao_arrombar_fechadura= tk.Button(self.janela, text="A - Tentar arrombar a fechadura\n da sua cela rapidamente", fg="white", bg="#75010b", command= self.arrombar_fechadura, width=30, height=2)
        botao_arrombar_fechadura.place(relx=0.3, rely=0.7, anchor="center")
        botao_rastejar_fresta_chao = tk.Button(self.janela, text="B - Usar o momento para rastejar\n para fora da cela por uma fresta no chão", fg="white", bg="#75010b", command= self.rastejar_fresta_chao, width=30, height=2)
        botao_rastejar_fresta_chao.place(relx=0.7, rely=0.7, anchor="center")
        self.animar_digitacao_geral(texto, label)
            
    def arrombar_fechadura(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - A Fechadura Cedendo"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = "Com a distração criada, você trabalha furiosamente na fechadura da cela. É um trabalho difícil, mas você consegue. A trava cede com um clique suave. Você abre a porta e se esgueira para fora, no corredor deserto."
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label)
        
    def rastejar_fresta_chao(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 5 - A Fresta Oculta"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = ("Durante a distração, você rasteja para fora da cela por uma fresta no chão que você havia encontrado. É apertado, mas você consegue passar para um túnel de manutenção sob o corredor.")
        label = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700, justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")
        self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="#75010b", fg="white", command= self.galeria_oculta, width=30, height=2, font=("Helvetica", 13))   
        self.botao_proximo.place(relx=0.5, rely=0.6, anchor="center")
        self.botao_proximo.bind("<Enter>", self.on_enter)
        self.botao_proximo.bind("<Leave>", self.on_leave)
        self.animar_digitacao_geral(texto, label) 
               
if __name__ == "__main__":
    app = Application()