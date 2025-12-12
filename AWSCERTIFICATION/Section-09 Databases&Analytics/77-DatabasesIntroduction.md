# Databases Intro
- When you are Storing data on disk (EFS,EBS,EC2 Instance Store,S3), you have your limits.
- If you want to store data in the structure way, you may want to store it in a database.
- And this sturcture is going to allow you to build indexes and to efficiently query or search through the data. 
- So well we have with EFS , EBS, EC2 instance store, S3, we can do per files operations. But with databases, it's going to be a lot more structured. We can even define relationships between your datasets. 
- So these databases nowadays, they're all optimized for a purpose and they will come with different features, shapes and contraints.

# Types of Databases

## Relational Databases 
- Looks just like Excel spreadsheets, but have links between each table. 
- We have students table with student id , dept id , name , email. 
- We have another departments table with dept id, spoc, email, phone.
- The idea is that in a relational database, you are defining a relation between the department id (the second column in students table) into the first column of the departments table. 
- You can even define more relations, for example , you can define a subject's table(having student id and subject) and link the table of the students to the subjects by defining another relation. That's why is called a relational databases.
- Now in relational databases, the particularity is that you can use SQL language to perform queries or lookups. 

## NoSQL Databases