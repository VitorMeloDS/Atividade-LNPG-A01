from  tkinter import Tk, Label, Button, Entry, Toplevel, Radiobutton, IntVar, END, messagebox
from tkinter.ttk import Combobox
from tkinter import ttk
import tkinter as tk
from domain import banda
from tkinter.messagebox import showinfo

def tabela_view():

    root = tk.Tk()
    root.title('Treeview demo')
    root.geometry('800x200')

    #pegando os dados da função
    dados = []
    pesquisa = tabela.get()
    data_radio = datas_radio.get()
    ano = lista_check.get()
    dados = banda.pesquisando(pesquisa, data_radio, ano)
    tabela.delete(0, END)
    
    
    # define columns
    columns = ('alb', 'band', 'dat', 'lancamento')

    tree = ttk.Treeview(root, columns=columns, show='headings')

    # define headings
    tree.heading('alb', text='Álbum')
    tree.heading('band', text='Banda')
    tree.heading('dat', text='Data')
    tree.heading('lancamento', text='Lançamento')

    # add data to the treeview
    for contact in dados:
        tree.insert('', tk.END, values=contact)


    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))


    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

    # add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    # run the app
    root.mainloop()

def tela_pesquisa():

    global janela2, tabela, datas_radio, lista_check

    # Tela de pesquisa
    janela2 = Toplevel()
    janela2.title("Pesquisar")
    janela2.geometry("600x500")
    janela2["bg"] = "#3D403F"

    Label(janela2, text="Pesquisar Dados", font="Courier 20 bold" ,bg="#3D403F", fg="white").place(x=170, y=20)
    Label(janela2, text="Pesquisar Album ou Banda:", font="Courier 16 bold" ,bg="#3D403F", fg="white").place(x=130, y=110)
    tabela = Entry(janela2, font="Courier 12", width=30, bg="#E9E9E9", cursor="dot")
    tabela.place(x=130, y=150)

    datas_radio = IntVar()
    es_entre = Radiobutton(janela2, text = 'Igual', variable=datas_radio,value=1, bg="#3D403F")
    es_posterior = Radiobutton(janela2, text = 'Posterior ', variable=datas_radio,value=2, bg="#3D403F")
    es_anterior = Radiobutton(janela2, text = 'Anterior ', variable=datas_radio,value=0, bg="#3D403F")
    es_entre.place(x=240, y=275)  
    es_posterior.place(x=340, y=275)
    es_anterior.place(x=140, y=275)
    anos_data = []
    for i in range(223):
        a = 1800 + i
        anos_data.append(a)
    
    Label(janela2, text="Inserir ano:", font="Courier 16 bold" ,bg="#3D403F", fg="white").place(x=130, y=200)
    lista_check = Combobox(janela2, value=anos_data, font="Courier 12", width=28, cursor="dot")
    lista_check.place(x=130, y=240)

    # Botão de pesquisa
    Button(janela2, text="Pesquisar", bg="#6FC497", font="Courier 16 bold", fg="white", command=tabela_view).place(x=230, y=360)

def tela_cadastro():

    global janela, album_lb, cpf_lb, matricula_lb, data_lb, nome_album, cpf_en, banda_en, data_en, album_lancamento

    # Tela de cadastro
    janela = Toplevel()
    janela.title("Cadastro de Dados")
    janela.geometry("600x800")
    janela["bg"] = "#3D403F"


    # Titulo da tela
    Label(janela, text="Formulário de cadastramento", font="Courier 22 bold" ,bg="#3D403F", fg="white").place(x=80, y=50)

    # Entrada do nome do cadastro
    album_lb = Label(janela, text="Nome do Álbum:", font="Courier 16 bold", bg="#3D403F", fg="white").place(x=140, y=130)
    nome_album = Entry(janela, font="Courier 12", width=30, bg="#E9E9E9", cursor="dot")
    nome_album.place(x=140, y=170)


    # Entrada do nome da banda do cadastro
    matricula_lb = Label(janela, text="Nome da Banda:", font="Courier 16 bold", bg="#3D403F", fg="white").place(x=140, y=200)
    banda_en = Entry(janela, font="Courier 12", width=30, bg="#E9E9E9", cursor="dot")
    banda_en.place(x=140, y=240)

    # Entrada da data de nascimento do cadastro
    data_lb = Label(janela, text="Ano de Lançamento:", font="Courier 16 bold", bg="#3D403F", fg="white").place(x=140, y=270)

    data_en = Entry(janela, font="Courier 12", width=30, bg="#E9E9E9", cursor="dot")
    data_en.place(x=140, y=310)

      # Checkbutton com Sim ou não
    album_lancamento = IntVar()
    Label(janela, text='Álbum lançamento?', font="Courier 16 bold", bg="#3D403F", fg="white").place(x=200, y=370)
    es_sim = Radiobutton(janela, text = 'Sim', variable=album_lancamento,value=1, bg="#3D403F")
    es_não = Radiobutton(janela, text = 'Não', variable=album_lancamento,value=0, bg="#3D403F")
    es_sim.place(x=310, y=450)  
    es_não.place(x=220, y=450)
    # Botão para cadastar as informações
    Button(janela, text="Cadastrar", bg="#6FC497", font="Courier 16", fg="white" ,command=save_button_command).place(x=220, y=540)
    
    Label(janela, text="Autor: Vitor, Denilson, Ykaro", font="Courier", fg="#787878", bg="#3D403F", ).place(x=10, y=720)

    janela.mainloop()

def save_button_command():
    #comando do botão "cadastrar"
    a = nome_album.get().title().strip()
    c = data_en.get().strip()
    b = banda_en.get().title().strip()
    d = album_lancamento.get()
    if a != '' and b != '' and c != '':
        if len(c) > 4 or len(c) < 4:
            messagebox.showinfo("insira os dados", "Por favor, insira o ano do album (ex: 2000)")
        else:
            mybanda = banda(nome_album=a, ano_lancamento=c, nome_banda=b, album_lancamento=d)
            mybanda.salvar()
        janela.destroy()
    else: messagebox.showinfo("insira os dados", "Todos os dados são obrigatórios!")
    
def tela_principal():
  # tela Principal
  tela = Tk()
  tela.title("Formulário")
  tela.geometry("600x300")
  tela["bg"] = "#3D403F"
  
  # Titulo das opções
  Label(text="Sistema de Dados", font='Courier 22 bold', bg="#3D403F", fg="white").place(x=165, y=20)
  
  # Botão para selecionar a opção de cadastro
  Button(text="Cadastrar Dados", font="Courier 16", fg="white", bg="#6FC497", command=tela_cadastro ).place(x=80, y=120)
  
  # Botâo para selecionar a opção de consutar dados 
  Button(text="Mostrar Dados", font="Courier 16", fg="white", bg="#6FC497", command=tela_pesquisa ).place(x=340, y=120)
  
  Label(text="Autor: Vitor Melo, Denilson Vieira, Ykaro Alexandre", font="Courier", fg="#787878", bg="#3D403F", ).place(x=10, y=270)
  
  tela.mainloop()
