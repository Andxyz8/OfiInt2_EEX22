from threading import Thread
from time import sleep
from componentes import Componentes

class Preparador(Thread):
    def __init__(self) -> None:
        super().__init__()

        self.componentes = Componentes()
        self.fila_pedidos = []
        self.fila_ip = []
        self.esta_ligado = False
        self.confirmado = False
        self.cancelado = False

    def run(self):
        """Processo principal que prepara os pedidos na lista de pedidos."""

        while(True):
            if(len(self.fila_pedidos) > 0):
                # IMPLEMENTAR FUNCIONALIDADE DO POSICIONAMENTO DO COPO (COLOCAR)
                # while(dist > 15):
                #   sleep(1)

                if(self.confirmado):
                    print(f'Lista de pedidos atual: {self.fila_pedidos}')
                    print('-'*50)

                    self.componentes.lcd_iniciando_pedido()

                    sleep(3)

                    self.prepara_pedido_fila(self.fila_pedidos[0])
                    
                    self.componentes.lcd_pedido_finalizado()
                    
                    sleep(3)
                    
                    # IMPLEMENTAR FUNCIONALIDADE DO POSICIONAMENTO DO COPO (RETIRAR)
                    # while(dist > 15):
                    #   sleep(1)
                    self.confirmado = False
                
                    self.retira_pedido_finalizado_fila()
                    
                elif (self.cancelado):
                    self.cancelado = False
                    self.retira_pedido_finalizado_fila()
                    self.componentes.lcd_pedido_cancelado()
                    sleep(3)
                    
                else:
                    self.componentes.lcd_aguardando_confirmacao()
                    sleep(3)

            else:
                print(self.fila_pedidos)

                self.componentes.lcd_aguardando_novo_pedido()

                sleep(1)


    def prepara_pedido_fila(self, pedido):
        """Aciona as bombas responsáveis por despejar as bebidas.

        Args:
            pedido (dict): dicionário que contém o pedido preparado no momento.
        """

        if(int(pedido['drink1']) > 0):
            self.componentes.peristaltica_1_despeja_bebida_1(int(pedido['drink1']))

        if(int(pedido['drink2']) > 0):
            self.componentes.peristaltica_2_despeja_bebida_2(int(pedido['drink2']))

        if(int(pedido['drink3']) > 0):
            self.componentes.mini_bomba_despeja_bebida_3(int(pedido['drink3']))


    def inclui_novo_pedido_fila(self, novo_pedido, endereco_ip):
        """Inclui um novo pedido na lista de pedidos.

        Args:
            novo_pedido (dict): pedido a ser incluído na lista de pedidos.
        """

        self.fila_pedidos.append(novo_pedido)
        self.fila_ip.append(endereco_ip)


    def retira_pedido_finalizado_fila(self):
        """Faz os tratamentos necessários com relação ao pedido que foi finalizado.
        """
        self.fila_pedidos = self.fila_pedidos[1:]
        self.fila_ip = self.fila_ip[1:]


    def inicia_preparador(self):
        """Dispara o processo que faz o preparo dos pedidos.
        """
        self.esta_ligado = True
        self.componentes.lcd_inicializa_display()
        self.start()


    def get_esta_ligado(self):
        """Retorna o estado do processo preparador dos pedidos.

        Returns:
            bool: True se o processo já foi iniciado, False caso contrário.
        """
        return self.esta_ligado

    def get_confirmado(self):
        """Retorna se o primeiro pedido da fila foi confirmado.
        
        Returns:
            bool: True se o pedido já foi confirmado, False caso contrário.
        """
        return self.confirmado
    
    def confirma_pedido(self) -> None:
        """Confirma o preparo do primeiro pedido da flia
        
        """
        self.confirmado = True
        
    def cancela_pedido(self) -> None:
        """Cancela o preparo do primeiro pedido da fila
        """
        self.cancelado = True