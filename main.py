import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use('TkAgg') #matplotlib backend

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import urllib
import json

import pandas as pd
import numpy as np

LARGE_FONT = ("Verdana", 12)
style.use('ggplot')
#constant configuartion of chart
f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)  # chart divisions


def animate(i):
    pullData = open("sampleData.txt","r").read() #read data
    dataList = pullData.splitlines()
    xList = []
    yList = []
    for data in dataList:
        if len(data) > 1:
            x,y = data.split(',')
            xList.append(float(x))
            yList.append(float(y)) #generate x and y lists for the data
    a.clear()
    a.plot(xList, yList)


class SeaofBTCapp(tk.Tk): #this class inherits from tKinter, it shares the name of the app
    #the baseline for adding pages

    def __init__(self, *args, **kwargs): #whats wanted when i startup, self represents our gui

        tk.Tk.__init__(self, *args, **kwargs) #starts up tKinter too, this is a container

        tk.Tk.iconbitmap(self, default=r"C:\Users\ruebe\Downloads\4810027-200 (1).ico") #must use .ico file
        tk.Tk.wm_title(self, "Sea of BTC client")



        container = tk.Frame(self)  #frame is a window

        container.pack(side="top", fill="both", expand=True) #in the Pack format

        container.grid_rowconfigure(0, weight=1) #"minimum size", "priority"
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} #the different veiws of an application
        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self) #making a frame called F (eg start container)

            self.frames[F] = frame #a frame called f (eg StartPage) is defined by our frame variable

            #in tkinter, empty cells are "ignored" in terms of spacing
            frame.grid(row=0, column=0, sticky="nsew") #a grid is created with North South East West
        #(being the directions the window stretches to from point (0,0)) (wrong)

        self.show_frame(StartPage) #below for info

    def show_frame(self, cont): #takes the frame passed through and raises to top
        frame = self.frames[cont]
        frame.tkraise()  #raises this frame to the top, top be seen/interacted with

def qf(stringtoprint): #"Quick Function"
    print(stringtoprint)


class StartPage(tk.Frame): #this is a frame, it inherits from tk

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) #apparantly same as line 8 and 9, where the parent is "seaofbtcapp"
        label = ttk.Label(self, text="Start Page", font=LARGE_FONT) #we made an object, next is to do stuff
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne)) #make object, make it of the tkinter buttons.
        # Pass: self, the text, and what it runs (command). Use lambda to make a function on the fly bc command
        # loads the function once and forgets... issiue is return statements but oh well

        button1.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One", font=LARGE_FONT)  # we made an object, next is to do stuff
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Next Page",
                            command=lambda: controller.show_frame(PageTwo))

        button1.pack()

        button2 = ttk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))

        button2.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Two", font=LARGE_FONT) #we made an object, next is to do stuff
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Next Page",
                            command=lambda: controller.show_frame(PageThree))

        button1.pack()


        button2 = ttk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))

        button2.pack()

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page Three", font=LARGE_FONT) #we made an object, next is to do stuff
        label.pack(pady=10, padx=10)

        # button1 = ttk.Button(self, text="Next Page",
        #                     command=lambda: controller.show_frame(PageFour))
        #
        # button1.pack()


        button2 = ttk.Button(self, text="Home",
                            command=lambda: controller.show_frame(StartPage))

        button2.pack()


        #matplotlib


        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self) #adds toolbar
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



app = SeaofBTCapp() #define app
ani = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()  #run app NB this only runs because app inherits from (seaofbtcapp which inherets from) tkinter
