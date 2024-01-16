from tkinter import *

def enviar():
    nome = caixaNome.get()
    print(nome, "Seja bem vindo(a)!!!")

janela = Tk()
janela.title("cadstro de cliente")
janela.iconbitmap("icone.ico")
janela.geometry("500x300+400+150")
#janela.resizable(False, False)
janela.maxsize(700,500)
janela.minsize(300,200)

lNome = Label(janela, text="Digite o nome: ",
              fg="blue",
              font=("Arial",20, "bold"))

caixaNome = Entry(janela, width=80)
btnEnviar = Button(janela,
                   text="Enviar",
                   bg="grey",
                   command=enviar)

lNome.pack() #mostrar o label
caixaNome.pack()
btnEnviar.pack()
janela.mainloop()