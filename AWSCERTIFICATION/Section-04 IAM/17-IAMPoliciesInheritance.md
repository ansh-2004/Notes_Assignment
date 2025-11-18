- Let's imagine , we have a group of Developers , Alice, Bob, Charles. We attach a policy at group level. In that case , the policy will get applied to every single member of the group so both Alice, Bob and Charles, they will all get access and inherit this policy. 
- Now the second group Operations  with a different policy , David and Edward will have a different policy, than the group of developers.
- If Fred is a user (not in any group), we have the possibility to create what's called inline policy which has a policy that's only attached to a user.So that user could or could not belong to a group, you can have inline policies for whatever user you want. 
- Now if charles and David both belong to audit team , you attach a policy to the audit team, charles and David will also inherit that policy from audit team . So in this case, charles has a policy from developers and policy from audit team. Similarly with the David. 


## Inline Policies

- **Definition:** An inline policy is a policy that is **embedded directly into a single IAM user, group, or role**.  
- **Scope:** It exists only for that entity—it’s tightly coupled and cannot be reused elsewhere.  
- **Lifecycle:** If you delete the user, group, or role, the inline policy is deleted with it.  

---

### 🔍 How Inline Policies Differ from Managed Policies
| **Type** | **Description** | **Reusability** | **Best Use Case** |
|----------|-----------------|-----------------|-------------------|
| **Inline Policy** | Attached directly to one user, group, or role | ❌ Not reusable | When you need **unique, one-off permissions** for a specific entity |
| **Managed Policy** | Standalone policy created and stored in IAM | ✅ Reusable across multiple users, groups, roles | When you need **consistent permissions** applied to many entities |

---

### 📌 Example
Suppose you have a user named **Fred**:
- You can attach an **inline policy** directly to Fred that allows him to access only one specific S3 bucket.  
- That policy is unique to Fred. If Fred is deleted, the policy disappears too.  

By contrast, a **managed policy** (like `AmazonS3ReadOnlyAccess`) can be attached to multiple users, groups, or roles.


## IAM Policies Structure 

- Consists of
    - Version: policy language version , always include "2012-10-17". This is the policy language version

    - Id : an identifier for the policy (optional) eg. 'S3-Account-Permissions'
    - Statement : one or more individual statements(required) [ {} ]

- Statement Consists of
    - Sid : an identifier for the statement (optional) eg. "1"
    - Effect : whether the statement allows or denies access (Allow,Deny)
    - Principal: account/user/role to which this policy applied to . Eg ,we can apply policy to root account
    - Action: list of actions this policy allows or denies
    - Resource : list of resouces to which the actions applied to
    - Condition: conditions for when this policy is in effect(optional) 

