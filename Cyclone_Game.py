from gpiozero import Button
from gpiozero import LED
from gpiozero import Buzzer
from time import sleep
import random as r

button = Button(21)
buzzer = Buzzer(17)
ledlst = [LED(27), LED(22), LED(23), LED(24), LED(25), LED(5), LED(6), LED(12), LED(13), LED(16), LED(26)]

speed = 0.1
game = True
p1score = 0
p2score = 0

while game == True:
  for x in range(1, 11):
    ledlst[x].on()
    sleep(speed)
    if button.is_pressed and x == 10:
        p2score = p2score + 1
        if p2score == 5:
            ledlst[0].on()
            ledlst[1].on()
            ledlst[2].on()
            ledlst[3].on()
            ledlst[4].on()
            ledlst[5].on()
            ledlst[6].on()
            ledlst[7].on()
            ledlst[8].on()
            ledlst[9].on()
            ledlst[10].on()
            print("Player 2 wins")
            sleep(10)
            game = False
            break
        print("Player 2 scores!")
        sleep(1)
        ledlst[x].off()
        sleep(.5)
        ledlst[x].blink(.5,.5)
        sleep(p2score)
        ledlst[x].off()
        x = r.randint(0,10)
        
    elif button.is_pressed and x != 10:
        print("Nope")
        sleep(2)
        ledlst[x].off()
        x = r.randint(0,10)
        
    else:    
      ledlst[x].off()
    
    
  for x in reversed(range(9)):
    ledlst[x].on()
    sleep(speed)
    if button.is_pressed and x == 0:
        p1score = p1score + 1
        if p1score == 5:
            ledlst[0].on()
            ledlst[1].on()
            ledlst[2].on()
            ledlst[3].on()
            ledlst[4].on()
            ledlst[5].on()
            ledlst[6].on()
            ledlst[7].on()
            ledlst[8].on()
            ledlst[9].on()
            ledlst[10].on()
            print("Player 1 wins")
            sleep(10)
            game = False
            break
        print("Player 1 scores!")
        sleep(1)
        ledlst[x].off()
        sleep(.5)
        ledlst[x].blink(.5,.5)
        sleep(p1score)
        ledlst[x].off()
        x = r.randint(0,10)
        
    elif button.is_pressed and x != 0:
        print("Nope")
        sleep(2)
        ledlst[x].off()
        x = r.randint(0,10)
       
    else:
      ledlst[x].off()
    
