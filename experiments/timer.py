import webbrowser
import time
import datetime


def countdown(h, m, s):
    total_seconds = h * 3600 + m * 60 + s

    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    webbrowser.get("chrome").open('https://www.youtube.com/watch?v=v6HBZC9pZHQ&ab_channel=BabyKeemVEVO')


# Inputs for hours, minutes, seconds on timer
h = input("Enter the time in hours: ")
m = input("Enter the time in minutes: ")
s = input("Enter the time in seconds: ")
countdown(int(h), int(m), int(s))


# alarm = webbrowser.get("chrome").open('https://www.youtube.com/watch?v=v6HBZC9pZHQ&ab_channel=BabyKeemVEVO')


