import random
import tkinter as tk
from tkinter import messagebox

alongamentos = [
    "Alongamento de Pernas",
    "Alongamento de Braços",
    "Alongamento de Costas",
    "Alongamento de Pescoço",
    "Alongamento de Ombros",
]

exercicios = [
    "Flexões",
    "Agachamentos",
    "Levantamento de Pernas",
    "Polichinelos",
    "Abdominais",
    "Corrida no Lugar",
]

series = [2, 3, 4, 5]
repeticoes = [5, 10, 15, 20]

def escolher_alongamento():
    alongamento = random.choice(alongamentos)
    return alongamento

def escolher_exercicio():
    exercicio = random.choice(exercicios)
    return exercicio

def serie_aleatoria():
    serie = random.choice(series)
    return serie

def repeticoes_aleatorias():
    quantidade = random.choice(repeticoes)
    return quantidade

def mostrar_escolhas():
    repeticao = repeticoes_aleatorias()
    serie = serie_aleatoria()
    alongamento = escolher_alongamento()
    exercicio = escolher_exercicio()

    label_alongamento.config(text=f"Faça {serie} séries de {repeticao} repetições de {alongamento}", fg='blue')  # Mudança de cor
    label_exercicio.config(text=f"Faça {serie} séries de {repeticao} repetições de {exercicio}", fg='blue')  # Mudança de cor

    contador = 1800
    def atualizar_contador():
        nonlocal contador
        if contador > 0:
            minutos = contador // 60
            segundos = contador % 60
            label_contador.config(text=f"Próxima atualização em {minutos} min {segundos} s", fg='red')
            contador -= 1
            janela.after(1000, atualizar_contador)
        else:
            label_contador.config(text="")
            mostrar_escolhas()  

    label_contador.config(text=f"Próxima atualização em 30 minutos", fg='red')
    janela.after(1000, atualizar_contador)  

janela = tk.Tk()
janela.title("Exercícios e Alongamentos Aleatórios")

label_alongamento = tk.Label(janela, text="", font=("Helvetica", 16))
label_alongamento.pack(padx=20, pady=10)

label_exercicio = tk.Label(janela, text="", font=("Helvetica", 16))
label_exercicio.pack(padx=20, pady=10)

label_contador = tk.Label(janela, text="", font=("Helvetica", 12))
label_contador.pack(padx=20, pady=5)

botao_fechar = tk.Button(janela, text="Fechar", command=janela.quit)
botao_fechar.pack()

mostrar_escolhas()  

janela.mainloop()