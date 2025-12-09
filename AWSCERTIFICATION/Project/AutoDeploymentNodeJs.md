# Automate Node js Deployment to AWS EC2 using Github Actions CI/CD

- We Create a nodejs project and deploy on Amazon EC2 using CI/CD pipeline .
- We use CI/CD pipeline because in future if we do any changes in our project then it get auto deployed when we push to github. 
- So first create a node js project . And push it to a github repo. (Also remember to add a start script)
- Now create an EC2 instance ,select ubuntu , generate a key pair, and in security group , we need both ssh rule and http rule so that we can call our api.
- Now connect this EC2 instance using your laptop terminal.(Remember need to connect in folder where you downlaod your .pem file)
- Now in gitub , we need to create actions to deploy our project. 
    - So go to actions tab , under Continous Integration , select Node js
    - Now we need to edit the CI 
    - We just want to run this when we push on our master branch , Not when we pull
    - Select Node js version 
    - Now at last , it will run that commands like , **npm ci** means download all the files
    - Then it will run **npm build** if present
    - But now we don't have build so remove this command
    - Also remove **npm test** command as we don't need it either
    - Also ,we want to run this on the server we provide , not on ubuntu server. So edit runs on as **self-hosted**
    - Now commit all these changes
- Now in actions , we see it has started his job already 
- Now go to settings , in actions , go to runners, as we select self-hosted runner , we need to create one 
- So create self-hosted-runner
    - select linux
    - Now we need to run all the commands (under downloads section ) in our terminal where we connect our ec2 instance
    - **mkdir actions-runner && cd actions-runner**
    - Next **curl -o actions-runner-linux-x64-2.329.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.329.0/actions-runner-linux-x64-2.329.0.tar.gz** (to donwload the latest runner package)
    - Next, run that echo command ( to validate the hash) **echo "194f1e1e4bd02f80b7e9633fc546084d8d4e19f3928a324d512ea53430102e1d  actions-runner-linux-x64-2.329.0.tar.gz" | shasum -a 256 -c**
    - Next , **tar xzf ./actions-runner-linux-x64-2.329.0.tar.gz** (to extract the installer )
    - Now also run commands under configuration
    - **./config.sh --url https://github.com/ansh-2004/AWS_EC2_deploy_CICD --token your_token**
    - Just enter and we see our self-hosted runner registration has successful 
    - It will create a folder in which our project is there whose name is _work bydefault which we can change

- Run ls command , we see multiple file in which we need to run **svc.sh** file
    - **sudo ./svc.sh install**  (now it will create runner ,check in your  github runners)
    - Check ip address of runner created (same as our ec2 instance private ip). This verifiers that runner is connected to our machine
    - Next start this runner using command **sudo ./svc.sh start**
    - Now it means our self-hosted server has started which is connected to our github. As it is connected to our github, our project will also be there
    - run ls command and we see  _work folder 
    - go to this folder and run ls command. We see we have our project folder in this
    - Go to this folder now and run ls command , we see all our project files. 
    - run ls -la command to check hidden files (.gitignore)

- Now we got our project , next we need to install node js 
    - so run **sudo apt update**  to update all the packages first 
    - next run **sudo apt-get install -y nodejs npm** to download node js and npm
    - next we need to install nginx **sudo apt-get install -y nginx**
    - next we donwload **pm2** . **sudo npm i -g pm2**
        - when we work on development , we use nodemon so that changes will automatically saved and server get restarted
        - Similarly , pm2 is for production manager

- Now , we need to set our nginx server
    - We have public ip in our EC2 instance , if we open this public ip on browser, we see it is runnig our nginx server. 
    - We see in our public ip , if we write :80 at last, it will be redirected to same our public ip
    - But if we write any other port like :8000 or any path like /api/ at last , it will show error 
    - It is because in our instance security group , we have a rule for http which has by default port 80 . 
    - But we need to customize our nginx server to run on 8000 also 
    - so for this go to **cd /etc/nginx/sites-available**
    - run ls , we see a **default** folder name
    - run **sudo nano default** to edit this default file
    - In this file, we see by default port 80
    - now paste this code under location /

    ```
    location /api {
    rewrite ^\/api\/(.*)$ /api/$1 break;
    proxy_pass http://localhost:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    ```
    - this code is telling that , if anyone hit on /api , redirect this to http://localhost:8000  which is path of our local machine  and then append api with it
    - Save and exit the file 
    - Now restart the nginx server using **sudo systemctl restart nginx**

- Now go to your project directory which is under actions-runner
    - cd ~/actions-runner/_work/your_project_folder
    - now run server.js file using pm2 **pm2 start server.js --name="Backend"**
    - We see our server has started

- Now on browser , now run **your_Ec2_public_ip/api/get**, 
    - we see our project is running
    - Our local host server is stopped  , but our project is running as it is successfuly deployed

- Now we want whenever we push to github , it automatically run 
    - So go to code , github/workflows
    - In the node.js.yml file , edit this and write command at last **-run: pm2 restart Backend**
    - Commit this file 

- Now if even close the machine from termianl , then still our server works
    - test is by updating  your project , make new api 
    - Commit it and push to github

- Now we see how can we add environment variables
    - create a .env file in your project , add only port in your .env file
    - as we don't push our .env file , we add in our .gitignore file 
    - so in github, go to setting , under secrets and variables , go to actions 
    - create a new repository secret
    - name it prod
    - now paste your data you have in your .env file in the secret block.
    - Add secret 
    - Now in your .yml file , we need to tell him about this environmental variables
        - so edit this and write command before restarting backend
        - run : | 
                - touch .env
                - echo "${{ secrets.prod }}" > .env
        - commit changes 

- Now you can check in your instance machine that your .env file is now available there

# Some important topics

## CI VS CD
- CI(Continuous Integration) focuses on automatically building and testing code changes frequently to catch bugs early, while CD (Continous Delivery/Deployment) extends CI bt automating the release process, ensuring code is always ready to Deploy (Delivery) or automatically deploying it to production(Deployment) after passing tests, making the whole lifecycle faster and more reliable. 
- CI is about code quality and integraion , CD is about releasing that quality code efficiently to users.

## Continuous Integraion (CI)
- Goal: Merge code changes into a shared repository often(daily) and run automated builds and tests to find issues quickly.
- Proces : Developers push code -> Automated build -> Automated tests (unit,integration)
- Benefit : Faster feedback for developers, fewer integration problems, higher code quality

## Continuous Delivery (CD)
- Goal : Ensure code is always in a deployable state , extending CI
- Process: CI pipeline runs successfully -> Code is automatically packaged and deployed to a staging /testing environment
- Benefit : Code is always production-ready; deployment to production is a manual , but simple step

## Continuous Deployment (CD)
- Goal : Fully automate the release process, going one step further than Delivery
- Process: Everything in Delivery , but after tests pass, the code is automatically deployed to production
- Benefit: Extremely fast release cycles,  direct and immediate value to users

## Key differences
- Scope : CI is about building & Testing ; CD is about releasing & deploying
- Automation : CI automates integration ; CD automates the path to production
- Manual Steps: Continuous Delivery might have a manual "go/no-go" for production; Continuous Deployment removes it.

## CI/CD Pipeline 
- It's the complete automated workflow from code commit to deployment , integrating both CI and CD practices. 

## NGINX
- It is a high-performance , open-source software that acts as a powerfull web server , reverse proxy, load balancer , cache and mail proxy, handling massive amounts of concurrent traffic efficently due to its event-driven , asynchronous architecture. It sits in front of backend servers, directing request, improving speed through caching, distributing loads, and offering security, making it essentail for modern high-traffic websites like netflix and Dropbox

    - **Web Servers** - Servers static content (HTML,CSS , images) directly to users.
    - **Reverse Proxy** - Sits in front of other servers(like Apache, Node.js) , forwarding client request to the appropriate backend server , hiding server details, and adding security layers.
    - **Load Balancer** - Distributes incoming traffic across multiple servers to pervent overload and ensure high availability.
    - **Caching** - Stores copies fo content (like files or API responses) to server them faster reducing load on origin servers.
    - **Mail Proxy** : Handles email protocols(IMAP,POP3,SMTP)
- NGINX is designed fro handling thousands of simultaneous connections efficiently.
- Combines multiple functionalities (proxy,load balancing,caching ) in one tool


## Proxy vs Reversy Proxy
- A proxy acts on behalf of the client to access the internet, while a reverse proxy acts on behalf of the server to recieve requests from clients
- Forward proxies are used by clients for tasks like privacy or bypassing restrictions, configured on the client-side. Reverse proxies are used by servers for performance, security, and load balancing, with the client typically unaware of their presence.                                                             


---

