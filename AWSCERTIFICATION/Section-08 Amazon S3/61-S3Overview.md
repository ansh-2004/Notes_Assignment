# Introduction to S3

- Amazon S3 is one of the main building blocks of AWS
- It's advertised as **infinitely scaling** storage
- Many websites use Amazon S3 as a backbone
- Many AWS services use Amazon S3 as an integration as well

## Amazon S3 Use cases
- It is used for backup and storage. It could be for your files, discs and so on. 
- For disaster Recovery. For eg, you will move your data to another region in case a region goes down then your data is backed up somewhere else. Use **Cross-Region Replication (CRR)** to copy data to another region. If one region fails, access data from the replicated region.
- For Archie purpose. You can archive files in S3 and retrive it at a later stage for much much cheaper. Store old or infrequently accessed data at low cost. Use S3 Glacier or Glacier Deep Archive for archival.
- For Hybrid Cloud Storage. So in case you have storage on premises, but you want expand it into the cloud, you can use S3 for this. Extend on-premises storage to the cloud. Use AWS Storage Gateway to integrate local storage with S3.
- Application hosting . Host application assets like images, scripts, or even entire apps. Mobile apps store user-uploaded content in S3.
- Media Hosting such as video files, images and so on. Integrates with CloudFront CDN for global delivery. Streaming platforms store video libraries in S3.
- Data lakes & big data analytics. To have a data lake , so to store a lot of data and to perform big data analytics. Integrates with AWS Athena, Redshift, EMR for analytics.
- Software delivery. For delivering software updates  or pataches. SaaS companies host installers and updates in S3.
- Static website. For hosting static websites and so on. Host HTML, CSS, JS files directly from S3. Enable Static Website Hosting in S3 bucket settings.Example: Documentation sites or landing pages.

- **Nasdaq stores** stores sever year of daya into the s3 glacier share service which is like the archival service of Amazon S3.
- **Sysco** runs analytics on its data and gain business insights from Amazon S3.
- S3 automatically stores your data redundantly across multiple AZs in the same region. This means if one AZ fails, your data is still available from another AZ in that region.

## Amazon S3 - Buckets
- S3 stores files(objects) into buckets(directories). 
- Buckets can be seen as top level directories.
- These buckets are created in your account and they must have a gloabally-unique name. That means that the name must be unique across all the regions you have it in your accounts but also all the accounts that exist out there on AWS. 
- Buckets are defined at teh region level so even though the name of the bucket is unique across all regions and all the accounts, the buckets must be defined in a specific AWS regions.
- So S3 looks like a global service but the buckets are actually created in a region. 
- Naming convention for S3 buckets
    - No uppercase, No underscore
    - 3-63 characters long
    - Not an IP
    - Must start with lowercase letter or number
    - Must not start with the prefix xn--
    - Must not end with the suffix -s3alias

## Amazon S3 - Objects
- They are files and they have a key. And an Amazon S3 object key is the full path of your file.
    - s3://my-bucket/my_file.txt   ( **my_file.txt**   this is the key)
    - s3://my-bucket/my_folder1/another_folder/my_file.txt  (**my_folder1/another_folder/my_file.txt**         this is the key)
- The key is composed fo a prefix and then an object name (**prefix + object name**)
    - s3://my-bucket/my_folder1/another_folder/my_file.txt (**my_folder1/another_folder/** is the prefix and **my_file.txt** is object name)
- Amazon S3 does not have a concept of directories within buckets (although when you look in the console, UI will trick you and you will actually create directories.). But anything and everything in Amazon S3 is actually a key.  
- Keys are just very , very long names that contain slashes and keys are made of a prefix and an object name

## Amazon S3 - Objects (cont.)
- Object values are the content of the body. You can upload a file , you can upload whatever(documents, binaries etc.) you want into Amazon History.
    - Max Object size is 5TB(5000GB) per object
    - If you upload a file that is very big and is greater than 5GB, then you must use **multi-part upload** to upload that file into several parts because uploading large files in one go is risky(network failures).Multi-part upload splits the file into smaller chunks (parts) and uploads them in parallel

    - So if you have of 5TB , then you must upload at least 1000 parts of 5GB each.

- Objects can also have metadata (list of keys-value pairs associated with the object) and that could by set by the **system** (content-type, last-modified etc.) or set by the **user**(custom info like **project=finance** or **owner = teamA**) to indicate some elements about the file,Some metadata. It helps application interpret or organize data.
- Tags 
    - Up to 10 tags per object
    - Tags are Unicode key-value pairs
    - Used for security policies (IAM conditions) and lifecycle rule (delete after 30 days)
    - Example : Environment=Production , CostCenter = 123
- Sometimes object will have a **version ID** if you have enabled versioning.

---

## four Amazon S3 bucket types and their differences:

***

###  **1. General Purpose Buckets**

*   **What they are:**  
    The standard S3 bucket type used for most workloads.
*   **Structure:**  
    Flat namespace (objects identified by keys, no real folders).
*   **Use cases:**
    *   Backups and archives
    *   Media hosting
    *   Static website hosting
    *   Data lakes
*   **Features:**
    *   Supports all S3 storage classes (Standard, IA, Glacier, etc.)
    *   Spans multiple Availability Zones for durability
    *   Compatible with most S3 features (versioning, lifecycle policies, replication)
*   **Analogy:**  
    A big storage bin where you throw everything in without hierarchy.   

***

###  **2. Directory Buckets**

*   **What they are:**  
    Buckets with a **hierarchical namespace** (like folders and subfolders).
*   **Structure:**  
    Organizes data into directories using `/` as a delimiter.
*   **Special behavior:**
    *   Designed for **low-latency access** and **data residency** use cases.
    *   Bucket names include AZ ID (e.g., `bucket-name--usw2-az1--x-s3`).
    *   If inactive for 90 days, transitions to an **inactive state** (temporarily inaccessible until reactivated).
*   **Use cases:**
    *   IoT data organized by region/device/date
    *   Logs structured for fast retrieval
*   **Differences from general purpose:**
    *   Supports zonal endpoints for faster access
    *   Deletes empty directories recursively when objects are deleted    

***

###  **3. Table Buckets**

*   **What they are:**  
    Buckets optimized for **structured data** (rows and columns).
*   **Structure:**  
    Stores data in a tabular format for analytics and querying.
*   **Use cases:**
    *   Product inventory (SKU, price, quantity)
    *   Logging structured events for dashboards
    *   Querying CSV/Parquet files with Athena or other analytics tools
*   **Analogy:**  
    Like a spreadsheet in the cloud—easy to filter and scan.    

***

###  **4. Vector Buckets**

*   **What they are:**  
    Purpose-built for **vector data** (high-dimensional embeddings used in AI/ML).
*   **Structure:**  
    Stores vectors inside **vector indexes** for similarity search.
*   **Use cases:**
    *   Semantic search
    *   Recommendation engines
    *   Chatbot memory retrieval
*   **Features:**
    *   Sub-second query performance
    *   Strong consistency for writes
    *   Supports metadata for filtering queries
*   **Analogy:**  
    A magnet board where similar items cluster together—search by meaning, not exact match.    

***

###  **Key Differences Summary**

| Bucket Type         | Structure      | Best For                             |
| ------------------- | -------------- | ------------------------------------ |
| **General Purpose** | Flat namespace | Backups, media, websites, data lakes |
| **Directory**       | Hierarchical   | Low-latency, organized logs, IoT     |
| **Table**           | Tabular        | Analytics, structured data           |
| **Vector**          | Vector indexes | AI/ML, semantic search               |

***

---

## General vs Directory Bucket

*   Internally, S3 uses a **flat namespace** where every object is identified by a **key** (a string).
*   Example:
    *   `photos/2025/image.jpg` is just a key, not a real folder structure.
*   The **console UI** shows folders for convenience, but they are simulated using prefixes (`photos/2025/`).

***
*   **Directory Buckets** introduce a **hierarchical namespace** for performance and organization, but it’s still implemented on top of keys.
*   The difference:
    *   **General Purpose Buckets:** Pure flat namespace.
    *   **Directory Buckets:** Enforce a structured prefix system and provide **zonal endpoints** for low-latency access.
*   So, even in directory buckets, the underlying storage is still key-based, but AWS adds **directory semantics** for:
    *   Faster lookups
    *   Recursive operations (delete empty directories)
    *   Better integration with workloads that expect hierarchy.

***

### ✅ **Key takeaway**

*   All S3 buckets ultimately store objects as **keys**.
*   Directory buckets **simulate real directories more closely** for specific use cases (IoT, logs, zonal performance).

---

### ✅ **What are Zonal Endpoints?**

*   Normally, S3 uses **regional endpoints** (e.g., `s3.us-east-1.amazonaws.com`), which span multiple Availability Zones (AZs).
*   **Directory buckets**, however, are designed for **low-latency, high-performance workloads** and **data residency**.
*   They provide **zonal endpoints**, meaning:
    *   The bucket is tied to a specific **Availability Zone**.
    *   The endpoint routes traffic directly to that AZ.
    *   Example:
            bucket-name--usw2-az1--x-s3.amazonaws.com
        Here, `usw2-az1` indicates the AZ.

***

### ✅ **Why Zonal Endpoints?**

*   **Performance:**
    *   Reduces network hops → lower latency.
    *   Ideal for workloads that need **fast, local access** (e.g., HPC, IoT).
*   **Data Residency:**
    *   Keeps data in a specific AZ for compliance or regulatory needs.
*   **Cost Optimization:**
    *   Avoids cross-AZ data transfer charges.

***

### ✅ **How Different from Regional Endpoints?**

| Feature    | Regional Endpoint    | Zonal Endpoint                |
| ---------- | -------------------- | ----------------------------- |
| Scope      | Entire region        | Single AZ                     |
| Durability | Multi-AZ replication | Single AZ (less redundancy)   |
| Use Case   | General workloads    | Low-latency, AZ-specific apps |

***

### ✅ **Important Considerations**

*   Zonal buckets **do not replicate across AZs** → less fault tolerance.
*   If the AZ goes down, data is temporarily unavailable.
*   Best for **specialized workloads**, not general-purpose storage.

