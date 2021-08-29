#run basic commands
#tell me time, set reminders, command line based, 
#weather, date, make device changes, location, 
#send emails, open emails, compose emails/messages
#create, manage and find files
#post a tweet

#consider making conversations: dictionary for common user convo starters as key and list of common responses as value. 
#random.choice on the list of values if convo starter matches a key

#make a README.txt file with instructions for the user
#stuff like installing plyer or setting up their email for the function to run properly

#function to calculate time ahead and behind, e.g. what is 30 days from now? what is 20 hours from now? what was 3 days ago?

import datetime
import os
import random
import time
import sys
import smtplib
import getpass
import subprocess
#from email.mime.text import MIMEText

end = ["goodbye", "bye", "see ya", "close", "end"]

def tellDate(): #done
    dd = datetime.datetime.now()
    print("Today's date is", str(dd.strftime("%A")), str(dd.strftime("%B")), str(dd.strftime("%d")) + ",", str(dd.strftime("%Y")))

def tellTime(): #done
    dd = datetime.datetime.now()
    print("The time is", str(dd.strftime("%I")) + ":" + str(dd.strftime("%M")) + ":" + str(dd.strftime("%S")), str(dd.strftime("%p")))

def timecalc(): #done
    calcType = input("Time Ahead or Time Before (A/B): ")
    if (calcType == "A"):
        weeks = int(input("Weeks: "))
        days = int(input("Days: "))
        hours = int(input("Hours: "))
        minutes = int(input("Minutes: "))
        res = datetime.datetime.now() + datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes)
        print(weeks, "week(s),", days, "day(s),", hours, "hour(s) and", minutes, "minute(s) from now is", str(res.strftime("%A")), str(res.strftime("%B")), str(res.strftime("%d")) + ",", str(res.strftime("%Y")), str(res.strftime("%I")) + ":" + str(res.strftime("%M")) + ":" + str(res.strftime("%S")), str(res.strftime("%p")))
    elif (calcType == "B"):
        weeks = int(input("Weeks: "))
        days = int(input("Days: "))
        hours = int(input("Hours: "))
        minutes = int(input("Minutes: "))
        res = datetime.datetime.now() - datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes)
        print(weeks, "week(s),", days, "day(s),", hours, "hour(s) and", minutes, "minute(s) before now was", str(res.strftime("%A")), str(res.strftime("%B")), str(res.strftime("%d")) + ",", str(res.strftime("%Y")), str(res.strftime("%I")) + ":" + str(res.strftime("%M")) + ":" + str(res.strftime("%S")), str(res.strftime("%p")))
    else:
        print("Invalid method")

def sendMail(): #half done
    #modify to determine which mail port and service to send with by checking what comes afer @
    #directly through mail service, 
    lst = []
    sender = input("Your email:  ")
    point = sender.find("@")
    if(sender[point:] == "@gmail.com"):
        smtpServer = "smtp.gmail.com"
        smtpPort = 465
    elif(sender[point:] == "@yahoo.com"):
        smtpServer = "smtp.mail.yahoo.com"
        smtpPort = 465
    elif(sender[point:] == "@icloud.com"):
        smtpServer = "smtp.mail.me.com"
        smtpPort = 587
    elif(sender[point:] == "@outlook.com"):
        smtpServer = "smtp-mail.outlook.com"
        smtpPort = 587

    sender_password = getpass.getpass()
    message = input("Your message... ")
    server = smtplib.SMTP(smtpServer, smtpPort)
    #smtp.mail.yahoo.com port 465
    #smtp.gmail.com port 465
    #smtp-mail.outlook.com port 587
    #smtp.mail.me.com port 587 icloud
    server.starttls()
    server.login(sender, sender_password)
    with open("mailList.txt", "r", encoding="utf8") as e:
        lst = e.readlines()
    for email in lst:
        server.sendmail(sender, email, message)
    server.quit()

def createFile(): #done
    filepath = input("File Name: ")
    with open("../../"+filepath, "w", encoding="utf8") as fileHandle:
        fileHandle.write("")
        print("The file", filepath, "has been created")

def deleteFile(): #done
    filepath = input("File Name: ")
    if os.path.isfile("../../"+filepath):
        os.remove("../../"+filepath)
        print("The file", filepath, "has been deleted")
    else:
        print("File not found")

def setReminder(): #done
    #don't know if it would work after shutting down/restarting system
    event = input("What would you like me to remind you? ")
    with open("event.txt", "w", encoding="utf8") as eventF:
        eventF.write(event)
    wait = input("In how many minutes? ")
    with open("reminder.bat", "w", encoding="utf8") as reminderF:
        reminderF.write("@echo off\npyw reminder.py ")
        reminderF.write(wait)
        reminderF.write("\nexit /s")
    #run batch file
    os.system("START /B reminder.bat")

def helpMe(): #done, constatly updated
    print("I can tell the date, the time, calculate time, create or delete a file, set a reminder, send an email, play TicTacToe (ttt), and play rock, paper, scissors (rps), all you have to do is ask :)")

def rps(): #done
    option = ["rock", "paper", "scissors"]
    go_on = ""
    score = [0, 0]
    while(go_on != "no"):
        comp = random.choice(option)
        player = input("Your move: ")
        print("Comp chooses", comp)
        if(player.lower() == comp):
            print("Tie!")
        elif(player.lower() == "rock"):
            if(comp == "scissors"):
                print("Rock smashes scissors. You win!")
                score[0] += 1
            elif(comp == "paper"):
                print("Paper covers rock. You lose :(")
                score[1] += 1
        elif(player.lower() == "paper"):
            if(comp == "scissors"):
                print("Scissors cuts paper. You lose :(")
                score[1] += 1
            elif(comp == "rock"):
                print("Paper covers rock. You win!")
                score[0] += 1
        elif(player.lower() == "scissors"):
            if(comp == "paper"):
                print("Scissors cuts paper. You win!")
                score[0] += 1
            elif(comp == "rock"):
                print("Rock smashes scissors. You lose :(")
                score[1] += 1
        else:
            print("This is invalid")
        go_on = input("Would you like to keep playing? ")
    print("You:", score[0], "| Comp:", score[1])
    print("Goodbye stink! :)")

def ttt(): #done
    os.system("py TicTacToe.py")

def openApp():
    app = input("What application in your desktop would you like to launch? ")
    os.system("start " + app)

def determineCommand(inputMsg): #done, constantly updated
    if inputMsg == "tell date" or inputMsg == "what is today's date" or inputMsg == "tell me the date":
        tellDate()
    elif inputMsg == "tell time" or inputMsg == "what is the time":
        tellTime()
    elif inputMsg == "play rps":
        rps()
    elif inputMsg == "create file" or inputMsg == "make file":
        createFile()
    elif inputMsg == "delete file":
        deleteFile()
    elif inputMsg == "help":
        helpMe()
    elif inputMsg == "send an email" or inputMsg == "send email":
        sendMail()
    elif inputMsg == "set reminder" or inputMsg == "set a reminder":
        setReminder()
    elif inputMsg == "play ttt":
        ttt()
    elif inputMsg == "calculate time":
        timecalc()
    elif inputMsg == "open app":
        openApp()

keywords = []
with open("keywords.txt", "r", encoding="utf8") as k:
    keywords = k.readlines()
#^^constantly updated as functions increase

for i in range(len(keywords)):
    keywords[i] = keywords[i].strip()

running = True

welcome = "Hello user, what can I do for you?\n"
for _ in welcome:
    sys.stdout.write(_)
    sys.stdout.flush()
    time.sleep(.05)

while running:
    instruction = input("> ")
    if instruction in end:
        goodbye = random.choice(["Goodbye user! :)\n", "Ciao!\n", "See you soon!\n", "Adios!\n"])
        for _ in goodbye:
            sys.stdout.write(_)
            sys.stdout.flush()
            time.sleep(.05)
        running = False
    elif instruction in keywords:
        determineCommand(instruction)
    else:
        print("I don't understand yet")