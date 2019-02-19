from microbit import*
import random

#show a smiling face and "Welcome, and shake me!"
#shake motion trigger scrolling game instruction
#show instruction, "Press A for even number, press B for odd number. Shake me to play."
#if user is ready to play, shake motion to continue play
while True:
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
    number = random.randint(1,100) #give a random number between 1 and 100
    display.show(number) # display the random number
#examine whether the number is odd or even
if (number % 2 == 0): #if an even number
    if button_a.is_pressed(): #press A
    display.show(Image.HAPPY) #press A is correct response
    else: #if press B
    display.show(Image.SAD) #wrong response
else: #if an odd number
    if button_a.is_pressed(): #press A
    display.show(Image.SAD) #press A is wrong response
    else: # if press B
    display.show(Image.HAPPY) #press B is correct response
else:
    break

#reapeat the game for as many times as the user want (if, then)