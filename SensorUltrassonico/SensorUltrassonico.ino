//Biblioteca do sensor ultrassonico
#include <Ultrasonic.h>
 
//Define os pinos para o trigger e echo
#define PINO_TRIGGER_SENSOR_ULTRASSONICO 4
#define PINO_ECHO_SENSOR_ULTRASSONICO 5
 
//inicializacao do sensor nos pinos definidos
Ultrasonic ultrasonic(PINO_TRIGGER_SENSOR_ULTRASSONICO, PINO_ECHO_SENSOR_ULTRASSONICO);
 
void setup(){
  Serial.begin(9600);
  Serial.println("=================================================");
  Serial.println("===== INICIANDO LEITURA DOS DADOS DO SENSOR =====");
}
 
void loop() {
  float dist_cm_sensor_ultrassonico = ultrasonic.convert(ultrasonic.timing(), Ultrasonic::CM);
 
  Serial.print("Distancia: ");
  Serial.print(dist_cm_sensor_ultrassonico);
  Serial.println("cm");
  delay(500);
}