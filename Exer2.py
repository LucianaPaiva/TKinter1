from tkinter import *

def calcular_media():
    try:
        nota1 = float(caixaNota1.get())
        nota2 = float(caixaNota2.get())
        media = (nota1 + nota2) / 2

        if media >= 7:
            resultado = "Aprovado"
        else:
            resultado = "Reprovado"



janela = Tk()
janela.title("Cadastro de Alunos")
janela.geometry("300x100+200+85")

lNome = Label(janela, text="Nome do Aluno(a): ",
              fg="grey",
              font=("Arial",20, "bold"))
caixaNome = Entry(janela, width=50)
lidade = Label(janela, text="Idade do Aluno(a): ",
              fg="grey",
              font=("Arial",20, "bold"))
caixaIdade = Entry(janela, width=30)

lHabilidades = Label(janela, text="Habilidades do Aluno(a): ",
              fg="grey",
              font=("Arial",20, "bold"))

check_var = BooleanVar()

ck1 = Checkbutton(janela,
                  text="Python")
ck2 = Checkbutton(janela,
                  text="js")
ck3 = Checkbutton(janela,
                  text="HTML")
ck4 = Checkbutton(janela,
                  text="CSS")

lGenero = Label(janela, text="Genero do Aluno(a): ",
              fg="grey",
              font=("Arial",20, "bold"))

var_genero = IntVar()

op1 = Radiobutton(janela,
                  text="Feminino",
                  variable=var_genero,
                  value=1)
op2 = Radiobutton(janela,
                  text="Masculino",
                  variable=var_genero,
                  value=2)
op3 = Radiobutton(janela,
                  text="Outros",
                  variable=var_genero,
                  value=3)

lNotadoaluno = Label(janela, text="Nota do Aluno(a): ",
              fg="grey",
              font=("Arial",20, "bold"))



lNome.pack() #mostrar o label
caixaNome.pack()
lidade.pack()
caixaIdade.pack()
lGenero.pack()
op1.pack()
op2.pack()
op3.pack()
# Botão de envio
btn_enviar = Button(janela, text="Enviar", command=enviar)
btn_enviar.pack()
lHabilidades.pack()
ck1.pack()
ck2.pack()
ck3.pack()
ck4.pack()
lNotadoaluno.pack()
# Botão de envio
btn_enviar = Button(janela, text="Enviar", command=enviar)
btn_enviar.pack()
janela.mainloop()



