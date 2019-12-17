from tkinter import *
from tkinter import ttk
from bluetooth import *

window = Tk()
window.title("Welcome to GUI")
window.geometry('950x350')

tab_control = ttk.Notebook(window)

# add tabs here for notebook tool
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

#change tab settings here
tab_control.add(tab1, text='Connect to Hololens')
tab_control.add(tab2, text='Send a Message')
tab_control.add(tab3, text='What they See')

lbl = Label(tab3, text="This is how the message will look like: ")
lbl.grid(column=0, row=2)
lbl1 = Label(tab1, text='Select local Bluetooth Addresses', padx=5, pady=10).grid(column=0, row=0)
