# Launching an EC2 Instance running Linux
- We'll be launching our first virtual server using AWS Console
- We will launch a web server directly on the EC2 Instance using a piece of code we will pass to the EC2 Instance that is called the user data. 
- We can start/stop/terminate our instance

## Steps:
- Go to EC2 > Instances > Launch Instance
- Name the instance **My First Instance**
- Next , you need to choose a base image for your EC2 instance. This is the operating system of your instance. Choose Amazon Linux 
- Next we need to choose instance type. Instance types are going to differ based on number of CPUs they have, the amount of memory they have and how much they cost. So choose t3.micro 
- Next , a key pair to login into your instance. This is necessary if we use the SSH utility to access our instance . So create a key pair. Give name **EC2 Tutorial**. Choose key pair type RSA and key format .pem (if windows 10 + , linux mac). If less than windows 10 , choose .ppk which use PuTTY for ssh
- Next, In network settings, kept everything default , instance will get a public IP
- Then we need to connect to our instance and for this there is going to be a security group attached to our instance , which is going to control the traffic from and to our instance and therefore we can add rules. The first by default security group created will be **launch-wizard-1** which have rules like
    - allow SSH Traffic from anywhere
    - also allow http traffic from the internet because we are going to launch a web server on our ec2 instance so we need it as well 
- Next configure storage, we see 8 gigabits gp2 root volume
- Next in advanced details , scroll down to User data . It is when we pass a script to execute on the first launch of our EC2 instance
```
#!/bin/bash
# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html

this script is going to update a few things (yum update -y) and then install the HTTPD web server on the machine (yum install -y httpd) and then write a file , an HTML file,  that will be our web server
```

- Next in summary , we want to start one instance , and review everything and then launch it. 

- Once instance state is running, there is instance id which is unique identifier for our instance , Then there is public IPv4 address which we will use to access our EC2 instance.  Then there is private IPv4 address , which is how to access the instance internally on the AWS network , which is private 

- Now to check the web server running on our instance , copy the public IPv4 address and paste on browser . (Note to use with http , not with https). we get this result 
```
Hello World from ip-172-31-22-117.ec2.internal

See this ip shown is private ip 
```

- Now we can stop instance , after stopping instance , it will not be charged 
- Then to get rid of instance , terminate it 
- Also when you stop instance and then start it again , your public IPv4 address will be changed. Private Ipv4 address will not be changed , only public will be changed. 