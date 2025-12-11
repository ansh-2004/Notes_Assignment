# Amazon S3 - Replication (CRR & SRR)

- The idea is that we have an S3 bucket in one region (let's say eu-west-1) and a target S3 bucket in another region (let's say us-east-2) and we want to set up asynchronous replication between these two buckets.
- So to do so , we first must enable versioning in the source and destination buckets
- If we do CRR (Cross-Region Replication) in which two regions must be different 
- If we do SRR (Same-Region Replication) in which two regions are the same 
- Now it's possible for you to have these buckets in different AWS accounts and copying happens asynchronously
- So the replication mechanism happens behind the scenes in the background
- And to make replication work , you must give proper IAM permissions to the S3 services so that it has the permission to read and write from specified buckets. 

## Use Cases
    - If we use CRR , it can be helpful for compliance or for providing lower latency access to your data because it is in another region or to replicate data across accounts
    - If we use SRR, it can be helpful to aggregate logs across multipe S3 buckets or to perform a live replication between a production and test accounts , so to have your own test enviroment 


---

# Amazon S3 replication overview

S3 Replication copies objects from a source bucket to a destination bucket automatically and asynchronously after upload. It supports Cross-Region Replication (CRR) and Same-Region Replication (SRR). You choose rules that define what to replicate (prefixes, tags), how to handle deletes, ownership, metadata, and encryption.

---

## Requirements and basics

- **Versioning:** Enable versioning on both source and destination buckets. Replication won’t start without it.
- **Permissions:** A replication IAM role must allow S3 to read from the source and write to the destination. The setup wizard can create this role automatically.
- **Asynchronous:** Replication happens in the background after object creation. It’s not immediate and ordering isn’t guaranteed for rapid updates.
- **New objects:** By default, only objects uploaded after you enable replication are copied. You can add “replication for existing objects” via Batch Operations or the “Replicate existing objects” feature.
- **Accounts and regions:** Works within the same account or across accounts; CRR requires different regions, SRR uses the same region.
- **Storage classes:** Replication can preserve the original class or change it at the destination (e.g., source Standard → destination Standard-IA).

---

## What gets replicated and how

- **Objects and metadata:** Object data, system metadata (size, storage class) and optional replication of object tags and ACL/ownership, depending on your rule settings.
- **KMS-encrypted objects:** Supported, but you must configure KMS permissions for both source and destination keys (allow S3 to decrypt/encrypt).
- **Delete markers and deletes:**
  - **Replicate delete markers:** If enabled, when you delete (add a delete marker) on source, a delete marker is added on destination. This hides the object at the destination without removing versions.
  - **Hard deletes of versions:** Replication does not remove specific versions at destination when you permanently delete a version on source.
- **Existing objects:** Not automatically replicated; use Batch Operations or enable “replicate existing objects.”
- **Replication time control (RTC):** Optional SLA to deliver 99.99% of objects replicated within 15 minutes for CRR; adds cost.

---

## CRR vs SRR: when to choose

| Goal | Choose CRR | Choose SRR |
|------|------------|------------|
| **Compliance/DR in another region** | Yes | No |
| **Lower latency for global users** | Yes | No |
| **Cross-account segregation (prod → DR)** | Yes (or SRR across accounts in same region) | Yes |
| **Aggregate logs across buckets** | Possible, but SRR is simpler and cheaper | Yes (common pattern) |
| **Blue/green or prod→test copy within region** | Not required | Yes |
| **Avoid inter-region data transfer costs** | No (CRR has inter-region charges) | Yes |

- **Choose CRR** for regulatory copies, disaster recovery, geo-proximity access, or isolating data in a separate region/account.
- **Choose SRR** for operational workflows inside one region: log aggregation, analytics pipelines, copying prod data to test, or multi-account mirroring without inter-region latency/cost.

> Tip: You can replicate to multiple destinations (multi-destination replication) to serve mixed needs (e.g., SRR to logs bucket and CRR to DR bucket).

---

## Key configuration options and best practices

- **Scope rules:**
  - **Prefixes:** Limit replication to folders (e.g., logs/, data/).
  - **Tags:** Replicate only objects matching specific tags (e.g., environment=prod).
  - Combine prefixes and tags to target exactly what you need.
- **Ownership and access:**
  - **Object Ownership (Bucket owner preferred):** Simplifies cross-account scenarios so destination account owns replicated objects.
  - **ACL/tag replication:** Enable only if required; prefer bucket policies and Object Ownership over ACLs.
- **Encryption:**
  - **SSE-S3:** Easiest; no extra setup.
  - **SSE-KMS:** Ensure key policies grant S3 service and source role decrypt permission, and destination key encrypt permission. Explicitly allow the replication role principal.
- **Storage classes:**
  - Use lower-cost classes at destination (Standard-IA, One Zone-IA, Glacier Instant Retrieval) if destination is for DR or analytics.
- **Delete behavior:**
  - Enable “replicate delete markers” for symmetric visibility across buckets.
  - Lifecycle rules can expire old versions and delete markers at destination independently.
- **Eventual consistency and ordering:**
  - Avoid workflows that depend on strict ordering. If your app updates the same key rapidly, consider object versioning semantics on the consumer side.
- **Monitoring and audit:**
  - **Replication status:** Check object metadata and S3 console for status (e.g., PENDING, COMPLETED, FAILED).
  - **CloudWatch metrics and Event notifications:** Alert on failures; log to S3 access logs for traceability.

---

## Common use cases in detail

- **Compliance and disaster recovery (CRR):**
  - **Why:** Regs require data in a separate region; DR demands an isolated copy.
  - **How:** Source in region A replicates to destination in region B with SSE-KMS; destination bucket denies public access and is read-only except for replication role. Optionally enable Replication Time Control.
  - **Extras:** Lifecycle at destination to transition to cheaper storage; regular DR testing with sampled restores.

- **Global user latency (CRR):**
  - **Why:** Users in different continents get better read latency from a nearby region.
  - **How:** Replicate frequently accessed keys; front with CloudFront in each region or use region-specific endpoints.
  - **Extras:** Cache-control headers and CDN to minimize origin hits.

- **Log aggregation (SRR):**
  - **Why:** Centralize application or access logs across many buckets and accounts.
  - **How:** Replicate from app buckets to a central logs bucket in same region. Filter by prefix “logs/”. Destination applies lifecycle to transition to Glacier.
  - **Extras:** Use S3 Object Lock (WORM) on destination for compliance if needed.

- **Prod → Test data mirroring (SRR or cross-account SRR):**
  - **Why:** Keep test/staging up-to-date with a subset of prod data without cross-region costs.
  - **How:** Replicate tagged objects (tag: replicate=true). Destination account owns objects; restrict access to test roles only.
  - **Extras:** Anonymize or filter PII by tagging only non-sensitive keys.

- **Multi-destination replication:**
  - **Why:** Different consumers need data in different places.
  - **How:** Create multiple rules: SRR to analytics bucket, CRR to DR bucket. Use prefixes/tags to avoid duplication where not needed.

