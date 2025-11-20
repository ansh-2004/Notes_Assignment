# Amazon EC2

- It is one of most popular of AWS offering
- EC2 = Elastic Compute Cloud = Infrastructure as a Service
- It is not just one service, it is composed of many things at high level:
    - Renting Virtual Machines on EC2 called **EC2 instances**
    - Storing data on virtual drives on **EBS volumes**
    - Distributing load across machines (**ELB**)
    - Scaling the services using an auto-scaling group (**ASG**)

 
## EC2 sizing & configuration options
- Operating System (OS) : Linux, Windows or Mac OS
- How much compute power & cores (CPU) on this virtual machine
- How much random-access memory (RAM) you want
- How much storage space :
    - With network-attached(EBS & EFS)
    - Hardware (EC2 Instance store)
- Type of network you want to attach with your ec2 instance. Network Card : speed of the card , Public IP address
- Firewall rules : security group
- Bootstrap script (configure instance at first launch) : EC2 User data

## EC2 User Data
- It is possible to bootstrap our instance using EC2 User data script.
- bootstrapping means launching commands when a machine starts
- That script is only run once at the instance first start
- EC2 User data is used to automate boot tasks such as :
    - Installing updates
    - Installing software
    - Downloading common files from the internet
    - Anything you can think of 
- The more you add into your User Data Script , the more your instance has to do at boot time. 
- The EC2 User Data Script runs with the root user , so any command you have will have the sudo rights 