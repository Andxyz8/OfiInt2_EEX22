from flask import Flask, request
from time import sleep
from gpiozero import DigitalOutputDevice
import I2C_LCD_driver


# FORMATO DO JSON RECEBIDO
# json_recebido = {
#     'drink1':'0',
#     'drink2':'500',
#     'drink3':'0'
# }

# As mangueiras marcadas são as que puxam o líquido

###################### INICIALIZAÇÃO ######################


###################### ###################### ###################### 
def tempo_despejamento(tempo, bomba, linha2):
    for contador in range(int(tempo)):
        progresso = round((contador+1)/tempo * 100, 2)
        LCD.lcd_clear()
        LCD.lcd_display_string(bomba+": - "+str(progresso)+"%", 1, 0)
        LCD.lcd_display_string(linha2, 2, 0)
        sleep(1)


def despeja_bebida_1(quantidade_ml):
    bomba = "P1"
    linha2 = "Bebida 1: " + str(quantidade_ml)
    
    LCD.lcd_clear()
    LCD.lcd_display_string(bomba, 1, 1)
    LCD.lcd_display_string(linha2, 2, 1)
    
    rele_peristaltica_1_bebida_1.on()
    
    tempo = (quantidade_ml / 100) * 165
    tempo_despejamento(tempo, bomba, linha2)
    
    rele_peristaltica_1_bebida_1.off()
    
    
def despeja_bebida_2(quantidade_ml):
    bomba = "P2"
    linha2 = "Bebida 2: " + str(quantidade_ml)
    
    LCD.lcd_clear()
    LCD.lcd_display_string(bomba, 1, 1)
    LCD.lcd_display_string(linha2, 2, 1)
    
    rele_peristaltica_2_bebida_2.on()
    
    tempo = (quantidade_ml / 100) * 165
    tempo_despejamento(tempo, bomba, linha2)
    
    rele_peristaltica_2_bebida_2.off()
    
    
def despeja_bebida_3(quantidade_ml):
    bomba = "Mini"
    linha2 = "Bebida 3: "+str(quantidade_ml)
    
    LCD.lcd_clear()
    LCD.lcd_display_string(bomba, 1, 1)
    LCD.lcd_display_string(linha2, 2, 1)
    
    rele_mini_bomba_bebida_3.on()
    
    tempo = (quantidade_ml / 100) * 3
    tempo_despejamento(tempo, bomba, linha2)
    
    rele_mini_bomba_bebida_3.off()


def prepara_pedido(lista_pedidos):
    pedido = lista_pedidos[0]
    print(pedido)
    if(int(pedido['drink1']) > 0):
        despeja_bebida_1(int(pedido['drink1']))

    if(int(pedido['drink2']) > 0):
        despeja_bebida_2(int(pedido['drink2']))

    if(int(pedido['drink3']) > 0):
        despeja_bebida_3(int(pedido['drink3']))
        
    LCD.lcd_clear()
    LCD.lcd_display_string("Pedido pronto!", 1, 0)
    LCD.lcd_display_string("Retire o copo!", 2, 0)

    sleep(5)

    LCD.lcd_clear()
    LCD.lcd_display_string("  Aguardando  ", 1, 1)
    LCD.lcd_display_string(" novo pedido! ", 2, 1)
    
    return lista_pedidos.remove(pedido)


lista_pedidos = []

LCD = I2C_LCD_driver.lcd()

rele_peristaltica_1_bebida_1 = DigitalOutputDevice(
        pin=27,
        active_high=False, 
        initial_value=False
    )

rele_peristaltica_2_bebida_2 = DigitalOutputDevice(
        pin=22,
        active_high=False, 
        initial_value=False
    )

rele_mini_bomba_bebida_3 = DigitalOutputDevice(
        pin=17,
        active_high=False, 
        initial_value=False
    )


app = Flask(__name__)
@app.route('/helloworld', methods = ['POST', 'GET', 'PUT'])
def hello_world():
    
    LCD.lcd_clear()
    LCD.lcd_display_string("Iniciando pedido", 1, 0)
    sleep(3)
    
    json_pedido = request.get_json()
    lista_pedidos = []
    lista_pedidos.append(json_pedido)
    
    if(len(lista_pedidos) > 0):
        lista_pedidos = prepara_pedido(lista_pedidos)
    
    return '0'


if (__name__ == '__main__'):
    app.run(debug=True, port=5000, host='0.0.0.0')
    
