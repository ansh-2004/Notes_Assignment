# EBS Hands On

- Go to your instance **My First Instance** and under the storage tab , we find that there is a root device and block device on it. 
- In the block device, we see there is one volume of 8 gigabytes currently attached into our EC2 Instance. Click on it and we get into the volume interface of AWS. 
- Now we can create a second volume 
- So, create volume and in volume type , we have many options to choose such as gp2,gp3 , io1,io2 and so on. Choose GP2 , choose size two gigabytes. 
- And kep IOPS as default 
- And for availability zone, choose the same one where my EC2 instance is 
- Now kept everthing default and create volume 
- Now we need to attach this volume to the our EC2 instance by going to action and attach volume 
    - Choose instance **My First Instance** 
    - choose device name as /dev/sdf . (Recommended device names for Linux: /dev/xvda for root volume. /dev/sd[f-p] for data volumes.)
- Now our instance now has two EBS volumes attached to it. We can verify this by going to our ec2 instance and under storage tab , we see in block devices, i have two block devices one of 8 GiB and other 2 GiB
- To actually use this new block device, it's bit more complicated and out of scope for this course

- Now ,how root device has delete on termination attribute yes? 
    - It is because when we create an instance, and in the storage , in the advanced menu , we see EBS Volumes already defined as 8 GiB, volume type gp2 and delete on termination attribute yes
    - Now terminate the instance, and check EBS Volumes, we see our eight gigabytes root volume disappeared. Only the 2 GiB volume we create was shown



---


## 1️⃣ **EBS Volume Types in EC2**
When you create an EBS volume, AWS gives you multiple types optimized for different workloads:

- **gp2 (General Purpose SSD)**  
  - Older generation general-purpose SSD.  
  - Balances price and performance.  
  - Performance scales with volume size (up to 16,000 IOPS).

- **gp3 (General Purpose SSD, newer)**  
  - Successor to gp2, cheaper and more flexible.  
  - Baseline performance: 3,000 IOPS and 125 MB/s throughput, independent of size.  
  - You can provision higher IOPS/throughput separately.

- **io1 (Provisioned IOPS SSD)**  
  - High-performance SSD for mission-critical workloads.  
  - You can provision up to 64,000 IOPS.  
  - Supports **Multi-Attach** (attach to multiple instances).

- **io2 (Provisioned IOPS SSD, newer)**  
  - More durable than io1 (99.999% durability).  
  - Same high IOPS provisioning, better reliability.  
  - Also supports **Multi-Attach**.

- **st1 (Throughput Optimized HDD)**  
  - Magnetic disk optimized for **big sequential workloads** (e.g., data warehouses, log processing).  
  - Cheaper than SSD, but not good for random I/O.

- **sc1 (Cold HDD)**  
  - Lowest-cost option.  
  - For infrequently accessed data (cold storage).  
  - Not recommended for performance-sensitive workloads.

---

## 2️⃣ **Device Names When Attaching Volumes**
When you attach an EBS volume to an EC2 instance, you must specify a **device name**. This is how the OS identifies the disk.

- **Root Volume :**  
  - Recommended name: `/dev/xvda`  
  - This is the primary boot disk where the OS is installed.  
  - AWS automatically attaches this when you launch an instance.

- **Data Volumes :**  
  - Recommended names: `/dev/sdf` through `/dev/sdp`  
  - These are additional disks you attach for application data, logs, or databases.  
  - Linux maps these names to actual device paths (sometimes `/dev/nvme...` depending on instance type).  

📌 **Why naming matters:**  
- Consistency: Using standard names avoids confusion.  
- Automation: Scripts and configuration tools expect predictable device names.  
- OS mapping: Linux kernel may remap device names internally, but AWS recommends these conventions for clarity.
 

### ✅ TL;DR
- **Volume types**: gp2/gp3 for general use, io1/io2 for high IOPS, st1/sc1 for HDD workloads.  
- **Device names**: `/dev/xvda` for root, `/dev/sdf–/dev/sdp` for data volumes. This ensures consistent and predictable disk mapping in Linux.

---

