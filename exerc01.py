from tkinter import *

def enviar():
    nome = caixaNome.get()
    senha = caixaSenha.get()
    if nome=="Luciana" and senha=="456789":
        print(nome, "Seja bem vindo(a)")
    else:
        print("ERRO")

janela = Tk()
janela.title("Cadastro de cliente")
janela.geometry("500x300+400+150")

lNome = Label(janela, text="Nome Usuario: ",
              fg="blue",
              font=("Arial",20, "bold"))
caixaNome = Entry(janela, width=80)
lsenha = Label(janela, text="Senha Usuario: ",
              fg="blue",
              font=("Arial",20, "bold"))
caixaSenha = Entry(janela, width=80)
btnEnviar = Button(janela,
                   text="Autenticar",
                   bg="grey",
                   command=enviar)

lNome.pack() #mostrar o label
caixaNome.pack()
lsenha.pack()
caixaSenha.pack()
btnEnviar.pack()
janela.mainloop()