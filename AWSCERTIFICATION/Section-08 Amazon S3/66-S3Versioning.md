# Amazon S3 - Versioning

- You can version your files in Amazon S3
- It is enabled at the bucket level 
- So we have our bucket and it's enabled with versioning. So whenever user uploads a file , it's going to create a version of that file at the selected key. 
- And then should we re-upload the same key, should we overwrite that file, then instead it's going to create a version two, then a version three and so on. 
- Therefore it is best practice to version your buckets
    - It protects against unintended deletes. For example , if you delete a file version, actually you just add a delete marker and therefore you can restore versions that were previously there instead. 
    - You can also easily roll back to a previous version  
- Note:- 
    - Any file that is not versioned prior to enabling versioning will the version null
    - Also if you suspend versioning, it does not delete the previous version. 


# Hands-On
- Go to properties where you have bucket versioning settings , edit this and enable this . Now anyfile we override now , is just going to add versions into our buckets. 
- Now say we want to update our website, currently we have I love Coffee written , we change it and write I love beaches and update the photo for beach.jpg
- Upload this same index.html file. Now when we open our website url , we see our content get changed 
- But what happened at the back . toggle show versions button, we are going to show the actuall version id with the files. So notice few things
    - the files we have uploaded before such as beach.jpg and coffee.jpg have a null version id because they were uploaded before we had enabled versioning. 
    - But the index.html file , you see two versions , one has version id null , which is the file we had uploaded  before enabling versioning. But the file we uploaded just right now has a version ID. And therefore by updating this file and uploading it into our S3 Bucket, we have created a new version ID . 
- With versioning , we can do is roll-back our page. We want to go back to our coffee content
    - Click on the newer version and delete a specific version id our our object 
    - It will be permanently deleted and cannot get back 

- Now toggle the show versioning, and delete coffee.jpg file , but this time we don't actually delete, we delete by adding a delete marker. So it doesn't actually delete the underlying object
    - Now toggle show  versioning, we see that we have a delete marker on our coffee.jpg file with this version id (this delete marker only show when show versioning toggle is off)
    - So if you open the website url , the image will now show,( opem the website url in different browser or do hard refresh tab otherwise image will be still visible)
    - To get back to image, delete this delete marker version id .