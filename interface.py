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

        self.label_boas_vindas = None

    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def intro(self):
        self.mensagem_inicial.set(" VOCÊ FOI PRESO ")
        label_intro = tk.Label(self.janela, textvariable=self.mensagem_inicial, fg="red", bg="#1a1a1a", font=("Impact", 45, "bold"), wraplength=800, justify="left")
        label_intro.place(relx=0.5, rely=0.4, anchor="center")
        self.barras.set("═══════════════════════════════════════════════")
        label_barras = tk.Label(self.janela, textvariable=self.barras, fg="red", bg="#1a1a1a")
        label_barras.place(relx=0.5, rely=0.3, anchor="center")
        self.barras2.set("══════════════════════════════════════════════")
        label_barras2 = tk.Label(self.janela, textvariable=self.barras, fg="red", bg="#1a1a1a")
        label_barras2.place(relx=0.5, rely=0.5, anchor="center")
        linha_decorativa = tk.Frame(self.janela, bg="#ffffff", width=390, height=2)
        linha_decorativa.place(relx=0.5, rely=0.467, anchor="center")
        linha_lat1 = tk.Frame(self.janela, bg="#a50b0b", width=1537, height=15)
        linha_lat1.place(relx=0.5, rely=0.01, anchor="center")
        linha_lat2 = tk.Frame(self.janela, bg="#a50b0b", width=1537, height=15)
        linha_lat2.place(relx=0.5, rely=0.99, anchor="center")
        linha_lat3 = tk.Frame(self.janela, bg="#a50b0b", width=15, height=1537)
        linha_lat3.place(relx=0.01, rely=0.4, anchor="e")
        linha_lat3 = tk.Frame(self.janela, bg="#a50b0b", width=15, height=1537)
        linha_lat3.place(relx=0.99, rely=0.4, anchor="w")
        botao_start = tk.Button(self.janela, text="▶ START", width=20, height=2, fg="white", bg="red", command=self.mostrar_campo_nome, font=("Consolas", 16, "bold"))
        botao_start.place(relx=0.5, rely=0.650, anchor="center")
        botao_start.bind("<Enter>", self.on_enter)
        botao_start.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        event.widget.config(bg="#701b1b", fg="white")

    def on_leave(self, event):
        event.widget.config(bg="red", fg="white")

    def botao_inicial(self):
        botao_volta_inicio = tk.Button(self.janela, text="Volte para tela inicial", command=self.voltar_para_inicio, font=("Helvetica", 14), bg="#222", fg="white")
        botao_volta_inicio.place(relx=0.5, rely=0.9, anchor="center")

    def voltar_para_inicio(self):
        self.limpar_tela()
        self.intro()

    def mostrar_campo_nome(self):
        self.limpar_tela()
        self.botao_inicial()

        self.texto.set("DIGITE O NOME DO SEU PERSONAGEM:")
        label_texto = tk.Label(self.janela, textvariable=self.texto, fg="red", bg="#1a1a1a", font=("Impact", 27), wraplength=800, justify="center")
        label_texto.place(relx=0.5, rely=0.2, anchor="center")
        self.nome_mensagem.set("")

        self.entry_nome = tk.Entry(self.janela, textvariable=self.nome_mensagem, fg="red", bg="#1a1a1a", font=("Helvetica", 14), justify="center", insertbackground="red")
        self.entry_nome.place(relx=0.5, rely=0.4, anchor="center")

        self.botao_confirmar = tk.Button(self.janela, text="Confirmar nome", command=self.pegar_nome, font=("Helvetica", 14), bg="#222", fg="white")
        self.botao_confirmar.place(relx=0.5, rely=0.470, anchor="center")

    def pegar_nome(self):
        nome_digitado = self.nome_mensagem.get()
        self.boas_vindas.set(f"Olá, {nome_digitado}. Bem-vindo(a) à sua nova realidade: uma cela fria e silenciosa. Você foi preso(a)... mas não sabe exatamente por quê. Suas escolhas daqui em diante serão cruciais. Cada decisão pode te levar à liberdade — ou te condenar para sempre. Está pronta para enfrentar as sombras dessa prisão?")
        if self.label_boas_vindas is None:
            self.label_boas_vindas = tk.Label(self.janela, textvariable=self.boas_vindas, fg="white", bg="red", font=("Impact", 14), wraplength=700, justify="center")
            self.label_boas_vindas.place(relx=0.5, rely=0.7, anchor="center")
        self.janela.after(3000, lambda: self.mostrar_escolha_nivel_um(nome_digitado))

    def mostrar_escolha_nivel_um(self, nome):
        self.limpar_tela()
        self.botao_inicial()

        texto = "[NÍVEL 1] - O Despertar\nVocê desperta em uma cela úmida e mal iluminada. O que deseja fazer?"
        label_texto = tk.Label(self.janela, text=texto, fg="white", bg="#1a1a1a", font=("Helvetica", 14), wraplength=700, justify="left")
        label_texto.place(relx=0.5, rely=0.2, anchor="center")

        botao_a = tk.Button(self.janela, text="A - Investigar a cela", command=lambda: self.investigacao_cela(nome))
        botao_a.place(relx=0.3, rely=0.6, anchor="center")

        botao_b = tk.Button(self.janela, text="B - Chamar por alguém", command=lambda: self.chamar_por_alguem(nome))
        botao_b.place(relx=0.5, rely=0.6, anchor="center")

        botao_c = tk.Button(self.janela, text="C - Esperar em silêncio", command=lambda: self.esperar_em_silencio(nome))
        botao_c.place(relx=0.7, rely=0.6, anchor="center")

    def investigacao_cela(self, nome):
        self.limpar_tela()
        self.botao_inicial()

        texto = f"{nome}, você começa a investigar a cela. Há rachaduras nas paredes e um pequeno buraco no chão."
        label_texto = tk.Label(self.janela, text=texto, fg="white", bg="#1a1a1a", font=("Helvetica", 14), wraplength=700, justify="left")
        label_texto.place(relx=0.5, rely=0.3, anchor="center")

    def chamar_por_alguem(self, nome):
        self.limpar_tela()
        self.botao_inicial()

        texto = f"{nome}, você chama por alguém, mas só o silêncio responde."
        label_texto = tk.Label(self.janela, text=texto, fg="white", bg="#1a1a1a", font=("Helvetica", 14), wraplength=700, justify="left")
        label_texto.place(relx=0.5, rely=0.3, anchor="center")

    def esperar_em_silencio(self, nome):
        self.limpar_tela()
        self.botao_inicial()

        texto = f"{nome}, você decide esperar em silêncio, sentindo o tempo passar lentamente."
        label_texto = tk.Label(self.janela, text=texto, fg="white", bg="#1a1a1a", font=("Helvetica", 14), wraplength=700, justify="left")
        label_texto.place(relx=0.5, rely=0.3, anchor="center")


app = Application()
