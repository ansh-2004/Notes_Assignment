# SSH Summary Table

## How do you connect inside of your servers to perform some maintenance or action?
- So for this , for linux servers, we can use SSH to do a sercure shell into our servers.
- Based on the operating system you have on you computer, you have different ways of achieving it . 
- **SSH is a command line interface utility that can be used on Mac or Linux as well as windows over version 10. On windows less than version 10 you can use Putty instead of SSH. Putty will exceed the same thing as SSH . Putty allow to use the SSH protocol to connect into your EC2 instances.**
- There is another things called **EC2 Instance Connect** which is going to use your web browser , not terminal , not putty, your web browser to connect to your EC2 instance. And this is used for every operating system whether it is Mac, Linux , Windows any version. 
- **EC2 Instance Connect** only works for now with Amaxon Linux 2. Not with this only , it also supports other Operating system but need to do some configuration. 

```
✅ Other Supported Operating Systems for EC2 Instance Connect

Amazon Linux 2: Fully supported and the default choice for EC2 Instance Connect.

Amazon Linux AMI: Earlier Amazon Linux versions also support it.

Ubuntu: Supported with EC2 Instance Connect packages installed.

Red Hat Enterprise Linux (RHEL): Supported with proper configuration.

CentOS: Works with EC2 Instance Connect setup.

macOS (for connecting clients): Supported as the system you connect from, not as an EC2 instance OS.
```


SSH Summary Table

| Operating System | SSH | PuTTY | EC2 Instance Connect |
|------------------|:---:|:-----:|:---------------------:|
| Mac              | ✓   |       | ✓                     |
| Linux            | ✓   |       | ✓                     |
| Windows < 10     |     | ✓     | ✓                     |
| Windows ≥ 10     | ✓   | ✓     | ✓                     |
