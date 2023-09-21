#!/usr/bin/env python

from tkinter import *
from Tkinter import *
from subprocess import *

app=Tk()
app.resizable(width=False, height=False)
app.title('Brightness Control')
app.geometry('350x75')
app.eval('tk::PlaceWindow . center')

def slider_changed(event):
	value = slider.get()
	value = int(float(value) * 2.5 + 5.0)
	call("sudo sh -c 'echo " + str(value) + " > /sys/class/backlight/rpi_backlight/brightness'", shell=TRUE)

slider=Scale(app, length=300, width=17, tickinterval=10, from_=10, to=100, orient=HORIZONTAL, command=slider_changed)
slider.set(50)
slider.pack()

mainloop()
