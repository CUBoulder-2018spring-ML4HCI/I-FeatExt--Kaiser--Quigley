""" sending OSC with pyOSC
https://trac.v2.nl/wiki/pyOSC
example by www.ixi-audio.net based on pyOSC documentation
"""
#Modified for Wekinator by Rebecca Fiebrink


import OSC
import time, random

import pandas as pd
import numpy as np
waka1 = pd.read_json("WakaFlockaBSM0.json")
waka2 = pd.read_json("WakaFlockaBSM1.json")
waka3 = pd.read_json("WakaFlockaBSM2.json")
waka4 = pd.read_json("WakaFlockaBSM3.json")
waka5 = pd.read_json("WakaFlockaBSM4.json")
waka6 = pd.read_json("WakaFlockaBSM5.json")
waka7 = pd.read_json("WakaFlockaBSM6.json")
waka8 = pd.read_json("WakaFlockaBSM7.json")
waka9 = pd.read_json("WakaFlockaBSM8.json")
waka10 = pd.read_json("WakaFlockaBSM9.json")
waka = pd.concat([waka1,waka2,waka3,waka4,waka5,waka6,waka7,waka8,waka9,waka10])
waka_rt = waka[["retweet_count"]].values
"""
note that if there is nobody listening in the other end we get an error like this
    OSC.OSCClientError: while sending: [Errno 111] Connection refused
so we need to have an app listening in the receiving port for this to work properly

this is a very basic example, for detailed info on pyOSC functionality check the OSC.py file
or run pydoc pyOSC.py. you can also get the docs by opening a python shell and doing
>>> import OSC
>>> help(OSC)
"""

print "*******"
print "This program sends 1 random inputs to Wekinator every second."
print "Default is port 6448, message name /wek/inputs"
print "If Wekinator is not already listening for OSC, we will get an error."
print "*******"


send_address = '127.0.0.1', 6448

# OSC basic client
c = OSC.OSCClient()
c.connect( send_address ) # set the address for all following messages

# lets try sending a different random number every frame in a loop
try :
    seed = random.Random() # need to seed first

    for RT in range (0,len(waka_rt)):
        rNum = OSC.OSCMessage()
        rNum.setAddress("/wek/inputs")
        n = RT # get a random num every loop
        rNum.append(n + 0.0) #0.0 here is hack to make it float

        c.send(rNum)
        print "Sent 1 values..."
        time.sleep(1) # wait here 1 second



except KeyboardInterrupt:
    print "Closing OSCClient"
    c.close()
    print "Done"
