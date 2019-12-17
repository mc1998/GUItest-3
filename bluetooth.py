# here is some other bluetooth codes that I was able to create using bits and pieces from other resources

from bluetooth import *
# 
# print("performing inquiry")
# 
# nearby_devices = discover_devices(lookup_names = True)
# 
# print("found %d devices" % len(nearby_devices))
# 
# for name, addr in nearby_devices:
#     print(" %s - %s" % (addr,name))
# 



target_name = "HIVE_HOLOLENS_2"
target_address = None # mac address of device

nearby_devices = bluetooth.discover_devices() # code to lookup devices via bluetooth

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break
   
if target_address is not None:
    print ("found target bluetooth device with address "), target_address
    print(target_address) #code prints out device addresses and reassigns the value of target_address
else:
    print("could not find target bluetooth device nearby")
    
