import customtkinter as ctk

janela = ctk.CTk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False, False)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for j in range(4):
    janela.grid_columnconfigure(j, weight=1)

entrada = ctk.CTkEntry(janela, font=("Arial", 28))
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

def clique(valor):
    if valor == "=":
        try:
            resultado = eval(entrada.get())
            entrada.delete(0, "end")
            entrada.insert("end", str(resultado))
        except:
            entrada.delete(0, "end")
            entrada.insert("end", "Erro")
    elif valor == "AC":
        entrada.delete(0, "end")
    else:
        entrada.insert("end", valor)

botoes = [
    ("AC", 1, 0),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("+", 5, 2), ("=", 5, 3)
]


for(texto, linha, coluna) in botoes:
    ctk.CTkButton(janela, text=texto, font=("Arial", 28),command=lambda t=texto: clique(t)).grid(row=linha, column =coluna, padx=5, pady=5, sticky="nsew")

janela.mainloop()