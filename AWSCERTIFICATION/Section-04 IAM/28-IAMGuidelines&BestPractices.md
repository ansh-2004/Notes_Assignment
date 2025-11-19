# IAM Guidelines & Best Practices

- Don't use the root account except for AWS account setup
- One physical user = One AWS user
- Assign users to groups and assign permissions to groups 
- Create a strong password policy 
- Use and enforce the use of MFA
- Create and use Roles for giving permissions to AWS services
- Use Access keys for Programmatic Access(CLI/SDK)
- Audit Permissions of your account using IAM Credentials Report & IAM Access Advisor feature