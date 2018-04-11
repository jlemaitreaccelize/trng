#!/usr/bin/env python
import sys, os, logging

# Add path to accelerator API
sys.path.append('acceleratorAPI/endUserAPI/python')
from acceleratorAPI.acceleratorAPI import *

# Configure logger
console = logging.StreamHandler()
console.setFormatter(logging.Formatter("%(asctime)s - %(levelname)-8s: %(name)-20s, %(funcName)-28s, %(lineno)-4d: %(message)s"))
console.setLevel(logging.INFO)
logging.getLogger().addHandler(console)
logging.getLogger('acceleratorAPI.acceleratorAPI').setLevel(logging.INFO)


# Create Accelerator Handler
print "Creating Accelerator Handler ..."
myaccel = AcceleratorClass(accelerator='secureic_trng')

# Create and Initialize Instance
print "Creating and Initializing Instance (it can take few minutes) ..."
myaccel.start()

# Process
print "Running Random Number Generation ..."
ret, processdict =  myaccel.process(file_out=os.path.join('results', 'output.bin'))

# Stop Accelerator
print "Stopping Accelerator ..."
stopdict = myaccel.stop()

