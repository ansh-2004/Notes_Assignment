# Amazon S3 - Security

- User-Based Security
    - A user can have **IAM Policies** that you and this IAM policy is going to authorize which API calls should be allowed for a specific IAM user. 
- Resorce-Based Security
     - In this we can use **S3 Bucket Policies** which are bucket wide rules that you  can assign directly from the S3 console. This will allow a specific user to come in or allow a user from another account (called cross-account) to access your S3 buckets. This is also how we'll make our S3 buckets public.
     - Next , we have the **Object Access Control List or ACL** , they are finer gain security and they can be disabled
     - Bucket Access Control List - They are at bucket level . They are very less common and can be disabled

- Note : In which situation can an IAM principal((users/roles)) can access an S3 object?
    - If the IAM permissions allow it OR if ith resource policies allows it
    - AND there is no explicity deny in the action , then the IAM principle can access the S3 object on the specified API call. 

- Another way to do security on Amazon S3 is to **encrypt the objects** in Amazon S3 using **encryption keys**.




## User-based security (identity policies)

- **What it is:**  
  Identity-based policies are JSON policies attached to IAM users, roles, or groups that specify which S3 API actions are allowed or denied.

- **Where it’s attached:**  
  IAM (not S3). You edit these in the IAM console and attach them to principals (users/roles).

- **How it works:**  
  The principal presents its IAM policy when calling S3. If the policy allows the action on the resource and nothing else denies it, access is granted.

- **Typical use cases:**  
  - **Internal apps and services:** EC2 or Lambda roles that need to read/write specific buckets or prefixes.  
  - **Developer access:** Grant fine-grained, least-privilege permissions for team members.  
  - **Conditional access:** Use conditions like `aws:PrincipalArn`, `s3:prefix`, `s3:ExistingObjectTag`, `aws:RequestTag`, `ipaddress`, `MultiFactorAuthPresent`.

- **Example allow policy (principal-centric):**  
  Grants read to a specific bucket and prefix.
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["s3:GetObject"],
        "Resource": "arn:aws:s3:::my-bucket/reports/*"
      }
    ]
  }
  ```


## Resource-based security (bucket and object policies, ACLs)

- **What it is:**  
  Policies attached to S3 resources (bucket or object) that define who can access them, including cross-account principals.

- **Bucket policies (recommended):**  
  - **Scope:** Apply at the bucket level (and can target prefixes).  
  - **Use cases:**  
    - **Cross-account access:** Allow roles from another account to read/write.  
    - **Public access (careful):** Enable read for static websites (typically only `GetObject`).  
    - **Compliance guards:** Require TLS (`aws:SecureTransport`), block non-allowed principals, enforce object ACLs/tags.  
  - **Tip:** Combine with **S3 Block Public Access** to prevent accidental public exposure unless explicitly intended.

- **Object ACLs (legacy, fine-grained):**  
  - **Scope:** Attach permissions to individual objects.  
  - **Use cases:**  
    - **Interoperability / legacy apps** that rely on ACLs.  
    - **Cross-account object ownership** scenarios (e.g., when a different account uploads into your bucket).  
  - **Best practice:** Prefer bucket policies; use ACLs only when you need per-object grants or ownership control (e.g., `BucketOwnerFullControl`).

- **Bucket ACLs (rare):**  
  - **Scope:** Grants for the bucket resource itself.  
  - **Use cases:** Mostly historical; commonly disabled in modern designs.  
  - **Best practice:** Avoid; rely on bucket policies.

- **Example bucket policy (resource-centric):**  
  Allow a specific cross-account role to read from a prefix.
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "AllowCrossAccountRead",
        "Effect": "Allow",
        "Principal": { "AWS": "arn:aws:iam::123456789012:role/analytics-reader" },
        "Action": ["s3:GetObject"],
        "Resource": "arn:aws:s3:::my-bucket/reports/*",
        "Condition": {
          "StringEquals": { "aws:PrincipalOrgID": "o-abc123" }
        }
      }
    ]
  }
  ```



## How AWS decides access (evaluation logic)

- **Identity OR resource allow:**  
  Access is granted if an IAM identity policy allows the action OR a resource policy allows the action.

- **Explicit deny wins:**  
  Any explicit deny in any applicable policy (identity, resource, permission boundary, SCP) overrides all allows.

- **Conditions must match:**  
  If a policy includes `Condition`, those must evaluate to true (e.g., must use TLS, must come from specific VPC endpoint, must have MFA).

- **Public access block:**  
  If S3 Block Public Access settings are enabled, they can override bucket policies that would otherwise make objects public.

- **Ownership matters:**  
  For object operations, the **object owner** (which may differ from bucket owner) affects who can change ACLs and some permissions. Use `BucketOwnerPreferred` or `ObjectOwnership` settings to simplify multi-account uploads.



## Choosing user-based vs resource-based (quick guidance)

- **Use user-based (IAM) when:**  
  - **Internal principals** in your account need access (EC2 roles, Lambda roles, developers).  
  - You want **centralized control** from IAM with least-privilege.

- **Use resource-based (bucket policy) when:**  
  - You need **cross-account** access without sharing credentials.  
  - You want to **enforce rules at the bucket boundary** (TLS-only, deny non-approved principals, limit by VPC endpoint).  
  - You need controlled **public read** for a website (with Block Public Access carefully configured).

- **Use ACLs only when:**  
  - You must grant per-object permissions or handle **object ownership** in multi-account upload workflows.


## Encryption overview (complementary to access control)

- **Server-side encryption (SSE):**  
  - **SSE-S3:** Managed by S3; easiest default-at-rest encryption.  
  - **SSE-KMS:** Uses AWS KMS keys; supports granular key policies, audit, and per-principal control.  
  - **SSE-C:** Customer-provided keys; niche use.

- **Client-side encryption:**  
  - **Encrypt before upload:** You manage keys and decrypt client-side; S3 stores opaque ciphertext.

- **Policy enforcement:**  
  - **Require encryption:** Use bucket policy conditions (e.g., require `x-amz-server-side-encryption` or `aws:SecureTransport` and deny unencrypted uploads).



## S3 Bucket Policies

- They are JSON based policies
```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid": "PublicRead",
      "Effect" : "Allow",
      "Principal": "*",
      "Action" : [
        "s3:GetObject"
      ] ,
      "Resource" : [
        "arn:aws:s3:::examplebucket/*"
      ]
    }
  ]
}
```
   - Resources : Resource tells the policy what buckets and objects this policy applies on. So "arn:aws:s3:::examplebucket/*" , * means , this policy applies to every object withing the examplebucket
   - Effect : Allow/Deny . And what we allow or Deny that is actions.
   - Actions : We have a set of APIs , we can either Allow or Deny and in this example, the action we Allow is GetObject. So this
   - Principal : The principle presents the account or the user to apply the policy to . And * means here we allow anyone to GetObject so to retreive an Object from my example Bucket
   - Therefore this examplebucket is setting public reads on all objects inside my Buckets

- Use S3 Bucket policy to:
  - Grant public access to the bucket
  - Force objects to be encrypted at upload
  - Grant access to another account (Cross account)


## Situation

- Here is a Bucket Policy for Public Access. 
- We have a user , it's on the worldwideweb. It's a website visitor and he want's to access fiels within our S3 buckets
- So we'll attach an S3 Bucket Policy that allow public access. 
- And once this Bucket policy is attached to the S3 Bucket, then the user can access any objects within it. 

#### Another way to do it (User access to S3 - IAM permissions)
- If you have a user within your account, so it's an IAM user and that user wants to access Amazon S3, then we can assign IAM permissions to that user through a policy and therefore because the policy allows access to the S3 buckets, then the user can access our S3 Buckets right now. 

#### EC2 instance access - Use IAM Roles
- If we have an EC2 instance and want to give access from the EC2 instance into the S3 buckets then the IAM users are not approprate. Use IAM roles instead.
- So create an EC2 instance role with the correct IAM permissions and that EC2 instance will be able to access the Amazon S3 buckets

#### Advanced : Cross-Account Access - Use Bucket Policy
- We have an IAM user in another AWS account . 
- We create an S3 Bucket policy that allows Cross-Account Access for the specific IAM user.
- Now the IAM user will be able to make API calls into our S3 Buckets

## Bucket setting for Block Public Access

- We see 4 options
```
Block all public access

- Block public access to buckets and objects granted through new access control lists (ACLs)

- Block public access to buckets and objects granted through any access control lists (ACLs)

- Block public access to buckets and objects granted through new public bucket or access point policies

Block public and cross-account access to buckets and objects through any public bucket or access point policies
```
- This is what we set to on when we created the Buckets
- These settings were invented by AWS as extra layer of security to prevent company data leaks 
- So even though you would set an S3 Bucket Policy that would make it public, if these settings are enabled, the bucket will never be public
- If you know that your Bucket should never be public , leave this On.
- If you know that none of your S3 buckets ever should be public, then you can set this at the account level


