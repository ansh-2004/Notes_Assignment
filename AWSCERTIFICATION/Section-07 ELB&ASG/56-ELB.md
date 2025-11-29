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


---

# 🌐 **What is Load Balancing? (Deep Explanation)**

Load balancing is the process of distributing incoming network traffic across multiple backend servers (EC2 instances in AWS). This ensures that:

* **No single server becomes overloaded**
* **Traffic is handled efficiently**
* **Applications remain available even when some servers fail**

In AWS, this capability is provided by **Elastic Load Balancing (ELB)**.

---

## ✔️ **How a Load Balancer Works**

Imagine your application is hosted on multiple EC2 instances:

```
           Users
        /    |     \
      U1    U2     U3
        \    |     /
       ┌───────────────┐
       │ Load Balancer │  <--- Public entry point (DNS)
       └───────────────┘
        /      |       \
   ┌──────┐ ┌──────┐ ┌──────┐
   │ EC2  │ │ EC2  │ │ EC2  │   <--- Backend servers
   └──────┘ └──────┘ └──────┘
```

### 🧠 What happens during traffic flow?

1. **User sends a request** to the load balancer DNS (e.g., `myapp-123.us-east-1.elb.amazonaws.com`)
2. The load balancer **chooses a healthy EC2 instance**
3. The instance responds to the load balancer
4. The load balancer sends the response to the user

### 🌀 How Load Balancing Helps With Scaling

* With **more users**, the load balancer automatically allocates traffic to multiple backend servers.
* When traffic increases, you can add more EC2 instances.
* When traffic decreases, you can reduce instances and lower costs.

---

# ⭐ **Why Use a Load Balancer? (Expanded)**

### 1️⃣ **Distribute Load Across Multiple Instances**

* Prevents any single server from becoming overwhelmed.
* Ensures the application performs well under heavy traffic.

### 2️⃣ **Single Point of Access (DNS Hostname)**

* Users don't need to know multiple EC2 IPs.
* They access a single endpoint provided by AWS, such as:

  ```
  myapp-1234567890.us-east-1.elb.amazonaws.com
  ```

### 3️⃣ **Automatic Health Checks**

The load balancer constantly performs health checks:

* If an instance is unhealthy (e.g., application crashed), traffic **is automatically stopped** from reaching it.
* Makes your full system more resilient.

Example:

```
EC2-1 : Healthy → Accept traffic
EC2-2 : Unhealthy → No traffic sent
EC2-3 : Healthy → Accept traffic
```

### 4️⃣ **SSL Offloading (HTTPS Termination)**

* The load balancer can handle HTTPS/TLS encryption.
* You upload your SSL certificate to AWS.
* EC2 instances receive **unencrypted** traffic internally (optional).

This:

* Reduces CPU usage on your EC2s.
* Simplifies certificate management.

### 5️⃣ **High Availability Across Availability Zones**

You can place backend EC2 instances in multiple AZs:

```
               Load Balancer
              /              \
      (AZ1) EC2-A1          EC2-A2 (AZ2)
      (AZ1) EC2-B1          EC2-B2 (AZ2)
```

This protects your system if one AZ fails. The load balancer itself is also multi-AZ.

---

# ⭐ **Why Use an Elastic Load Balancer (ELB)?**

Elastic Load Balancing is a **fully managed load balancing service** by AWS. Here’s what that means:

### ✔️ AWS Handles:

* Server provisioning
* Maintenance and patching
* Scaling the load balancer itself
* High availability
* Upgrades and monitoring

### ✔️ You Only Configure:

* Listener ports (e.g., HTTP:80, HTTPS:443)
* Security groups
* Health checks
* Routing rules (ALB-specific)

### 💰 Cost Effective

Running your own load balancer on EC2 means:

* You must manage OS updates
* Handle failover logic
* Configure scaling
* Implement health checks manually

Using ELB reduces operational overhead significantly.

---

# 🧩 **Types of AWS Load Balancers (Full Deep Dive)**

AWS offers **three modern load balancers**, each designed for a specific use case.
The Classic Load Balancer has been retired (2023).

---

# 1️⃣ **Application Load Balancer (ALB)**

**Layer: 7 (Application Layer)**
**Protocols: HTTP, HTTPS, gRPC**

---

## ✔️ ALB Features (Detailed)

### 🔹 **Advanced Routing (Layer 7 Intelligence)**

ALB understands HTTP/HTTPS and can inspect:

* URL paths (`/login`, `/api/*`)
* Host headers (`api.myapp.com`)
* HTTP headers
* Query strings
* Cookies

This allows rules like:

```
/api/* → Target group A (API servers)
/images/* → Target group B (Image servers)
/admin → Target group C (Admin servers)
```

### 🔹 **Supports WebSockets & gRPC**

### 🔹 **Static DNS**

ALBs have a constant DNS name (but IP changes internally):

```
myapp-alb-123456.us-east-1.elb.amazonaws.com
```

### 🔹 **Use Cases**

* Web applications (React, Angular, Laravel, Django)
* Microservices routing
* REST or gRPC APIs
* Serverless (Lambda targets supported)
* Path or host-based routing

---

# 2️⃣ **Network Load Balancer (NLB)**

**Layer: 4 (Transport Layer)**
**Protocols: TCP, UDP, TLS**

---

## ✔️ NLB Features (Detailed)

### 🔹 **Massive Performance**

Handles:

* **Millions of requests per second**
* **Ultra-low latency (sub-millisecond)**

Ideal for:

* Real-time gaming
* Financial systems
* High-frequency trading
* IoT
* Custom TCP/UDP applications

### 🔹 **Static IPs**

Unlike ALB, NLB supports:

* **Static IPv4 addresses**
* **Elastic IP addresses (EIPs)**

This is required for firewalls or on-premises routing.

### 🔹 **TLS Termination Support**

You can offload TLS decryption to NLB.

### 🔹 **Zonal Failover Support**

Traffic can shift between availability zones automatically.

### 🔹 **Use Cases**

* Non-HTTP apps
* Load balancing databases (e.g., MySQL TCP traffic)
* VPN termination
* SIP or VoIP
* Custom network protocols

---

# 3️⃣ **Gateway Load Balancer (GLB / GWLB)**

**Layer: 3 (Network Layer)**
**Protocol: GENEVE (Generic Network Virtualization Encapsulation)**

---

## ✔️ What Makes GLB Different?

GLB is **not for load balancing application traffic**.
It is for balancing **network traffic through virtual appliances**, such as:

* Firewalls (Palo Alto, Fortinet)
* Intrusion Detection Systems (IDS)
* Intrusion Prevention Systems (IPS)
* Deep Packet Inspection tools
* Custom packet analyzers

### 🔹 **How GLB Works (Flow Explained)**

```
User Request
     ↓
Gateway Load Balancer
     ↓  (encapsulates traffic using Geneve protocol)
Security Appliances on EC2 (firewall / IDS)
     ↓  (after analysis, sends traffic back)
Gateway Load Balancer
     ↓
Application Servers
```

### 🔹 Key Concept: **Service Insertion**

GLB inserts security appliances **in the middle of the traffic path** without changing routing logic.

### 🔹 Use Cases

* Enterprise-grade firewalls
* Traffic inspection
* Threat detection
* Compliance requirements
* Multi-tenant firewalling

---

# 📘 Summary Table (Clean Version)

| Feature          | Application Load Balancer (ALB) | Network Load Balancer (NLB)      | Gateway Load Balancer (GLB)                   |
| ---------------- | ------------------------------- | -------------------------------- | --------------------------------------------- |
| Layer            | Layer 7                         | Layer 4                          | Layer 3                                       |
| Protocols        | HTTP, HTTPS, gRPC               | TCP, UDP, TLS                    | GENEVE                                        |
| Routing Features | Path/host-based routing         | None (just forwarding)           | Traffic inspection & appliance load balancing |
| Performance      | High                            | Extremely High (millions of RPS) | Appliance-level                               |
| Static IP        | ❌ DNS only                      | ✔️ Supports Elastic IP           | ✔️ IP mode                                    |
| Use Case         | Web apps, APIs                  | Non-HTTP apps, real-time apps    | Firewalls, IDS/IPS, packet inspection         |

---

# 🎯 Final Notes

* **ALB** → For web apps & APIs
* **NLB** → For fastest performance (TCP/UDP apps)
* **GLB** → For traffic security appliances
* **Classic LB** → Retired in 2023

