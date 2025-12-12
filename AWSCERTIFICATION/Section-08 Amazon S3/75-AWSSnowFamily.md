# AWS Snowball

- It is a higly secure and portable device that allows you to collect and process data at the edge and migrate data in and out of AWS. 
- So if you have migration (say petabytes of data), snowball may be a good use case. 

## Two Kinds of Snowball edge devices : Edge Storage Optimized & Edge Compute Optimized. 
- The difference lies in their storage
- Edge storage has 210 TB and edge compute has 28 TB because this is only used for compute


## Data Migrations With Snowball
- It takes a lot of time to transfer some data over a specific bandwidth speed. 
- For example , if you want to transfer a hundred terabytes over one gigabytes per second connection, it would take you 12 days.
- When you have a slow connection , you may have limited connectivity , limited bandwidth ,very high network cost and you have to share the bandwidth with some other applications, the connection may not be stable . So whenever you have these kind of challenges, or if it takes you , for example, over a week to transfer data over the network, the recommendation is to use a snowball device. 

## Idea
- If you upload directly to Amazon S3, it is simple but it may use all you bandwidth
- If you use Snowball, you are going to receive a physical Snowball device in your own infrastructure and then you load it with the data you need and then finally you ship it back to AWS. And then you will be having an export process within AWS to take your data from the snowball onto , for example, Amazon S3
- This is the main use case of a snowball device. Other use case is a **edge computing**

# Edge Computing
- You want to process data while it's being created on an edge location .
- For example , it's a truck on the road or a ship in the sea or a mining station on the ground. 
- These locations may have no internet acccess or limited access to internet or compute power
- So here we order one of these big snowball edge devices and we do edge computing
- And so that means that we have the compute optimized for the search optimized devices. And then because they have computing capability, we can actually run EC2 instances or lambda function directly on these devices. 
- The idea is that once the data is created and processed , we can send it back again to AWS. but by using an edge computing device, we can pre-process the data or we can do machine learning at the edge or directly transcode media at the edge. 


#### Snowball is something that is used for data migrations and edge computing. 


# Hands-On
- First we give job name say **MyImportJob**
- Then choose job type, you want to **import into Amazon S3** where Amazon will ship a snowball device to you and then you send it back to AWS or you want to **export data from Amazon S3** and it gets loaded into the snowball device and then you recieve it  or if you want to just **do edge computing**, you do local compute and storage only.
- Then we have snow devices , so we can choose two of them snowball edge storage optimized with 210 tb or snowball edge compute optimized
- Next you choose pricing option  so on-demad per day pricing
- Next select the storage type s3 data tranfer and then the buckets you want to transfer data back into
- Next security , how do you encrypt your data, how do you access services types where you need to choose a service role and this service role will have access to amazon s3 to allow to create this servicelink role and make sure that our snow device has the right to write to our s3 buckets
- Next you tell shipping address


```
For New Customers
New customers are no longer able to order Snowball Edge devices. AWS suggests considering the following alternatives: 
*For online data transfers*: AWS DataSync automates and accelerates data migration over a network. The AWS Data Transfer Terminal offers a secure physical location for high-speed data transfer using your own storage devices. Additionally, solutions from AWS Partners are available in the AWS Marketplace.
For edge computing workloads: AWS Outposts provides a range of managed solutions that extend AWS infrastructure and services to on-premises or edge locations for a consistent hybrid experience. 
```


## Snowball Edge pricing
- You pay for device usage and data transfer out of AWS 
- If you put data onto your snowball edge and then put that data onto amazon s3 , it is going to be free $0 per gigabytes . So putting data in amazon s3 is free. 
- Next for the pricing of the device itself, there are two levels.
    - On-demand : where you have a one-time service fee per job, so you are going to pay something but as part of the service fee you are going to get 10 days of usage for the 80 terabytes snowball edge storage optimized or 15 days for 210 tb. And then the shipping days are not included towards 10 or 15 days limit. So shipping from it was to you or from you to aws is free. and then just days of usage is counted per days after 10 or 15 days. 
    - Committed upfront : you pay for in advance for monthly , one year, three year usage of snowball edge device for edge computing. You get up to 62% of discounted pricing because you are committing upfront to long-term usage