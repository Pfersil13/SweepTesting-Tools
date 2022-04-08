
#include "AudioTeensy.h"
#include "AudioIn.h"

// Remember which mode we're doing
int mode = -2;  // 0=stopped, 1=recording, 2=playing
const int Button_1 = 32;
const int Button_2 = 33;
bool state = 0;
bool pulseState = 1;

void StartCycle_ISR(){
  pulseState = 0;
}
void Gain_ISR(){
  state = 0;
}

void setup() {
  setupAudio();
  setUpSD();
  pinMode(Button_1, INPUT_PULLUP);
  pinMode(Button_2, INPUT_PULLUP);

  Serial.begin(115200);
  Serial6.begin(460800 , SERIAL_8N1 );  //Serial for bluetooth

  //Interruptions
  attachInterrupt(digitalPinToInterrupt(Button_1), StartCycle_ISR, RISING); 
  attachInterrupt(digitalPinToInterrupt(Button_2), Gain_ISR, RISING);
  
  
}

void loop() {
if(pulseState == 0){
startCycle(3);
}
  pulseState = 1;

}
