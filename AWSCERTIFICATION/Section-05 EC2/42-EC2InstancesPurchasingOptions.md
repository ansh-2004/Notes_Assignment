# EC2 Instances Purchasing Options

- On-demand Instances - They allow us to run instances on demands. They are good for short workload, predictable pricing, pay by seconds.

#### But if you have differnet kind of workloads , you can optimize your discounts and your pricing by specifying it to AWS. For eg, you can use
- Reserved Instances (1 & 3 years)
    - Reversed Instances - long workloads. For eg, runing databases for long time 
    - Convertible Reserved Instances - long workloads with flexible instances. For eg, you want to change the instance type over time 
- Saving Plans (1 & 3 years) - commitment to an amount of usage , long workload
- Spot Instances - short workloads, cheap , can lose instance(less reliable)
- Dedicated Hosts - book an entire physical server, control instance placement
- Dedicated Instances - no other customers will share your hardware
- Capacity Reservations - reserve capacity in a specific AZ for any duration

## EC2 On Demand
- Pay for what you use:
    - Linux or Windows - billing per second , after the first minute
    - all other operating systems - billing per hour
- Has the highest cost but no upfront payment
- No long-term commitment 
-  Recommeded for a short-term and un-interrupted workloads, where you can't predict how the application will behave

## EC2 Reserved Instances
- Up to 72% discount compared to On-demand
- You reserve a specific instance attributes (Instance type, region , Tenancy , OS)
- You specify a reservation periosd - 1 year (+ discount) or 3 years (+++ discount)
- Payment options - No upfront(+), Partial Upfront(++), All Upfront(+++)
- Reserved Instance's Scope - Regional or Zonal (reserve capacity in an AZ)
- Recommended for steady-state usage applications (Think database)
- You can buy and sell in the Reserved Instance Marketplace if you don't need them anymore

- **Convertible Reserved Instance** - It is a specific kind of reserved instances. 
    - It allows you to change the EC2 instance type, instance family , OS , scope and tenancy
    - Up to 66% discount due to more flexibilty

## EC2 Savings Plans
- Get a discount based on long-term usage (up to 72% - same as RIs)
- But instead, you're going to say , I want to spend $10 per hour for the next 1,2,3 years means you hae to commit to a certain type of usage.($10/hour for 1 or 3 years)
- Usage beyond EC2 Saving Plans is billed at the On-Demad price
- With saving plans , you are locked to a specific instance family & AWS region (eg, M5 in us-east-1)
- But you are flexible across 
    - Instance Size (e.g, m5.xlarge,m5.2xlarge)
    - OS (eg, you can switch between linux , windows or so on)
    - Tenancy (you can switch between Host,Dedicated , Defaut)

## EC2 Spot Instances
- Can get a discount of up to 90% compared to On-demand
- But they are instances you can "lose" at any point of time because you define a max price you are willing to pay for your spot instances. And if the spot price goes over it , then you are going to lose it . 
- The MOST cost-efficient instances in AWS
- Useful for workloads that are resilent to failure ( This refers to tasks or applications that can tolerate interruptions, crashes, or restarts without causing major problems. If part of the system fails, the workload can continue or easily restart. These types of workloads typically don’t require constant uptime or real-time responses.)
    - Batch jobs
    - Data analysis
    - Image processing 
    - Any distributed workloads
    - Workloads with a flexible start and end time
- Not suitable for critical jobs or databases

## EC2 Dedicated Hosts
- A physical server with EC2 instance capacity fully dedicated to your use
- Allows you address compliance requirements and use you existing sever-bound software licenses(per-socket, per-core,pe-VM software licenses)
- Purchasing options:
    - On-demand - pay per second for active Dedicated host
    - Reserved - 1 or 3 years (No Upfront, Partial Upfront,All upfront)
- The most expensive option because you actually reserve a physical server
- Useful for software that have complicated licensing model (BYOL - Bring Your Own License)
- Or for companies that have strong regulatory or compliance needs

#### Explanation in simple terms 


## **EC2 Dedicated Hosts (Simple Explanation)**

An **EC2 Dedicated Host** is basically **your own physical server in AWS**, not shared with anyone else.

### **Why is this useful?**

#### **1. For compliance rules**

Some companies must follow strict rules (like in finance or healthcare) that require:

* Their data to run on **hardware not shared with other customers**
  A Dedicated Host satisfies this.

#### **2. For special software licenses**

Some old or expensive software licenses are tied to:

* The server’s **CPU cores**
* The server’s **sockets**
* Each **virtual machine (VM)**

This is called **“Bring Your Own License (BYOL)”**.
These licenses often don’t work well on shared cloud servers.
A Dedicated Host gives you a **real physical server**, so your licenses work properly.

---

## **Purchasing Options**

You are paying for a whole physical machine, so the options are:

* **On-Demand**:
  Pay per second while the host is running.

* **Reserved Host (1 or 3 years)**:
  Commit to a long-term contract to save money.
  Choices:

  * **No Upfront** – pay monthly
  * **Partial Upfront** – pay some now, some later
  * **All Upfront** – pay everything now for the biggest discount

---

## **Why is it expensive?**

You are *renting an entire physical server*—not just a small part.
This costs much more than normal EC2 instances.

---

## **When do people use this?**

* When they must follow strict laws or security rules
* When their software licenses are difficult or expensive
* When they need hardware isolation from other AWS customers

Here’s a simple explanation of the **licenses** being talked about:

---

## ✅ **What “licenses” means in EC2 Dedicated Hosts**

Some software—especially older or enterprise software—requires a **license** to use.
These licenses often depend on the **hardware** the software runs on.

### These licenses can be based on things like:

* **Per socket** → Each CPU socket on the physical server
* **Per core** → Each CPU core on the physical server
* **Per VM** → Each virtual machine you run
* **Physical machine identity** → Some licenses are tied to a specific physical server

In a normal cloud environment, AWS shares hardware among many customers, so:

* You **don’t know** which physical machine you’re on
* You **can’t guarantee** the number of sockets/cores
* Some licenses **won’t work** or become extremely expensive

---

## 🔑 **Dedicated Hosts solve that**

A Dedicated Host gives you **your own physical server**, so:

* You know exactly how many cores/sockets exist
* You can map your licenses directly
* You can legally use “Bring Your Own License (BYOL)” software

---

## 🧩 **Examples of software that use these licenses**

* **Oracle databases**
* **Microsoft Windows Server**
* **Microsoft SQL Server**
* **SAP applications**
* **VMware-based software**

These often have **per-core** or **per-VM** pricing rules.

---

## 📌 In simple terms

The “license” refers to **software you paid for** that can only run:

* Per physical CPU
* Per CPU core
* Or per virtual machine

A Dedicated Host lets you use these licenses legally and cost-effectively.

---

## EC2 Dedicated Instances
- Instances run on hardware that's dedicated to you which is different from the physical server.
- But you may share hardware with other instances in same account
- No control over instance placement (Can move hardware after stop /start)

## Difference between Dedicated Hosts and Dedicated Instance
- Dedicated Instances mean that you have your own instance on your own hardware, whereas dedicated host, you get access to the physical server itself and it gives you visisbility into the lower level hardware.

## EC2 Capacity Reservations

- Reserve On-Demand instances capacity in a specific AZ for any duration
- You always have access to EC2 capacity when you need it . 
- No time commitment(Create,cancel anytime) , no billing discounts'
- Combine with Regional Reserved Instances and Savings Plans to benefit from billing discounts
- You're charged at On-Demand rate whether you run instances or not 
- Suitable for short-term , uninterrupted workloads that needs to be in specific AZ


# Which purchasing option is right for me?
- On demand : coming and staying in resourt whenever we like , we pay the full price.
- Reserved : like planning ahead and if we plan to stay for long time , we may get a good discount.
- Savings Plan : pay a certain amount per hour for certain period and stay in any room type (e.g, King,Suite,Sea View...)
- Spot instances : the hotel allows people to bid for the empty rooms and the highest bidder keeps the rooms , You can get kicked out at any time.
- Dedicated Hosts : We book an entire building of the resort
- Capacity Reservation : You book a room for a period with full price even you don't say in it. 



# Summary of all these with real examples


# 🌟 **EC2 Purchasing Options Explained in Simple Terms (with Real Company Examples)**

---

# ✅ **1. On-Demand Instances**

### **Simple Meaning:**

Pay only when you use it. No commitment. Most flexible but most expensive.

### **Real Life Example:**

Like booking a hotel room **whenever you want**, paying **full price**, no planning.

### **Used by companies for:**

* New apps still being tested
* Unpredictable workloads
* Emergency capacity

**Example:**
A startup runs their new mobile app backend. They don't know traffic yet, so they use On-Demand.

---

# ✅ **2. Reserved Instances (RI) – 1 or 3 years**

### **Simple Meaning:**

You commit to a specific instance for 1–3 years → **big discount (up to 72%)**.

### **Real Life Example:**

You book the same hotel room for 1 year → you get a huge discount.

### **Used by companies for:**

* Long-running workloads
* Databases
* Stable servers

**Example:**
A bank runs its PostgreSQL database 24/7. They buy a 3-year reserved instance to save money.

---

# 👉 **Convertible Reserved Instances**

### **Simple Meaning:**

Like a Reserved Instance, but you can **switch instance types** later (e.g., from m5.large → m6i.large).

### **Real Life Example:**

Booking a hotel room for a long stay but able to **change room type** anytime.

### **Used by companies for:**

* Long workloads that may need upgrades over time
* Companies unsure of future instance types

**Example:**
An e-commerce company expects its web servers to grow over time. They buy Convertible RIs so they can upgrade instance families later.

---

# ✅ **3. Savings Plans (1 or 3 years)**

### **Simple Meaning:**

You commit to spending **$X per hour** for 1 or 3 years.
AWS gives you big discounts (like Reserved Instances) but with more **flexibility**.

### **Real Life Example:**

You tell a hotel:
“I will spend **$300 per month** for 3 years. Let me stay in **any room type**.”

### **Used by companies for:**

* Organizations with many EC2 types
* Workloads that change instance types often

**Example:**
Netflix runs many types of services. Savings Plans help them save money across thousands of instances.

---

# ✅ **4. Spot Instances**

### **Simple Meaning:**

Super cheap (up to 90% off) but can be **taken away anytime**.

### **Real Life Example:**

A hotel sells empty rooms for cheap, but can **kick you out** when a full-price customer arrives.

### **Used by companies for:**

* Fault-tolerant workloads
* Batch jobs
* Machine learning
* Image/video processing

**Example:**
Airbnb uses Spot Instances to process millions of images. If an instance disappears, the job simply restarts elsewhere.

---

# ✅ **5. Dedicated Hosts**

### **Simple Meaning:**

You get the **entire physical server**. No one else can use it.

### **Real Life Example:**

You rent an **entire building** in a resort — all rooms are yours.

### **Used by companies for:**

* Very strict compliance rules
* Old software licenses tied to physical hardware
* BYOL (Bring Your Own License)

**Example:**
A financial company must follow strict regulations. They use Dedicated Hosts so their servers are isolated.

---

# ✅ **6. Dedicated Instances**

### **Simple Meaning:**

Your EC2 runs on hardware **only your account uses**, but you **don’t control the physical server**.

### **Real Life Example:**

You still stay in your own building wing, but the hotel chooses your room.

### **Used by companies for:**

* Companies that want hardware isolation
* But don’t need full visibility into the server

**Example:**
A healthcare company needs isolation for patient data but doesn’t need full hardware control.

---

# ✅ **7. Capacity Reservations**

### **Simple Meaning:**

You pay full price to **reserve capacity in a specific Availability Zone**.

### **Real Life Example:**

You pay full price to reserve a hotel room for the weekend — even if you don’t stay.

### **Used by companies for:**

* Workloads that must run in a specific AZ
* Disaster recovery
* Government systems

**Example:**
An airline reserves EC2 capacity in a specific AZ to ensure flight booking servers always have space.

---

# 🌟 **Easy Comparison Summary**

| Option                    | Simple Meaning              | Best For                     |
| ------------------------- | --------------------------- | ---------------------------- |
| **On-Demand**             | Pay as you go               | Unpredictable workloads      |
| **Reserved Instances**    | Commit to specific instance | Databases, steady workloads  |
| **Convertible RIs**       | Commit but flexible         | Growing apps                 |
| **Savings Plans**         | Commit to $/hour            | Flexible long-term workloads |
| **Spot Instances**        | Cheapest but interruptible  | Batch, ML, image processing  |
| **Dedicated Hosts**       | Entire physical server      | Licensing & compliance       |
| **Dedicated Instances**   | Isolated hardware           | Security, less strict        |
| **Capacity Reservations** | Hold capacity               | Guaranteed AZ availability   |

