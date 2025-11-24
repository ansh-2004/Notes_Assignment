# EBS Snapshots

- You can take your EBS volumes and make a snapshot which is also called a backup at any point of time that you wanted to. 
- The idea is that you will be able to backup the state of it, and even if the EBS volume is terminated later on , you could restore it from that backup. 
- Now to make a backup , it is not necessary to detach volume prior to doing the backup but it is recommended just to make sure that everything is clean on your EBS volume. 
- We can copy snapshots across AZ or Region and the idea is that you would be able to tranfer some of your data in a different region on AWS to leverage the gloabal infrasture. 
- So if we look at US-EAST-1A and we want to transfer an EBS volume to US-EAST-1B, the way we do it is that we would have the EBS volume(50 GB) attached to the EC2 instance, and then we would snapshot it. So maybe we would stop the EC2 instance ahead of time to make sure the snapshot is clean. Now the EBS snapshots exist in your region and the EBS snapshot can be used to restore a new EBS volume in another availability zone(let's say US-EAST-1B) and then we can attach this new EBS volume to an EC2 instance in US-EAST-1B.

## EBS Snapshots Features

- EBS Snapshot Archive
    - It allows you to move your snapshots to another storage tier called an archive tier, and that tier is 75% cheaper. 
    - But if you have it in the archive, it takes you between 24 to 72 hours to restore from the archive. 
    - So these are for snapshot that are not very important to you to restore it in a rush but you wanna save some cost on them.

- Recycle Bin for EBS Snapshots
    - By default, when you delete snapshots , they're gone. 
    - But you can setup a recycle bin , and the recycle bin will have all the snapshots that are deleted. And then after a while , maybe you can specify from one day to one year, the snapshots are gone from the Bin.
    - So on deleting snapshots, it would go into recylce bin. And you may have , for example, one year to recover the snapshots , which allows you to protect yourself against accidental deletion. 