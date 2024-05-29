import tkinter as tk
import random

squad_list=['Amanda Costa','Eliseu Silva','Tiago Rocha','Victor Jesus','Amanda Gabrielle Silva','Paola Toledo','Jorge Harbes','Rafael Albino']

def sortear():
    numero_sorteado = random.randint(0, len(squad_list)-1)
    label_resultado.config(text=f"O sortudo do momento é: {squad_list[numero_sorteado]}")

# main window
janela = tk.Tk()
janela.title("Sorteador do Digital Squad")
janela.geometry("300x200")

# widgets creation
label_titulo = tk.Label(janela, text="Sorteador do Digital Squad", font=("Arial", 16))
label_titulo.pack(pady=10)

botao_sortear = tk.Button(janela, text="Sortear", command=sortear)
botao_sortear.pack(pady=10)

label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

# starts window loop
janela.mainloop()
