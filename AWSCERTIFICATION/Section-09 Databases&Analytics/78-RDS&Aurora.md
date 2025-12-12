# Amazon RDS Overview
- RDS stands for Relational Database Service. 
- It is only for relatinal databases so we will be using the SQL language.
- It's a managed database service for databases that will use SQL as a query language. 
- It allow you to create databases in the cloud that will be managed by AWS. 
- These databases can be of different kinds
    - Postgres
    - MySQL
    - MariaDB
    - Oracle
    - Microsoft SQL Server
    - IBM DB2
    - Aurora (AWS Proprietary Database)

## Advantages over using RDS versus deploying DB on EC2
- RDS is a managed database service so :
    - Provisioning the database will be automatic, patching of OS will be done by AWS
    - We will have continuous backups,  restore options with point in time restore (restore to specific timestamp)
    - We'll have monitoring dashboards
    - We'll be able to scale the reads by creating read replicas and improve the read performance. 
    - We will have the way to set up multi AZ to make sure that we're ready to have a plan for disaster recovery against a whole availability zone going down. 
    - We can set up maintenance windows for updgrades
    - We can scale veritcally and horizontally
    - The storage is going to be backed by EBS. 
- Only things we cannot do with an RDS database is that we cannot SSH into your RDS database instance. We are just using the service. AWS manage entirely the database for us so we cannot use the SSH utility to see what's going on within our database. 

## RDS Solution Architecture

- Where does RDS fit in our solution architecture?

- We have our elastic load balancer and it's fronting multiple backend EC2 Instance. They're possibly into an auto scaling group and they need to store and share the data somewhere. And this is structured data, so they're not going to use EBS or EFS, or EC2 Instance store. They will be using a database. And in this example , it is a relational database. So the EC2 instances will be connecting to database and doing rewrites and all at once. So they will be sharing the database in the backend. This is a classic solutin architecture, not just using RDS, but using any kind of database.
- You have the load balancer layer that will be taking the web request, the backend EC2 instances doing the application logic, and the last tier we have database tier doing the reads and the writes of the data. 

# Amazon Aurora
- It is a database technology created by AWS. It is not open source and it works the same way as RDS. 
- We have our EC2 instances connecting directly into an Amazon Aurora. 
- Aurora supports two kinds of database technologies. It supports PostgreSQL and MySQL
- The idea with Aurora is that it's going to be **cloud-optimized**. And so there is a 5X performance improvement over MySQL on RDS and a 3X performance improvement over using Postgres on RDS.
- On top of things, we don't need to worry about the storage of an Aurora database because the storage will grow automatically in increments of 10GigaBytes upto 256 TeraBytes
- Even if Aurora is going to be more expensive than RDS (about 20% more), it is going to be more efficient and more cost - effective.


#### For the exam perspective , RDS and Aurora are the two ways for you to create relational databases on AWS. They are both managed and Aurora is going to be more cloud-native, whereas RDS is going to be running the technologies you know directly as a managed service. 

## Amazon Aurora Serverless
- We also have serverless option for Amazon Aurora. 
- This is where the database instantiation is going to be automated. And you will have autoscaling based on actual usage of your database. 
- So , both PostgreSQL and MySQL are supported as engines of Aurora Serverless database. 
- You don't need to do any kind of capacity planning.
- There is no management because you don't manage servers. 
- You are going to pay per second so it can be a lot more cost-effective than provisioning an Aurora cluster yourself. 
- So this is going to be great when you have infrequent or intermittent or unpredictable workloads

### How it works?
- It connects to a proxy fleet that is managed by Aurora and Aurora behind the scenes is going to instantiate database instances when it needs to scale up or down. And these Aurora databases are going to be sharing the same storage volume no matter what.

```
                                        client
                                          ^
                                          |
                                          |
                                          v
                                    Proxy Fleet 
                                     /   /   |  \
                                    /   /    |   \
                                   /   /     |    \
                                  /   /      |     \
                            Aurora  Aurora Aurora Aurora

                            <-----Shared Storage Volume-------->
                                
```

- So from exam perspective, if you see Aurora with no management overhead and so on, think of Aurora serverless