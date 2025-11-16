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
