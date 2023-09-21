from tkinter import *
from subprocess import *

app=Tk()
app.resizable(width=False, height=False)
app.title('Brightness Control')
app.geometry('350x65')
app.eval('tk::PlaceWindow . center')

def slider_changed(event):
	value = slider.get()
	call("sudo sh -c 'echo " + str(value) + " > /sys/class/backlight/rpi_backlight/brightness'", shell=TRUE)
	call("sudo sh -c 'echo " + str(value) + " > /sys/class/backlight/10-0045/brightness'", shell=TRUE)

slider=Scale(app, length=300, width=17, from_=50, to=250, orient=HORIZONTAL, command=slider_changed)
slider.set(100)
slider.pack()

mainloop()
