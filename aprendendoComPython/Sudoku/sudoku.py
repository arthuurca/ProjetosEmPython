import customtkinter as ctk

janela = ctk.CTk()
janela.title("Sudoku")
janela.geometry("400x500")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()

def iniciar_jogo():
    global tabuleiro, estado,


