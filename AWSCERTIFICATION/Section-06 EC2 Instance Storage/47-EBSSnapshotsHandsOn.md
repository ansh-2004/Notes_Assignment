# EBS Snapshots Hands On

- We have this 2 GiB GP2 EBS Volume available to us. And we can take a snapshot from it. Go to actions > create snapshot. Enter description as DemoSnapshot and create snapshot.
- Now go to snapshots (on the left hand menu , under Elastic Block Store)
- Now we can copy this snapshot into other region. In the actions tab , click copy snapshot . Now you see in destionation region , that you can copy it in any other region .

- Now other thing I can do is recreate a Volume from it. So in the actions, click create volume from snapshots . Choose Volume type GP2, size 2 GiB, then target AZ, then create volume.

- Now in the snapshots , we have recycle bin, It is a way for you to protect your EBS Snapshots and EBS Volumes from accidental deletion as well as your Amazon Machine Images. 
    - In the recycle bin , we create a retention rule , 
    - name it as like DemoRetentionRule
    - In the resource type , select EBS Snapshots
    - click apply to all resources
    - Give retention period(time period that the resouces can be recovered after deletion) as 1 day
    - In the rule lock settings , select unlock so that you can delete this retention rule whenever you want. 
    - create retention role

    - In the resource tab, we can see if we have resources in the recycle bin , 

- Next, we have storage tier, in the snapshot we have storage tier, where we see it as type standard. But you can move the storage tier by Archiving a snapshots, (click on action and archieve snapshots)