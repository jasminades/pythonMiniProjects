from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"




def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    print("Alarm will sound in: ")
    while time_elapsed < seconds:
        time.sleep(1)                   #wait for one second
        time_elapsed += 1

        time_left = seconds - time_elapsed
        hours_left = time_left // 3600
        minutes_left = (time_left%3600) // 60
        seconds_left = time_left % 60


        print(f"{CLEAR_AND_RETURN}{hours_left:02d}:{minutes_left :02d} :{seconds_left :02d}")

    playsound("alarm.mp3")

hours = int(input("Set hours for the alarm: "))
minutes = int(input("Set minutes for the alarm: "))
seconds = int(input("Set seconds for the alarm: "))
total = hours * 3600 + minutes * 60 + seconds
alarm(total)


