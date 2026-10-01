import redis

# Conectar ao Redis
r = redis.Redis(host='localhost', port=6379, db=0)
# redis.Redis: Cria uma conexão com o servidor Redis especificando o host, porta e banco de dados.

# Armazenar um valor no Redis com TTL de 60 segundos
r.set('chave_exemplo', 'valor_exemplo', ex=60)
# r.set: Armazena um valor no Redis com uma chave específica e define um TTL de 60 segundos.

# Recuperar o valor armazenado
valor = r.get('chave_exemplo')
print(valor.decode('utf-8'))  # Saída: valor_exemplo
# r.get: Recupera o valor armazenado usando a chave especificada.

# Verificar o tempo restante de TTL
ttl = r.ttl('chave_exemplo')
print(f'Tempo restante de TTL: {ttl} segundos')
# r.ttl: Retorna o tempo restante de TTL para a chave especificada, 
# permitindo monitorar quando o valor será removido automaticamente.