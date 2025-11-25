# EC2 Image Builder

- It is used to automate the creation of Virtual Machines or container images.
    - That means that you're gonna be able with EC2 Image Builder to automate the creation , maintain, validate and test AMIs for EC2 instances.
- Example, we have the EC2 Image Builder service and it is automatically , when it's going to run, it is going to create an EC2 instance called a Builder EC2 instance and that EC2 instance is going to build components and customize the software , for example, install java, update the CLI, update the software system, maybe install firewalls, whatever you define to happen on that EC2 instance may be install your application and then once this is done, then an AMI is going to be created out of that EC2 instance but all of this is obviously automated. Then the AMI is created , but we want to validate it, so EC2 Image Builder will automatically create a test EC2 instance from that AMI and going to run a bunch of tests that you are defining in advance. And if you don't want to run test , you can just skip that test but the test can be asking is the AMI working, is it secure? , is my application running correctly. And then once the AMI is tested, then the AMI is going to be distributed . So while EC2 image builder is original service,it is possible for you to take that AMI and distribute it to multiple regions therefore allowing your application and your workflow to be truly global.
- Next , EC2 Image Builder can be run on a schedule, so you can define a weekly schedule , or you can say you can run whenever packages are updated or you can run it manually 
- It is free service so you're only going to pay for the underlying resources means if you create an EC2 instance during this process and EC2 Image Builder will create these EC2 instances then you are going to pay for these EC2 instances and when the AMI is created and distributed, you're going to pay for the storage of that AMI wherever it has been created and whereever it has been distributed



# Summary 


## 🚀 What EC2 Image Builder Does
EC2 Image Builder is a **managed AWS service** that automates the lifecycle of creating, customizing, testing, and distributing **Amazon Machine Images (AMIs)** or **container images**. Instead of manually launching an instance, installing software, and creating an AMI, Image Builder does all of this for you in a repeatable pipeline.


## 🧩 Key Steps in the Process

1. **Builder EC2 Instance**
   - When you start a pipeline, Image Builder automatically launches a temporary EC2 instance called the **builder instance**.
   - This instance runs the **components** you define (scripts or recipes) — e.g., install Java, update CLI, patch OS, configure firewalls, or install your app.
   - Once customization is complete, the builder instance is terminated.

2. **AMI Creation**
   - The customized builder instance is turned into an **AMI**.
   - Behind the scenes, AWS creates **EBS snapshots** of the volumes, but you don’t manage them directly — they’re tied to the AMI.

3. **Test EC2 Instance**
   - Optionally, Image Builder launches a **test instance** from the new AMI.
   - It runs validation tests you define (e.g., “Is the app running?”, “Is the OS secure?”).
   - If tests pass, the AMI is marked as **ready**. If not, you can troubleshoot.

4. **Distribution**
   - The validated AMI can be **distributed across multiple regions**.
   - This allows you to launch identical EC2 instances globally, ensuring consistency in deployments.

5. **Scheduling**
   - Pipelines can run **on a schedule** (e.g., weekly builds).
   - They can also run **on-demand** (manual trigger) or **based on package updates** (e.g., when new patches are available).



## 💰 Cost Model
- **Image Builder itself is free.**  
- You only pay for:
  - The **EC2 instances** launched during build and test phases.  
  - The **EBS volumes/snapshots** created for AMIs.  
  - The **storage cost** of AMIs in each region where they’re distributed.  


## 📌 Why It’s Useful
- **Automation:** No manual steps — consistent builds every time.  
- **Validation:** Ensures AMIs are secure and functional before use.  
- **Global distribution:** Same image across multiple regions.  
- **Compliance:** Helps enforce patching and security policies.  
- **Cost efficiency:** You only pay for resources used during build/test, not the service itself.


✅ **TL;DR:**  
EC2 Image Builder automates the pipeline of **building → customizing → testing → distributing AMIs**. It spins up temporary EC2 instances to apply your software/configuration, creates AMIs, optionally tests them, and then distributes them globally. The service is free — you only pay for the EC2, EBS, and AMI storage resources used during the process.