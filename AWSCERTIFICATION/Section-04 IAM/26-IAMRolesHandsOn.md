# IAM Roles

- Go to IAM > Roles 
- You will see some roles may have already been created for your accounts
- We are going to create our own role 
- So role is a way to give AWS entities permissions to do stuff on AWS. 
- there are different type for which you can create role for like for AWS SERVICE, for AWS account, For web identity , and more
- We choose AWS Service
- Then we need to choose for which aws service or use case  we want this role to apply to. Lets choose EC2
- Now we need to choose different use cases for ec2 but Select just EC2 which allows ec2 instances to call AWS services on your behalf. 
- Next , we need to attach a permission policy, we choose IAMReadOnlyAccess to allow my ec2 instance to read whatever is in my IAM. 
- Next , give the role name , description and review it 
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"  
            ],
            "Principal": {
                "Service": [
                    "ec2.amazonaws.com"
                ]
            }
        }
    ]
}

In this action , sts:AssumeRole meaning , the entity with this policy is permitted to call the AssumeRole API, which grants temporary security credentials for the role being assumed.

sts:AssumeRole : Refers to the AWS Security Token Service (STS) operation that lets a principal (user, application, or service) assume an IAM role.

Why It’s Important
Temporary credentials: Instead of using long-term access keys, STS issues short-lived credentials.

Cross-account access: Enables users or services in one AWS account to access resources in another account securely.

Delegation: Allows applications or services to act with the permissions of a role, without needing permanent IAM users


This trust policy is typically attached to an IAM role for EC2.

When you launch an EC2 instance and attach this role, the instance can automatically obtain temporary credentials.

Those credentials allow the instance to access AWS services (like S3, DynamoDB, CloudWatch) according to the permissions defined in the role’s permission policy.

So, this trust policy is the "who can assume the role" part, while the role’s permission policy defines "what they can do once they assume it."

```

- 