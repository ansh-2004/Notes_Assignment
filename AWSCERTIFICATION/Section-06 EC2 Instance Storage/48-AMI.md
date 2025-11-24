# AMI Overview :- powers our EC2 Instances

- AMI = Amazon Machine Image
- They represent a customization of an EC2 instance. So you can use AMIs created by AWS or you can customize it into your own 
    - You add your own software , configuration, define and set up the operating system  ,set up any monitoring tool ...
    - If we create our own AMI, we are going to get a faster boot time and configuration time because all the software that we want to install onto our EC2 instance is going to be prepackaged through the AMI.

- We can build our own AMIs, and they can be built for a specifc region and they can be copied across region if we wanted to use it and leverage the AWS global infrastructure.
- We can launch EC2 instances from differnet kind of AMIs
    - A public AMI : provided by AWS. Eg, Amazon Linux 2 AMI 
    - Your own AMI : you make and maintain them yourself. There are tools to automate this which you have to do not AWS. 
    - An AWS Marketplace AMI : An AMI that has been made by someone else and potentially sold by someone else. 

## AMI Process (From an EC2 instance)

- Start an EC2 instance and customize it
- Stop the instance to make sure the data integrity is correct
- Then we can build an AMI from it . This will also create EBS snapshots behind the scenes
- Finally , we can launch instances from other AMIs

- Example, we have US-EAST-1A and we can create same instance as US-EAST-1B. How ? We launch the instane in US-EAST-1A , we are going to customize it , then we are going to create an AMI from it and this will be our custom AMI and then in US-EAST-1B , we will be able to launch from that AMI and we'll effectively create a copy of our EC2 instance.
