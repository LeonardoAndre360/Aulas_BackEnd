from kafka import KafkaProducer
# KafkaProducer: Cria um produtor Kafka que se conecta ao servidor Kafka especificado em bootstrap_servers.

# Criação de um produtor Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')


# Envio de uma mensagem para o tópico 'livros'
producer.send('livros', b'Novo livro adicionado')
# producer.send: Envia uma mensagem codificada em bytes para o tópico 'livros'. Neste exemplo, a mensagem é 'Novo livro adicionado'.


# Fechamento do produtor
producer.close()
# producer.close: Fecha o produtor para liberar recursos após o envio da mensagem.