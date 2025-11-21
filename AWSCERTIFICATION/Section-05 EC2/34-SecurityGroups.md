# Introduction To Security Groups (firewalls)

- Security Groups are the fundamental of network security in AWS
- They control how traffic is allowed into or out of our EC2 instances.
- Security Groups only contain **allow** rules. So we can say what is allowed to go in and to go out.
- Security Groups can have rules that reference either by IP addresses, so where your computer is from or by other security groups. Security groups can reference each other
- Eg, we are on our computer , so we are on the public internet and we are trying to access our EC2 instance from our computer. We are going to create a security group around our EC2 instance that is the firewall that is around it. And then this security group is going to have rules and these rules are going to say whether or not some inbound traffic from the outside into the EC2 instance is allowed. And also if the EC2 instance can perform some outbound traffic so to talk from where it is into the internet.

```
                                                  
                Inbound traffic                 |-------------|----------------|
        www ------------------------------------|--> security |   EC2 Instance |
            <-----------------------------------|--- group    |                |
                  Outbound traffic              |-------------|----------------|

```

# Security Groups Deeper Dive

- Security Groups are acting as a **firewall** on EC2 instances
- They regulate
    - Access to Ports (where the traffic can go through on the instance)
    - Authorised IP ranges - IPv4 and IPv6
    - Control of inbound network (from other to the instance)
    - Control of outbound network (from the instance to other)

## Some important points regarding security group
- Can be attached to multiple instances
- An instance can have multiple security groups too.
- Security groups are locked down to a region / VPC combination. So if you switch to another region , you have to create a new security group and if you have another vpc , you have to recreate the security groups. 
- Security groups live **Outside** the EC2 - if traffic is blocked the ec2 instance won't see it
- It is good practice to maintain one separate security group for SSH access. Because Usually SSH access is the most complicated thing.
- If your application is not accessible (Time out) , then it's a security group issue. 
- If your application gives a **connection refused** error, then it's an application error or it's not lauched
- All inbound traffic is blocked by default. 
- All outbound traffic is authorised by default. 


## How to reference security groups from other security groups. 
- We have an EC2 instance, and it has a security group attached named as **security group 1** and inbound rules is basically saying, I'm authorizing security group number one inbound and security group number two.
- If we launch another EC2 instance and it has **security group two** attached to it, then it can directly connect to our 1st ec2 instance without thinking of IPs
- Similarly if we make another ec2 instance and attached security group 1 with it , then it can also connect to our 1st ec2 instance


## Classic Ports to know for the Exam

- We need to know about SSH or secure shell
    - 22 = SSH (Secure Shell) - log into a Linux instance
- 21 = FTP (File Transfer Protocol) - upload files into a file share
- 22 = SFTP (Secure File Transfer Protocol) - upload files using SSH
- 80 = HTTP - access unsecured websites
- 443 = HTTPS - access secured websites
- 3389 = RDP (Remote Desktop Protocol) - log into a Windows Instance

