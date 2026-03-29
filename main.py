# Importando o Tkinter
from tkinter import *
from tkinter import ttk

# Importando o PIL
from PIL import Image, ImageTk

# Importando o "requests"
import requests

# Importando o "json"
import json

# Cores
co0 = "#444466"  # preta / black
co1 = "#feffff"  # branca / white 
co2 = "#6f9fbd"  # azul / blue
fundo = "#484f60" # background

# Criando a janela
janela = Tk()
janela.title("")
janela.geometry("320x350")
janela.configure(bg=fundo)
janela.resizable(width=FALSE, height=FALSE)

# Dividindo a janela em dois frames
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

# Criando o frame de cima
frame_cima = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0, relief="flat")
frame_cima.grid(row=1, column=0)

# Criando o frame de baixo
frame_baixo = Frame(janela, width=320, height=300, bg=fundo, pady=0, padx=0, relief="flat")
frame_baixo.grid(row=2, column=0, sticky=NW)

# Função para pegar dados
def info():
    # Link da API
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,AOA,BRL"

    # HTTP requests
    response = requests.get(api_link)

    # Convertendo os dados em dicionário
    dados = response.json()

    # Valor em USD
    valor_usd = float(dados["USD"])
    valor_formatado_usd = "$ {:,.2f}".format(valor_usd)
    l_p_usd["text"] = "Em Dólares é: " + valor_formatado_usd

    # Valor em EUR
    valor_euro = float(dados["EUR"])
    valor_formatado_euro = "€ {:,.2f}".format(valor_euro)
    l_p_euro["text"] = "Em Euros é: " +  valor_formatado_euro

    # Valor em BRL
    valor_real = float(dados["BRL"])
    valor_formatado_real = "R$ {:,.2f}".format(valor_real)
    l_p_real["text"] = "Em Reais é: " + valor_formatado_real

    # Valor em AOA
    valor_kz = float(dados["AOA"])
    valor_formatado_kz = "Kz {:,.2f}".format(valor_kz)
    l_p_kz["text"] = "Em Kwanzas é: " + valor_formatado_kz

    frame_baixo.after(1000, info)

# Configurando o frame de cima
imagem = Image.open("images/bitcoin.png")
imagem = imagem.resize((30, 30))
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, compound="left", bg=co1, relief="flat")
l_icon.place(x=10, y=10)

l_nome = Label(frame_cima, text="Bitcoin Price Tracker", font=("Arial 18 bold"), compound="left", bg=co1, fg=co2, relief="flat", anchor="center")
l_nome.place(x=50, y=10)

# Configurando o frame de baixo
l_p_usd = Label(frame_baixo, text="", font=("Arial 18"), compound="left", bg=fundo, fg=co1, relief="flat", anchor="center")
l_p_usd.place(x=0, y=50)

l_p_euro = Label(frame_baixo, text="", font=("Arial 12"), compound="left", bg=fundo, fg=co1, relief="flat", anchor="center")
l_p_euro.place(x=10, y=130)

l_p_real = Label(frame_baixo, text="", font=("Arial 12"), compound="left", bg=fundo, fg=co1, relief="flat", anchor="center")
l_p_real.place(x=10, y=160)

l_p_kz = Label(frame_baixo, text="", font=("Arial 12"), compound="left", bg=fundo, fg=co1, relief="flat", anchor="center")
l_p_kz.place(x=10, y=190)

info()

# Visualizando a janela
janela.mainloop()