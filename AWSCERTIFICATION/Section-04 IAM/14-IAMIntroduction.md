## IAM: Users & Groups

- IAM = Identity and Access Management, Global Service
- In IAM , we are going to create our users and assign them to group
- Root accout created by default , shouldn't be used or shared. We should create users.
- **Users** are people within your organization , and can be grouped. One User respresent one person within your organization. And the users can be grouped together if it makes sense.

- Eg, we have an organization with 6 people, Alice, Bob, charles, David , Edward , Fred. Now Alice , Bob , Charles work together , they all are developers.So we are going to create Group: Developers regrouping alice, bob , charles. Now it turns out David and Edward also work together , so we are going to crete an Group : Opearations. Now we have 2 groups within IAM. **Now Groups can only contains users, not other groups**. Now some users don't have to belong to a group like Fred. This is not best practice, it is something you can do in AWS. **Also a user can belong to multiple groups**. Means suppose if charles and David work together and they are part of Audit team. you can create a third group Audit team with charles and David. Now you see Charles and david are part of two differnet groups.

#### So why do we create users and why do we create groups?
- Because we want to allow them to use our AWS accounts and to allow them to do so , we have to give them permissions called IAM : Permissions

## IAM: Permissions
- Users or Groups can be assigned JSON documents called policies (IAM policy). This policy told what a user is allowed to do or what a group and all the users withing that group are allowed to do.  
- So these policies define permissions of the users. In AWS you don't allow everyone to do anything , that would be catastrophic, because a new user could basically launch so many services and they will cost you a lot of money.
- So in AWS , you apply the least privilege principle : don't give more permissions than a user needs