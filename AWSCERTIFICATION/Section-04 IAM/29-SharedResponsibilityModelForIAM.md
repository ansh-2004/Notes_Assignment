# Shared Responsibility Model for IAM 

- AWS is responsible for everthing that they do , for example , 
    - their infrastructure (global network security)
    - Configuration and vulnerability analysis of the services they offer
    - Compliance validation

- You are responsible for 
    - creating your own users ,groups , roles , policies management and monitoring
    - Enable MFA on all accounts
    - Rotate all your keys often 
    - Use IAM tools to apply appropriate permissions
    - Analyze access patterns and review permissions in your account