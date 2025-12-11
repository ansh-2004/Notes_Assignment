# S3 Storage Classes

- Amazon S3 Standard - General Purpose
- Amazon S3 Standard-Infrequent Access (IA)
- Amazon S3 One Zone-Infrequent Access
- Amazon S3 Glacier Instant Retrieval
- Amazon S3 Glacier Flexible Retrieval
- Amazon S3 Glacier Deep Archive
- Amazon S3 Intelligent Tiering


---
- When you create an object in Amazon S3 , you can choose its class, you can also modify its storage class manually or you can use Amazon S3 Lifecycle Configurations to move objects automatically between all these storage classes. 

# Concept of Durability and Availability

## Durability
- It represents how many times an object is going to be lost by Amazon S3. So Amazon S3 has a very high durability(11 9's , 99.999999999%) 
- That means that on average if you store 10 million objects on Amazon s3, you can expect to lose a single object once every 10000 years.So it's quite durable
- The durability is the same for all storage classes

## Availability
- It represents how readily a service is.
- This depends on the storage class.
- For example, S3 standard has 99.99% Availability . That means that about 53 minutes a year,the service is not going to be available. That means that you will get some errors when you deal with the service. 

## Cost trade-off: Cheaper storage classes = lower availability or slower retrieval.
---

# Amazon S3 Standard - General Purpose
- 99.99% Availability
- Used for frequently accessed data. This is the kind of storage you use by default. 
- Low latency and high throughput.
- Sustain 2 concurrent facility failures on the side of AWS
- Use cases :- Big Data Analytics, mobile and gaming applications , content distribution

# Infrequent Access
- This is data that is going to be less frequently accessed but required rapid access when needed.
- Lower cost than S3 Standard but you will have a cost on retrieval

## - Amazon S3 Standard-Infrequent Access (IA)
    - 99.9% Availability 
    - Use case: Disaster Recovery , backups
## - Amazon S3 One Zone-Infrequent Access
    - High Durability (99.999999999%) in a single AZ, data lost when AZ destroyed
    - 99.5% Availability
    - Use cases: Store secondary copy of backups of on-premises data, or data you can recreate.

# Glacier Storage Classes
- It is low cost object storage meant for archiving and backup. 
- Pricing : pay for the storage + pay for retrieval cost 

## - Amazon S3 Glacier Instant Retrieval
- Millisecond retrieval , great for data accessed once a quarter
- Minimum storage duration of 90 days
- So this is a backup but you need to access it within milliseconds
## - Amazon S3 Glacier Flexible Retrieval( formerly Amazon S3 Glacier)
- You have **expedited** where you get the data back between one and five minutes. You have **standard** to get the data back between three to five hours, or **bulk** which is free, where you get data back between five to 12 hours. 
- Minimum storage duration of 90 days

##### So Instant means you retrieve data instantly and flexible means that your are willing to wait up to for example 12 hours to retrieve your data. 

## - Amazon S3 Glacier Deep Archive - for long term storage. 
- **Standard** (12 hours) , **Bulk** (48 hours). So you may be ready to wait a lot of time to retrive the data .
- It is going to give you the lowest cost. 
- Minimum storage duration of 180 days


# Amazon S3 Intelligent Tiering

- It is going to allow you to move objects between excess tiers based on usage patterns 
- And for this , you are going to incur a small monthly monitoring fee, and auto tiering fee.
- There are no retrieval charges in S3 Intelligent Tiering
- So there is the **Frequent access tier** that's automatic the default tier
- Then we have the **Infrequent Access tier** automatic as well for objects not accessed for example for 30 days
- Then we have **Archive Instant Access Tier** automatic as well for objects not accessed over 90 days. 
- Then we have **Archive Access tier (optional)** you can configure it from 90 days to 700+ days
- Then we have **Deep Archive Access Tier (optional)**  you can configure for objects that haven't been accessed between 180 days to 700+ days