# How to SSH into your EC2 Instance

## Linux / Mac OS X

- We'll learn how to SSH into your EC2 instance using Linux/Mac
- SSH is one of most important function when you deal with Amazon Cloud. It allows you to control a remote machine or server , all using the command line or terminal. 
- Eg, we have our EC2 machine and we launched Amazon Linux 2 on it and our machine has a public IP. Now we want to access that machine. And for this we have a security group and on it we allowed the Port 22 of SSH. Now our computer or laptop will access over the web through that port 22, it will access the EC2 machine. Basically , our Command line Interface is going to be just as if we were inside that machine.

- Now we have .pem file downloaded when we create instance. Remove the space in the name of .pem file **EC2Tutorial.pem**. And placed this file in a folder (**let's say aws-course**)

- Now we have an EC2 instance **My First Instance** . We are going to SSH into it. Means we are going to open a remote terminal into it . For this , I need to get the public IPv4 address.

- Next check the security of the instance that there is Port 22 SSH port From anywhere 0.0.0.0/0 inbound rule in the security group attached to the instance. 

- Then open a terminal , and write command 

```
ssh ec2-user@instance_public_IPv4_address


- ec2-user , because Amazon Linux 2 AMI has one user already set up for us and that user is named ec2-user
```

- Now this command will give authentication error because we need to provide .pem file also.
- For this , firstly make sure that terminal should be open in location where .pem file is there i.e, inside **aws-course**

```
ssh -i EC2Tutorial.pem ec2-user@instance_public_IPv4_address
```

- We can get an error unprotected key file and we need to change the permissions for it. 
```
chmod 0400 EC2Tutorial.pem
```

- Now try the same command again as before
```
ssh -i EC2Tutorial.pem ec2-user@instance_public_IPv4_address
```
- Now you finally logged into your machine means you have done SSH into the **My First Instance**

- Try few commands 
```
$ whoami
ec2-user
$ ping google.com

```

- To exit the instance itself , you can either type **exit**  or **CTRL + G** then you will close the connection


---


### 🔎 Command
```bash
ssh -i EC2Tutorial.pem ec2-user@instance_public_IPv4_address
```

---

### 🧩 Explanation of Each Part

- **`ssh`**  
  - Stands for *Secure Shell*.  
  - It’s a protocol and command used to securely connect to remote servers over the network.  
  - Provides encrypted communication between your local machine and the remote EC2 instance.

- **`-i EC2Tutorial.pem`**  
  - The `-i` flag specifies the *identity file* (private key) to use for authentication.  
  - `EC2Tutorial.pem` is the private key file you downloaded when you created the EC2 instance key pair in AWS.  
  - This file proves your identity to the server. Without it, you won’t be able to connect unless you’ve set up other authentication methods.  
  - Important: The `.pem` file must have proper permissions (usually `chmod 400 EC2Tutorial.pem`) so only you can read it.

- **`ec2-user`**  
  - This is the *username* you’re logging in as on the EC2 instance.  
  - For Amazon Linux, the default user is `ec2-user`.  
  - Other AMIs (Amazon Machine Images) have different defaults:  
    - Ubuntu → `ubuntu`  
    - CentOS → `centos`  
    - RHEL → `ec2-user` or `root` depending on setup  
    - Debian → `admin` or `root`  

- **`@`**  
  - Separates the username (`ec2-user`) from the host address (`instance_public_IPv4_address`).  
  - It tells SSH: “Log in as this user on that machine.”

- **`instance_public_IPv4_address`**  
  - This is the *public IP address* assigned to your EC2 instance.  
  - Example: `54.210.123.45`  
  - It’s how your local machine knows where to connect on the internet.  
  - If your instance only has a private IP (inside a VPC), you won’t be able to connect directly from the internet without a bastion host or VPN.

---

### ⚙️ What Happens When You Run It
1. Your local machine starts an SSH session.  
2. It uses the private key in `EC2Tutorial.pem` to authenticate against the EC2 instance.  
3. AWS checks that the key matches the public key stored on the instance.  
4. If successful, you’re logged in as the `ec2-user` on that remote server.  
5. You now have a secure terminal session to run commands on the EC2 instance.

---

### 🛡️ Security Notes
- Always keep your `.pem` file safe — it’s like a password.  
- Restrict file permissions (`chmod 400`) so only you can read it.  
- Use Security Groups in AWS to allow SSH (port 22) only from trusted IPs.  

---

👉 In short: This command securely logs you into your EC2 instance using your private key file, the default user (`ec2-user`), and the instance’s public IP address.

