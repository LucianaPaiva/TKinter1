from tkinter import *

habilities =  []

def cadastrar():
    nome = name.get()
    nota1 = n1.get()
    nota2 = n2.get()
    idade = age.get()
    genero = generoVar.get()

    media = int(nota1) + int(nota2)/2

    print(f"Olá {nome}!")
    if(media >= 7):
        print("Aprovado")
    else:
        print("Reprovado") 

    if(check_var1.get() == True):
        habilities.append("Python")
    if(check_var2.get() == True):
        habilities.append("JS")
    if(check_var3.get() == True):
        habilities.append("HTML")
    if(check_var4.get() == True):
        habilities.append("CSS")
    
    print('#'*20)
    print(f"Nome: {nome}\nIdade: {idade}\nSexo: {genero}") 
    print(f"Habilidades: {habilities}")
    print('#'*20)


janela = Tk()

janela.title("Tkinter II")
janela.geometry("600x400+200+100")

nome = Label(janela, 
             text="Nome: ",
             font=("Arial",15,"bold"))
name= Entry()

idade = Label(janela, 
             text="Idade: ",
             font=("Arial",15,"bold"))
age= Entry()

genderChoice = Label(janela,
                     text="Gênero")

nota1 = Label(janela,
                     text="Nota 1")
n1 = Entry()

nota2 = Label(janela,
                     text="Nota 2")
n2 = Entry()

habilidades = Label(janela,
                     text="Habilidades")


btnCadastrar = Button(text="Cadastrar",
                      command=cadastrar)

generoVar = StringVar()
masculino = Radiobutton(janela,text="MASCULINO",variable=generoVar,value="masculino")
feminino = Radiobutton(janela,text="FEMININO", variable=generoVar,value="feminino")
outros = Radiobutton(janela,text="OUTROS", variable=generoVar,value="outros")

check_var1 = BooleanVar()
check_var2 = BooleanVar()
check_var3 = BooleanVar()
check_var4 = BooleanVar()
python = Checkbutton(janela, text="Python",variable=check_var1)
js = Checkbutton(janela, text="JS",variable=check_var2)
html = Checkbutton(janela, text="HTML",variable=check_var3)
css = Checkbutton(janela, text="CSS",variable=check_var4)


nome.pack()
name.pack()

idade.pack()
age.pack()

masculino.pack()
feminino.pack()
outros.pack()

habilidades.pack()
python.pack()
js.pack()
html.pack()
css.pack()

nota1.pack()
n1.pack()

nota2.pack()
n2.pack()


btnCadastrar.pack()

janela.mainloop()
caixa.grid(column=1,row=0,padx=5,pady=140)
btn.grid(column=2,row=0,padx=5,pady=140)
janela.mainloop()