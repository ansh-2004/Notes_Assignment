# IAM Defence Mechanisms

## IAM - Password Policy

- Now that we have created users in groups, it is time for us to protect these users in groups from being compromised. 

- So for this , we have two defense mechanisms. The first one is **password policy** because :-
    - Strong password = Higher security for your account
    - In AWS, you can setup a password policy: 
        - Set a minimum password length
        - Require specific character types
            - including uppercase letter
            - lowercase letters
            - numbers
            - non-alphanumeric characters
        - Allow all IAM users to change their own passwords
        - Require users to change their password after some time (password expiration)
        - Prevent password re-use


## Multi Factor Authentication - MFA

- The second defence mechanism is **Multi Factor Authentication - MFA**
    - Users have access to your account and can possibly change configurations or delete resources in your AWS account
    - So , you want to protect your Root Accounts and IAM users
    - MFA = password you know + security device you own
    - Main Benefit of MFA :- 
        - If a password is stolen or hacked , the account is not compromised because the hacker will need to also get a hold of the physical device of Alice that could be a phone for example to do a login


### MFA devices options in AWS
- Virtual MFA device :- Google Authenticator (phone only means working on one phone at a time) , Authy (phone only , in this you have support for multiple tokens on a single device )

- Universal 2nd Factor(U2F) Security Key :- A physical device ,for example, Yubikey by Yubico. It also supprts multiple root and IAM users using a single security key

- Hardware key Fob MFA Device :- physical device provided by Gemalto
- Hardware key Fob MFA Device for AWS GovCloud (US) : special key device provided by SurePassID
