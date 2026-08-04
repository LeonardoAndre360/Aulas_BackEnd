from sqlalchemy import create_engine, Column, Integer, String
# create_engine: Cria uma conexão com o banco de dados SQLite, especificando o arquivo example.db como o banco de dados.
from sqlalchemy.ext.declarative import declarative_base
# declarative_base: Cria uma classe base para definir estruturas de tabelas no banco de dados.
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados SQLite
engine = create_engine('sqlite:///example.db')
Base = declarative_base()

# Definição da classe User como uma tabela no banco de dados
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
# User: Define uma classe que representa a tabela users no banco de dados, com colunas id, name e age.

# Criação da tabela no banco de dados
Base.metadata.create_all(engine)
# create_all: Cria a tabela users no banco de dados, se ela ainda não existir.

# Criação de uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()
# sessionmaker: Cria uma fábrica de sessões para interagir com o banco de dados.

# Exemplo de inserção de um novo usuário
new_user = User(name='Alice', age=30)
session.add(new_user)
# session.add: Adiciona um novo usuário à sessão para ser inserido no banco de dados.
session.commit()
# session.commit: Confirma as alterações feitas na sessão, persistindo-as no banco de dados.

# Consulta de todos os usuários
users = session.query(User).all()
for user in users:
    print(user.name, user.age)
# session.query: Consulta todos os usuários na tabela users e imprime seus nomes e idades.

# Fechamento da sessão
session.close()
# session.close: Fecha a sessão, liberando recursos.