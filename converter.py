from tkinter import *

def mile_to_km():
    miles = float(milesInput.get())
    km =round( miles * 1.609)
    textlabel.config(text = km)


window = Tk()
window.title("Mile to km Converter")
# window.minsize(350,350)
milesInput = Entry()
milesInput.grid(column=1,row=0)
mileslabel = Label(text="Miles")
mileslabel.grid(column=2,row=0)
is_equal = Label(text="is equal to")
is_equal.grid(column=0,row=1)
textlabel = Label(text=0)
textlabel.grid(column=1,row=1)
kmLabel = Label(text="km")
kmLabel.grid(column=2,row=1)
calculateButton = Button(text="Calculate",command=mile_to_km)
calculateButton.grid(column=1,row=2)
window.mainloop()