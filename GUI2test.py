# This is the same code but with the bluetooth code added onto it.

from tkinter import *
from tkinter import ttk # adds the ttk library
from bluetooth import *

#functions for later use in code
def getMAC(interface='eth0'):
    # return the MAC address of the specified interface
    try:
        str = open('/sys/class/net/%s/address' %interface).read()
    except:
        str = "00:00:00:00:00:00"
    return str[0:17]             # call this function with getMAC('eth0')

def populate_list():
    print('Populate')

# window / gui
window = Tk()
window.title("Welcome to GUI")
window.geometry('950x350') # sets window width to 350 pixels and height to 200 pixels

tab_control = ttk.Notebook(window) # menu/tabs puts tabs on window(gui)

# add tabs here
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

# change tabs settings here
tab_control.add(tab1, text='Connect to HoloLens')
tab_control.add(tab2, text='Send a Message')
tab_control.add(tab3, text='What they see')



# Tab1 widgets
lbl1 = Label(tab1, text='Select local Bluetooth Addresses', padx=5, pady=5).grid(column=0, row=0) #label for tab1
#lbl1.grid(column=0, row=0) moved to side to save room
lbl1_a = Label(tab1, text='Connect to this address?',padx=10, pady=10).grid(column=0, row=3) # adding a labeled frame
lbl2 = Label(tab2, text='Send a message ', padx=5, pady=5).grid(column=0, row=0) # labels for tab2
lbl3 = Label(tab3, text= 'Message from rover', padx=5, pady=5).grid(column=0, row=0) # label that will be changed when message is sent

# bluetooth stuff
print("performing inquiry...")
nearby_devices = discover_devices(lookup_names = True)
print("found %d devices" % len(nearby_devices))

for name, addr in nearby_devices:
    print(" %s - %s" % (addr,name))


#bluetooth addresses on listbox
bt_addresses = Listbox(tab1, height=8, width=50, border=0)
bt_addresses.grid(column=0, row=3, columnspan=3, rowspan=6, pady=20, padx=20) # bluetooth addresses will go here
#create scrollbar
scrollbar = Scrollbar(tab1)
scrollbar.grid(row=3, column=3)
#set scroll to listbox
bt_addresses.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=bt_addresses.yview)




# text entries
textSent = Entry(tab2, width=10).grid(column=2, row=2) # entry for tab 2

# button definitions
def onclick1(): # button function for connectHoloBUtt
    print("Connect button clicked")

# def onclick2(): # definition for clicking send button and updating lbl2 in tab 3
#     print("Send button clicked")
#     res = "Message from SEV: " + txt.get() # format in which user will receive message
#     lbl3.configure(text= res)
#     
# sendMessageButt = Button(tab2, text='Send',command=onclick2).grid(column=3,row=2) # send message button
connectHoloButt = Button(tab1, text='Connect',command=onclick1).grid(column=0,row=10, pady=20) # button on tab1



tab_control.pack(expand=1, fill='both') # have each tab right after the next
print ("Complete") # program has zero errors

#populate data table
populate_list()

window.mainloop() # function calls the endless loop of the window, so the window will wait for interaction until closed
