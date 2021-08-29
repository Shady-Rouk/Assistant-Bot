import time
from plyer import notification
import sys

def setReminder():
    #event = input("What should I remind you? ")
    #wait = float(input("In how many minutes? "))
    mainevt = ""
    with open("event.txt", "r", encoding="utf8") as eventF:
        mainevt = eventF.read()
    wait = float(sys.argv[1]) #wait
    wait *= 60
    time.sleep(wait)
    notification.notify(
        title = 'Reminder',
        message = mainevt,
        app_icon = r'./Bell.ico',
        timeout = 10,
        toast = False
    )

setReminder()