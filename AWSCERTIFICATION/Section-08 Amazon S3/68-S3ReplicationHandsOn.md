- Create a new bucket **anshgupta-demo-v2** in the region **us-east-1**. It will by origin bucket and data will be replicated from this bucket to another bucket
- Enable versioning and create bucket.
- Now create a new bucket **anshgupta-demo-v3** in another region **ap-south-1** which we be our target bucket. Also enable versioning in this .
- Now in the origin bucket , upload a file beach.jpg. Now to setup replication , on the origin bucket , go under management, here we have replication rules, create a replication rule 
    - Name it as **DemoReplicationRule**
    - Set status **Enabled** (This status just ask to Choose whether the rule will be enabled or disabled when created.)
    - For source bucket , we'll leave it as is and in terms of rule scope, we will **apply it to all objects in the buckets**. We also have option to Limit the scope of this rule using one or more filters where You can filter objects by prefix, object tags, or a combination of both
    - Now under destination , we can specify a bucket in this account or another account, For now choose this account.
    - Enter target bucket name and destination region will be automatically identified
    - Now for IAM role ,we need to create a new role for this 
    - We also have some other additional replication options like
        - Replication Time Control (RTC): Replication Time Control replicates 99.99% of new objects within 15 minutes and includes replication metrics. Additional fees will apply
        - Replication metrics: With replication metrics, you can monitor the total number and size of objects that are pending replication, and the maximum replication time to the destination Region. You can also view and diagnose replication failures. CloudWatch metrics fees apply.
        - Delete marker replication: Delete markers created by S3 delete operations will be replicated. Delete markers created by lifecycle rules are not replicated
        - Replica modification sync: Replicate metadata changes made to replicas from the destination bucket to the source bucket. 
- Save it , we get a prompt where we are asked for replicate existing objects .If we say yes , then it enable a one-time Batch Operations job from this replication configuration to replicate objects that already exist in the bucket and to synchronize the source and destination buckets. For now say no 

- No check in target bucket , we see that objects haven't been replicated. So upload a new file (coffee.jpg)in source bucket . Now check in the target bucket , it takes some times in first replication and we see we have coffee.jpg file in our target bucket 
- Version id of the object is same in both source and target bucket. So the versions id are replicated
- If we also want beach.jpg file which we uploaded before enabling replication , need to upload it again
- If we delete files in source bucket , then it will not be deleted in target bucket

---


---

## 🔹 Why a Role is Needed
Replication is not done by *you* directly — it’s done by the **Amazon S3 service itself**.  
- S3 needs permission to **read objects from the source bucket**.  
- S3 also needs permission to **write those objects into the destination bucket**.  
- Since services can’t use your personal IAM user, AWS creates a **special IAM role** that S3 assumes when performing replication.

---

## 🔹 What Happens When You Create the Role
When you set up replication in the console:
1. AWS prompts you to **create a new IAM role** (or use an existing one).  
2. This role has a **trust policy** that allows the S3 service (`s3.amazonaws.com`) to assume it.  
3. The role also has **permissions policies** attached that grant:
   - `s3:GetObject`, `s3:GetObjectVersion`, `s3:GetObjectAcl` on the **source bucket**.  
   - `s3:ReplicateObject`, `s3:ReplicateDelete`, `s3:ReplicateTags`, `s3:PutObjectAcl` on the **destination bucket**.  

So the role acts like a “middleman” — S3 uses it to legally and securely copy data between buckets.

---

## 🔹 Example Role Policy

**Trust policy (who can assume the role):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "s3.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Permissions policy (what the role can do):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObjectVersion",
        "s3:GetObjectAcl"
      ],
      "Resource": "arn:aws:s3:::anshgupta-demo-v2/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:ReplicateObject",
        "s3:ReplicateDelete",
        "s3:ReplicateTags",
        "s3:PutObjectAcl"
      ],
      "Resource": "arn:aws:s3:::anshgupta-demo-v3/*"
    }
  ]
}
```

---

## 🔹 Key Points About the Role
- **Created automatically** if you let the console do it.  
- **Owned by your account**, but only usable by the S3 service.  
- **Critical for replication** — without it, S3 cannot copy objects.  
- **Cross-account replication:** If destination is in another AWS account, the role must also be trusted by that account’s bucket policy.

---

✅ **In short:**  
The role is the “permission slip” that allows the S3 service to act on your behalf — read from the source bucket and write into the destination bucket. Without this IAM role, replication cannot happen.

