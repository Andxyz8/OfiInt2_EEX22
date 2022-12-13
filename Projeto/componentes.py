from time import sleep
from gpiozero import DigitalOutputDevice
from libs import I2C_LCD_driver

class Componentes():
    def __init__(self) -> None:
        self.LCD = I2C_LCD_driver.lcd()

        self.rele_peristaltica_1_bebida_1 = DigitalOutputDevice(
                pin=27,
                active_high=False, 
                initial_value=False
            )

        self.rele_peristaltica_2_bebida_2 = DigitalOutputDevice(
                pin=22,
                active_high=False, 
                initial_value=False
            )

        self.rele_mini_bomba_bebida_3 = DigitalOutputDevice(
                pin=17,
                active_high=False, 
                initial_value=False
            )

# ===================== MÉTODOS RELACIONADOS AO LCD =====================
    def lcd_inicializa_display(self) -> None:
        self.LCD.lcd_display_string(" ", 1, 0)
        self.LCD.lcd_display_string(" ", 2, 0)

    def lcd_limpa_display(self) -> None:
        self.LCD.lcd_clear()

    
    def lcd_iniciando_pedido(self) -> None:
        self.lcd_limpa_display()
        self.LCD.lcd_display_string("Iniciando pedido", 1, 0)
        self.LCD.lcd_display_string("Posicione o copo", 2, 0)
    

    def lcd_pedido_finalizado(self) -> None:
        self.lcd_limpa_display()
        self.LCD.lcd_display_string("Pedido pronto!", 1, 0)
        self.LCD.lcd_display_string("Retire o copo!", 2, 0)
    

    def lcd_aguardando_novo_pedido(self) -> None:
        self.lcd_limpa_display()
        self.LCD.lcd_display_string("  Aguardando  ", 1, 1)
        self.LCD.lcd_display_string(" novo pedido! ", 2, 1)
        
        
    def lcd_aguardando_confirmacao(self) -> None:
        self.lcd_limpa_display()
        self.LCD.lcd_display_string("  Aguardando  ", 1, 1)
        self.LCD.lcd_display_string("confirmacao...", 2, 1)
        
        
    def lcd_pedido_cancelado(self) -> None:
        self.lcd_limpa_display()
        self.LCD.lcd_display_string("    Pedido    ", 1, 1)
        self.LCD.lcd_display_string("  cancelado!  ", 2, 1)


    def lcd_texto_bomba(self, status_progresso, primeira_linha_lcd, segunda_linha_lcd):
        self.lcd_limpa_display()
        self.LCD.lcd_display_string(primeira_linha_lcd+": "+str(status_progresso)+"%", 1, 1)
        self.LCD.lcd_display_string(segunda_linha_lcd, 2, 1)

# ===================== MÉTODOS RELACIONADOS AO LCD =====================

# ===================== MÉTODOS RELACIONADOS ÀS BOMBAS =====================
    def tempo_acionamento_bomba(self, tempo, lcd_linha_1, lcd_linha_2) -> None:
         for contador in range(int(tempo)):
            status_progresso = round((contador+1)/tempo * 100, 2)
            self.lcd_texto_bomba(status_progresso, lcd_linha_1, lcd_linha_2+"ml")
            sleep(1)


    def peristaltica_1_despeja_bebida_1(self, quantidade_ml) -> None:
        lcd_linha_1 = "P1"
        lcd_linha_2 = "Bebida 1: " + str(quantidade_ml)

        self.rele_peristaltica_1_bebida_1.on()

        tempo = (quantidade_ml / 100) * 165
        self.tempo_acionamento_bomba(tempo, lcd_linha_1, lcd_linha_2)

        self.rele_peristaltica_1_bebida_1.off()


    def peristaltica_2_despeja_bebida_2(self, quantidade_ml) -> None:
        lcd_linha_1 = "P2"
        lcd_linha_2 = "Bebida 2: " + str(quantidade_ml)

        self.rele_peristaltica_2_bebida_2.on()

        tempo = (quantidade_ml / 100) * 165
        self.tempo_acionamento_bomba(tempo, lcd_linha_1, lcd_linha_2)

        self.rele_peristaltica_2_bebida_2.off()


    def mini_bomba_despeja_bebida_3(self, quantidade_ml) -> None:
        lcd_linha_1 = "Mini"
        lcd_linha_2 = "Bebida 3: "+str(quantidade_ml)

        self.rele_mini_bomba_bebida_3.on()

        tempo = (quantidade_ml / 100) * 3
        self.tempo_acionamento_bomba(tempo, lcd_linha_1, lcd_linha_2)

        self.rele_mini_bomba_bebida_3.off()
# ===================== MÉTODOS RELACIONADOS ÀS BOMBAS =====================
