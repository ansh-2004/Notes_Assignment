# IAM Security Tools

- We can create an **IAM Credentials Report (account-level)**
    - a report that lists all your account's users and the status of their various credentials

- Second tool is **IAM Access Advisor (user-level)**
    - Access advisor shows the service permissions granted to a user and when those services were last accessed . 
    - you can use this information to revise your policies to inline with principle of least privilege. 

# Hands-On

## Generating Credentials report 
- Go to IAM> Credential Report and download it 

## IAM Access Advisor
- For this , Go to the user ansh ,  under the **Last Accessed** section (**Note:- Access Advisor has been renamed Last Access**)
- This will show you which services were acccessed by my user and when