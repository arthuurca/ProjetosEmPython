import customtkinter as ctk

janela = ctk.CTk()
janela.title("Jogo da Velha")
janela.geometry("400x500")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def limparTela():
    for widget in janela.winfo_children(): #para cada botao ou janela que tiver 
        widget.destroy()

def iniciar_jogo(vs_cpu = False):
    global tabuleiro, estado, jogador_atual, modo_cpu

    limparTela()
    modo_cpu = vs_cpu
    jogador_atual = "X"
    estado = [""] * 9 #cria a representação lógica do tabuleiro 9 strings vazias
    tabuleiro = [] #representação visual do tabuleiro

    frame = ctk.CTkFrame(janela) #cria um conteiner
    frame.pack(pady=20) #faz este conteiner visivel

    for i in range(3):
        linha = []
        for j in range(3):
            indice = i * 3 + j #forma para localizar posição dentro do tabuleiro
            botao = ctk.CTkButton(frame, text="", width= 100, height=100, font=("Arial", 24, "bold"),
            command= lambda idx=indice: jogar(idx)) #atribui um indice para o botao a ser clicado, jogara naquele indice especificado
            botao.grid(row=i, column =j, padx=5, pady=5)
            linha.append(botao)
        tabuleiro.append(linha)

    ctk.CTkButton(janela, text="Voltar ao menu", command=abre_menu).pack(pady=10)

def jogar():
    return

def abre_menu():
    limparTela()
    titulo = ctk.CTkLabel(janela, text="Jogo da Velha", font=("Arial", 24, "bold"))
    titulo.pack(pady=30)

    botao1x1= ctk.CTkButton(janela, text="1x1", font=("Arial",14), command= lambda: iniciar_jogo(vs_cpu=False))
    botao1x1.pack(pady=10)

    botaoCpu = ctk.CTkButton(janela, text="1xCpu", font=("Arial",14), command=lambda: iniciar_jogo(vs_cpu=False))
    botaoCpu.pack(pady=10)


abre_menu()
janela.mainloop()