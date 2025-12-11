# S3 Express One Zone

- It is another type of storage class but different from other ones
- It is high performance , but for a single Availability Zone type of storage class
- It means that your objects are stored not on the standard bucket on S3, but on Directory Bucket which is special type of s3 bucket but this bucket , instead of being distributed across multiple availabilty zone , it is going to be in a single availability zone only. And you get to choose which one it to be in . 
- Because you are in a single AZ , then you're going to be able to handle hundredes of thousands of requests per second with single digit millisecond latency. So very high performance
- You get about 10 times the performance of S3 standard with about 50% lower the cost. 
- So good durability , but the availability is of course lower because now instead of being three availability zones with some replication , you only have one availability zone . And of course , if there is a problem on this AZ, you are going to be directly affected. 
- Idea of using this S3 Express One Zone is that you're gonna be able to co-locate your storage and compute resources in the same availability zone and therefore reduce latency and maybe even reduce your networking cost. 
- **Use cases** : Latency-sensitive apps, data-intensive apps, for AI&ML Training, financial modeling , media processing , HPC
- Best integrated with , for example, Sage Maker Model Training, Athena , EMR, Glue all these kind of data services. 