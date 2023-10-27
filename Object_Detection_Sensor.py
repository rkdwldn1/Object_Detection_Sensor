# 학교에서 한 프로젝트 - 라즈베리파이를 이용한 물체 충돌 감지 센서(라즈베리파이 환경에서 진행)
include <wiringPi.h>
include <softTone.h>
include <stdio.h>

define TRIG_PIN 0
define ECHO_PIN 1
define LED1_PIN 5
define LED2_PIN 4
define BUZZER_PIN 2

void buzzerOn(){
    softToneWrite(BUZZER_PIN,500);
}

void buzzerOff(){
    softToneWrite(BUZZER_PIN,0);
}

int main(){

    if (wiringPiSetup() == -1){
        printf("wiringPi setup failed.\n");
        return 1;
    }

    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
    pinMode(LED1_PIN, OUTPUT);
    pinMode(LED2_PIN, OUTPUT);
    softToneCreate(BUZZER_PIN);

    digitalWrite(TRIG_PIN, LOW);
    delay(30);

    while (1){
        digitalWrite(TRIG_PIN,HIGH);
        delayMicroseconds(20);
        digitalWrite(TRIG_PIN,LOW);

        while (digitalRead(ECHO_PIN) == LOW);
        long startTime = micros();

        while (digitalRead(ECHO_PIN) == HIGH);
        long travelTime = micros() - startTime;

        int distance = travelTime / 58;

        if(distance >= 10){
            digitalWrite(LED1_PIN, HIGH);
            digitalWrite(LED2_PIN, LOW);
            buzzerOff();
        }
        else {
        digitalWrite(LED1_PIN,LOW);

        for (int i=0; i<2; i++) {
            digitalWrite(LED2_PIN,HIGH);
            buzzerOn();
            delay(500);
            digitalWrite(LED2_PIN,LOW);
            buzzerOff();
            delay(500);
        }
    }
}

return 0;
}