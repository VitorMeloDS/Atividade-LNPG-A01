import json

class database:

  def __init__(self):
    self.file_name = 'data_file_base.json'
  
  #Adicionando dados
  def write_infile(self, data):
    with open(self.file_name, 'r') as json_file:                
      oldData = json.load(json_file)
    with open(self.file_name, 'w') as json_file:        
      oldData.append(data)
      jsoned_data = json.dumps(oldData, indent=True)
      json_file.write(jsoned_data)

  #Pesquisa os dados pesquisados
  def search_infile(self, search):
    lista=[]
    with open(self.file_name, 'r') as json_file:                
      oldData = json.load(json_file)
    for cadastro in oldData:
        if search.lower() in cadastro['Banda'].lower() or search.lower() in cadastro['Nome'].lower():
          lista.append(cadastro)
    return lista
      
  #Entregando todos os dados caso não seja pesquisado nada
  def all_data(self):
    with open(self.file_name, 'r') as f:
      return json.load(f)
