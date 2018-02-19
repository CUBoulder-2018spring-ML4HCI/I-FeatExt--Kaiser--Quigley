""" sending OSC with pyOSC
https://trac.v2.nl/wiki/pyOSC
example by www.ixi-audio.net based on pyOSC documentation
"""
#Modified for Wekinator by Rebecca Fiebrink



import OSC
import time, random
import pandas as pd
import numpy as np
gucci1 = pd.read_json("gucci10170.json")
gucci2 = pd.read_json("gucci10171.json")
gucci3 = pd.read_json("gucci10172.json")
gucci4 = pd.read_json("gucci10173.json")
gucci5 = pd.read_json("gucci10174.json")
gucci6 = pd.read_json("gucci10175.json")
gucci7 = pd.read_json("gucci10176.json")
gucci8 = pd.read_json("gucci10177.json")
gucci9 = pd.read_json("gucci10178.json")
gucci10 = pd.read_json("gucci10179.json")
gucci = pd.concat([gucci1,gucci2,gucci3,gucci4,gucci5,gucci6,gucci7,gucci8,gucci9,gucci10])
gucci_rt = gucci[["retweet_count"]].values
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

    for RT in range (0,len(gucci_rt)):
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
