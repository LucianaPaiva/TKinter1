import tkinter as tk 


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry("300x400")
        self.resultado_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entrada para exibir os números e resultados
        display = tk.Entry(self, textvariable=self.resultado_var, font=('Helvetica', 20), justify='right')
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

        # Definindo os botões
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Adicionando os botões à grade
        for i, button_text in enumerate(botoes):
            row_val, col_val = divmod(i, 4)  # Divide o índice pelo número de colunas (4 neste caso)
            tk.Button(self, text=button_text, padx=20, pady=20, font=('Helvetica', 14), command=lambda b=button_text: self.on_button_click(b)).grid(row=row_val + 1, column=col_val)

    def on_button_click(self, button):
        current_text = self.resultado_var.get()

        if button == "=":
            try:
                result = str(eval(current_text))
                self.resultado_var.set(result)
            except Exception as e:
                self.resultado_var.set("Erro")
        else:
            self.resultado_var.set(current_text + button)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
