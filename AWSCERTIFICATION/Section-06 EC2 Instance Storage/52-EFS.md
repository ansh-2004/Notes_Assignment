# EFS - Elastic File System

- Third type of storage you can attach onto an EC2 instance.
- This is a network file system or NFS. So EFS is a managed network file system and it can be mounted to hundreds of EC2 Instances at a time. 
- Before we had an EBS Volume attached to only one EC2 instance at a time but with an EFS drive, you can mount it onto hundreds of EC2 instances.
- So that makes it a shared network file system or shared NFS
- EFS works only with your Linux EC2 Instances and top of it ,it works across multple availability zones. So it is possible for an instance, in one AZ to be attached the same EFS volume as the instance in another AZ
- EFS is highly availbale, scalable , pretty expensive. It's about three times of a gpt2 EBS Volume. 
- But you pay per use and don't plan for capacity so that it means if you store 20 gigabytes of data onto your EFS drive then you're only going to pay for these 20 gigabytes
- Example, we have an EFS file system with a security group and then we have EC2 instances in various availability zones connected to it. So we have EC2 instances in us-east-1a, EC2 Instances in us-east-1b, as well as EC2 instances in us-east-1c and they all connected to the same EFS file system.

## EBS vs EFS

- So , with EBS , say we had EC2 instance in one AZ and another one . Then the EBS volume can only be attached to one instance in one specific AZ and the EBS volumes are bound to specific availability zone. 
- But if we wanted to move over the EBS volume from one AZ to another , we could create a snapshot, it would create an EBS snapshot and then restore that snapshot into a new availablity zone. And effectively we would've moved the EBS volume over. But this is a copy , this is not an in-sync replica

- EFS is a network file system, that means whatever is on the EFS drive, is shared by everything that is mounted to it. 
- Say we have many instances in Availability zone 1 and many instances as well on Availability zone 2. 
- At the same time , all these instances can mount the same EFS drive using a mount target and they will all see the same files. That makes it a shared file system. 

## EFS Infrequent Access (EFS -IA)
- It is a storage class for EFS.
- This storage class is going to be cost-optimized for files that you don't access very often.
- This storage class will give you upto 92% lower cost for storing the data compare to other surge class (EFS standard)
- If you enable EFS-IA , then EFS will automatically move your files to EFS-IA based on the last times they were accessed and something called a lifecycle policy. 
- Example, we have our EFS file system. We have three files in EFS standard and maybe a fourth file in EFS standard which hasn't been accessed for 60 days means no one has either write or read this file . So if you define your lifecycle policy and you enable EFS-IA , then for example , you can say :
    - hey , after 60 days, please move this file to a different storage class which is called EFS-IA which is going to have some cost saving. 
    - This is going to be done automatically, now next time you access this file, it's going to be put back into EFS standard because it's more accesssed more often
- It is very transparent to the applications that means that your applications don't even need to know where the file is if it's an EFS standard or EFS-IA, it will access all these files the same way. It is just behind the scenes , EFS will do some cost optimizations