import time
from time import sleep

import pyfiglet
from gtts import gTTS
from playsound import playsound

Time = time.strftime("%H:%M")
print(pyfiglet.figlet_format("Alarm Clock"))
alarm = input("Choose your time to wake up: (Example: 6:30) -> ")


while Time != alarm:
    Time = time.strftime("%H:%M")
    sleep(1)

if Time == alarm:
    tts = gTTS("WAKE UP !", lang='en')
    tts.save("wakeup.mp3")
    tts = gTTS("It is {}".format(Time), lang='en')
    tts.save('timeis.mp3')
    tts = gTTS("I said WAKE UP !", lang='en')
    tts.save('wakeup2.mp3')
    playsound('timeis.mp3')
    playsound("wakeup.mp3")
    sleep(2)
    playsound('wakeup2.mp3')
    sleep(5)
    playsound('giant.mp3')
    print(pyfiglet.figlet_format("Chicken Time !"))
    playsound('chicken.mp3')
