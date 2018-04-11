# TRNG Accelerator
The TRNG accelerator provides an hardware-accelerated True Random Number Generator that exploits electronic noise to provide random bytes.<br/>

## Requirements
+ Access Key (create it within your [AccelStore account](https://accelstore.accelize.com/user/applications))
+ [Python 2.7](https://www.python.org/download/releases/2.7/)

## Quick Start
```bash
# Initialize acceleratorAPI
git submodule update --init --recursive
sudo pip install -r acceleratorAPI/requirements.txt

# Update configuration file
## Set the Access Key, SSH Key, target CSP name and credentials values
vi accelerator.conf

# Run the quickstart script
python quickStart.py
```
The quickStart.py script automatically starts a server hosted by your CSP, load and run the accelerator to generate 1MB of true random data.
data is stored in the "output.bin" file in the results folder.<br/>
<br/>

## Metering
Check the accelerator metering information on your [AccelStore account](https://accelstore.accelize.com/user). 

## Features
+ FPGA-accelerated true random number generation
+ Randomness achieved using electronic noise (better than any software-based random number generation)
+ Remote or local execution facility
+ Simplified API

## Limitations
+ Output data size could not exceed 30GB
+ Some limitations are inherent to the [Accelerator API](https://github.com/Accelize/AcceleratorAPI).

## Expert mode
### Run QuickStart on an already existing instance
```bash
# Run the quickstart script
python examples/quickStartReuseInstance.py ${instance_id}
```
### Local execution on instance
```bash
# Start the Accelerator (with instance creation)
python examples/startAccelerator.py

# Connect to the Instance
ssh -Yt -i ${ssh_key} centos@${instance_ip_address}

# Run the TRNG accelerator
## where :
##      ${parameterFile} is a JSON file containing the number of bytes to generate (example provided in 'examples' folder)
##      ${outputFile} is the output file name where the random bytes will be stored
sudo /opt/accelize/accelerator/accelerator -j ${parameterFile} -o ${outputFile} -m 1

# Stop the Accelerator
python examples/stopAccelerator.py ${instance_id}

```
### Troubleshooting
- [Create an AWS account](https://aws.amazon.com/resources/create-account/)
- [Get an AWS access key](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html)
- [Request an adjustment to the limit of AWS EC2 F1 instances you can launch (0 by default)](http://aws.amazon.com/contact-us/ec2-request) 
- [Create an OVH account](https://www.ovh.co.uk/support/new_nic.xml)
- [Get an OVH acces key ](https://api.ovh.com/g934.first_step_with_api)
## Support and enhancement requests
[Contact us](https://accelstore.accelize.com/contact-us/) if you have any support or enhancement request.
