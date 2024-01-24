//Include Libraries
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

//create an RF24 object
RF24 radio(9, 8);  // CE, CSN

//address through which two modules communicate.
const byte address[6] = "00001";

void setup()
{
  radio.begin();
  Serial.begin(9600);
  
  //set the address
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  //Set module as transmitter
  radio.stopListening();
}
void loop()
{
  //Send message to receiver
  const char text[] = "Hello World";
  Serial.println("main toh sirf junnu ke liye kaam kar raha hoon");
  radio.write(&text, sizeof(text));
  
  delay(500);
}