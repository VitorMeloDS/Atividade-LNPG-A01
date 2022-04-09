from cgitb import text
from msilib.schema import ComboBox
from tkinter import *
from tkinter.ttk import Combobox


# Vai exibir na tela o resultado da pesquisa 
def mostra_pesquisa():
    
    cadastro = dados_pessoal[tabela.get()]
    nome_ps.configure(text=f"Nome: {cadastro[0]}")
    cpf_ps.configure(text=f"CPF: {cadastro[1]}")
    matricula_ps.configure(text=f"Matrícula: {cadastro[2]}")
    data_ps.configure(text=f"Data de Nascimento: {cadastro[3]}")


# Função para escolher quem vai pesquisar
def como_pesquisar():

    global janela2, dados_pessoal, tabela, nome_ps, cpf_ps, matricula_ps, data_ps

    # Tela de pesquisa
    janela2 = Toplevel()
    janela2.title("Pesquisar")
    janela2.geometry("600x500")
    janela2["bg"] = "#3D403F"

    # Lendo o arquivo e organizando os dados
    arquivo = open("texto.txt", "r")
    dados = arquivo.readlines()
    nome_lista = []
    dados_pessoal = {}
    for i in dados:
        i = i.split(";")
        nome_lista.append(i[0])
        dados_pessoal.setdefault(i[0], i[0:])
    arquivo.close()

    # Caixa de pesquisa
    Label(janela2, text="Pesquisar Dados", font="Courier 20 bold" ,bg="#3D403F", fg="white").place(x=170, y=20)
    tabela = Combobox(janela2, value=nome_lista, font="Courier 12", width=30)
    tabela.place(x=100, y=120)

    # Botão de pesquisa
    Button(janela2, text="Pesquisar", bg="#6FC497", font="Courier 9 bold", fg="white", width=8, command=mostra_pesquisa).place(x=430, y=120)

    # Nome do usuário pesquisado
    nome_ps = Label(janela2, text="Nome:", font="Courier 16 bold", bg="#3D403F", fg="white")
    nome_ps.place(x=100, y=240)

    # cpf do usuário pesquisado
    cpf_ps = Label(janela2, text="CPF:", font="Courier 16 bold", bg="#3D403F", fg="white")
    cpf_ps.place(x=100, y=270)

    # Número da matricula pesquisada
    matricula_ps = Label(janela2, text="Matrícula:", font="Courier 16 bold", bg="#3D403F", fg="white")
    matricula_ps.place(x=100, y=300)

    # Data de nascimento pesquisada
    data_ps = Label(janela2, text="Data de Nascimento:", font="Courier 16 bold", bg="#3D403F", fg="white")
    data_ps.place(x=100, y=330)

    Label(janela2, text="Autor: Vitor Melo da Silva", font="Courier", fg="#787878", bg="#3D403F", ).place(x=10, y=470)


    janela2.mainloop()


# função para cadastras as informações
def cadastrar():
    # Vai procurar um aruqivo com o mesmo nome se não achar irar criar um
    arquivo = open("texto.txt", "a")

    # Recebe as entradas do usuarios
    nome = nome_en.get().title().strip()
    cpf = cpf_en.get().strip()
    matricula = matricula_en.get().strip()
    data = data_en.get().strip()

    # Escreve os dados no arquivo
    arquivo.write(f"{nome};{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]};{matricula};{data[:2]}/{data[2:4]}/{data[4:8]}\n")

    arquivo.close()


# função e tela de cadastro 
def inserir_info():

    global janela, nome_lb, cpf_lb, matricula_lb, data_lb, nome_en, cpf_en, matricula_en, data_en

    # Tela de cadastro
    janela = Toplevel()
    janela.title("Cadastro de Dados")
    janela.geometry("600x500")
    janela["bg"] = "#3D403F"

    # Titulo da tela
    Label(janela, text="Formulário de cadastramento", font="Courier 22 bold" ,bg="#3D403F", fg="white").place(x=80, y=20)

    # Entrada do nome do cadastro
    nome_lb = Label(janela, text="Nome:", font="Courier 16 bold", bg="#3D403F", fg="white").place(x=140, y=100)
    nome_en = Entry(janela, font="Courier 12", width=30, bg="#E9E9E9", cursor="dot")
    nome_en.place(x=140, y=130)

    # Entrada do cpf do cadastro
    cpf_lb = Label(janela, text="CPF:", font="Courier 16 bold", bg="#3D403F", fg="white").place(x=140, y=160)
    cpf_en = Entry(janela, font="Courier 12", width=30, bg="#E9E9E9", cursor="dot")
    cpf_en.place(x=140, y=190)

    # Entrada da matrícula do cadastro
    matricula_lb = Label(janela, text="Matrícula:", font="Courier 16 bold", bg="#3D403F", fg="white").place(x=140, y=220)
    matricula_en = Entry(janela, font="Courier 12", width=30, bg="#E9E9E9", cursor="dot")
    matricula_en.place(x=140, y=250)

    # Entrada da data de nascimento do cadastro
    data_lb = Label(janela, text="Data de nascimento:", font="Courier 16 bold", bg="#3D403F", fg="white").place(x=140, y=280)
    data_en = Entry(janela, font="Courier 12", width=30, bg="#E9E9E9", cursor="dot")
    data_en.place(x=140, y=310)

    # Botão para cadastar as informações
    Button(janela, text="Cadastrar", bg="#6FC497", font="Courier 16", fg="white" ,command=cadastrar).place(x=220, y=380)
    
    Label(janela, text="Autor: Vitor Melo da Silva", font="Courier", fg="#787878", bg="#3D403F", ).place(x=10, y=470)

    janela.mainloop()


# tela principal do programa
tela = Tk()
tela.title("Formulário")
tela.geometry("600x300")
tela["bg"] = "#3D403F"

# Titulo das opções
Label(text="Sistema de Dados", font='Courier 22 bold', bg="#3D403F", fg="white").place(x=165, y=20)

# Botão para selecionar a opção de cadastro
Button(text="Cadastrar Dados", font="Courier 16", fg="white", bg="#6FC497", command=inserir_info ).place(x=80, y=120)

# Botâo para selecionar a opção de consutar dados 
Button(text="Mostrar Dados", font="Courier 16", fg="white", bg="#6FC497", command=como_pesquisar ).place(x=340, y=120)

Label(text="Autor: Vitor Melo da Silva", font="Courier", fg="#787878", bg="#3D403F", ).place(x=10, y=270)

tela.mainloop()
