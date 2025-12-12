- Till now we see amazon s3 as a standalone service , but it is possible for you to use it in a hybrid cloud type of setting. 

# Hybrid cloud for storage
- AWS wants you to bridge between your on-premises environment to AWS and that's called a hybrid cloud. 
- So part of your infrastructure is going to be on-premises and the rest is going to be on the cloud
- Because sometimes you have created like your on-premises infrastructure first and you are doing a migration but it could be long or for security requirements or compliance requirements. Maybe is's your strategy to have part of it on the cloud and part of it on-premises
- Amazon s3 is a proprietary storage technology. It is not something like the EFS service or NFS service which we can use directly on two servers on-premises. 
- For exposing s3 data on-premises, you have to use **storage gateway**


# AWS Storage Cloud Native Options
### Summarize the storage options on AWS
- The block storage would be EBS or an EC2 instance store.
- The file storage would be a network file system so Amazon EFS
- The Object sotrage storage would be Amazon S3 or Glacier. 
- Storage gatways is going to be bridging your on-premises data and cloud data in AWS. 
    - So your Hybrid Storage will allow your on-premises systems to seamlessly use the cloud to extend the storage capability. 
    - Can be used for disaster recovery , backup and restore or tiered storage

## Types of storage gatway
- File Gateway
- Volume Gatway
- Type gatway

### Under the scene storage gatway will be using Amazon EBS, S3, Glacier behind the scenes