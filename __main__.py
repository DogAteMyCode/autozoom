#!/usr/bin/env python3
import os
import sys
import logging
logging.basicConfig(level=logging.INFO, format="'%(asctime)s %(message)")
def say(msg):
    logging.info(msg)

try:
    import keyboard
    import datetime
    import pyperclip
    from time import sleep
    from elevate import elevate
except ModuleNotFoundError:
    import subprocess
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "keyboard", "datetime", "pyperclip", "elevate", "--user"])
    import keyboard
    import datetime
    import pyperclip
    from time import sleep
    from elevate import elevate
elevate()
location = sys.argv[0]
os.system("clear")
say("If you want to add your schedule run with the -v flag \nto stop excecution use ^c (control+c) \n")
try:
    sys.argv.index("-v")
    v = True
    say(
        "Remember that the module will only start after you completely close the .csv editor\nThis module stores your shedule in .csv format, save the in csv format")
except ValueError:
    v = False
    pass
if v:
    if sys.platform == "darwin":
        os.system("open " + location.replace("__main__.py", "") + '/' + "schedule.csv -W")
    else:
        say("only works in OS X")
say("Started")

f = open(location.replace("__main__.py", "") + '/' + "schedule.csv", "r+")
dayDictionary = {"Date": "Empty"}
for line in f.readlines():
    if line.lower().startswith("date"):
        continue
    line = line.strip('\n')
    day = line.split(",")
    dayDictionary[day.pop(0)] = day
f.close()
meetingSchedule = [dayDictionary["Monday"],
                   dayDictionary["Tuesday"],
                   dayDictionary["Wednesday"],
                   dayDictionary["Thursday"],
                   dayDictionary["Friday"],
                   dayDictionary["Saturday"],
                   dayDictionary["Sunday"]]
day = 0
while True:
    date = datetime.datetime.now()
    old = date.hour
    new = date.hour
    while old == new:
        try:
            date = datetime.datetime.now()
            day = date.today().weekday()
            new = date.hour
            sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)
    try:
        say(meetingSchedule[day][date.hour])
        say(day)
        say(date.hour)
        if meetingSchedule[day][date.hour] != "":
            os.system("open -a /Applications/zoom.us.app &")
            sleep(1)
            keyboard.press_and_release('command+j')
            sleep(1)
            keyboard.press_and_release('command+a')
            keyboard.press_and_release('delete')
            sleep(1)
            pyperclip.copy(meetingSchedule[day][date.hour])
            keyboard.write(meetingSchedule[day][date.hour])
            say(meetingSchedule[day][date.hour])
            if meetingSchedule[day][date.hour] == "":
                say("Nada")
            keyboard.press_and_release('enter')
            sleep(2400)
        else:
            say("Skipped")
    except IndexError:
        say("Skipped")
        pass
