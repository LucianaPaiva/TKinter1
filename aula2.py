from tkinter import *

janela = Tk()
frame = Frame(janela,
              width=200,
              height=300,
              bg="blue",
              borderwidth=5,
              relief=RAISED)

check_var = BooleanVar()

ck = Checkbutton(janela,
                 text="Li e concordo", variable=check_var)

op1 = Radiobutton(janela,
                  text="Parda")
op2 = Radiobutton(janela,
                  text="Branco")
op3 = Radiobutton(janela,
                  text="Amarela")

frame.pack()
ck.pack(side=)
op1.pack()
op2.pack()
op3.pack()
janela.mainloop()
