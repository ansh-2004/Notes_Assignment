# Amazon S3 - Static Website Hosting 

- In this we see , how Amazon S3 can be used to create a static websites.
- S3 can host static websites and have them accessible on the internet
- The website URL will be Depending on the AWS region where you create this, 
    - http://bucket-name.s3-website-aws-region.amazonaws.com
    Or
    - http://bucket-name.s3-website.aws-region.amazonaws.com
- So we have an S3 bucket and it will contain files , maybe HTML files, maybe images and then we're going to enable this to be compatible with hosting a website
- Then the user will access our S3 buckets. But this will not work if we don't have public reads enabled on our S3 buckets.
- So if you have a 403 forbidden error after enabling your s3 bucket for reads, then that means that your bucket is not public. Therefore you must attach an S3 bucket policy that allows it to be public. 

# Hands-On
- Let's enable our bucket to be website. First upload two files beach.jpg and coffee.jpg in the bucket
- Go under properties and at last you will see static website hosting , edit it and enable it
    - In hosting type , select host a static website
    - Next, we need to specify an index document(Specify the home or default page of the website), so write index.html . We need to upload that file 
    - Save this 
    - Upload index.html file 
    - Also remember to give public access to bucket which we have already done in previous file.
    - We now have a bucket website endpoint **http://anshgupta-demo-s3-v1.s3-website-us-east-1.amazonaws.com/**
    - If we right click on image shown in this , we see our public url of our coffee.jpg