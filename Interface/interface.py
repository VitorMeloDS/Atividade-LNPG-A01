from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter.messagebox import showinfo

# Vai exibir na tela o resultado da pesquisa 
def mostra_pesquisa():
    
    try:  
        cadastro = dados_pessoal[tabela.get()]
        nome_ps.configure(text=f"Álbum: {cadastro[0]}")
        banda_ps.configure(text=f"Banda: {cadastro[1]}")
        data_ps.configure(text=f"Data de Criação: {cadastro[2]}")
        lancamento_ps.configure(text=f"Álbum Lançamento do Artista:: {cadastro[3]}")
    except:
        messagebox.showwarning("Sem Dados", "Insira um Album!")
        janela2.destroy()


# Função para escolher quem vai pesquisar
def como_pesquisar():

    global janela2, dados_pessoal, tabela, nome_ps, banda_ps, data_ps, lancamento_ps

    # Tela de pesquisa
    janela2 = Toplevel()
    janela2.title("Pesquisar")
    janela2.geometry("600x500")
    janela2["bg"] = "#3D403F"

    # Lendo o arquivo e organizando os dados
    arquivo = open("db.txt", "r")
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
    nome_ps = Label(janela2, font="Courier 16 bold", bg="#3D403F", fg="white")
    nome_ps.place(x=100, y=240)

    # cpf do usuário pesquisado
    banda_ps = Label(janela2, font="Courier 16 bold", bg="#3D403F", fg="white")
    banda_ps.place(x=100, y=270)

    # Número da matricula pesquisada
    data_ps = Label(janela2, font="Courier 16 bold", bg="#3D403F", fg="white")
    data_ps.place(x=100, y=300)

    # Data de nascimento pesquisada
    lancamento_ps = Label(janela2, font="Courier 16 bold", bg="#3D403F", fg="white")
    lancamento_ps.place(x=100, y=330)

    Label(janela2, text="Autores: Vitor Melo, Denilson, Ykaro", font="Courier", fg="#787878", bg="#3D403F", ).place(x=10, y=470)

    janela2.mainloop()


# função para cadastras as informações
def cadastrar():

    # Vai procurar um aruqivo com o mesmo nome se não achar irar criar um
    arquivo = open("db.txt", "a")

    # Recebe as entradas do usuarios
    nome = nome_en.get().title().strip()
    matricula = matricula_en.get().strip()
    data = data_en.get().strip()
    escolha = str(valor_escolha.get())
    result = ''
    if escolha == '1':
      result = 'Sim'
    else: result = 'Não'
    # Escreve os dados no arquivo
    arquivo.write(f"{nome};{matricula};{data[:2]}/{data[2:4]}/{data[4:8]}; {result}\n")
    messagebox.showinfo("Salvo", "Álbum salvo com sucesso!")

    arquivo.close()
    nome_en.delete(0, END)
    matricula_en.delete(0, END)
    data_en.delete(0, END)


# função e tela de cadastro 
def inserir_info():

    global janela, album_lb, cpf_lb, matricula_lb, data_lb, nome_en, cpf_en, matricula_en, data_en, valor_escolha

    # Tela de cadastro
    janela = Toplevel()
    janela.title("Cadastro de Dados")
    janela.geometry("600x800")
    janela["bg"] = "#3D403F"

    # Titulo da tela
    Label(janela, text="Formulário de cadastramento", font="Courier 22 bold" ,bg="#3D403F", fg="white").place(x=80, y=50)

    # Entrada do nome do cadastro
    album_lb = Label(janela, text="Nome do Álbum:", font="Courier 16 bold", bg="#3D403F", fg="white").place(x=140, y=130)
    nome_en = Entry(janela, font="Courier 12", width=30, bg="#E9E9E9", cursor="dot")
    nome_en.place(x=140, y=170)


    # Entrada do nome da banda do cadastro
    matricula_lb = Label(janela, text="Nome da Banda:", font="Courier 16 bold", bg="#3D403F", fg="white").place(x=140, y=280)
    matricula_en = Entry(janela, font="Courier 12", width=30, bg="#E9E9E9", cursor="dot")
    matricula_en.place(x=140, y=310)

    # Entrada da data de nascimento do cadastro
    data_lb = Label(janela, text="Ano de Lançamento:", font="Courier 16 bold", bg="#3D403F", fg="white").place(x=140, y=210)

    data_en = Entry(janela, font="Courier 12", width=30, bg="#E9E9E9", cursor="dot")
    data_en.place(x=140, y=240)

      # Checkbutton com Sim ou não
    valor_escolha = IntVar()
    Label(janela, text='Álbum lançamento?', font="Courier 16 bold", bg="#3D403F", fg="white").place(x=200, y=370)
    es_sim = Radiobutton(janela, text = 'Sim', variable=valor_escolha,value=1, bg="#3D403F")
    es_não = Radiobutton(janela, text = 'Não', variable=valor_escolha,value=2, bg="#3D403F")
    es_sim.place(x=310, y=450)  
    es_não.place(x=220, y=450)
    # Botão para cadastar as informações
    Button(janela, text="Cadastrar", bg="#6FC497", font="Courier 16", fg="white" ,command=cadastrar).place(x=220, y=540)
    
    Label(janela, text="Autores: Vitor Melo, Denilson, Ykaro", font="Courier", fg="#787878", bg="#3D403F", ).place(x=10, y=720)

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

Label(text="Autores: Vitor Melo, Denilson, Ykaro", font="Courier", fg="#787878", bg="#3D403F", ).place(x=10, y=270)

tela.mainloop()