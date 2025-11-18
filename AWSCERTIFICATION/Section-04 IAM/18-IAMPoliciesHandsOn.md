- In the root account, remove user ansh from the group admin, we see that now in the user account , if we go to IAM > Users , we get Access Denied (You don't have permission to iam:ListUsers).

- To fix this , we need to give permission policy to the user. So for this , in the root account, go to user ansh. in the permissions  tab, add permission. Now there are two options we can add permission directly or create inline policy .We choose add permission directly

- Now in that we also have option , to add this user to a group (which we already done before), but for now we choose attach policy directly. **Add policy IAMReadOnlyAccess**. This will allow my user ansh to read anything on IAM which is what we want

- Now in the user account ,w e see now we can see users in IAM > Users. Not only Users , i can view user groups also as i have given IAMReadOnlyAccess 

- Note try creating a user group in user account , we see we can't able to do it as we are not allowed to create anything. 


- Now we have AdministrativeAccess policy in admin group , IAMReadOnlyAccess policy for our ansh user. Now in the root account , create a new user group developer , add ansh user to this group and attach any policy(let's say AlexaForBusinessDevelopment). Now also add ansh to admin group again . Now if we see the permission policy of ansh user , we will have 3 policies now, AdministrativeAccess which is attached via Group admin, IAMReadOnlyAccess which is attached directly , and AlexaForBusinessDevelopment which is attached via Group Developers. 

- Now if see inside of AdministrativeAccess policy , how it is defined in JSON , WE SEE
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}

* means everything
```  

- Similarly if we see inside of iamreadonlyaccess, we see 
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:GenerateCredentialReport",
                "iam:GenerateServiceLastAccessedDetails",
                "iam:Get*",
                "iam:List*",
                "iam:SimulateCustomPolicy",
                "iam:SimulatePrincipalPolicy"
            ],
            "Resource": "*"
        }
    ]
}

here, Get* means everthing start from get , 

```

- We can also create our own policy 

