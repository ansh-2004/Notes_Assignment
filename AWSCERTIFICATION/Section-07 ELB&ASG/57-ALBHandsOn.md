- Before launching a load balacer, we need to send traffic to something, so first we will launch EC2 Instances. 
- So go to launch instances and launch 2 instances(My First Instance and My Second Instance). Also paste the user data which we used before.
- Now if we copy the public ipv4 address and try to access that , we see , there are two different urls to access both, i.e,

```
My First Instance
http://18.204.227.92/  -> Hello World from ip-172-31-64-92.ec2.internal

My Second Instance
http://13.222.8.14/  -> Hello World from ip-172-31-65-80.ec2.internal

```

- No we would like to do is to have only one URL to access these two EC2 instances and balance the load between them . So for this , we are going to use Load Balancer

- Go to load balancer and create a load balancer, you need to select which type of load balancer you want , so choose Application Load Balancer as it is for http/https type of traffic

- Give it name **DemoALB**
- Select scheme **Internet-facing** which  
```
Serves internet-facing traffic.
Has public IP addresses.
DNS name resolves to public IPs.
Requires a public subnet.
```
```
Other scheme is 
**Internal** which 
Serves internal traffic.
Has private IP addresses.
DNS name resolves to private IPs.
Compatible with the IPv4 and Dualstack IP address types.
```
- Keep address type as IPv4
- For network mapping, we need to decide where to deploy the load balancer and how many availability zones. So let's deploy it in all 6 zones . 
- Next we need to assign a security group to our load balancer, So you need to create a new security group for it , and we need to only allow HTTP traffic. So name the securtiy group as **demo-sg-load-balancer**. Give description as Allow HTTP into load balancer. Add inbound rule which is going to allow all HTTP from anywhere. create it.
- Next assign this security group to our load balancer
- Now under listeners and routing, we need to route the traffic from HTTP on port 80 to a target group and the target group is nothing more than a group of my EC2 instances that were created. So need to create a target group , 
- we have differnet target type like instances, ip addresses,lambda function , application load balancer, choose instnaces
- Give it a name, **demo-tg-alb**
- choose protocol HTTP on port 80
- choose address type as IPv4
- Select default vpc 
- choose version of http as 1 
- The health check is good 
- click on next
- Now we need to register our targets , so we're going to register both EC2 instnaces on port 80 and click include as pending below and create the target group 
- Now add this target group to our load balancer under listeners and routing
- Now create load balancer
- Wait untill it is in provisioning state. 
- When it will be active, there is DNS name available for me 
- copy this and paste it in new tab and through the application load balancer, i am able to get a hello world. Now if I refresh the page and keep on refreshing it, you see target is changing. That's because my application load balancer is actually redirecting between both my EC2 instances. 
- If we see targets of our target group , we see they are both healthy that means the application load balancer through the target group is going to send traffic to both of them , one after the other. 
- Now stop one of the instance which makes it unhealthy so cannot respond anymore to the traffic coming in, now check targets in target group , you see my that instance is now show unused




----------------------------------------------------------
# Deep dive: AWS load balancers, target groups, and security groups


## Application load balancer options

### Listener and routing

- **Protocols:**  
  ALB understands Layer 7 (application-level) protocols like HTTP, HTTPS, and gRPC. That means it can look inside requests (paths, headers, cookies) to make smart routing decisions instead of just shuttling packets blindly.  
- **TLS certificates:**  
  For HTTPS, you attach an SSL/TLS certificate to the ALB listener. AWS Certificate Manager (ACM) issues and renews these for you, avoiding manual certificate management. You also choose a TLS policy (sets allowed versions/ciphers) to match your clients’ capabilities and security posture (e.g., modern-only vs. legacy compatibility).  
- **Rules:**  
  ALB applies routing rules in priority order. You can forward based on path (e.g., /api vs. /images), hostnames (foo.example.com), headers, cookies, and query strings. You can also return fixed responses, perform redirects (commonly force HTTP→HTTPS), or split/weight traffic to multiple target groups for canary or multi-service setups.  
- **Stickiness:**  
  Session stickiness uses a cookie to send repeat requests from the same client to the same target. This helps when your app keeps state in-memory per instance. It’s a trade-off: pick a short duration to reduce uneven load and stale sessions; longer durations help stateful apps but can worsen imbalance and failover behavior.

### Scheme and addressing

- **Internet-facing:**  
  An internet-facing ALB has public IPs and a public DNS name people can reach from anywhere. You place it in public subnets (those routing to an Internet Gateway) so traffic can enter from the internet.  
- **Internal:**  
  An internal ALB exposes a private DNS name and private IPs only within your VPC (or connected networks). It’s ideal for microservices or internal apps where clients exist inside the network.  
- **IP address type:**  
  ALB can serve only IPv4 or dualstack (IPv4+IPv6). Dualstack lets IPv6-capable clients connect natively, useful for global reach and modern networks.

### Availability zones and subnets

- **Network mapping:**  
  You choose one subnet per Availability Zone (AZ) to “place” the ALB there. Using more AZs increases resilience: if one AZ fails, the ALB still operates in others.  
- **Cross-zone load balancing:**  
  With ALB, cross-zone is always on and included. Requests are balanced across targets in all enabled AZs, not just within the source AZ, which smooths load distribution and improves utilization.

### Security, visibility, and protection

- **Security groups:**  
  ALBs require security groups (SGs), which act like stateful firewalls. Typically, allow inbound 80/443 only; block everything else. Outbound should be restricted to what targets or services truly need.  
- **Access logs:**  
  ALB can write detailed request logs to S3 (method, path, status, bytes, timings). Enable them when you need analytics, investigations, or compliance evidence; leave off to save cost if unnecessary.  
- **Monitoring:**  
  Core CloudWatch metrics include ELB-side errors (5XX), target response time, and target health counts. ALB also adds tracing headers (like X-Amzn-Trace-Id) that help correlate requests through your stack.  
- **WAF & Shield:**  
  AWS WAF adds Layer 7 protection (block bad patterns, bots, SQLi, XSS). Shield Standard protects against common DDoS automatically; Shield Advanced adds stronger protections and response SLAs for high-risk workloads.

### Performance and behavior

- **Load balancing algorithm:**  
  ALB uses “least outstanding requests,” which is dynamic: it favors targets with fewer in-flight requests, improving latency under uneven workloads. You can still use weighted forwarding across target groups for traffic shaping.  
- **Idle timeout:**  
  Connections inactive longer than the idle timeout are closed. Default is 60 seconds—fine for typical web apps. Increase for long-polling or WebSockets; too short causes unexpected disconnects.  
- **HTTP/2 and gRPC:**  
  HTTP/2 multiplexes multiple streams over one connection and reduces overhead for many small requests. gRPC benefits from streaming and binary framing; enable when clients and services support it to cut latency and improve throughput.

---

## Network and gateway load balancers: when and why

### Quick comparison

| Capability | Application LB (ALB) | Network LB (NLB) | Gateway LB (GWLB) |
|------------|----------------------|------------------|-------------------|
| OSI layer | L7 (HTTP/HTTPS/gRPC) | L4 (TCP/UDP/TLS) | L3 (Geneve encapsulation) |
| Use cases | Web apps, microservices, advanced routing | High-throughput/low-latency, static IPs, TLS passthrough | Inserting third-party/DIY firewalls, IDS/IPS |
| IP addressing | DNS name only | Static IPs via EIP and DNS | VPC endpoints for service chaining |
| Health checks | HTTP/HTTPS | TCP/HTTP/HTTPS | Appliance-driven health probes |
| Security groups | Required on ALB | Not attached to NLB itself (targets use SGs) | SGs typically applied around appliances, not GWLB itself |
| Pros | Rich L7 features, redirects, WAF | Extreme performance, static IPs, TLS terminate or passthrough | Native, scalable traffic inspection |
| Cons | No static IPs, L7 overhead | Limited L7 routing, fewer rule types | Operational complexity managing appliances |

> Sources: This table summarizes platform behavior commonly used in AWS designs.

### Choosing the right type

- **Choose ALB:**  
  When you need content-based routing, redirects, authentication offload, and web-specific protections and features.  
- **Choose NLB:**  
  When performance and static IPs matter most, or you’re handling raw TCP/UDP or TLS without L7 parsing (e.g., databases, custom protocols, IoT).  
- **Choose GWLB:**  
  When you must transparently steer traffic through security appliances (firewalls, IDS/IPS) at scale, without changing client/server configurations.

---

## Target groups in depth

### Target types

- **Instances:**  
  Register EC2 instances by ID. Health checks hit the instance’s port directly. Simple and common for traditional apps.  
- **IP addresses:**  
  Register private IPs, which lets you balance to on-prem servers (via VPN/Direct Connect) or container tasks that aren’t directly mapped to instance IDs. Good for hybrid or custom networking.  
- **Lambda functions:**  
  ALB can invoke Lambda per HTTP request, turning serverless functions into web backends without managing servers.  
- **ALB as target:**  
  You can chain ALBs to build layered routing (fan-in/fan-out), but complexity rises—use only for advanced scenarios where rule composition at a single tier isn’t enough.

### Protocols, ports, and versions

- **Protocols:**  
  Match target group protocol to the load balancer: ALB uses HTTP/HTTPS; NLB uses TCP/UDP/TLS. Pick what your app speaks.  
- **Port:**  
  Targets listen on a specific port. In ECS, tasks often use dynamic ports; the service registers the actual task port in the target group automatically.  
- **HTTP versions:**  
  Targets may speak HTTP/1.1 or HTTP/2. Align with your app stack to avoid downgrade or incompatibilities.

### Health checks

- **Path and success codes:**  
  For HTTP checks, point to a lightweight endpoint like /health returning 2XX. You can extend accepted codes (e.g., include 204 or 301) if your health endpoint behaves differently.  
- **Interval/timeout/thresholds:**  
  - **Interval:**  
    How often checks run. Lower intervals detect failures faster but increase noise and traffic.  
  - **Timeout:**  
    How long to wait for a response. Set just above typical response times to avoid false fail.  
  - **Healthy/Unhealthy thresholds:**  
    Number of consecutive passes/fails required to flip status. Stricter thresholds reduce flapping but delay failover.  
- **Matcher:**  
  Defines which status codes count as “healthy” for HTTP checks. Useful if your health endpoint returns non-200 codes intentionally.

### Attributes and behavior

- **Deregistration delay:**  
  Time the LB keeps sending existing connections to a target after it’s removed, so in-progress requests finish gracefully. Default ~300s; shorter for fast deploys, longer for streaming/long-lived requests.  
- **Slow start mode (ALB):**  
  Newly added targets ramp traffic gradually, letting caches warm or JIT compilation complete. Prevents sudden load spikes on cold instances.  
- **Stickiness (ALB):**  
  Enforces per-target affinity using a target-group cookie. Helpful when state isn’t externalized; disable once you centralize state (e.g., Redis) to improve balancing.  
- **Proxy protocol (NLB):**  
  NLB can prepend connection metadata (client IP/port) to the TCP stream. Your app or reverse proxy must parse it; otherwise, you’ll see garbled traffic.

### Registration and lifecycle

- **Registered vs pending vs unused:**  
  Registered means actively part of load balancing. Pending indicates registration in progress or waiting for health to pass. Unused often means stopped instances, wrong ports, or failed health checks.  
- **Target weights:**  
  Assign weights to split traffic unevenly across target groups. Great for blue/green and canaries—start with a small percentage and ramp up as confidence grows.

---

## Security groups: design and best practices

### For ALB

- **Inbound rules:**  
  Allow only 80 (HTTP) and/or 443 (HTTPS). For public sites, 0.0.0.0/0 is typical; for restricted portals, limit to specific CIDRs or trusted networks.  
- **Outbound rules:**  
  Default “allow all” is convenient; tightening to target subnets reduces blast radius if compromised. Ensure health checks and upstream calls still work.

### For EC2 targets

- **Inbound rules:**  
  Allow traffic from the ALB SG (use the SG ID as the source). This prevents direct internet access while permitting only LB-originating requests.  
- **Allow SSH/RDP from admin CIDRs only:**  
  Restrict management ports to your office/VPN ranges. Never expose SSH/RDP to the world in production.  
- **Outbound rules:**  
  Permit only what the app needs: databases, caches, APIs. Least privilege limits lateral movement and data exfiltration.

### Patterns to secure workloads

- **SG reference chaining:**  
  Referencing SG IDs instead of CIDRs lets membership update dynamically as instances scale, reducing manual rule changes.  
- **No public IP on instances:**  
  Keep instances in private subnets behind ALB. Use NAT for controlled outbound access if needed.  
- **Layered defenses:**  
  Combine ALB + WAF for L7 threats, and add GWLB appliances for deeper inspection. Defense-in-depth reduces single points of failure.

---

## Architecture choices and operational practices

### Subnets and routing

- **Public subnets for internet-facing ALB:**  
  Public subnets route to an Internet Gateway. The ALB lives there to accept external traffic, not your app servers.  
- **Private subnets for targets:**  
  Put app instances in private subnets without public IPs. If they need outbound internet (e.g., for updates), route via NAT Gateway/NAT instance to keep them unreachable from the outside.

### DNS and client access

- **ALB DNS name:**  
  ALB gives you a DNS name. In Route 53, create an alias (A/AAAA) or CNAME pointing your domain (e.g., app.example.com) to it. Dualstack aliases provide both IPv4 and IPv6.  
- **HTTP→HTTPS redirect:**  
  Keep a port 80 listener with a rule that issues a 301/302 to HTTPS. This improves security and user experience for clients typing plain http URLs.

### Observability and reliability

- **Access logs to S3:**  
  Enable when you need per-request visibility. Consider compression and lifecycle policies to control storage costs.  
- **CloudWatch metrics and alarms:**  
  Watch target health counts, LB 5XXs (issues at LB/NLB layer), target 5XXs (app errors), and response times. Alarms on spikes or latency anomalies help catch incidents quickly.  
- **Autoscaling integration:**  
  Attach your Auto Scaling Group (ASG) to the target group so instances register/deregister automatically. Scale on CPU, RequestCountPerTarget, or custom metrics to match demand.  
- **Blue/green and canary releases:**  
  Use weighted target groups to shift traffic gradually. Combine with slow start and stickiness for smoother warm-ups, then remove stickiness as state externalizes.

### Cost and performance considerations

- **ALB vs NLB cost:**  
  NLB often wins on raw throughput cost; ALB adds L7 features (routing, WAF integration, redirects) that justify price for web apps. Choose based on needs, not just cost per request.  
- **Cross-zone LB:**  
  ALB includes cross-zone. For NLB, enabling it improves balance but can affect data transfer charges—model costs if traffic is heavy and AZs imbalanced.  
- **Idle timeout and keep-alives:**  
  Right-size timeouts for WebSockets/SSE to avoid disconnects. Ensure backend keep-alives align with client behavior to reduce connection churn.

---

## How to choose the right options quickly

- **Need advanced routing, redirects, auth, WAF?**  
  Choose ALB.  
- **Need static IPs, TCP/UDP, super-low latency, or TLS passthrough?**  
  Choose NLB.  
- **Need traffic inspection via appliances?**  
  Choose GWLB.  
- **Public app for internet users?**  
  Internet-facing ALB in public subnets; targets in private subnets.  
- **Private microservices?**  
  Internal ALB; SG rules between tiers; no public IPs.  
- **Sticky sessions required?**  
  Enable ALB stickiness, or better, externalize state (e.g., Redis) and disable stickiness for cleaner scaling.  
- **Uneven deployments or canaries?**  
  Weighted target groups plus slow start; health checks tuned to detect issues quickly without flapping.

---

## Common gotchas and tips

- **Don’t forget health checks:**  
  Misconfigured paths or status codes cause healthy instances to be marked unhealthy, blackholing traffic.  
- **TLS policies matter:**  
  Old clients may fail with “modern only” ciphers. Balance compatibility with security; audit your client base.  
- **Stickiness can hide problems:**  
  Sticky sessions keep users on a failing instance longer. Use short durations and strong health checks.  
- **Proxy protocol requires parsing:**  
  Enabling it without app support breaks traffic. Confirm your reverse proxy/app can read it.  
- **Route 53 alias vs. CNAME:**  
  Prefer alias records to the LB for root domains (zone apex); CNAMEs aren’t allowed at the apex.  
- **Logs and metrics cost:**  
  Turn on what you’ll actually use; add lifecycle policies for S3 logs to control spend.

 