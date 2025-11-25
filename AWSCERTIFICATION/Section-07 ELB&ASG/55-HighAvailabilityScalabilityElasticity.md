# Scalability & High Availability

# Scalability

- So, if your applications can scale, that means that it can handle greater loads by adapting.
- There are two kinds of scalability in the cloud:
    - Vertical Scalability
    - Horizontal Scalability also called **elasticity**.
- Scalability is going to be linked, but different to High Availability.

- Imagine, we have a call center and we just receive calls, now see what it means to be scalable in that case. 

## Vertical Scalability
- In AWS , when you are vertically scalable, that means that you can increase the size of the instance.
- So for our call center, say we have a junior operator and say we were able to upgrade that operator , we would get a senior operator. And a senior operator can handle a lot more calls than the junior operator because it's more experienced. So this would be what vertical scalability looks like in a call center. 
- So in AWS, for example, say your application runs on the t2.micro, and to do a vertical scalability for that application, that means that now we run our application on a t2.large. So we've changed the size of our EC2 instance. 
- Vertically scalability is very common when you have a non-distributed system, such as database. If you want to give more performance to your database, you would just increase the size of your database.
- But usually with vertically scalability, there is a liimt to how much you can vertically scale and that is a limit of the hardware. 

#### In simpler terms
- Vertical scalability (also called scaling up) means increasing the power of a single machine — more CPU, more RAM, more storage — instead of adding more machines.
- Analogy (Call Center): Upgrading a junior operator to a senior operator. Same person (same machine), but now they can handle more calls (more workload).
- In AWS, this usually means changing the instance type of your EC2:
    - Example: Start with a t2.micro (small, low resources).
    - Scale up to a t2.large (same application, but more CPU and memory).
- You don’t change your architecture — you just give the same server more horsepower.
- Example: A single MySQL database running on one EC2 instance. If it needs more performance, you scale vertically by moving it to a bigger instance type.
- This is simpler than redesigning the system to run across multiple servers.
- Hardware limits: You can only scale up to the largest instance AWS offers.
- Cost efficiency: Bigger instances are more expensive, and at some point, scaling horizontally (adding more servers) is cheaper.


## Horizontal Scalability
- Instead of increasing the size of your EC2 instance, you increase the number of instances or systems (independent copies of your application environment) for your application.
- So for our call center, we have an operator and we want to do horizontal scalability for that opearator, that means we will add another operator. And if we need to handle more calls, we will add another operator and so on, so maybe we can scale horizontally from one operator all the way to six operator. 
- So when you have horizontal scaling, then you need to have a distributed system. And for call center, that makes sense, you don't need these people to be talking constantly. For a call center, each of the individual operators can take calls on their own. In AWS , or for web applications, this is going to be very common , So if you have a web application or a modern application, you usually desing it with horizontal scalability in mind. 
- Example:
    - You have a web app running on one EC2.
    - To handle more traffic, you launch 5 EC2s, each running the same app.
    - Together, those 5 EC2s form multiple “systems” serving the same application.

- Not all applications can simply be copied to multiple servers. For horizontal scaling, the app must be stateless or distributed:
    - Stateless apps: Each server can handle requests independently without needing to know what other servers are doing.
        - Example: A web server that just serves HTML pages — any server can respond to any user.
    - Distributed apps: If the app needs shared state (like a database), it must use replication, clustering, or load balancing so multiple servers can coordinate.
        - Example: A database cluster where writes are replicated across nodes.
- Meaning: Your app must be architected so that adding more servers actually increases capacity instead of breaking functionality.
- In summary, Horizontal scaling requires distributed design — your app must be able to run on multiple servers at once, either by being stateless or by using clustering/replication for shared state.
- It's easy on AWS to scale with EC2 and auto scaling groups

#### In simple terms
- Horizontal scalability (also called scaling out) means adding more machines (instances) to handle increased workload instead of making one machine bigger.
- Analogy (Call Center): Instead of upgrading one operator to a senior operator (vertical scaling), you hire more operators. Each operator handles calls independently, so the system can handle more calls overall.
- In AWS, this usually means adding more EC2 instances to run your application
- You don’t rely on one big server — instead, you spread the workload across multiple smaller servers.
- AWS makes this easy with Auto Scaling Groups (ASGs):
    - ASGs automatically add or remove EC2 instances based on demand.
    - Example: If traffic spikes on your web app, ASG launches more EC2s. When traffic drops, it terminates extra EC2s to save cost.
- For horizontal scaling to work, your application must be designed to run across multiple servers.
- Each server should be able to handle requests independently without needing constant coordination.
- Examples:
    - Web applications: Each EC2 instance can serve different users.
    - Call center analogy: Each operator takes calls separately.
- Databases are trickier — they often need replication and clustering to scale horizontally.
- Global reach: You can scale across Availability Zones and Regions.


---
# High Availability
- High Availability goes hand in hand with horizontal scaling.
- High Availability means that you are running your application and system in at least two availability zones on AWS.
- But for our call center ,it means that we have a call center in New York and maybe a second call center in San Francisco. And somehow if one of these call centers in down , for example , say there's a power outage in New York, then we can still take calls in San Francisco. And so we are highly available
- The goal of high availability is to survive a data center loss (disaster)



# Summary 
- Vertically Scaling : Increasing instance size (= scale up/down)
    - From t2.nano of 0.5 gigabytes of RAM and one vCPU, all the way to u-12tb1.metal having 12.3 terabytes of RAM and 448 vCPUs

- Horizontal Scaling : Increase number of instances (= scale out/in)
    - Auto Scaling Group
    - Load Balancer
- High Availability : Run instances for the same application across multi AZ
    - This will be again leveraged by an Auto Scaling Group in multi AZ mode. 
    - And Load Balancer in multi AZ


# Scalability vs Elasticity vs Agility

- Scalability : ability for a system to accommodate a larger load by making the hardware stronger (Scale up) , or by adding nodes(scale out). Key idea: You can grow your system to meet demand, but it’s a manual decision.
- Elasticity : Elasticity is something a bit more cloud native. This is once a system is actually scalable, (either by scale up or scale out), Elasticity means that there will be some sort of auto scaling in it so that system can scale based on the load that it's receiving. And in this case, we're going to pay per use, we are going to match the demand we're receiving , with a number of servers, and obviously we are going to pay just the right amount  so will optimize cost. Key idea: Pay‑per‑use efficiency — you only run the resources you need at any given time.

- Agility: Agility is not related to scalability or elasticities. It means that the new IT resources are only a click away, which means that you can reduce the time to make these resources available to your developers from weeks to just minute. And so your organization is more agile, it can iterate more quickly and you are going faster. In AWS, you can spin up servers, databases, or storage in minutes instead of waiting weeks for hardware. A developer needs a test environment → clicks a few buttons → EC2 and RDS are ready instantly.Key idea: Faster innovation cycle — organizations can experiment, iterate, and deliver products quickly.