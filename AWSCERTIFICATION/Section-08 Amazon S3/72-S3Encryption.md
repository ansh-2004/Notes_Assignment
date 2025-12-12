# S3 Encryption

## Server-Side Encryption (Default) 
- It is by default whenever you create a bucket or whenever you upload an object, it will be encrypted .
- The user uploads an object into Amazon S3, and then that object when it arrives in the bucket is going to be encrypted by Amazon S3 for security purposes. The idea is that the server is doing the encryption and therefore we call this server-side encryption.

## Client-Side Encryption 
- This is when the user will actually take the file, will encrypt it before uploading it, so the lock is done by the user and then put it in the bucket 