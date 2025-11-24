# Shared Responsibility Model for EC2

## AWS
- AWS is responsible for all data centers, their infrastructure and the security of them. 
- AWS is responsible for making sure you have isolation on the physical host. 
- Replacing faulty hardware if one of the servers if failing. 
- Compliance validation

## User 
- You are responsible for the security in the cloud means you define your own security group rules 
- You own the entire virual machine inside your EC2 instance so that means that your OS , all the patches and the updates you have to do them not AWS
- All the software and the utilities that are installed on this EC2 instance also are yours to be responsible for. 
- IAM Roles assigned to EC2 & IAM user access management
- Data security on your instance