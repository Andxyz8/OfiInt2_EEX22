from flask import Flask, request
from preparador import Preparador


app = Flask(__name__)
@app.route('/FastDrink', methods = ['POST', 'GET', 'PUT'])
def recebe_pedido():
    if(not preparador_pedidos.get_esta_ligado()):
        preparador_pedidos.inicia_preparador()

    # Escreve o ip do dispositivo que fez a requisição
    pedido = request.get_json()
    
    pedido['ip'] = request.access_route[0]
    preparador_pedidos.inclui_novo_pedido_fila(pedido)
    
    return '0'


if (__name__ == '__main__'):
    preparador_pedidos = Preparador()
    app.run(debug=True, port=5000, host='0.0.0.0')
    
