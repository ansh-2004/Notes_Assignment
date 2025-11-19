# CloudShell
## Alternative to using the terminal to issue commands against AWS. 

**Note:- Cloudshell is not available in every region.** 

- In the cloudshell you can run commands , like **aws --version**
```
~ $ aws --version
aws-cli/2.31.34 Python/3.13.9 Linux/6.1.155-176.282.amzn2023.x86_64 exec-env/CloudShell exe/x86_64.amzn.2023
~ $ 

```

- Cloudshell is basically a terminal in the cloud of AWS. 

```
~ $ aws iam list-users
{
    "Users": [
        {
            "Path": "/",
            "UserName": "ansh",
            "UserId": "AIDA4SY7X5IXRXWQPGRIK",
            "Arn": "arn:aws:iam::864965618223:user/ansh",
            "CreateDate": "2025-11-18T05:22:56+00:00",
            "PasswordLastUsed": "2025-11-19T04:45:39+00:00"
        }
    ]
}
~ $ 

```

- In the cloudshell  , you have a full repository, 

```
~ $ ls
output.txt
~ $ echo "output" > output.txt
~ $ cat output.txt
output
~ $ 

```
- If you ever restart your cloudshell , your files will be there always 