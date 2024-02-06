const int pin1 = 0;
const int pin2 = 1;

void setup()
{
  Serial.begin(115200);
}

void loop()
{

  float voltage1, temp1, voltage2, temp2;
  // Gets voltages and turns them into temps in C
  voltage1 = getVoltage(pin1);
  voltage2 = getVoltage(pin2);

  temp1 = (voltage1 - 0.5) * 100.0;
  temp2 = (voltage2 - 0.5) * 100.0;
  // Prints temps to serial port
  Serial.print(temp1);
  Serial.print(", ");
  Serial.println(temp2);
  delay(1000);
}

float getVoltage(int pin)
{

  return (analogRead(pin) * 5 / 1024.0);
}
