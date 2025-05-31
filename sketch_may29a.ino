const int pinSensor = A0;
const int pinLED = 8;
int nilaiGas;
int gasSebelumnya = -1;
const int ambangBahaya = 400;

void setup() {
  Serial.begin(9600);
  pinMode(pinLED, OUTPUT);
}

void loop() {
  nilaiGas = analogRead(pinSensor);

  // Nyalakan LED jika gas melebihi ambang bahaya
  if (nilaiGas > ambangBahaya) {
    digitalWrite(pinLED, HIGH);
  } else {
    digitalWrite(pinLED, LOW);
  }

  // Kirim data hanya jika ada perubahan signifikan
  if (abs(nilaiGas - gasSebelumnya) >= 10) {
    Serial.println(nilaiGas);
    gasSebelumnya = nilaiGas;
  }

  delay(1000);
}
