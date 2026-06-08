import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('example.db')
# sqlite3.connect: Conecta ao banco de dados SQLite 
# chamado 'example.db'. Se o arquivo não existir, ele será criado.

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')
# cursor.execute: Executa comandos SQL. 
# Primeiro, cria uma tabela chamada 'users' com colunas para 'id', 'name' e 'email'. 
# Em seguida, insere um novo usuário na tabela.

# Inserir dados na tabela
cursor.execute('''
INSERT INTO users (name, email) VALUES (?, ?)
''', ('Alice', 'alice@example.com'))

# Salvar (commit) as alterações
conn.commit()
# conn.commit: Salva as alterações feitas no banco de dados.

# Fechar a conexão
conn.close()
# conn.close: Fecha a conexão com o banco de dados para liberar recursos.