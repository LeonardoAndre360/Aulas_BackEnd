from flask import Flask, jsonify, request

app = Flask(__name__)
# Flask: Um micro framework para Python usado para criar aplicações web. 
# Aqui, ele é usado para criar uma API simples 

# Dados de exemplo
items = [
    {"id": 1, "name": "item 1"},
    {"id": 1, "name": "item 2"}
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)
# get_items: Função que responde ao método GET na roda /items, 
# retornando uma lista de itens em formato JSON

@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get.json()
    items.append(new_item)
    return jsonify(new_item), 201
# add_item: Função que responde ao método POST na rota /items. 
# Ela adiciona um novo item à lista de itens e retorna o item adicionado com o código de status 201(Created).

if __name__ == '__main__':
    app.run(debug=True)
# app.run(debug=True): Inicia o servidor Flask em modo de depuração, 
# permitindo que a aplicação seja executada localmente para testes.