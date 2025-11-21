- Under the Network & Security Tab, we have security Group .
- In this , we see we have 2 security group , one is default security group  created by default and the **launch-wizard-1** security group which was created when we created our EC2 instance. 
- In this we have inbound rules which are the rules that allow connectivity from the outside into the EC2 instance. Here we have 2 inbound rules. The first one is of type SSH, which allows port 22 in our instance from anywhere 0.0.0.0/0. The second one is HTTP which allows port 80 from anywhere IPv4 0.0.0.0/0

- Next, we have outbound rule , which allow all traffic on IPv4 to anywhere. So this allow our ec2 instance to get full internet connectivity anywhere. 