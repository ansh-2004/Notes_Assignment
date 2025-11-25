# Shared Responsibility Model For EC2 Storage

### AWS
- Responsible for their infrastructure
- Also because in the technical specification of EBS,EFS, they tell you the data is replicated across many hardware. It is AWS responsibility to perform that replication, so that if one day some hardware is not working, you as a customer is not impacted. 
- Anytime an EBS drive would fail, or one part of it would fail , it is AWS responsibilty to replace that faulty hardware. 
- It is responsibility for aws to ensure that their employees cannot access your data. 

## Customer
- Setting up backup or snapshot procedures so that you don't lose your data. 
- setting up data encrytion is another level of protection to ensure that people cannot have access to your data would it be AWS or other customers of AWS
- Any data you set on the drive is your responsibilty. Anything you write to that disk is your own responsibility
- If you're using an EC2 instance store, you need to understand the risks that are associated with it which is that you can lose the drive if somehow there's a faulty hardware or that if you stop or terminate the EC2 instance that has an instance store, then the data will be lost. So it is your responsibilty to back it up .