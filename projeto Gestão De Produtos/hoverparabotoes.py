from tkinter import *
from turtle import bgcolor

janela = Tk()

def hover(botao, color1,color2,color3):
    botao.configure(bg=color1)
    def fora(e):
        botao.configure(bg=color1)
    def dentro(e):
        botao.configure(bg=color2)
    def pressionando(e):
        botao.configure(activebackground=color3)


    botao.bind("<Enter>", dentro)
    botao.bind("<Leave>", fora)
    botao.bind("<ButtonPress-1>", pressionando)
janela.configure(bd=30)  
botao1 = Button(janela, width=10, height=4, text="inserir", bd=0, fg="#fff", cursor="hand2", font=("Arial",20))
botao1.pack()
hover(botao1, "black", "gray","violet")
janela.mainloop()