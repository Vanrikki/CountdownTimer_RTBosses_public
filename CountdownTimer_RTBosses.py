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
import keyboard
from playsound import playsound
import time
import pathlib as ostdir

class CountdownTimer:
    #Creates window with times and buttons. When buttons are pressed they create thread for timer.
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("290x235")
        self.root.title("Countdown Timer")
        self.root.wm_attributes("-topmost",1)

        def openAboutWindow():
            aboutWindow = tk.Toplevel(self.root)
            aboutWindow.title("About")
            aboutWindow.geometry("400x125")
            aboutWindow.wm_attributes("-topmost",1)
            aboutLabel = tk.Label(aboutWindow, font=("Helvetica", 15), text="This program creator: Vanrikki", anchor="w",justify=tk.LEFT)
            aboutLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")
            aboutLabel2 = tk.Label(aboutWindow, font=("Helvetica", 15), text="It is used to help RushTimes in DriftCity.", anchor="w",justify=tk.LEFT)
            aboutLabel2.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")
            aboutLabel3 = tk.Label(aboutWindow, font=("Helvetica", 15), text="Written in Python.")
            aboutLabel3.grid(row=2, column=0, columnspan=2, padx=5, pady=5 ,sticky="w")
            aboutWindow.grab_set()

        def openHelpWindow():
            helpWindow = tk.Toplevel(self.root)
            helpWindow.title("Settings")
            helpWindow.geometry("550x155")
            helpWindow.wm_attributes("-topmost",1)
            helpLabel = tk.Label(helpWindow, font=("Helvetica", 15), text="First click start buttons on RTboss skills.", anchor="w",justify=tk.LEFT)
            helpLabel.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")
            helpLabel2 = tk.Label(helpWindow, font=("Helvetica", 15), text="Get next to RT boss, wait boss to use skill.", anchor="w",justify=tk.LEFT)
            helpLabel2.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")
            helpLabel3 = tk.Label(helpWindow, font=("Helvetica", 15), text="When boss uses skill press given hotkey to start timer.")
            helpLabel3.grid(row=2, column=0, columnspan=2, padx=5, pady=5 ,sticky="w")
            helpLabel4 = tk.Label(helpWindow, font=("Helvetica", 15), text="You will hear soundeffect when boss is about to use skill")
            helpLabel4.grid(row=3, column=0, columnspan=2, padx=5, pady=5 ,sticky="w")
            helpWindow.grab_set()

        
        self.Bluetime_label= tk.Label(self.root, font=("Helvetica", 20), text="Blue: 00.00")
        self.Bluetime_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.Pooptime_label= tk.Label(self.root, font=("Helvetica", 20), text="Poop: 00.00")
        self.Pooptime_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.Greenbeamtime_label= tk.Label(self.root, font=("Helvetica", 20), text="Green: 00.00")
        self.Greenbeamtime_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.startBlueButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_blue)
        self.startBlueButton.grid(row=1, column=2, padx=5, pady=5)

        self.startPoopButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_poop)
        self.startPoopButton.grid(row=2, column=2, padx=5, pady=5)

        self.startGreenbeamButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_greenbeam)
        self.startGreenbeamButton.grid(row=3, column=2, padx=5, pady=5)

        self.helpButton= tk.Button(self.root, font=("Helvetica", 10), text="Help", command=openHelpWindow)
        self.helpButton.grid(row=0, column=1, padx=5, pady=5)

        self.aboutButton= tk.Button(self.root, font=("Helvetica", 10), text="About", command=openAboutWindow)
        self.aboutButton.grid(row=0, column=2, padx=5, pady=5)

        self.root.mainloop()
    
    
    def start_thread_blue(self):
        #Changes Start button to Stop and starts thread
        self.startBlueButton= tk.Button(self.root, font=("Helvetica", 20), text="Stop", command=self.stopBlue)
        self.startBlueButton.grid(row=1, column=2, padx=5, pady=5)
        t = threading.Thread(target=self.startBlue)
        t.start()
            
    def startBlue(self):
        #Program waits for input before starting timer. You can reset timer by holding Q and program will prompt to press it again to start timer.
        #Reset has been made if timer starts go off or it has started wrong time.
        #All three skills are made same way
        #V2.0 timers are looking cpu time. Should be more accurate.
        blueTargetTime = 6.44
        bluePlaysong = False
        self.bluestop_loop = False
        blueReadKeyStatement = False
        self.Bluetime_label.config(text=f"Press q: 00.00")
        self.root.update()
        while blueReadKeyStatement == False:
            if keyboard.read_key() == "q":
                blueReadKeyStatement = True
                blueFirst_time = time.time()
                blueFirst_time -= 0.4
                time.sleep(0.2)
        while not self.bluestop_loop:
            blueGoingTime = time.time()
            BlueTimeGone = blueGoingTime - blueFirst_time
            self.Bluetime_label.config(text=f"Blue: {blueTargetTime - BlueTimeGone:.2f}")
            self.root.update()
            time.sleep(0.05)
            if keyboard.is_pressed('q'):
                self.Bluetime_label.config(text=f"Press q: 00.00")
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
                        bluePlaysong = False
            if BlueTimeGone > blueTargetTime:
                blueLeftOverTime = blueTargetTime - BlueTimeGone
                blueFirst_time = time.time()
                blueFirst_time += blueLeftOverTime
                bluePlaysong = False
            if BlueTimeGone >= 5.0 and BlueTimeGone <= 5.1 and bluePlaysong == False:
                bluePlaysong = True
                R = threading.Thread(name="playsound",target=self.playBlue)
                R.start()

    def start_thread_poop(self):
        self.startPoopButton= tk.Button(self.root, font=("Helvetica", 20), text="Stop", command=self.stopPoop)
        self.startPoopButton.grid(row=2, column=2, padx=5, pady=5)
        t = threading.Thread(target=self.startPoop)
        t.start()
  
    def startPoop(self):
        poopTargetTime = 19.95
        poopPlaysong = False
        self.poopstop_loop = False
        poopReadKeyStatement = False
        self.Pooptime_label.config(text=f"Press e: 00.00")
        self.root.update()
        while poopReadKeyStatement == False:
            if keyboard.read_key() == "e":
                poopReadKeyStatement = True
                poopFirst_time = time.time()
                poopFirst_time -= 0.2
                time.sleep(0.3)
        while not self.poopstop_loop:
            poopGoingTime = time.time()
            poopTimeGone = poopGoingTime - poopFirst_time
            self.Pooptime_label.config(text=f"Poop: {poopTargetTime - poopTimeGone:.2f}")
            self.root.update()
            time.sleep(0.05)
            if keyboard.is_pressed('e'):
                self.Pooptime_label.config(text=f"Press e: 00.00")
                self.root.update()
                time.sleep(0.5)
                poopReadKeyStatement = False
                while poopReadKeyStatement == False:
                    if keyboard.read_key() == "e":
                        poopReadKeyStatement = True
                        poopFirst_time = time.time()
                        poopFirst_time -= 0.2
                        time.sleep(0.2)
                        poopPlaysong = False
            if poopTimeGone > poopTargetTime:
                poopLeftOverTime = poopTargetTime - poopTimeGone
                poopFirst_time = time.time()
                poopFirst_time += poopLeftOverTime
                poopPlaysong = False
            if poopTimeGone >= 18.0 and poopTimeGone <= 18.1 and poopPlaysong == False:
                poopPlaysong = True
                P = threading.Thread(name="playsound",target=self.playPoop)
                P.start()
                
    def playPoop(self):
        playsound(ostdir.Path.joinpath(ostdir.Path(__file__).parent,"soundeffect","WaterDrop.mp3").as_posix())

    def playBlue(self):
        playsound(ostdir.Path.joinpath(ostdir.Path(__file__).parent,"soundeffect","Quack.mp3").as_posix())

    def playGreen(self):
        playsound(ostdir.Path.joinpath(ostdir.Path(__file__).parent,"soundeffect","Boing.mp3").as_posix())

    #Greenbeam is not yet optimized
    def start_thread_greenbeam(self):
        self.startGreenbeamButton= tk.Button(self.root, font=("Helvetica", 20), text="Stop",command=self.stopGreenbeam)
        self.startGreenbeamButton.grid(row=3, column=2, padx=5, pady=5)
        t = threading.Thread(target=self.startGreenbeam)
        t.start()

    def startGreenbeam(self):
        greenTargetTime = 36.95
        greenPlaysong = False
        self.greenstop_loop = False
        greenReadKeyStatement = False
        self.Greenbeamtime_label.config(text=f"Press r: 00.00")
        self.root.update()
        while greenReadKeyStatement == False:
            if keyboard.read_key() == "r":
                greenReadKeyStatement = True
                greenFirst_time = time.time()
                greenFirst_time -= 0.2
                time.sleep(0.2)
        while not self.greenstop_loop:
            greenGoingTime = time.time()
            greenTimeGone = greenGoingTime - greenFirst_time
            self.Greenbeamtime_label.config(text=f"Green: {greenTargetTime - greenTimeGone:.2f}")
            self.root.update()
            time.sleep(0.05)
            if keyboard.is_pressed('r'):
                self.Greenbeamtime_label.config(text=f"Press r: 00.00")
                self.root.update()
                time.sleep(0.5)
                greenReadKeyStatement = False
                while greenReadKeyStatement == False:
                    if keyboard.read_key() == "r":
                        greenReadKeyStatement = True
                        greenFirst_time = time.time()
                        greenFirst_time -= 0.2
                        time.sleep(0.2)
                        greenPlaysong = False
            if greenTimeGone > greenTargetTime:
                greenLeftOverTime = greenTargetTime - greenTimeGone
                greenFirst_time = time.time()
                greenFirst_time += greenLeftOverTime
                greenPlaysong = False
            if greenTimeGone >= 34.4 and greenTimeGone <= 34.5 and greenPlaysong == False:
                greenPlaysong = True
                G = threading.Thread(name="playsound",target=self.playGreen)
                G.start()

    def stopBlue(self):
        self.bluestop_loop = True
        self.Bluetime_label.config(text="Blue: 00.00")
        self.startBlueButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_blue)
        self.startBlueButton.grid(row=1, column=2, padx=5, pady=5)

    def stopPoop(self):
        self.poopstop_loop = True
        self.Pooptime_label.config(text="Poop: 00.00")
        self.startPoopButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_poop)
        self.startPoopButton.grid(row=2, column=2, padx=5, pady=5)

    def stopGreenbeam(self):
        self.greenstop_loop = True
        self.Greenbeamtime_label.config(text="Green: 00.00")
        self.startGreenbeamButton= tk.Button(self.root, font=("Helvetica", 20), text="Start", command=self.start_thread_greenbeam)
        self.startGreenbeamButton.grid(row=3, column=2, padx=5, pady=5)

CountdownTimer()