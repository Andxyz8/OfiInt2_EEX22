//sda -> branco

#include <Wire.h> //Biblioteca utilizada gerenciar a comunicação entre dispositicos através do protocolo I2C
#include <LiquidCrystal_I2C.h> //Biblioteca controlar display 16x2 através do I2C

#define PINO_RELE_MINI_BOMBA 7
#define PINO_RELE_PERISTALTICA_1 8
#define PINO_RELE_PERISTALTICA_2 9
#define COLUNAS_LCD 16 //Define o número de colunas do display utilizado
#define LINHAS_LCD 2 //Define o número de linhas do display utilizado
#define ENDERECO_I2C  0x27 //Define o endereço do display

LiquidCrystal_I2C DisplayLCD(ENDERECO_I2C, COLUNAS_LCD, LINHAS_LCD); //Cria o objeto lcd passando como parâmetros o endereço, o nº de colunas e o nº de linhas


void setup() {
  Serial.begin(9600);
  Serial.println("Iniciando...");

  DisplayLCD.init(); //Inicializa o display
  DisplayLCD.clear(); //Limpa a tela do display
  DisplayLCD.backlight(); //Luz de fundo do display

  DisplayLCD.setCursor(0, 0);
  DisplayLCD.print("   FAST DRINK   ");
  DisplayLCD.setCursor(0, 1);
  DisplayLCD.print("    STATION!    ");

  pinMode(PINO_RELE_MINI_BOMBA, OUTPUT);
  pinMode(PINO_RELE_PERISTALTICA_1, OUTPUT);
  pinMode(PINO_RELE_PERISTALTICA_2, OUTPUT);
  digitalWrite(PINO_RELE_MINI_BOMBA, LOW);
  digitalWrite(PINO_RELE_PERISTALTICA_1, LOW);
  digitalWrite(PINO_RELE_PERISTALTICA_2, LOW);
}

void loop() {
  delay(2500);
  DisplayLCD.display();// Liga a exibicao no display

  digitalWrite(PINO_RELE_MINI_BOMBA, LOW);
  digitalWrite(PINO_RELE_PERISTALTICA_1, HIGH);
  digitalWrite(PINO_RELE_PERISTALTICA_2, HIGH);
  Serial.println("MiniBomba ligada");
  delay(5000);
  digitalWrite(PINO_RELE_MINI_BOMBA, HIGH);
  digitalWrite(PINO_RELE_PERISTALTICA_1, HIGH);
  digitalWrite(PINO_RELE_PERISTALTICA_2, HIGH);
  Serial.println("MiniBomba desligada");

  digitalWrite(PINO_RELE_MINI_BOMBA, HIGH);
  digitalWrite(PINO_RELE_PERISTALTICA_1, LOW);
  digitalWrite(PINO_RELE_PERISTALTICA_2, HIGH);
  Serial.println("Peristaltica 1 ligada");
  delay(5000);
  digitalWrite(PINO_RELE_MINI_BOMBA, HIGH);
  digitalWrite(PINO_RELE_PERISTALTICA_1, HIGH);
  digitalWrite(PINO_RELE_PERISTALTICA_2, HIGH);
  Serial.println("Peristaltica 1 desligada");

  digitalWrite(PINO_RELE_MINI_BOMBA, HIGH);
  digitalWrite(PINO_RELE_PERISTALTICA_1, HIGH);
  digitalWrite(PINO_RELE_PERISTALTICA_2, LOW);
  Serial.println("Peristaltica 2 ligada");
  delay(5000);
  digitalWrite(PINO_RELE_MINI_BOMBA, HIGH);
  digitalWrite(PINO_RELE_PERISTALTICA_1, HIGH);
  digitalWrite(PINO_RELE_PERISTALTICA_2, HIGH);
  Serial.println("Peristaltica 2 desligada");
  
  delay(2500);
  DisplayLCD.noDisplay(); // Desliga a exibicao no display
}