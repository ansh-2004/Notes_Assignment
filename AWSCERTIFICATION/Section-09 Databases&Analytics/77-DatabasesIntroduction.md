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
- NoSQL means non-SQL which means non relational databases. 
- They are built for specific purpose with a specific data model in mind and have a **flexible schema** for building moden application.
- The schema is basically the shape of the data. 
- Benefits of using a NoSQL database:
    - You have more **Flexibility** . It's easier to make the data model evolve. 
    - It's **scalable** , so it's designed to scale out by adding distributed servers/clusters.  In relational database, it's not easy to add servers to scale it. You have to scale up by doing some vertical scaling. But with NoSQL databases, you can do horizontal scaling. 
    - It is also **high performance**. It's optimized for a specific data model
    - It is **highly functional**. The types are optimized for the model
- Examples: Key-value databases, document, graph , im-memory or a search databases.

### NoSQL data example:JSON
- In the NoSQL database, you can have the data in JSON format(JavaScript Object Notation)
- JSON is very common way to describe data. We can have different sub nesting of the data. We have different fields , different names , different types
- So JSON is a very common way to model data in a NoSQL model.
- Fields can change over time. So it's up to us to add a new field into our JSON documents.
- They have support for Arrays also.

# Databases & Shared Responsibility on AWS
- AWS will offer to manage different databases for us. 
- Benefits of using a managed database are :
    - It's very quick to **provision** **(Setting up and making a database ready to use)**. Usually a database will have **high availability** in mind when designing it **(Ensuring the database is accessible even if part of the system fails. AWS achieves this by replicating data across multiple Availability Zones (AZs) so downtime is minimized.)**. And it you wanna scale your database, you can do vertical and horizontal scaling pretty easily. 
    - They will also include some utilities to do automated backup and restore of your databases as well as operations and upgrades
    - **Patch the operating system** of the underlying instance, is reponsibility of AWS.**(Applying updates to fix bugs, security vulnerabilities, or improve performance)** So AWS will be responsible for the entire database in terms of patching
    - The **monitoring and alerting** are going to be integrated (AWS integrates tools like CloudWatch to track database health, performance, and usage. Alerts notify you if something unusual happens (e.g., high CPU usage).) and this is why using a managed database on AWS is very , very important and very beneficial.

- You are able to run your own database technology on an EC2 instance, but if you do so , you need to handle yourself all the things associated with **resiliency** **(The ability of your database to recover quickly from failures (hardware crash, network outage).)** , backup , patching, high availability , fault tolerance , and scaling.