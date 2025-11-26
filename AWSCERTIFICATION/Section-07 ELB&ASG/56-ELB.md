# What is Load Balancing?

- Load Balancer is a server that will forward the internet traffic down to multiple servers(EC2 instances) downstream.
- They're also called the backend EC2 instances. 
- So elastic load balancing is something that is managed by AWS
- So we have load balancer and this is what we will be publicly exposing for our users. And behind that load balancer, we will have multiple EC2 instances. And then we have our first user talking to our load balancer and the load balancer will be directing the traffic to one the EC2 instances. And the EC2 instance will reply back with something and the user will get the response. 
- But now if a second user comes in , then they will get the reply from another EC2 instance and if a third user comes in , it will be replying from another EC2 instance. 
- So the load balancer , the more users we have, the more it will balance the load across multiple EC2 instancs and that will allow us to scale better our backend. 

## Why use a load balancer?
- You can spread load across multiple downstream instances.
- You can expose a single point of access , DNS hostname , for your application.
- You can seamlessly handle the failures of downstream instances.
- So, we do regular health checks on our instances and if one of them is failing , then the load balancer will not direct traffic to that instance. So we can hide the failure of an instance using a load balancer. 
- We can also provide SSL termination, so HTTPS for your websites very easily
- You can able to use load balancer across multiple availability zones which was making your application highly available. 

## Why use an Elastic Load Balancer?
- So ELB is a managed load balancer so you don't need to be a provisioning servers. AWS will do it for you . 
    - AWS will guarantee that it will be working
    - AWS will take care of all the upgrades, maintenance, high availability of that elastic load balancer. 
    - The only thing we have to do is to configure a few things for the behavior of that load balancer
- It is less expensive if you want to set up your own load balancer on EC2 but there will be a lot more effort on your end for maintenance, integration , maintaining and taking care of the OS upgrades etc. 
- 4 kinds of load balancers offered by AWS:
    - **Application Load Balancer** for **HTTP or HTTPS** only traffic which is called a **layer 7 type** of load balancer because it's HTTP and HTTPS
    - **Network Load Balancer** : It's ultra high performance, it allows for **TCP and UDP** actually. And it's **layer 4** because it's lower level , so TCP and UDP
    - **Gateway Load Balancer** : **Layer 3**
    - **Classic Load Balancer** (retired in 2023) - **Layer 4 & 7** . It has been replaced by ALB(application load balancer) and NLB (network load balancer)



| Application load balancer                 | Network Load Balancer                           | Gateway Load Balancer                    |
|------------------------------------------ |:-----------------------------------------------:|:----------------------------------------:|
| Http/HTTPS/gRPC protocols (layer7)        | TCP/UDP protocols (layer 4)                     | Geneve Protocol on the IP packets themselves. (layer 3)  | 
| Http routing features                     | High performance; millions of request per second| Route traffic to firewalls that you manage on EC2 instances       | 
| Static DNS (url)                          | It gives static IP, not static URL through the use of elastic ip | so you can do classic firewall or instrusion detection or deep packet inspection           | 
|The users access your load balancers on one of the protocols and then the load balancer routes traffic to the downstream EC2 instance. For eg, if you've chosen the targets to be EC2    | Architecture same as ALB  | Architecture is little bit complicated so GLB doesnot balance the load to your application. It actually balances the load of the traffic to the virtual appliances that you run on EC2 instances so that you can analyze the traffic or perform firewall operations. That's way is called third-party security virtual appliances. And therefore , the traffic , when it goes to gateway load balancer, first sends the traffic to these ec2 instances that will analyze the traffic. The traffic will be sent back afterwards  to the gateway load balancer and then forwarded back to the applications. So the gateway load balancer here is in the middle to allow us to inspect the IP packets themself and to perform firewall features or intrusion detectioni or deep packet inspection | 



