# EC2 Instance Types 

- You can use differnet types of EC2 instances that are optimised for different use cases (https://aws.amazon.com/ec2/instance-types/) and they have different types of optimization. 


- we have different types of EC2 Instance
    - General Purpose
    - Compute Optimized
    - Memory Optimized
    - Accelerated Computing
    - Storage Optimized
    - HPC Optimized 

- For each type of instance , we have differnet families

- AWS has the following naming convention:
    - For eg, **m5.2xlarge** instance
    - m : instance class. In this case a general purpose type of instance
    - 5 : generation of the instance(As it improves the hardware over time, it will release a new generation of hardware. So after m5 , if they improve the m type of instance class, then it will go to m6. )
    - 2xlarge : size within the instance class (it starts as small and then large,then 2xlarge, 4xlarge and so on.  ). The more the size , the more the memory,the more the CPU you're going to have on your instance


## EC2 Instance Types - General Purpose

- Great for a diversity of workloads such as web servers or code repositories. 
- They have good balance between :
    - Compute
    - Memory
    - Networking
- We will mostly use t2.micro which is General Purpose EC2 instance

## EC2 Instance Types - Compute Optimized

- Great for compute-intensize tasks that require high performance processors:
    - Batch processing workloads
    - Media transcoding
    - High performance web servers
    - High performance computing (HPC)
    - Scientific modeling & machine learning
    - Dedicated gaming servers
- All these things are tasks that require a very good CPU 
- All the compute optimized instances in EC2 are of C name so c5, c6 and so on

## EC2 Instances Types - Memory Optimized

- Fast performance for workloads that process large data sets in memory (RAM)
- Use cases:
    - High performance, relational/non-relational databases or in-memory databases
    - Distributed web scale cache stores
    - In-memory databases optimized for BI (Business intelligence)
    - Applications performing real-time processing of big unstructured data

- All the Memory Optimized instances are of R series because R stands for RAM.But there is also be X1, High memory and Z1 

## EC2 Instances Types - Storage Optimized

- Great for storage-intensive tasks that require high, sequential read and write access to large data sets on local storage. 
- Use cases:
    - High frequency online transaction processing (OLTP) systems
    - Relational & NoSQL databases
    - Cache for in-memory databases (For example ,Redis)
    - Data warehousing applications
    - Distributed File systems

- These instances start from I or D or H1