# How to SSH into your EC2 Instance 

## Windows

- We will configure all the required parameters necessary for doing SSH o windows using the free tool Putty. 

- Go on google and download **putty**
- PuTTY does not understand .pem files. You must convert the .pem file into .ppk using PuTTYgen if you want to connect to your EC2 instance from Windows using PuTTY.
- We have two thins on Putty , Putty app as well as PuTTYgen. And in case you did not download your file in the PPK format, you can actually generate the PPK format from the PuTTYgen.
- load the .pem file in the PuTTYgen. After you can save it as Private Key. Now you have successfuly converted PEM file into PPK format.
- Next we need to set up Putty to access our EC2 instance. Open the Putty app .
- Enter the host name or an IP address of where we are trying to connect. So copy the public IPv4 address from our EC2 Instance and paster here . In the Saved Sessios, Type EC2 Instance and save. 
- It will show error as you need to provide the secret key , for this go to auth and load the ppk file you converted. 


## Windows 10 (same steps as linux/mac)

- In windows 10 , we can use SSH command , open powershell or cmd
- Be in the directory where your .pem file is there
- next enter the same command we use for linux / mac. 
- To exit , either type exit or ctrl + D