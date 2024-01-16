from tkinter import *


janela =  Tk()
janela.title("calculadora")
#janela.iconbitmap("calculadora.ico")
janela.geometry("500x300+400+150")
janela.resizable(False,False)

lN1 = Label(janela,
            text="Informe o primeiro valor: ")
caixaN1 = Entry(janela)

LN2 = Label(janela,
            text="Informe o segundo valor: ")
            
caixaN2 = Entry(janela)
                
btncalcular = Button(janela)
                    

lN1.grid(column=0,row=0, pady=10)
caixaN1.grid(column=1, row=0, Widget=30)
LN2.grid(column=0, row=1)
caixaN2.grid(column=1,row=1)
btncalcular.grid(column=0,row=2,)

janela.mainloop()