import asyncio

async def process_order(order_id):
# process_order: Função assíncrona que simula o processamento de um pedido. 
# Utiliza await asyncio.sleep(2) para simular um atraso no processamento.
    print(f"Processing order {order_id}")
    await asyncio.sleep(2)  # Simulate a delay in processing
    print(f"Order {order_id} processed")

async def main():
# main: Função principal que cria uma lista de tarefas para processar múltiplos pedidos simultaneamente usando asyncio.gather.
    orders = [1, 2, 3, 4, 5]
    tasks = [process_order(order) for order in orders]
    await asyncio.gather(*tasks)

asyncio.run(main())
# asyncio.run(main()): Executa a função main, iniciando o loop de eventos assíncrono.




# Este exemplo demonstra como a comunicação assíncrona pode ser usada para processar múltiplas tarefas simultaneamente, melhorando a eficiência do sistema.