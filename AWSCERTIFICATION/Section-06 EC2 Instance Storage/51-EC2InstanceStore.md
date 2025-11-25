# EC2 Instance Store

- EBS Volumes are network drives with good but "limited" performance
- If you need a high-performance hardware disk attached to your EC2 instance , use **EC2 Instance Store**
- So, EC2 instance is a virtual machine but it is obviously attached to a real hardware server and some of these servers do have disk space that is attached directly you know, with a physical connection onto the server.
- And so a special type of EC2 instance can leverage something called an EC2 Instance Store which is the name of the hardware, the hard drive attached to the physical server.
- We use them for better I/O performance.
- They have good throughput
- If you stop or terminate your EC2 instance that has an instance store, then the storage will be lost and therefore it's called an ephemeral storage so that means that the EC2 Instance Store can not be used as a durable long term place to store your data. 
- It is good for buffer, a cache, scratch data or temporary content.
- Risk of data loss if hardware fails because the hardware attached to the EC2 Instance will fail as well. 
- So backups and Replication are your responsibility if you use EC2 Instance Store.


- From the exam perspective, if you see very high performance hardware attached volume for your EC2 Instance, think of Local EC2 Instance Store. 


---

## 💾 **EBS vs Instance Store**
- **EBS Volumes (Elastic Block Store):**
  - Network-attached storage (your instance connects to it over the AWS network).
  - Persistent: data survives instance stop/terminate (unless you choose delete-on-termination).
  - Flexible: can be detached, re-attached, resized, snapshotted, and replicated.
  - Performance: good, but limited compared to direct hardware disks.

- **EC2 Instance Store:**
  - Physical disk **directly attached to the host server** running your EC2 instance.
  - Extremely high I/O performance and throughput (better than EBS).
  - Ephemeral: data is **lost** if the instance stops, terminates, or the hardware fails.
  - Cannot be detached or moved between instances.
  - Best for temporary workloads like cache, buffer, scratch space, or ephemeral data.

---

## ⚡ Characteristics of Instance Store
- **High Performance:** Because it’s local hardware, latency is lower and throughput is higher than EBS.  
- **Ephemeral Storage:** Data disappears when the instance stops or terminates.  
- **Risk of Data Loss:** If the underlying physical server fails, the data is gone.  
- **Use Cases:**  
  - Temporary files  
  - Cache storage  
  - Scratch space for computations  
  - High-performance workloads that don’t need persistence  

---

## 📌 Exam Tip
If you see a question mentioning:
- **“Very high performance local disk”**  
- **“Ephemeral storage”**  
- **“Data lost when instance stops/terminates”**  

👉 The answer is **EC2 Instance Store**.

---

## ✅ TL;DR
- **EBS = persistent, network-attached, flexible storage.**  
- **Instance Store = ephemeral, hardware-attached, ultra-fast storage.**  
- Use Instance Store for temporary, high-speed workloads — but always back up important data elsewhere.

---

## Meaning of this line **Physical disk directly attached to the host server running your EC2 instance.**

## 🖥️ EC2 Basics
- An **EC2 instance** is a virtual machine running on a physical server in an AWS data center.  
- Normally, when you attach storage (like **EBS volumes**), it’s **network-attached** — meaning your instance talks to a storage system over the AWS network, not directly to the hardware disk.


## 💾 Instance Store (Directly Attached Disk)
- Some EC2 instance types come with **local disks physically built into the host server**.  
- These disks are **wired directly to the server’s motherboard/storage controller** — just like the SSD or HDD inside your personal laptop or desktop.  
- When your EC2 instance runs on that server, it can use those disks as **Instance Store volumes**.  
- Because the disk is local, I/O operations are **much faster** (lower latency, higher throughput) compared to network-attached EBS.

---

## ⚡ Why It Matters
- **Performance:** Direct hardware access = faster reads/writes than EBS.  
- **Ephemeral:** Data is tied to the physical server. If the instance stops, terminates, or the host fails, the data is lost.  
- **Use Cases:** Temporary storage like cache, scratch space, or high-speed buffers.  

---

## 📌 Analogy
Think of it like this:
- **EBS volume:** Like plugging in an external hard drive over a network cable — flexible, persistent, but slower.  
- **Instance Store:** Like using the internal SSD inside your computer — super fast, but if the computer dies, the data is gone.

---

✅ **TL;DR:**  
“Physical disk directly attached to the host server” means the EC2 instance is using the **actual hardware disk inside the physical server it runs on**, not a networked storage system like EBS. This gives **higher performance but no durability guarantees**.

✅ **TL;DR:** 
- Instance Store is available only on certain EC2 families like C5d/M5d/I3/H1/D2 and newer Graviton “gd” types. The “d” suffix is your clue that the instance has local NVMe SSDs attached to the host server.