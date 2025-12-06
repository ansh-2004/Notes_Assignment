- Go to S3 and create a bucket
- We see region is already selected (US East (N. Virginia) us-east-1)
- Now we need to choose bucket type(not available in all regions but default type is General Purpose). Directory buckets are for a specific type of use case
- Now enter a bucket name which must be unique across all regions **anshgupta-demo-s3-v1**
- Next we have Object ownership, By default ACL is disabled which is recommended settings for the security purpose
    - ACLs disabled (recommended):- All objects in this bucket are owned by the particular account. Access to this bucket and its objects is specified using only policies.
    - ACLs enabled:- Objects in this bucket can be owned by other AWS accounts. Access to this bucket and its objects can be specified using ACLs.
- Now under Block Public Access settings for this bucket
    - leave this enabled so we'll block all public access and we want to have maximum securtiy in our bucket. So only us can upload files to it. 
- Next for bucket versioning, disable it for now
- For default encryption , use server-side encryption with Amazon s3 managed keys. So all my objects are going to be encrypted .
- Enable the bucket key
- Create bucket

- Now this will deploy buckets for all AWS regions, not just the one you're in right now , but all regions. 
```


### ✅ **Why do you see the bucket in every region?**

*   **Amazon S3 is a global service**, but **buckets are region-specific**.
*   When you create a bucket in `us-east-1`, the bucket **physically resides in that region**, but the **S3 console is global**.
*   That’s why you can see the bucket name from any region in the console—it’s just showing your account’s buckets globally.



### ✅ **Does this mean S3 is global?**

*   **S3 service is global**, but **your data is not**.
*   Each bucket is tied to one region for:
    *   **Data residency**
    *   **Latency optimization**
    *   **Compliance**
*   So, S3 is globally accessible, but storage location is regional.



### ✅ **Can you access the bucket from another region?**

Yes!

*   You can **read/write objects from anywhere** using the bucket’s endpoint or ARN.
*   Example:
    *   If your bucket is in `us-east-1`, you can upload/download from `us-west-2` or even from outside AWS.
*   **Why?**
    *   S3 is designed for global access via HTTPS endpoints.
*   **Important:**
    *   Data transfer across regions incurs **cross-region data transfer costs**.
    *   Latency will be higher if you access from far away.



### ✅ **Benefit of global visibility**

*   Easier management: You don’t need to switch regions to see all buckets.
*   But remember: **Operations happen in the bucket’s region**.


### ✅ **Best Practice**

*   For **disaster recovery**, use **Cross-Region Replication (CRR)**.
*   For **performance**, use **S3 Multi-Region Access Points**.

```

- Now go inside your bucket and start uploading objects
- Click on upload and then can add files.Choose coffee.jpg file which is of size 100 kb
- Under the destination tab we see 
```
s3://anshgupta-demo-s3-v1  . It is equivalent to 
    - https://us-east-1.console.aws.amazon.com/s3/buckets/anshgupta-demo-s3-v1?region=us-east-1 
    - It is the address of our bucket
```
- Under the properties you see, the storage classes, tags , metadata and many more but for now keep it default, 
- Upload it
- Now we want to open this object and see if we can open it, click on **open** button and we are able to see our jpg file
- Now try to open with the **Object URL** , we see we can't able to open we get access denied error. This tells that i cannot access my object using this public URL but the URL we open before (using Open buton) is working file . So the difference between these two URL is , the beginning of two URLs is exactly the same, but the rest is very very complicated and long url in the case of Open button because it's called an **S3 pre-signed URL**. Because this URL contains actually a signature that verifies that I am the one making the request, and therefore it has my credentials in it. The public url does not work, but this pre-signed URL with my own credentials works.
- Now go to your bucket, **anshgupta-demo-s3-v1**, create a folder,
    - Enter name of folder images and create it 
- Now i have images folder in my bucket, and within it , i can upload again a file, so upload beach.jpg file . Now you see the destination is now 

```
s3://anshgupta-demo-s3-v1/images/       . It is equivalent to 
    - https://us-east-1.console.aws.amazon.com/s3/buckets/anshgupta-demo-s3-v1?region=us-east-1&prefix=images%2F&tab=objects
```
- Upload this