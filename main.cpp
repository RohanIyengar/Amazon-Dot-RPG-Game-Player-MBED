#include "mbed.h"

Serial pc(USBTX, USBRX);
DigitalOut myled(LED1);

char buffer[20];
char hi;
volatile char curr[20];

int main() {
    myled = 1;
    while(1) {
        wait(.01);
        if (pc.readable()) {
            pc.scanf("%s", buffer);
            //hi = (char) pc.getc();
            //curr = buffer;
            pc.printf(buffer);
            myled = 1;
        } else {
            //pc.printf(curr + "\n");
            myled = 0;
        }
        //pc.printf(curr);
    }
}
