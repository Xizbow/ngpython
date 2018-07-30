from winsound import *
from time import *
import threading
KeepPlaying = True
def Main():
    global KeepPlaying
    global thesong
    bgm.start()
##    while(True):
##        thesong = input("Enter the song: ")
##        KeepPlaying = False

def BGMusic():
    global KeepPlaying
    while(True):
        if thesong == "title":
            TitleMusic()
        if thesong == "calm":
            CalmMusic()
        if thesong == "shopping"
            ShoppingMusic()
        if thesong == "fight"
            FightMusic()
        KeepPlaying = True

def ChangeMusic(_thesong):
    global thesong
    global KeepPlaying
    KeepPlaying = False
    thesong = _thesong

def CalmMusic():
    Beep(700, 1100)
    if KeepPlaying == False:
        return
    Beep(1100, 500)
    if KeepPlaying == False:
        return
    Beep(500, 1000)
    if KeepPlaying == False:
        return
    sleep(1)

def ShoppingMusic():
    Beep(500, 100)
    if KeepPlaying == False:
        return
    sleep(.5)
    if KeepPlaying == False:
        return
    Beep(500, 100)
    if KeepPlaying == False:
        return
    sleep(.5)
    if KeepPlaying == False:
        return
    Beep(500, 100)
    if KeepPlaying == False:
        return
    Beep(500, 100)
    if KeepPlaying == False:
        return
    sleep(.5)
    if KeepPlaying == False:
        return
    Beep(500, 100)
    if KeepPlaying == False:
        return
    sleep(.5)
    if KeepPlaying == False:
        return
    Beep(500, 100)
    if KeepPlaying == False:
        return
    sleep(.5)
    if KeepPlaying == False:
        return
    Beep(900, 100)
    if KeepPlaying == False:
        return
    Beep(900, 100)
    if KeepPlaying == False:
        return
    Beep(900, 100)
    if KeepPlaying == False:
        return

def FightMusic():
    Beep(300, 100)
    if KeepPlaying == False:
        return
    Beep(300, 100)
    if KeepPlaying == False:
        return
    sleep(.5)
    if KeepPlaying == False:
        return
    Beep(300, 100)
    if KeepPlaying == False:
        return
    Beep(300, 100)
    if KeepPlaying == False:
        return
    sleep(.5)
    if KeepPlaying == False:
        return
    Beep(300, 100)
    if KeepPlaying == False:
        return
    Beep(300, 100)
    if KeepPlaying == False:
        return
    sleep(.5)
    if KeepPlaying == False:
        return
    Beep(300, 100)
    if KeepPlaying == False:
        return
    Beep(300, 100)
    if KeepPlaying == False:
        return
    Beep(700, 300)
    if KeepPlaying == False:
        return
    sleep(.5)
    if KeepPlaying == False:
        return

def GameOverMusic():
    Beep(700, 300)
    if KeepPlaying == False:
        return
    Beep(500, 300)
    if KeepPlaying == False:
        return
    Beep(200, 2000)
    if KeepPlaying == False:
        return

def TitleMusic():
    Beep(300, 500)
    if KeepPlaying == False:
        return
    Beep(300, 500)
    if KeepPlaying == False:
        return
    Beep(300, 500)
    if KeepPlaying == False:
        return
    Beep(300, 500)
    if KeepPlaying == False:
        return
    Beep(300, 500)
    if KeepPlaying == False:
        return
    Beep(300, 100)
    if KeepPlaying == False:
        return
    Beep(300, 100)
    if KeepPlaying == False:
        return
    Beep(300, 100)
    if KeepPlaying == False:
        return
    Beep(300, 100)
    if KeepPlaying == False:
        return
    Beep(700, 700)
    if KeepPlaying == False:
        return
    sleep(.5)
    if KeepPlaying == False:
        return

def EnemyDeathSound():
    Beep(700, 300)
    Beep(650, 50)
    Beep(600, 50)
    Beep(550, 50)
    Beep(500, 50)
    Beep(450, 50)
    Beep(400, 50)
    Beep(350, 50)
    Beep(300, 50)
    Beep(250, 50)
    Beep(200, 50)

def ItemPickupSound():
    Beep(700, 300)
    Beep(1200, 700)

def OpenChestSound():
    Beep(300, 300)
    Beep(500, 300)
    Beep(700, 300)
    Beep(900, 300)
    Beep(1100, 500)

thesong = "title"
bgm = threading.Thread(target=BGMusic)

