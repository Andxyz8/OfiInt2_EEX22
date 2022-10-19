#include <Wire.h> //Biblioteca utilizada gerenciar a comunicação entre dispositicos através do protocolo I2C
#include <LiquidCrystal_I2C.h> //Biblioteca controlar display 16x2 através do I2C

#define COLUNAS_LCD 16 //Define o número de colunas do display utilizado
#define LINHAS_LCD 2 //Define o número de linhas do display utilizado
#define ENDERECO_I2C  0x27 //Define o endereço do display

LiquidCrystal_I2C DisplayLCD(ENDERECO_I2C, COLUNAS_LCD, LINHAS_LCD); //Cria o objeto lcd passando como parâmetros o endereço, o nº de colunas e o nº de linhas


void setup() {
  DisplayLCD.init(); //Inicializa o display
  DisplayLCD.clear(); //Limpa a tela do display
  DisplayLCD.backlight(); //Luz de fundo do display

  DisplayLCD.setCursor(0, 0);
  DisplayLCD.print("   FAST DRINK   ");
  DisplayLCD.setCursor(0, 1);
  DisplayLCD.print("    STATION!    ");
}

void loop() {
  delay(500);
  DisplayLCD.noDisplay(); // Desliga a exibicao no display
  delay(500);
  DisplayLCD.display();// Liga a exibicao no display
}