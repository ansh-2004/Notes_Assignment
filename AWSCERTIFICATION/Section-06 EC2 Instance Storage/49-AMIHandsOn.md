# AMI Hands On 

- Launch the instance , and in the user data write only 
```
#!/bin/bash
# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version) (httpd is apache web server)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
```

- Now when you open the instance using public Ip , you see it is working (it shows **It works!**) This is the basic page from the Apache Web Server
- Now create AMI from it beacuse we want to save the state of our ec2 instance and reuse that ,by going to action and create image, 
- Give image name and leave settings as default
- Now in the AMI image tab , you see your AMI, now click launch instance from that AMI, by giving security group , key pair and so on. 
- In the user data now write only this 
```
#!/bin/bash
# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version)
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
```
- In the script , no need to install httpd as it is already available in our AMI image, which is why we will speed up in the boot up time. 
- Now launch instance , and access using public ip , you see you get your response

```
Hello World from ip-172-31-22-117.ec2.internal

```

- You see , this takes less time than before because in this , boot time will be less as no need to install anything
