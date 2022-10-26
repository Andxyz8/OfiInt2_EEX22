/*******************************************************************************
* Projeto Dispenser de Alcool Gel (v1.0)
* 
* Codigo fonte do Kit Dispenser de Alcool em Gel 
* (https://www.robocore.net/produtos/kit-faca-voce-mesmo-dispenser-automatico-liquidos)
* 
* Assim que voce colocar sua mao abaixo do sensor ultrassonico a bomba 
* peristaltica sera acionada para despejar alcool gel, assim voce podera 
* higienizar a sua mao sem ter de tocar na garrafa.
* 
* Copyright <2022> RoboCore.
* Escrito por @LENZ (25/08/2022).
* 
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU Lesser General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version (<https://www.gnu.org/licenses/>).
*******************************************************************************/

//Adiciona a biblioteca ao codigo
#include "Ultrasonic.h"

//Declaracao dos pinos conectados ao sensor ultrassonico
const int PINO_ECHO = 13;
const int PINO_TRIGGER = 12;
const int PINO_VCC = 11;

//Cria o objeto "sensor" para a biblioteca "Ultrassonic" 
//de acordo com os pinos conectados ao "trigger" e "echo" do sensor
Ultrasonic ultrasonic(PINO_TRIGGER, PINO_ECHO);

//Declaracao da variavel que armazena o pino conectado ao rele
int PINO_RELE = 5;

//Declaracao da variavel auxiliar "mao" com o valor inicial "false"
boolean objeto_na_frente = false;

//Declaracao das variaveis auxiliares para a leitura do sensor e acionamento da bomba
int distancia = 0; //Recebe a leitura do sensor
const int DISTANCIA_MIN_ACIONAR = 10; //Distancia minima para o acionamento
const int DISTANCIA_MAX = 18; //Distancia maxima de leitura do sensor
const int TEMPO_ACIONAMENTO = 5000; //Duracao do acionamento da bomba (milissegundos)

void setup() {
  
  //Inicializacao do monitor serial
  Serial.begin(9600);
  Serial.println("Iniciando...");

  //Configura o pino conectado ao rele como uma saida e com o nivel logico baixo inicial
  pinMode(PINO_RELE, OUTPUT);
  digitalWrite(PINO_RELE, LOW);

  //Configura o pino conectado ao VCC do sensor como uma saida e com o nivel logico alto (HIGH), para ligar o sensor 
  //(so podemos fazer isso porque a corrente de consumo do sensor eh muito baixa)
  pinMode(PINO_VCC, OUTPUT);
  digitalWrite(PINO_VCC, HIGH);
  
}

void loop() {

  //Verifica se o valor retornado pela funcao "checaDistancia" eh menor que a distancia minima para acionamento, e se a variavel "objeto_na_frente" eh falsa ("false")
  if (checaDistancia() <= DISTANCIA_MIN_ACIONAR && objeto_na_frente == false) {
    delay(200); //Debounce
    if (checaDistancia() <= DISTANCIA_MIN_ACIONAR) { //Se for verdadeiro
      //Inverte o estado da variavel "objeto_na_frente" e aciona a bomba pelo tempo determinado na variavel "TEMPO_ACIONAMENTO"
      objeto_na_frente = true;
      digitalWrite(PINO_RELE, HIGH);
      Serial.println("Bomba ligada");
      delay(TEMPO_ACIONAMENTO);
      digitalWrite(PINO_RELE, LOW);
      Serial.println("Bomba desligada");
    }
  } else {
    delay(500);
    objeto_na_frente = false;
  } 
  
  delay(100); //Aguarda 100 milissegundos para nova leitura
  
}

int checaDistancia() {
  float dist_cm_sensor_ultrassonico;
  //Atribui a leitura do sensor a variavel "dist_cm_sensor_ultrassonico"
  dist_cm_sensor_ultrassonico = ultrasonic.convert(ultrasonic.timing(), Ultrasonic::CM);
  Serial.print("Distancia: ");
  Serial.print(dist_cm_sensor_ultrassonico);
  Serial.print(" cm");
  //Verifica se a leitura do sensor eh maior que a distancia de leitura maxima
  while(dist_cm_sensor_ultrassonico > DISTANCIA_MAX){ //Se for verdadeiro
    Serial.println(" -> Distancia invalida!");
    delay(200);
    //Atualiza a leitura do sensor
    dist_cm_sensor_ultrassonico = ultrasonic.convert(ultrasonic.timing(), Ultrasonic::CM);
    Serial.print("Distancia: ");
    Serial.print(dist_cm_sensor_ultrassonico);
    Serial.print(" cm");
  } //Caso contrario
  Serial.println(" -> Distancia OK!");
  delay(100);
  return dist_cm_sensor_ultrassonico; //Retorna o valor lido para o codigo
  
}