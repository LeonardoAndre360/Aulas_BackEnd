# Orquestração de Ambiente Kafka local

Este repositório contém a infraestrutura básica para rodar um ambiente de mensageria local utilizando o Apache Kafka. O projeto foi desenvolvido como parte do módulo de Filas de Mensagens e Processamento Assíncrono do curso de Back-end Python da EBAC.

## 🛠️ Arquitetura do Ambiente

A infraestrutura é orquestrada via `docker-compose.yml` e sobe três serviços interligados:

1. **ZooKeeper (`confluentinc/cp-zookeeper:7.4.3`):** Serviço centralizado de coordenação e sincronização exigido pelo Kafka.
2. **Apache Kafka (`confluentinc/cp-kafka:7.4.3`):** A plataforma de streaming de eventos distribuída (Broker).
3. **Kafka UI (`provectuslabs/kafka-ui:latest`):** Interface visual web para facilitar o monitoramento de clusters, tópicos e mensagens sem a necessidade de comandos de terminal.

## 🚀 Como executar o projeto

Certifique-se de ter o **Docker** e o **Docker Compose** (ou Podman) instalados na sua máquina.

1. Clone este repositório ou acesse a pasta raiz do projeto.
2. Abra o terminal e execute o comando abaixo para construir e iniciar os contêineres em background:
   ```bash
   docker-compose up -d --build
```
   *(Nota: Caso utilize o Podman, substitua por `podman-compose up -d --build`).*

3. Aguarde cerca de 10 a 15 segundos para a inicialização completa do Kafka.
4. Acesse a interface de monitoramento no seu navegador:
   **[http://localhost:8080](http://localhost:8080)**

# Como encerrar o ambiente

Para parar e remover os contêineres, redes e volumes criados por este projeto, execute:

```bash
docker-compose down
```