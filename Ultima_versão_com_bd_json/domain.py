from pickle import TRUE
from dbjson import database


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
        data = {
            "Nome": self.nome_album,
            "Banda": self.nome_banda,
            "Ano": self.ano_lancamento[:5], 
            "Lancamento" : self.album_lancamento
        }
        print(data)
        try:
            my_data = database()
            my_data.write_infile(data)            
            return True
        except Exception as e:
            print(e)
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

            try:
                ano = int(val)
                a = int(n['Ano'])
                if radio == 2:
                    if ano < a:
                        dados.append((f'{n["Nome"]}', f'{n["Banda"]}', f'{n["Ano"]}', f'{n["Lancamento"]}'))
                    
                elif radio == 1:
                    if ano == a:
                        dados.append((f'{n["Nome"]}', f'{n["Banda"]}', f'{n["Ano"]}', f'{n["Lancamento"]}'))
                    
                elif radio == 0:
                    if ano > a:
                        dados.append((f'{n["Nome"]}', f'{n["Banda"]}', f'{n["Ano"]}', f'{n["Lancamento"]}'))
            except: dados.append((f'{n["Nome"]}', f'{n["Banda"]}', f'{n["Ano"]}', f'{n["Lancamento"]}'))

        return dados

    
    
