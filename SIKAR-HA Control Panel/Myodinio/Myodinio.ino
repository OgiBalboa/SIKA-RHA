
#include <Servo.h>
//KAYIT İÇİN GİRİŞ VE ÇIKIŞLAR
int button=8;
int led = 13;
int buttonst= 0;
int tkr =1;
int i;
int Play=10;
int playstate = 0;
int led2 = 7;
int Play2= 0;
int myo;
int sayac =0;
// SERVOLAR
Servo base;
Servo yatay;
Servo dikey;
Servo gripper;

// MOTOR AÇI KAYITLARI
int mbase;
int myatay;
int mdikey ;
int mgripper;
//KAYIT AÇILARI
int mbase2;
int myatay2;
int mdikey2;
int mgripper2;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(180);
  base.attach(2); 
  yatay.attach(3);
  dikey.attach(4);
  gripper.attach(5);
pinMode(button,INPUT);
pinMode(led,OUTPUT);
pinMode(led2,OUTPUT);
mbase = 90;
myatay = 1;
mdikey = 170;
mgripper = 179;
}

void loop() {  


buttonst= digitalRead(button);

  if (buttonst==LOW){
   myo = Serial.parseInt();
   Serial.println(myo);
   HareketEt();
  }
  else digitalWrite(led,LOW);
  
  
playstate = digitalRead(Play); // oynatma girişi kontrol

/*

if (Serial.available()){
  digitalWrite(led2,HIGH);
 mbase2 = Serial.parseInt();
 myatay2=Serial.parseInt();
 mdikey2 = Serial.parseInt();
 mgripper2 = Serial.parseInt();
  while(mbase != mbase2) {
  if(mbase>mbase2) mbase-=1;
  else {mbase+=1;}
  base.write(mbase);
  delay(5);
 }
 
 while(myatay2!=myatay) {
   if (myatay>myatay2) myatay-=1;
   else {myatay+=1;} 
   yatay.write(myatay);
   delay(5);
 }
 
 
 while (mdikey2!=mdikey) {
   if(mdikey>mdikey2) mdikey-=1;
   else { mdikey+=1; }
 dikey.write(mdikey);
 delay(5);
 }

}
else digitalWrite(led2,LOW);
*/
}


void HareketEt() 
{
 if (myo == 20 && mbase <180) sayac = 1;
  while (sayac == 1) {
    if (myo == 49) sayac =0;
    mbase+=1;
  delay(5);
}
if(myo ==21 && mbase >0) sayac = 1;
  while (sayac == 1) {
    if (myo == 49) sayac =0;
  mbase-=1;
  delay(5);
}


if (myo == 11 && mdikey>0) sayac = 1;
  while (sayac == 1) {
    if (myo == 49) sayac =0;
  mdikey-=1;
  delay(5);
}
if(myo == 10 && mdikey <180) {
  mdikey+=1;
  delay(5);
}


/*if (x2pos > 900 && myatay>0) {
  myatay-=1;
  delay(5);
}
if(x2pos < 100 && myatay < 180) {
  myatay+=1;
  delay(5);
}

if (y2pos > 900 && mgripper>150) {
  mgripper-=1;
  delay(5);
}
if(y2pos < 100 && mgripper < 180) {
  mgripper+=1;
  delay(5);
}
*/
base.write(mbase); // arka
dikey.write(mdikey);
yatay.write(myatay);
gripper.write(mgripper);

delay(15); 
}
//  ROBOTUN BULUNDUĞU KONUMU RASPBERRY'YE GÖNDER
void VerileriGonder() {
  
 digitalWrite(led,HIGH);
 Serial.println(mbase);
 delay(15);
 Serial.println(myatay);
  delay(15);
 Serial.println(mdikey);
  delay(15);
 Serial.println(mgripper);
  delay(1500);
}
