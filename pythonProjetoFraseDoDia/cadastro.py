from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#cores
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#00FA9A"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

# criando a janela
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

#dividindo janela
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

#configurando parte de cima
um_nome = Label(frame_cima, text="Cadastre-se", anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
um_nome.place(x=50, y=5)

um_linha = Label(frame_cima, text="",width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
um_linha.place(x=10, y=45)


#configurando parte de baixo
um_nome = Label(frame_baixo, text="Crie seu nome de login *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
um_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

um_pass = Label(frame_baixo, text="Crie sua palavra passe *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
um_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)

b_confirmar = Button(frame_baixo, text="CADASTRAR",width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)

janela.mainloop()