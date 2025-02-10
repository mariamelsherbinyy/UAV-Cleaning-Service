const int pumpPin = 5;  // GPIO pin connected to the water pump

void setup() {
  pinMode(pumpPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Turn on the water pump
  digitalWrite(pumpPin, HIGH);
  Serial.println("Pump ON");
  delay(5000);  // Run the pump for 5 seconds

  // Turn off the water pump
  digitalWrite(pumpPin, LOW);
  Serial.println("Pump OFF");
  delay(5000);  // Wait for 5 seconds before turning it on again
}