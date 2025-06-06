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
        label_intro = tk.Label(self.janela, textvariable=self.mensagem_inicial, fg="red", bg="#1a1a1a",
                               font=("Impact", 45, "bold"), wraplength=800, justify="left")
        label_intro.place(relx=0.5, rely=0.4, anchor="center")

        self.barras.set("═══════════════════════════════════════════════")
        label_barras = tk.Label(self.janela, textvariable=self.barras, fg="red", bg="#1a1a1a")
        label_barras.place(relx=0.5, rely=0.3, anchor="center")

        self.barras2.set("══════════════════════════════════════════════")
        label_barras2 = tk.Label(self.janela, textvariable=self.barras2, fg="red", bg="#1a1a1a")
        label_barras2.place(relx=0.5, rely=0.5, anchor="center")

        linha_decorativa = tk.Frame(self.janela, bg="#ffffff", width=390, height=2)
        linha_decorativa.place(relx=0.5, rely=0.467, anchor="center")

        botao_start = tk.Button(self.janela, text="▶ START", width=20, height=2, fg="white", bg="red",
                                command=self.mostrar_campo_nome, font=("Consolas", 16, "bold"))
        botao_start.place(relx=0.5, rely=0.650, anchor="center")
        botao_start.bind("<Enter>", self.on_enter)
        botao_start.bind("<Leave>", self.on_leave)

        texto_inf = tk.Label(self.janela,
                             text="Suas escolhas moldarão o caminho. Cuidado... cada decisão pode te aproximar da verdade — ou do fim.",
                             fg="white", bg="#1a1a1a", font=("Lucida Console", 8, "italic"), wraplength=500)
        texto_inf.place(relx=0.5, rely=0.9, anchor="center")

    def on_enter(self, event):
        event.widget.config(bg="#701b1b", fg="white")

    def on_leave(self, event):
        event.widget.config(bg="red", fg="white")

    def botao_inicial(self):
        botao_volta_inicio = tk.Button(self.janela, text="Volte para tela inicial", command=self.voltar_para_inicio,
                                      font=("Helvetica", 14), bg="red", fg="white")
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

        if self.label_boas_vindas is None:
            self.label_boas_vindas = tk.Label(self.janela, text="", fg="white", bg="#1a1a1a", font=("Courier New", 11),
                                              wraplength=700, justify="center")
            self.label_boas_vindas.place(relx=0.5, rely=0.7, anchor="center")

            self.botao_proximo = tk.Button(self.janela, text="Próximo", bg="red", fg="white",
                                          command=self.mostrar_escolha_nivel_um)
            self.botao_proximo.place(relx=0.9, rely=0.9, anchor="w")
            self.botao_proximo.bind("<Enter>", self.on_enter)
            self.botao_proximo.bind("<Leave>", self.on_leave)

        self.texto_atual = ""
        self.indice_char = 0

        self.animar_digitacao()

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

    def mostrar_escolha_nivel_um(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        titulo = "NÍVEL 1  - O Despertar"
        label_titulo = tk.Label(self.janela, text=titulo, fg="red", bg="#1a1a1a", font=("Impact", 17), justify="center")
        label_titulo.place(relx=0.5, rely=0.1, anchor="center")
        texto = "Você desperta em uma cela úmida e mal iluminada. O que deseja fazer?"
        label_texto = tk.Label(self.janela, text=texto, fg="red", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                              justify="left")
        label_texto.place(relx=0.5, rely=0.2, anchor="center")

        botao_a = tk.Button(self.janela, text="A - Investigar a cela", fg="white", bg="#75010b",
                            command=self.investigacao_cela, width=27, height=2)
        botao_a.place(relx=0.199, rely=0.6, anchor="center")

        botao_b = tk.Button(self.janela, text="B - Chamar por alguém", fg="white", bg="#75010b",
                            command=self.chamar_por_alguem, width=27, height=2)
        botao_b.place(relx=0.500, rely=0.6, anchor="center")

        botao_c = tk.Button(self.janela, text="C - Esperar em silêncio", fg="white", bg="#75010b",
                            command=self.esperar_em_silencio, width=27, height=2)
        botao_c.place(relx=0.800, rely=0.6, anchor="center")

    def investigacao_cela(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        texto1 = (
            f"{self.nome_jogador}, Você começa a investigar a cela. Há rachaduras nas paredes e um pequeno buraco no chão. Passa os dedos pelas rachaduras nas paredes e examina a cama enferrujada. "
            f"Atrás de um tijolo solto, encontra um bilhete amassado. "
            f"Confie em ninguém. A saída está sob seus pés. "
            f"Você sente o chão tremer levemente... algo está escondido ali.")

        label_texto1 = tk.Label(self.janela, text=texto1, fg="white", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                                justify="left")
        label_texto1.place(relx=0.5, rely=0.2, anchor="center")

        botao_cavar = tk.Button(self.janela, text="A - Cavar Saida", fg="white", bg="#75010b", command=self.cavar_saida,
                                width=27, height=2)
        botao_cavar.place(relx=0.3, rely=0.6, anchor="center")

        botao_bilhete = tk.Button(self.janela, text="B - Esperar depois bilhete", fg="white", bg="#75010b", command=self.esperar_depois_bilhete,
                                width=27, height=2)
        botao_bilhete.place(relx=0.7, rely=0.6, anchor="center")

    def cavar_saida(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        texto = (f"{self.nome_jogador}, Com uma colher enferrujada escondida sob o colchão, você começa a cavar."
                 f"Horas se passam. Finalmente, um túnel apertado se revela."
                 f"Você rasteja por ele até encontrar uma grade solta que leva aos esgotos."
                 f"Antes de entrar, um outro prisioneiro o intercepta. Ele diz que quer ajudar, mas parece instável.")
        label = tk.Label(self.janela, text=texto, fg="white", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")

        botao_companheiro = tk.Button(self.janela, text="A- Deixar ele vim junto", fg="white", bg="#75010b", command=self.companheiro_esgoto, width=27, height=2)

        botao_companheiro.place(relx=0.3, rely=0.6, anchor="center")

        botao_conflito = tk.Button(self.janela, text="B- Ameaçar Ele", fg="white", bg="#75010b", command=self.companheiro_esgoto, width=27, height=2)

        botao_conflito.place(relx=0.3, rely=0.6, anchor="center")




    def esperar_depois_bilhete(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        texto = (f"{self.nome_jogador}, Você guarda o bilhete e finge dormir. Um guarda entra para inspeção e você nota que ele carrega um molho de chaves solto no cinto."
                 f"Você pode tentar se aproximar dele em outro momento e usar isso a seu favor.")
        label = tk.Label(self.janela, text=texto, fg="white", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")

    def chamar_por_alguem(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        texto = f"{self.nome_jogador}, você chama por alguém, mas não obtém resposta."
        label = tk.Label(self.janela, text=texto, fg="white", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")

    def esperar_em_silencio(self):
        self.limpar_tela()
        self.linhas()
        self.botao_inicial()
        texto = f"{self.nome_jogador}, você decide esperar em silêncio, escutando os sons da prisão."
        label = tk.Label(self.janela, text=texto, fg="white", bg="#1a1a1a", font=("Impact", 17), wraplength=700,
                         justify="left")
        label.place(relx=0.5, rely=0.3, anchor="center")




if __name__ == "__main__":
    app = Application()
