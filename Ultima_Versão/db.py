
class database:

  def __init__(self):
    self.file_name = 'data_file_base.txt'
  
  #salva os dados
  def write_infile(self, data):
    arquivo = open(self.file_name,'a')
    arquivo.write(data)
    arquivo.close()

  #pesquisa os dados pesquisados
  def search_infile(self, search):
    lista = []
    with open(self.file_name) as f:
        datafile = f.readlines()
    for line in datafile:
        if search in line:
          lista.append(line)
    return lista
      
  
  #retorna todos os dados
  def all_data(self):
    lista=[]
    with open(self.file_name) as f:
        datafile = f.readlines()
    for line in datafile:
        lista.append(line)
    return lista
