//Declaracao da variavel que armazena o pino conectado ao rele
int PINO_RELE = 8;

void setup() {
  
  //Inicializacao do monitor serial
  Serial.begin(9600);
  Serial.println("Iniciando...");

  //Configura o pino conectado ao rele como uma saida e com o nivel logico baixo inicial
  pinMode(PINO_RELE, OUTPUT);
  digitalWrite(PINO_RELE, LOW);
  Serial.println("Pino RELE OFF...");
}

void loop() {
  //Aciona a bomba pelo tempo determinado na variavel
  digitalWrite(PINO_RELE, HIGH);
  Serial.println("Bomba ligada");
  delay(5000);
  digitalWrite(PINO_RELE, LOW);
  Serial.println("Bomba desligada");
}
