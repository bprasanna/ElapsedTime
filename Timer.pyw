#!/usr/bin/python

import tkinter
import tkinter.messagebox
import tkinter.font
import time
import sys 
import _thread


from tkinter import *
from time import strftime
top = tkinter.Tk()
top.wm_attributes("-topmost", 1)
timer_stop = 0 

def startCountDown():
   try:
      _thread.start_new_thread( startTimer , ("Thread-1", 2, ) ) 
   except:
      tkinter.messagebox.showinfo( "Error", "Unable to start thread")

def startTimer( threadName, delay):
   global timer_stop
   time_start = time.time()
   hours = 0
   seconds = -1 
   minutes = 0
   prev_second = 0
   current_second = 0

   var7.set(strftime("%H:"))
   var8.set(strftime("%M:"))
   var9.set(strftime("%S"))

   while True:
       try:
           current_second = strftime("%S")
           time.sleep(500/1000.0)
           if prev_second != current_second:
               seconds += 1
               prev_second = current_second

               if seconds == 60: 
                   minutes += 1
                   seconds = 0

               if minutes == 60: 
                   hours += 1
                   minutes = 0 

               var1.set(str(hours) + ": ")
               var2.set(str(minutes) + ": ")
               var3.set(str(seconds) + " ")
               var4.set(strftime("%H:"))
               var5.set(strftime("%M:"))
               var6.set(strftime("%S"))

           if timer_stop == 1:
               timer_stop = 0
               break
       except KeyboardInterrupt:
           break

def stopTimer():
   global timer_stop
   timer_stop = 1


B1 = tkinter.Button(top, text ="Start", command = startCountDown).grid(row=0,column=3);
B2 = tkinter.Button(top, text ="Stop", command = stopTimer).grid(row=1,column=3);

cFont = tkinter.font.Font(family="sans-serif", size=16)

var1 = StringVar()
label1 = Label( top, textvariable=var1, relief=FLAT ,font=cFont).grid(row=0,column=0);
var2 = StringVar()
label2 = Label( top, textvariable=var2, relief=FLAT ,font=cFont).grid(row=0,column=1);
var3 = StringVar()
label3 = Label( top, textvariable=var3, relief=FLAT ,font=cFont).grid(row=0,column=2);

var4 = StringVar()
label4 = Label( top, textvariable=var4, relief=FLAT ,font=cFont).grid(row=1,column=0);
var5 = StringVar()
label5 = Label( top, textvariable=var5, relief=FLAT ,font=cFont).grid(row=1,column=1);
var6 = StringVar()
label6 = Label( top, textvariable=var6, relief=FLAT ,font=cFont).grid(row=1,column=2);

var7 = StringVar()
label7 = Label( top, textvariable=var7, relief=FLAT ,font=cFont).grid(row=2,column=0);
var8 = StringVar()
label8 = Label( top, textvariable=var8, relief=FLAT ,font=cFont).grid(row=2,column=1);
var9 = StringVar()
label9 = Label( top, textvariable=var9, relief=FLAT ,font=cFont).grid(row=2,column=2);

top.title("Elapsed Time")
top.mainloop()
