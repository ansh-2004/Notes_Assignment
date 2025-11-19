# IAM Roles for Services

- Some AWS service will need to perform actions on your behalf. And for this to do these actions, they are just like the users, they will need some kind of permissions , so we need to assign permissions to AWS services, To do so , we are going to create what's called an IAM Role. These IAM role will be just like a user, but they are intended to be used not by physical people, but instead they will be used by AWS services.
- **So , assigning permissions to AWS services with IAM Roles**
- For eg, we are going to create EC2 Instance (virtual server). This ec2 instance my want to perform some actions on AWS and to do so , we need to give permissions to our EC2 instance. To do so, we are going to create an IAM Role and together they are going to make one entity and together once the EC2 instance is trying to access some information from AWS, then it will use the IAM role and if the permission assigned to the IAM Role is correct, then we're going to get access to the call we are trying to make .
- Some common roles includes:
    - EC2 Instance Roles
    - Lambda function Roles
    - Roles for CloudFormation


---
- A **role** is an IAM identity that is not tied to a specifc user, Instead it can be assumed by any trusted entity(users, applications , AWS services)
- Purpose:- Provide temporary permissions without needing long-term credentials. 
- How it works:
    - Roles have policies attached
    - A user , service, or application can assume the role to gain those permissions for a limited time. 
- Example:
    - An EC2 instance needs to read from S3. Instead of storing access keys on the server, you assign an IAM role to the EC2 instance. 
    - The instance automatically gets temporary credentials to access S3 securely. 
- Hence, roles are for temporary access (Any trusted entity can assume them , including AWS services)