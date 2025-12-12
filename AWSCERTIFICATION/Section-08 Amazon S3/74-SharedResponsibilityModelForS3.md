# Shared Responsibility Model For S3

## AWS
- Responsible for Infrastructure that includes all the things specific to S3 like durability , availability, the fact that it can actually sustain current losses of two facilities. 
- Responsible for their own internal configuration and vulnerability analysis.
- For compliance validation

## User
- You are supposed to set up correctly S3 Versioning to make sure you set up the right S3 Bucket Policy so that the data is protected within your buckets.
- You need to make sure that if you want Replication , you set it up yourself. 
- Logging and monitoring is optional so you have to enable it yourself. 
- You make sure that you are using the most optimal cost storage class that is going to the most cost friendly is also your responsibility. 
- If yo wanted to encrypt your data onto your Amazon S3 bucket that is up to you as well