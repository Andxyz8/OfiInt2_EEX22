from flask import Flask, request
from preparador import Preparador


app = Flask(__name__)
@app.route('/helloworld', methods = ['POST', 'GET', 'PUT'])
def hello_world():
    if(not preparador_pedidos.get_esta_ligado()):
        preparador_pedidos.inicia_preparador()

    # Escreve o ip do dispositivo que fez a requisição
    # print(request.access_route)
    preparador_pedidos.inclui_novo_pedido(request.get_json())
    
    return '0'


if (__name__ == '__main__'):
    preparador_pedidos = Preparador()
    app.run(debug=True, port=5000, host='0.0.0.0')
    
