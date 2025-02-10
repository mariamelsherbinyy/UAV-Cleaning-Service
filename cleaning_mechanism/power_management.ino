const int batteryPin = A0;  // Analog pin connected to the battery voltage divider

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Read the battery voltage
  int sensorValue = analogRead(batteryPin);
  float voltage = sensorValue * (5.0 / 1023.0) * 2;  // Assuming a voltage divider with 2:1 ratio

  // Print the battery voltage
  Serial.print("Battery Voltage: ");
  Serial.println(voltage);

  delay(1000);  // Wait for 1 second
}