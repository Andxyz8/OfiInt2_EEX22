from threading import Thread
from time import sleep
from componentes import Componentes

class Preparador(Thread):
    def __init__(self) -> None:
        super().__init__()

        self.componentes = Componentes()
        self.fila_pedidos = []
        self.esta_ligado = False

    def run(self):
        """Processo principal que prepara os pedidos na lista de pedidos."""

        while(True):
            if(len(self.fila_pedidos) > 0):
                # IMPLEMENTAR FUNCIONALIDADE DO POSICIONAMENTO DO COPO
                # while(dist > 15):
                #   sleep(1)

                
                print(f'Lista de pedidos atual: {self.fila_pedidos}')
                print('-'*50)
                print("Iniciando pedido", 1, 0)

                self.componentes.lcd_iniciando_pedido()

                sleep(1)

                self.prepara_pedido_fila(self.fila_pedidos[0])

                print('Pedido finalizado!')
                self.componentes.lcd_pedido_finalizado()

                self.retira_pedido_finalizado()

            else:
                print(self.fila_pedidos)
                print('Aguardando novo pedido!')

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


    def inclui_novo_pedido(self, novo_pedido):
        """Inclui um novo pedido na lista de pedidos.

        Args:
            novo_pedido (dict): pedido a ser incluído na lista de pedidos.
        """

        self.fila_pedidos.append(novo_pedido)


    def retira_pedido_finalizado(self):
        """Faz os tratamentos necessários com relação ao pedido que foi finalizado.
        """
        self.fila_pedidos = self.fila_pedidos[1:]


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