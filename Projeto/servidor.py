from flask import Flask, request
from preparador import Preparador


app = Flask(__name__)
@app.route('/FastDrink', methods = ['POST', 'GET', 'PUT'])
def hello_world():
    if(not preparador_pedidos.get_esta_ligado()):
        preparador_pedidos.inicia_preparador()

    # Escreve o ip do dispositivo que fez a requisição
    # print(request.access_route)
    preparador_pedidos.inclui_novo_pedido_fila(request.get_json(), request.remote_addr)
    
    return '0'

@app.route('/verificafila')
def verifica_fila():
    if (request.remote_addr == preparador_pedidos.fila_ip[0]):
        return app.make_response("aguardar" if preparador_pedidos.get_confirmado() else "confirmar")
    else:
        return app.make_response("aguardar")
    
@app.route('/confirmapedido')
def confirma_pedido():
    if (request.remote_addr == preparador_pedidos.fila_ip[0]):
        preparador_pedidos.confirma_pedido()
        return app.make_response("confirmado")
    return app.make_response("erro")

@app.route("/cancelapedido")
def cancela_pedido():
    if (request.remote_addr == preparador_pedidos.fila_ip[0]):
        preparador_pedidos.cancela_pedido()
        return app.make_response("cancelado")
    return app.make_response("erro")


if (__name__ == '__main__'):
    preparador_pedidos = Preparador()
    app.run(debug=True, port=5000, host='0.0.0.0')
    
