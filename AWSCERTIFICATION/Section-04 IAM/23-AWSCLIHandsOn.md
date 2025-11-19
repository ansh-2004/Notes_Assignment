## How to create Access Key
- From the root account , Go to IAM > Users > ansh
- Under Security Credentials, We have Access Keys, Create access Key
- You will see there are some selection you will need to do based on your use case , 
    - Command Line Interface (CLI) : You plan to use this access key to enable the AWS CLI to access your AWS account.
    - Local code: You plan to use this access key to enable application code in a local development environment to access your AWS account.
    - Application running on an AWS compute service : You plan to use this access key to enable application code running on an AWS compute service like Amazon EC2, Amazon ECS, or AWS Lambda to access your AWS account.
    - Third-party service : You plan to use this access key to enable access for a third-party application or service that monitors or manages your AWS resources.
    - Application running outside AWS : You plan to use this access key to authenticate workloads running in your data center or other infrastructure outside of AWS that needs to access your AWS resources.

- Also , for each of this use case , aws has an alternative , for example if you choose CLI, aws give you alternative to either use **CloudShell** or **AWS CLI V2**

- After creating secret key for CLI ,you get 2 things **Access key id and Secret Access Key**

- Go to terminal and type **aws configure**, you will be asked for **AWS Access key id** , provide it and then you will be asked for **AWS Secret Access Key** , provide it. Then you will be asked for **Default region name** , provide region which is close to you like eu-west-1. Then you will be asked for **Default output format** just press enter . 
- Now aws cli is configured , to check write any command let's say , **aws iam list-users** . It will list all the users in my account

- If we remove permissions from our users, and then try to use this cli command , we get no response from cli because actually request was denied 