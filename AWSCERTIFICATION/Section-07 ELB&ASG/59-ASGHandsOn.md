- Create an Auto Scaling group
- Name the auto scaling group **DemoASG**
- Next we need to create a **launch template**. (launch template allows you to create a saved instance configuration that can be reused , shared and launched at a later time. )
    - Name it as **DemoLaunchTemplate**. This template is being used to tell to the ASG how to create EC2 instances within it. The interface of launch template looks very very similar to what we have when we create EC2 instances. 
    - Choose Amazon Linux AMI
    - Choose Instance type
    - You can skip including key pair in launch template
    - For subnets , we will not include this in launch template
        - Subnets are tied to specific Availability Zones (AZs).
        - ASG needs flexibility to launch instances across multiple AZs for fault tolerance.
        - If you hardcode a subnet in the template, ASG can only launch in that AZ → single point of failure.

    - For security group , we can select our existing security group , launch-wizard-1
    - For EBS volume storage, we don't need to do anything
    - In advanced details , we want these instances to start with some user data. So paste the same user data we are using before
    - Create the launch template
- Now choose this DemoLauchTemplate with version 1 where it describes what is going to happen , the type of instance we are going to have, the security groups and so on. 
- Next, we have instance type requirements, we can see , instance type is directly coming from my launch template, we can override this but not do it now. 
- Then for network which is a VPC , and within the vpc we choose the differnet availablity zones where we may want to launch our EC2 instances.
- Then just use **balanced best effort** as an AZ distribution (If launches fail in one Availability Zone, Auto Scaling will attempt to launch in another healthy Availability Zone.)
- Next , we need to choose about load balancing. So we want to attach our ASG to our existing load balancer target group **demo-tg-alb** to automatically attach these new EC2 instances to the target group. 
- For the health check , we have the EC2 health checks always enabled but also turn on ELB health checks so that if my load balancer detects that my EC2 instances are unhealthy, it will automatically terminate them. 
- Next, we have group size, so here we can define the desired capacity as well as the minimum capacity and the maximum capacity. So choose desired capacity of 2. And min is 1 , and max has been automatically adjusted to 2 but we can also change it , so change it to 4. 
- Next we have the ability to have automatic scaling.But for now choose No scaling policies
- Then we ahve instance maintenance policy. choose no policy for simplicity
- Rest is default and go next
- No need notifications and tag. 
- Review it and create  auto scaling group 

```
If you get an error saying "The Max value in VCpuCount cannot be 0 . Then in step 2 , make sure you click on Reset to lauch template"
```

- Now initially we see state is **updating capacity** because we have zero instances in our ASG. But we want two . 
- Go under Instance management and we see two EC2 instances are in the pending state  . In the ui of ec2 instances , we see two instances are running . These have been created by my auto scaling group . 
- So the benefit is that now they are fully managed by my ASG.
- Now go to target group , and we see our target, we have two total targets and these are targets created by auto scaling group . This is due to integrations we that we have defined between the auto scaling group and the load balancer. We are able to have automatically these new EC2 instances registered as targets in our target group. 
- Now in the ASG, if we terminate one of the instance, then my ASG is going to detact that, and because my ASG has desired capacity of two instances, automatically a new instance should appear
- We can check all these in activity history . 
- In next level , we can go around automatic scaling to define scaling policies to automatically increases or decreases the desired capacity over time based on our load and so on. 


---
## Detailed explanation

## ✅ **1. Instance Launch Options**

*   **Launch Template vs Launch Configuration**  
    Launch Template is preferred because it supports:
    *   Multiple versions
    *   Parameter overrides
    *   Advanced features like mixed instance types and spot instances.

*   **Mixed Instances Policy**  
    Allows ASG to use multiple instance types and purchase options (On-Demand + Spot) for cost optimization.



## ✅ **2. Network Settings**

*   **Subnets**  
    You select multiple subnets across different Availability Zones for **fault tolerance**.
*   **AZ Distribution Strategies**
    *   **Balanced Best Effort** (default): Distributes evenly across AZs.
    *   **Prioritized**: Launches in preferred AZ first.



## ✅ **3. Load Balancing**

*   **Attach to Target Group**  
    Ensures new instances automatically register with ALB/NLB.
*   **Health Checks**
    *   EC2 health checks (default)
    *   ELB health checks (recommended for real-world apps)



## ✅ **4. Group Size & Scaling**

*   **Min, Desired, Max Capacity**
    *   Min = baseline
    *   Desired = current target
    *   Max = upper limit
*   **Scaling Policies**
    *   **Target Tracking**: Maintain a metric (e.g., CPU at 50%)
    *   **Step Scaling**: Scale in/out based on thresholds
    *   **Scheduled Scaling**: Scale at specific times (e.g., business hours)



## ✅ **5. Advanced Features**

*   **Instance Refresh**  
    Rolling updates when you change AMI or configuration.
*   **Lifecycle Hooks**  
    Run custom scripts before instance termination or after launch.
*   **Warm Pools**  
    Pre-initialized instances for faster scaling.
*   **Capacity Rebalancing**  
    Redistributes instances if AZ imbalance occurs.



## ✅ **6. Maintenance & Notifications**

*   **Instance Maintenance Policy**  
    Controls how ASG handles unhealthy instances.
*   **Notifications**  
    Send alerts for scaling events via SNS.
*   **Tags**  
    Useful for cost allocation and automation.



### ✅ Why These Matter in Real World

*   **High Availability**: Multi-AZ + health checks prevent downtime.
*   **Cost Optimization**: Mixed instances + spot reduce costs.
*   **Automation**: Lifecycle hooks + scaling policies = zero manual intervention.
*   **Security & Compliance**: Tags and notifications help track resources.
