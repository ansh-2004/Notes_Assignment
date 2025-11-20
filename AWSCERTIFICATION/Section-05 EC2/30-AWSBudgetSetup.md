# AWS Budget Setup

- Set up a Budget for IAM User and an alarm for that budget in order not to spend any money or too much money.
- In the IAM User account, For this go to Billing console from top left corner and click on Billing and cost management
- We see although this IAM User has administrative access , but he can't have access to Billing and cost management . To give IAM user access for this , go to root account and scrolling down you see **IAM user and role access to Billing information** , active it , now IAM user has billing access .

## Setting a budget

- Go to Budget and create a budget