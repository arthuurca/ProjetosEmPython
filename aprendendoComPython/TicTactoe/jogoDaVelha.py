import customtkinter as ctk
import random

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

    for i in range(3):#limita a criação de linhas em 3
        linha = []
        for j in range(3): #limita a criação de colunas para 3
            indice = i * 3 + j #forma para localizar posição dentro do tabuleiro
            botao = ctk.CTkButton(frame, text="", width= 100, height=100, font=("Arial", 24, "bold"),
            command= lambda idx=indice: jogar(idx)) #atribui um indice para o botao a ser clicado, jogara naquele indice especificado
            botao.grid(row=i, column =j, padx=5, pady=5)
            linha.append(botao) #coloca o botao na linha do indice
        tabuleiro.append(linha) #coloca a linha naquele indice dentro do tabuleiro

    ctk.CTkButton(janela, text="Voltar ao menu", command=abre_menu).pack(pady=10)

def jogar(indice):
    global jogador_atual

    if estado[indice] != "":
        return

    estado[indice] = jogador_atual
    linha, coluna = divmod(indice, 3) #retorna a linha e a coluna divmod faz a divisao dos 2 valores (divisao inteira, resto)
    tabuleiro[linha][coluna].configure(text=jogador_atual)#atribui o texto de jogador atual no botão

    if verificar_vitoria(jogador_atual):
        mostrar_resultado(f"'{jogador_atual}' venceu!")
        return
    elif "" not in estado:
        mostrar_resultado(f"Empate!")
        return

    jogador_atual = "O" if jogador_atual == "X" else "X"

    if modo_cpu and jogador_atual == "O": #verifica se esta em modoCpu e se e a vez da cpu
        janela.after(500, jogada_cpu)

def mostrar_resultado(texto):
    limparTela()
    ctk.CTkLabel(janela, text=texto, font=("Arial", 24, "bold")).pack(pady=30)
    ctk.CTkButton(janela, text="Jogar novamente", command=lambda: iniciar_jogo(vs_cpu=modo_cpu)).pack(pady=10)
    ctk.CTkButton(janela, text="Voltar ao menu", command=abre_menu).pack(pady=10)

def jogada_cpu():
    global jogador_atual
    posicoes_vazias = [i for i, v in enumerate(estado) if v == ""]#analisa o indice e o valor do estado e caso seja" ele atribui a variavel
    if not posicoes_vazias:
        return
    escolha = random.choice(posicoes_vazias)
    jogar(escolha)
    
def verificar_vitoria(simbolo):
    combinacoes = [[0, 1, 2], [3,4,5], [6, 7, 8],
                   [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]
                   
                   ]
    for c in combinacoes: #verifica canda i de combinacoes se é igual "X" ou "O"
        if(estado[c[0]])== estado[c[1]] == estado[c[2]] == simbolo:
            return True
    return False

def abre_menu():
    limparTela()
    titulo = ctk.CTkLabel(janela, text="Jogo da Velha", font=("Arial", 24, "bold"))
    titulo.pack(pady=30)

    botao1x1= ctk.CTkButton(janela, text="1x1", font=("Arial",14), command= lambda: iniciar_jogo(vs_cpu=False))
    botao1x1.pack(pady=10)

    botaoCpu = ctk.CTkButton(janela, text="1xCpu", font=("Arial",14), command=lambda: iniciar_jogo(vs_cpu=True))
    botaoCpu.pack(pady=10)


abre_menu()
janela.mainloop()