## AWS Regions
- AWS has Regions all around the world
- Names can be us-east-1,eu-west-3...
- A region is a cluster of data centers. So many different data centers look at it in near,for example, Ohio, or Singapore, or Sydney , or Tokyo. 
- Most AWS services are region-scoped means if we use a service in one region and we try to use it in another region, it will be like a new time of using the service.

### How to choose an AWS Region?
#### If you need to launch a new application, where should you do it? Should you do it in America, in Europe, in South America , or in Australia?

- **Compliance** with data governance and legal requirements: data never leaves a region without your explicit permission. It is because Sometimes governments want the data to be local to the country you're deploying the application in. 
- **Proximity** to customers: reduced latency. If most of your users are going to be in America, it makes sense to deploy your application in America close to your users, because they will have a reduced latency. 
- **Available services** within a Region: new services and new features aren't available in every Region
- **Pricing** : pricing varies region to region and is transparent in the service pricing page

## AWS Availability Zones
- Each region has many availability zones (usually 3, min is 3, max is 6). Example: Sydney region : ap-southeast-2. We have 3 availability zone is sydney ap-southeast-2a, ap-southeast-2b, ap-southeast-2c

- Each availability zone(AZ) is one or more discrete data centers with redundant power, networking and connectivity. That means that is southeast-2a, i can have two data centers maybe as well and 2 in 2b and 2 in 2c.But it could be one , it could be three , it could be four , we don't really know , it always doesn't tell us that.

- But these availability zones are separate from each other , so that they're isolated from disasters

- These data centers/ availability zones are connected with high bandwidth(Bandwidth is the maximum amount of data that can be transferred over a network connection in a given time.), ultra-low latency (Latency is the time it takes for data to travel from one point to another.) networking and therefore altogether being linked together formed a region.


## AWS Points of Presence (Edge Locations)

- Amazon has 400+ Points of Presence (400+ Edge Locations & 10+ Regional Caches) in 90+ cities across 40+ countries.
- Content is delivered to end users with lower latency

## Tour of AWS Console

- AWS has Global Services: (not Region-scoped)
    Identity and Access Management(IAM)
    Route 53 (DNS service)
    CloudFront(Content Delivery Network)
    WAF(Web Application Firewall)

- Most AWS services are Region-scoped:
    Amazon EC2 (Infrastructure as a Service)
    Elastic Beanstalk(Platform as a service)
    Lambda (Function as a Service)
    Rekognition(Software as a service)


## Shared Responsibility Model Diagram 

- Customer = Responsibility for the security **in** the cloud. Whatever you use in the cloud, however you configure it is your entire responsibility. That includes security , your data, your operating system, your network and firewall configuration.

- AWS = Responsibility for the security **of** the cloud. So all the infrastructure , all the hardware, all the software , all their own internal security they are responsible of. 

## AWS Acceptable Use Policy
- No Illegal , harmful or Offensice use or content
- No security violations
- No Network Abuse
- No E-mail or Other Message Abuse