#!/usr/bin/env python
import sys, os, logging

# Add path to accelerator API
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_PATH,os.pardir,"acceleratorAPI")))
from acceleratorAPI import *

# Configure logger
console = logging.StreamHandler()
console.setFormatter(logging.Formatter("%(asctime)s - %(levelname)-8s: %(name)-20s, %(funcName)-28s, %(lineno)-4d: %(message)s"))
console.setLevel(logging.INFO)
logging.getLogger().addHandler(console)
logging.getLogger('acceleratorAPI.acceleratorAPI').setLevel(logging.INFO)

# Parse args
if len(sys.argv) != 2:
    print "One argument neeeded : 'instance_id'"
    sys.exit(1)

# Create Accelerator Handler
print "Creating Accelerator Handler ..."
myaccel = AcceleratorClass(accelerator='secureic_trng', instance_id=sys.argv[1])

# Connecting to Instance
print "Connecting to Instance ..."
myaccel.start(stop_mode=KEEP)

# Process
print "Running Random Number Generation ..."
ret, processdict =  myaccel.process(file_out=os.path.join('results', 'output.bin'))

