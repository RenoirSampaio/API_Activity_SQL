from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
  pessoa = Pessoas(nome='Renoir', idade=50)
  print(pessoa)
  pessoa.save()

# Consulta dados na tabela pessoa
def consulta_pessoas():
  pessoas = Pessoas.query.all()
  print(pessoas)
  pessoa = Pessoas.query.filter_by(nome='Pedro').first()
  print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
  pessoa = Pessoas.query.filter_by(nome='Renoir').first()
  pessoa.nome = 'Sampaio'
  pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
  pessoa = Pessoas.query.filter_by(nome='Renoir').first()
  pessoa.delete()

if __name__ == '__main__':
  # insere_pessoas()
  # altera_pessoa()
  exclui_pessoa()
  consulta_pessoas()
