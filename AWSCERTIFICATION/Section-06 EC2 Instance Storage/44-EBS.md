# What's and EBS Volume?

- An EBS (Elastic Block Store) Volume is a network drive you can attach to your instances while they run. 
- It allows your instance to persist data, even after their termination. And so that's the whole purpose. We can recreate an instance and mount the same EBS Volume from before and we will get back our data. 
- They can only be mounted to one instance at a time (at the CCP level)
### Note: CCP - Certified Cloud Practitioner - one EBS can be only mounted to one EC2 instance. Associate Level (Solutions Architect, Developer,SysOps) : "multi- attach" feature for some EBS
- When you create an EBS Volume , it is bound to specific availability zone. That means that you cannot have an EBS Volume in created for example , us-east-1a attached to an instance in us-east-1b
- Analogy : Think of them as a "network USB stick". It is a USB stick that you can take from a computer and put it in another computer but you actually don't physically put it in a computer, it's attached through the network. 

## Summary for EBS Volume
- It's a network drive (i.e, not a physical drive)
    - It uses the network to communicate between the instance and the EBS Volume, which means there might be a bit of latency from one computer to reach to another server. 
    - As EBS Volume are network drive , they can be detached from an EC2 Instance and attahed to another one quickly
- It's locked to a specific Availability Zone. 
    - That means , if it's created in us-east-1a cannot be attached to us-east-1. But we will see that if we do a snapshot then we are able to move a volume across from different availability zones.
- As EBS is a volume , so you have to provision capacity in advance, so you need to say how many  gigabytes you want in advance, and the IOPS , which is IO opeartions per second and you're basically defining how you want your EBS volume to perform. 
    - You are going to get billed for that provision capacity
    - You can increase the capacity over time it you want to have better performance or more size. 

## EBS Volume - Example

- We have us-east-1a, we have one EC2 instance and we can attach , for example , one EBS Volume(10 GB) to that EC2 instance. If we create another EC2 instance(althogh in same AZ), an EBS Volume cannot be attached to two instances at a time at the CCP Level. And therefore this other EC2 instance needs to have its own EBS volume attached to it but it is very possible for us to have two EBS volumes attached to one instance. 
- Now EBS volumes are linked to an availability zone. So if you wanted to have other EBS volumes in other AZ then you would need to create this separately in other availability zone. 
- Also , it is possibly for us to create EBS Volumes and leave them unattached that don't need to be necessarily attached to an EC2 instance, that can be attached on-demand

## EBS - Delete on Termination attribute
- When we create EBS Volumes through EC2 instances , there is this thing called a delete on termination attribute.
- When we create an EBS Volume in the console, when we create an EC2 instance, there is second to last column called delete on termination and by default , it is ticked for the root volume and not ticked for a new EBS volume.
- This controls the EBS Behaviour when an EC2 instance terminates
    - By default , the root EBS Volume is deleted alongside the instance being terminated. (attribute enabled)
    - And by default, any other attached EBS volume is not deleted.  (attribute disabled)
- But this can be controlled by the AWS console/aws cli
- Use case : preserve root volume when instance is terminated to save some data then you can disable delete on termination for the root volume

```
Note:-

About EBS Multi-Attach

While  EBS volumes cannot be attached to multiple instances, but it is not true for io1 and io2 volume types: this is called the EBS Multi-Attach feature.

From an AWS Cloud Practitioner exam perspective this out of scope for the exam.
```