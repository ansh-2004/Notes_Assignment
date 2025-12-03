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



---
## About sizes in ASG

### **1. Key Size Parameters in ASG**

An Auto Scaling Group has three main size-related settings:

####  **Minimum Size**

*   This is the **lowest number of EC2 instances** that your ASG will maintain at all times.
*   Even if demand drops to zero, ASG will **never scale below this number**.
*   Example: If `min size = 1`, you will always have at least **one instance running**.



#### **Desired Capacity**

*   This is the **target number of instances** that ASG tries to maintain.
*   It usually starts equal to the minimum size, but you can **manually set it** or let scaling policies adjust it.
*   When you create an ASG, you often set the desired capacity to match your expected workload.
*   Example: If `desired capacity = 3`, ASG will launch or terminate instances to keep **exactly 3 running**.



#### ✅ **Maximum Size**

*   This is the **upper limit** of instances ASG can scale up to.
*   Even if demand spikes, ASG will **never exceed this number**.
*   Example: If `max size = 10`, ASG can scale out up to **10 instances**, but not more.



### **How They Work Together**

*   **Scaling Policies** (based on CPU, memory, or custom CloudWatch metrics) adjust the **desired capacity** dynamically.
*   ASG will **never go below min size** or **above max size**, even if policies suggest otherwise.
*   If desired capacity is outside min/max bounds, ASG automatically adjusts it to fit within the range.



### **2. Interaction with Load Balancer**

*   ASG typically works with an **Elastic Load Balancer (ELB)** or **Application Load Balancer (ALB)**.
*   When ASG launches new instances, it **registers them with the load balancer**.
*   The load balancer then **distributes incoming traffic** across all healthy instances.
*   If an instance fails health checks, ASG replaces it automatically.



### **Example Scenario**

*   **Min size:** 2
*   **Desired capacity:** 4
*   **Max size:** 8
*   If traffic spikes, ASG can scale up to 8 instances (but not more).
*   If traffic drops, ASG can scale down to 2 instances (but not less).
*   Desired capacity will fluctuate between 2 and 8 based on scaling policies.


## Minimum vs Desired capacity

### ✅ **Minimum Size**

*   This is a **hard lower limit** for the Auto Scaling Group.
*   Even if your desired capacity is set to zero or scaling policies suggest fewer instances, ASG will **never go below the minimum size**.
*   It acts as a **safety net** to ensure you always have at least some capacity running (for availability or compliance reasons).

***

### ✅ **Desired Capacity**

*   This is the **current target number of instances** ASG tries to maintain.
*   It can **change dynamically** based on:
    *   Manual updates
    *   Scaling policies (CPU, memory, request count, etc.)
*   ASG will launch or terminate instances to match this number, but **within the min–max range**.

***

### **Why have both?**

*   **Minimum size** ensures you never scale down too far (e.g., to zero), which could cause downtime.
*   **Desired capacity** gives flexibility to adjust based on workload.
*   Example:
    *   Min = 2
    *   Desired = 4
    *   Max = 8  
        → If traffic drops, ASG can reduce desired capacity to 2 (but not below). If traffic spikes, it can increase up to 8.

***

Think of it like this:

*   **Minimum size = baseline guarantee**
*   **Desired capacity = current goal**
*   **Maximum size = upper limit**

