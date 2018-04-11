# TRNG Accelerator
The TRNG accelerator provides an hardware-accelerated True Random Number Generator that exploits electronic noise to provide random bytes.<br/>

## Features
+ FPGA-accelerated true random number generation
+ Randomness achieved using electronic noise (better than any software-based random number generation)
+ Compliant with NIST FIPS SP-800 90B and BSI AIS 31 industrial standards
+ Remote or local execution facility
+ Simplified API

## Requirements
[Check the AcceleratorAPI requirements](https://github.com/Accelize/acceleratorAPI/blob/master/readme.md#requirements)

## Installation

- Git clone the trng repository
  - This will clone the [accelerator API](https://github.com/Accelize/AcceleratorAPI)
  - This will install AcceleratorAPI related modules using pip
  ```sh
  git clone --recursive https://github.com/Accelize/trng
  cd trng
  pip install -r acceleratorAPI/requirements.txt
  ```

## Getting started - Remote mode

The trng git repository conveniently contains:
- a universal Python API to execute any AccelStore-compliant accelerator
- a pre-built example to run the trng accelerator


#### 1. Edit the [configuration file](accelerator.conf) with your Access Key, SSH Key, target CSP name and credentials
```sh
 vi accelerator.conf
```
[Description of the configuration file ](https://github.com/Accelize/acceleratorAPI/blob/master/docs/api-guide/configuration_file.md)



##### 1.a [optional] [run configuration check](#script-quickstartpy) 
    python quickStart.py


#### 2. Execute the accelerator
```python
    python
    from acceleratorAPI.acceleratorAPI import *
    myaccel = AcceleratorClass(accelerator='secureic_trng')
    myaccel.start()
    myaccel.process(file_out='results/output.bin')
    #... Repeat 
    myaccel.process(file_out='results/output2.bin')
    myaccel.stop()
```
#### 3. Inspect output file 

- Check this accelerator statistic and the results files

#### 4. Check the metering information on your [AccelStore account](https://accelstore.accelize.com/user/applications). 

[Advanced mode available](https://github.com/Accelize/acceleratorAPI/blob/master/ocs/tutorial/)

## Getting started - Local execution on instance

#### 1. [Start](examples/startAccelerator.py) the Accelerator (with instance creation)
```sh
 python examples/startAccelerator.py
```
#### 2. Connect to the Instance
```sh
 ssh -Yt -i ${ssh_key} centos@${instance_ip_address}
```

#### 3. Run the TRNG accelerator
```sh
## where :
##      ${parameterFile} is a JSON file containing the number of bytes to generate (example provided in 'examples' folder)
##      ${outputFile} is the output file name where the random bytes will be stored
sudo /opt/accelize/accelerator/accelerator -j ${parameterFile} -o ${outputFile} -m 1
```
#### 4. [Stop](examples/stopAccelerator.py) the Accelerator
```sh
 python examples/stopAccelerator.py ${instance_id}
```

## quickStart.py explanation 
The quickStart.py script automatically starts a server hosted by your CSP, load and run the accelerator to generate 1MB of true random data.<br/>
Data is stored in the "output.bin" file in the results folder.<br/>
<br/>

## Metering
Check the accelerator metering information on your [AccelStore account](https://accelstore.accelize.com/user). 



## Limitations
+ Output data size could not exceed 30GB
+ Some limitations are inherent to the [Accelerator API](https://github.com/Accelize/AcceleratorAPI).



## Troubleshooting
- [Create an AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start)
- [Guide to Create an AWS Access Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
- [Create an OVH account](https://www.ovh.com/fr/support/new_nic.xml?redirectTo=https%3A%2F%2Fwww.ovh.com%2Fmanager%2Fcloud%2F%23%2F)
- [Guide to Create an OVH Access Keys](https://docs.ovh.com/ie/en/public-cloud/configure_user_access_to_horizon/)
- [Request an adjustment to the limit of AWS EC2 F1 instances](http://aws.amazon.com/contact-us/ec2-request) you can launch (0 by default)
- [Documentation on configuration file](https://github.com/Accelize/acceleratorAPI/blob/master/ocs/api-guide/configuration_file.md)
- [Documentation on python API ](https://github.com/Accelize/acceleratorAPI/blob/master/docs/api-guide/acceleratorclass.md)

## Support and enhancement requests
[Contact us](mailto:support@accelize.com) if you have any support or enhancement request.
