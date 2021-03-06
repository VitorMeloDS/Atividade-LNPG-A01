from pickle import TRUE
from db import database


class banda:

    #receber os dados dos Entry
    def __init__(self, nome_album, ano_lancamento, nome_banda, album_lancamento):
        self.nome_album = nome_album
        self.ano_lancamento = ano_lancamento
        self.nome_banda = nome_banda
        self.album_lancamento = album_lancamento
        if self.album_lancamento == 1:
            self.album_lancamento = 'Sim'
        else:
            self.album_lancamento = 'Nao'   
    
    #função para salvar
    def salvar(self):
        data = f"{self.nome_album};{self.nome_banda};{self.ano_lancamento[:5]}; {self.album_lancamento}\n"
        try:
            my_data = database()
            my_data.write_infile(data)            
            return True
        except Exception as e:
            return False
     
    #retorno da pesquisa
    def pesquisando(pesquisa, radio, val):
        mydb = database()
        data = []
        dados = []
        search = pesquisa
        if search == '':
            data = mydb.all_data()
        else:
            data = mydb.search_infile(search)
        for n in data:
            newdata = n.split(';')
            a = int(newdata[2])
            try:
                ano = int(val)
                if radio == 2 and ano < a:
                        dados.append((f'{newdata[0]}', f'{newdata[1]}', f'{newdata[2]}', f'{newdata[3]}'))
                elif radio == 1 and ano == a:
                        dados.append((f'{newdata[0]}', f'{newdata[1]}', f'{newdata[2]}', f'{newdata[3]}'))
                elif radio == 0 and ano > a:
                        dados.append((f'{newdata[0]}', f'{newdata[1]}', f'{newdata[2]}', f'{newdata[3]}'))
            except: dados.append((f'{newdata[0]}', f'{newdata[1]}', f'{newdata[2]}', f'{newdata[3]}'))
        return dados
