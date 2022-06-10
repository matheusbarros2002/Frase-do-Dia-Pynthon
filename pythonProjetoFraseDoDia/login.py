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
um_nome = Label(frame_cima, text="LOGIN", anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
um_nome.place(x=102, y=5)

um_linha = Label(frame_cima, text="",width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
um_linha.place(x=10, y=45)

credenciais = ['jean','1234']

def verifica_senha():
    nome2 = e_nome.get()
    senha2 = e_pass.get()

    if nome2 == credenciais[0] and senha2 == credenciais[1]:
        command = janela.destroy
        janela2 = Tk()
        janela2.title('')
        janela2.geometry('380x300')
        janela2.configure(background=co1)
        janela2.resizable(width=FALSE, height=FALSE)

        # dividindo janela
        frame_cima2 = Frame(janela2, width=380, height=50, bg=co1, relief='flat')
        frame_cima2.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

        frame_baixo2 = Frame(janela2, width=380, height=250, bg=co1, relief='flat')
        frame_baixo2.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        # configurando parte de cima
        um_nome2 = Label(frame_cima2, text="Frase do dia !", anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
        um_nome2.place(x=80, y=5)

        um_linha2 = Label(frame_cima2, text="", width=350, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
        um_linha2.place(x=10, y=45)

        # configurando parte de baixo
        um_nome = Label(frame_baixo2, text="Digite um número de um a 20 *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        um_nome.place(x=85, y=20)
        e_nome2 = Entry(frame_baixo2, width=5, justify='left', font=("", 15), highlightthickness=1, relief='solid')
        e_nome2.place(x=140, y=50)

        um_pass2 = Label(frame_baixo2, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
        um_pass2.place()
        e_pass2 = Entry(frame_baixo2, width=25, justify='left', show='*', font=("", 15), highlightthickness=1,
                        relief='solid')
        e_pass2.place()

        b_confirmar2 = Button(frame_baixo2, text="Buscar frase", width=30, height=2, font=('Ivy 8 bold'), bg=co2,
                              fg=co1, relief=RAISED, overrelief=RIDGE)
        b_confirmar2.place(x=70, y=90)

        janela2.mainloop()
    else:
        messagebox.showwarning('Erro','Credenciais invalidas')

#configurando parte de baixo
um_nome = Label(frame_baixo, text="Nome *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
um_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)

um_pass = Label(frame_baixo, text="Palavra passe *", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
um_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)

b_confirmar = Button(frame_baixo, command=verifica_senha, text="Entrar",width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)

janela.mainloop()