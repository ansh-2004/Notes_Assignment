# IAM Roles for our EC2 Instance.

- Connect to the EC2 Instance using either SSH or EC2 Instance Connect
- Now we have to run some IAM Commands. The cool things is that the Amazon Linux 2 AMI we are using right now comes with the **AWS CLI**. So we can start using commands like aws --version , aws iam list-users

```
$ aws --version
aws-cli/2.30.4 Python/3.9.24 Linux/6.1.158-178.288.amzn2023.x86_64 source/x86_64.amzn.2023
```

```
$ aws iam list-users
Unable to locate credentials. You can configure credentials by running "aws configure".


- Need to confire credentials using **aws configure** like we did before when we install aws cli, but this is bad idea because if we run aws configure and enter our personal details onto this EC2 Instance, then anyone else in our accounts could again connect to our EC2 Instance using EC2 Instance Connect and retrieve the value of these credentials in our instance which is not what we want. So we would never have to enter IAM API KEY(Access key id and secret access key id ) into an EC2 instance.

```

- We use IAM rules to solve this problem. 
- We know we have already created a role (demorole in IAM > Roles) which has IAMReadOnlyAccess policy . 
- We are going to attach this role onto our EC2 Instance to provide it with credentials.
- For this , go to your instance, under the security tab , we see there is no IAM role set up . So to set up this go to actions > security > Modify IAM Role.
- Choose demorole and save it . Now this IAM role is attached into our instance. 
- Now in the terminal (EC2 Instance Connect) , if we write command aws iam list-users, we are getting a response around the users from IAM. 

```
$ aws iam list-users

{
    "Users": [
        {
            "Path": "/",
            "UserName": "ansh",
            "UserId": "AIDA4SY7X5IXRXWQPGRIK",
            "Arn": "arn:aws:iam::864965618223:user/ansh",
            "CreateDate": "2025-11-18T05:22:56+00:00",
            "PasswordLastUsed": "2025-11-22T05:41:52+00:00"
        }
    ]
}
```

- Now see , we did not run the command aws configure, we just attached an IAM role and ran this command and it works.
- To verfiy , detach the permissoiin IAMReadOnlyAccess from the demo role in IAM , and run the command again , we will get access denied. 
- So , this is how we provide AWS credentials to our EC2 Instances only through IAM roles. 