from tkinter import *
import numpy as np
import cv2
import pyautogui
import time
import os
import sys

running = False  # Global flag
idx = 0  # loop index


def screenshot():

        # take screenshot using pyautogui
        date = time.strftime("%d-%m-%Y", time.localtime())
        Desktop=os.path.expanduser("~\Desktop\\")
        # directory='C:\Users\aaliyan\Desktop\'
        os.chdir(Desktop)
        try:
            os.mkdir(date)
        except:
            os.chdir(Desktop+date)

        os.chdir(Desktop+date)

        image = pyautogui.screenshot()

        # since the pyautogui takes as a
        # PIL(pillow) and in RGB we need to
        # convert it to numpy array and BGR
        # so we can write it to the disk
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        today = time.strftime("%d-%m-%Y %H-%M-%S", time.localtime())
        # writing it to the disk using opencv
        filename = "image"+today+".png"
        # print(filename)
        cv2.imwrite(filename, image)
        return 0

def stopper():
    try:
        os.execl(sys.executable, sys.executable, *sys.argv)
    except:
        print(os.error)

def starter():
    global running
    running=True
    return 1
   
 
root = Tk()
root.geometry("500x500")  #size of panel
frame = Frame(root)
frame.grid(column=3,row=0)


 
label = Label(frame, text = "Screen Shooter") #lable
label.grid(column=5,row=1)

label2=Label(frame, text = "Enter secs", anchor='c', pady=120) #lable
label2.grid(column=4, row=2)

sec=StringVar()
seconds = Entry(frame ,textvariable = sec) #input box
seconds.grid(column=5, row=2)



# buttons 
button1 = Button(frame, text = "Start", command=starter).grid(column=3, row=3)
button2 = Button(frame, text = "Stop", command=stopper).grid(column=5, row=3)

 
root.title("Screen Shooter")

while True:
    if idx % 500 == 0:
        root.update()

    
    if running:
        sec1=int(sec.get())
        sec1=sec1 * 1000
        root.after(sec1,print(sec1))
        screenshot()
        root.update()
        idx += 1
    
        