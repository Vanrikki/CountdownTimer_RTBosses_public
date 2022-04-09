#Author: Ville Tuominen, IGN: Vanrikki
#Title: CountdownTimer_RTBosses
#This CountdownTimer is made for Drift City RushTime bosses (stage1).
#Timer can be started by pressing start buttons and pressing given hotkey (atm "q" for blue, "e" for poop, "z" for greenbeam)
#Timer can reset either pressing stop and start or you can hold given hotkey. After holding hotkey program will prompt to press given hotkey again and timer starts.
#Timer has been made so that it will make sound effect just before specific skill happens. Example when blue timer hits 0.8s it will play Quack sound effect.
#Purpose of this is to make RushTimes easier by knowing when boss makes skill.

import threading
import time
import tkinter as tk
from turtle import width
import keyboard
from playsound import playsound
import time

class CountdownTimer:
    #Creates window with times and buttons. When buttons are pressed they create thread for timer.
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x220")
        self.root.title("Countdown Timer")
        self.root.wm_attributes("-topmost",1)

        self.Bluetime_label= tk.Label(self.root, font=("Helvetica", 20), text="Blue: 0")
        self.Bluetime_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.Pooptime_label= tk.Label(self.root, font=("Helvetica", 20), text="Poop: 0")
        self.Pooptime_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.Greenbeamtime_label= tk.Label(self.root, font=("Helvetica", 20), text="Greenbeam: 0")
        self.Greenbeamtime_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.startBlueButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_blue)
        self.startBlueButton.grid(row=0, column=2, padx=5, pady=5)

        self.startPoopButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_poop)
        self.startPoopButton.grid(row=1, column=2, padx=5, pady=5)

        self.startGreenbeamButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_greenbeam)
        self.startGreenbeamButton.grid(row=2, column=2, padx=5, pady=5)

        self.root.mainloop()

    def start_thread_blue(self):
        #Changes Start button to Stop and starts thread
        self.startBlueButton= tk.Button(self.root, font=("Helvetica", 20), text="Stop", command=self.stopBlue)
        self.startBlueButton.grid(row=0, column=2, padx=5, pady=5)

        t = threading.Thread(target=self.startBlue)
        t.start()
            
    def startBlue(self):
        #Program waits for input before starting timer. You can reset timer by holding Q and program will prompt to press it again to start timer.
        #Reset has been made if timer starts go off or it has started wrong time.
        #All three skills are made same way
        #V2.0 timers are looking cpu time. Should be more accurate.
        blueTargetTime = 6.4
        bluePlaysong = False
        self.bluestop_loop = False
        blueReadKeyStatement = False
        self.Bluetime_label.config(text=f"Press q: 0")
        self.root.update()
        while blueReadKeyStatement == False:
            
            if keyboard.read_key() == "q":
                blueReadKeyStatement = True
                blueFirst_time = time.time()
                blueFirst_time -= 0.2
                time.sleep(0.2)
            
        while not self.bluestop_loop:
            blueGoingTime = time.time()
            BlueTimeGone = blueGoingTime - blueFirst_time
            self.Bluetime_label.config(text=f"Blue: {blueTargetTime - BlueTimeGone:.2f}")
            self.root.update()
            time.sleep(0.05)
            if keyboard.is_pressed('q'):
                self.Bluetime_label.config(text=f"Press q: 0")
                self.root.update()
                time.sleep(0.5)
                blueReadKeyStatement = False
                blueFirst_time = time.time()
                while blueReadKeyStatement == False:
                    if keyboard.read_key() == "q":
                        blueReadKeyStatement = True
                        blueFirst_time = time.time()
                        blueFirst_time -= 0.2
                        time.sleep(0.2)
            if BlueTimeGone >= blueTargetTime:
                blueFirst_time = time.time()
                bluePlaysong = False

            if BlueTimeGone >= 5.0 and BlueTimeGone <= 5.1 and bluePlaysong == False:
                bluePlaysong = True
                R = threading.Thread(name="playsound",target=self.playBlue)
                R.start()

    def start_thread_poop(self):
        self.startPoopButton= tk.Button(self.root, font=("Helvetica", 20), text="Stop", command=self.stopPoop)
        self.startPoopButton.grid(row=1, column=2, padx=5, pady=5)

        t = threading.Thread(target=self.startPoop)
        t.start()
  
    def startPoop(self):
        poopTargetTime = 19.95
        poopPlaysong = False
        self.poopstop_loop = False
        poopReadKeyStatement = False
        self.Pooptime_label.config(text=f"Press e: 0")
        self.root.update()
        while poopReadKeyStatement == False:
            
            if keyboard.read_key() == "e":
                poopReadKeyStatement = True
                poopFirst_time = time.time()
                poopFirst_time -= 0.2
                time.sleep(0.2)
            
        while not self.poopstop_loop:
            poopGoingTime = time.time()
            poopTimeGone = poopGoingTime - poopFirst_time
            self.Pooptime_label.config(text=f"Poop: {poopTargetTime - poopTimeGone:.2f}")
            self.root.update()
            time.sleep(0.05)
            if keyboard.is_pressed('e'):
                self.Pooptime_label.config(text=f"Press e: 0")
                self.root.update()
                time.sleep(0.5)
                poopReadKeyStatement = False
                while poopReadKeyStatement == False:
                    if keyboard.read_key() == "e":
                        poopReadKeyStatement = True
                        poopFirst_time = time.time()
                        poopFirst_time -= 0.2
                        time.sleep(0.2)
            if poopTimeGone >= poopTargetTime:
                poopFirst_time = time.time()
                poopPlaysong = False

            if poopTimeGone >= 18.0 and poopTimeGone <= 18.1 and poopPlaysong == False:
                poopPlaysong = True
                P = threading.Thread(name="playsound",target=self.playPoop)
                P.start()
                
    def playPoop(self):
        playsound('C:/soundeffect/WaterDrop.mp3')

    def playBlue(self):
        playsound('C:/soundeffect/Quack.mp3')

    #Greenbeam is not yet optimized
    def start_thread_greenbeam(self):
        self.startGreenbeamButton= tk.Button(self.root, font=("Helvetica", 20), text="Stop",command=self.stopGreenbeam)
        self.startGreenbeamButton.grid(row=2, column=2, padx=5, pady=5)

        t = threading.Thread(target=self.startGreenbeam)
        t.start()
  
    def startGreenbeam(self):
        self.greenbeamstop_loop = False
        Greenbeamtime = 37
        while Greenbeamtime > 0 and not self.greenbeamstop_loop:
            Greenbeamtime -= 1
            self.Greenbeamtime_label.config(text=f"Greenbeam: {Greenbeamtime:2d}")
            self.root.update()
            time.sleep(1)
            if keyboard.is_pressed('z'):
                Greenbeamtime = 37
            if Greenbeamtime == 1:
                Greenbeamtime = 37

    def stopBlue(self):
        self.bluestop_loop = True
        self.Bluetime_label.config(text="Blue: 0")
        self.startBlueButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_blue)
        self.startBlueButton.grid(row=0, column=2, padx=5, pady=5)

    def stopPoop(self):
        self.poopstop_loop = True
        self.Pooptime_label.config(text="Poop: 0")
        self.startPoopButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_poop)
        self.startPoopButton.grid(row=1, column=2, padx=5, pady=5)

    def stopGreenbeam(self):
        self.greenbeamstop_loop = True
        self.Greenbeamtime_label.config(text="Greenbeam: 0")
        self.startGreenbeamButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_greenbeam)
        self.startGreenbeamButton.grid(row=2, column=2, padx=5, pady=5)

CountdownTimer()