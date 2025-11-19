## How can users access AWS ?

- To access AWS , you have three options:-
    - AWS Management Console (protected by password + MFA)
    - AWS Command Line Interface (CLI) : protected by access keys. Access Keys our credentials need to download to access AWS from our terminal . 
    - AWS Software Developer KIT (SDK) : for code: protected by access keys. It is used whenever you want to call APIs from AWS from within your application code. 

- Access Keys are generated through the AWS Console.
- Users manage their own access keys
- Access keys are secret , just like a password. Don't share them
- Treat Access key ID as username and Secret Access Key as Password

## What's the AWS CLI?
- A tool that enables you to interact with AWS service using commands in your command-line shell
- Direct access to the public APIs of AWS services
- You can develop scripts to manage your resources and automate some of your tasks
- It's open-source
- Alternative to using AWS Management Console

## What's the AWS SDK?
- AWS Software Development Kit (AWS SDK)
- This is a set of libraries. Language-specific APIs. So we get SDK for different programming languages.
- Enables you to access and manage AWS services programmatically
- SDK is not something you use within your terminal , it is something that you embed within your application that you have to code. 
- Supports
    - SDKs (JavaScript,Python,PHP,.NET,Rubt,Java,Go,Node.js,C++)
    - Mobile SDKs (Android,iOS,...)
    - IoT Device SDKs (Embedded C, Arduino,...)
- Example: AWS CLI is built on AWS SDK for python named **Boto**.