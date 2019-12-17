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

lbl1 = Label(tab1, text='Select local Bluetooth Addresses', padx=5, pady=10).grid(column=0, row=0) #label for tab1
lbl1_a = Label(tab1, text='Connect to this address?', padx=5, pady=5).grid(column=0, row=0) #adding a labeled frame

lbl2 = Label(tab2, text='Send a message ', padx=5, pady=10).grid(column=0, row=0) #label for tab2
lbl3 = Label(tab3, text='Howdy ', padx=5, pady=10).grid(column=0, row=0) #label that will change when message is sent

listbox = Listbox(tab1).grid(column=0, row=2) #bluetooth addresses will need to be programmed to show here

txt = Entry(tab2, width=40)
txt.grid(column=1, row=0)

def clicked():
  print("send button clicked")
  res = "Message from SEV: " + txt.get()
  lbl.configure(text= res)
  
def onclick1():#button function fro connectHoloButton
  print("Connect button clicked")
  
btn = Button(tab2, text="Click Me", command = clicked)
btn.grid(column=2, row=0)
connectHoloButt = Button(tab1, text='Connect', command=onclick1).grid(column=0, row=4) # button on tab1

tab_control.pack(expand=1, fill='both') #have each tab right after the next
print("complete") #program has zero errors
  
window.mainloop() # function calls the endless loop of the window, so the window will wait for interaction until closed
  
  
