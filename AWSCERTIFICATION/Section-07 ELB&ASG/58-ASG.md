# What's an Auto Scaling Group?

- We have an application that can be load balaced through a load balancer, but how do we create , automatically these servers in the backend. For these we can use an auto scaling group . 
- In real-life, the load on your websites and application can change over time. Like we can say we have more load on our website during the day and less load during night.
- So in the cloud we know we can create and get rid of servers very quickly and so the goal of an auto scaling group is to 
    - Scale out :- that means add EC2 instances to match an increased load
    - Scale in :- that means remove EC2 instances to match a decreased load
    - With this , we can ensure that we have, a minimum and maximum number of machines running at any point of time. 
    - Once the auto scaling group does create, or remove EC2 instances , we can make sure that these instances will be registered, or de-registered into our load balancer. So these two things work hand in hand
    - Finally, in case one of our servers becomes unhealthy, maybe there's an application bug, then the auto scaling group can detect it , de-register it,terminate it and replace it by a new healthy one. 
- Cost Savings:- We are only running all the time at the optimal capacity

## Auto Scaling Group in AWS
- If we look at our auto scaling group in AWS, we have a minimum size, maybe it's one EC2 instance. 
- Then there is a setting called desired capacity, which is also usually the acutal size of your auto scaling group 
- And then you can define a maximum size of your auto scaling group and automatically your ASG can scale out or scale in  as needed. 
- It work hand in hand with a **load balancer**

## Auto Scaling Group in AWS With Load Balancer
- It means that if we have our auto scaling group , for example with one EC2 instance, web traffic can be coming in through our load balancer, which will be redirecting the traffic, directly into your EC2 instance and as our auto scaling group scales out by adding EC2 instances, the load balancer will have them registerd and will send traffic to them as well . So as we add on more and more EC2 instances, the load balancer distributes more and more of the traffic, all the way to the maximum size of your auto scaling group if it scales all that point. 
