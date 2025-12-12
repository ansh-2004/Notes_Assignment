# IAM Access Analyzer for S3 

- This is a monitoring features for your Amazon S3 buckets to ensure that only the intended people have access to your S3 buckets.
- It is going to analyze your Bucket Policies, your S3 ACLs, your S3 Access Point policies and is going to surface to you which buckets are going to be publicly accessible, which buckets have been shared with other AWS accounts and so on. 
- The idea is that you can review this and say ,okay, this is normal , this is expected or this looks a bit as a security issue because I did not intend to share this bucket with these people, and therefore you can take action. 
- This is powered by IAM Access Analyzer which allows you to find our resources in your account that are shared with other entities. 