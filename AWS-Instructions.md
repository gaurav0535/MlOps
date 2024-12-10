**Instructions to Deploy Applications on AWS.** 

**Plan of Action:**

1. Create a repo on ECR.  
2. Push the docker image to the ECR repo.  
3. Run the image using ECS \- Fargate.  
4. To run the image create a cluster and run a task inside a container. 

**Detailed Steps:**

1. Log in to the AWS Labs and make sure the region is ‘us-east-1’ or N. Virginia.  
2. Search for ECR service.  
   1. Create an ECR repo with the name `flask_loan_app`  
3. Search for the IAM service to create access keys.  
   1. Go to Users on the left panel.  
   2. There’s already a username. Click on that.   
   3. Security credentials.  
   4. Access Key create  
   5. Use CLI  
   6. Store ID and secret key somewhere.  
4. Install AWS CLI \[Optional\]  
   1. Official docs \- [https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)  
5. AWS CLI Configuration  
   1. Write the command `aws configure` in the terminal  
   2. Input the access ID and secret key here.   
   3. Leave remaining default.  
   4. Successfully configured.  
6. Build Docker Image and Push to ECR  
   1. Go to ECR service and inside the `flask_loan_app` repo you’ve created.  
   2. On the top right→ View Push commands.  
   3. Execute these commands one by one in the terminal (except 2nd command)  
   4. 1st command is to log in yourself from the CLI.  
   5. Use this command to build docker image `docker build —-platform=linux/amd64 -t flask_loan_app .`  
   6. The third command is used to give a tag  
   7. The fourth command is to push the image to the ECR repo.   
   8. Copy the URI from the pushed image.  
7. ECS for execution  
   1. Search for ECS service. click → Get Started  
   2. Create a new cluster   
   3. Name: `loan_app_cluster`  
   4. Infrastructure: `Fargate`  
   5. Leave everything default. Click→  Create  
8. Create a Task Definition  
   1. From the left panel, go to task definition and click → create a new task definition.   
   2. Name: `loan_app_task`  
   3. Container-1:   
      1. Name: `loan_app_container`  
      2. Img URI : `<paste docker img URI>`  
   4. Click Create.  
   5. Go inside this newly created task.  
9. Run Task  
   1. Click on the Deploy button → Run the task  
   2. Keep everything default. Come to the Networking section.  
   3. Click Create own security group.  
   4. HTTP → Port 80 → source : Anywhere  
   5. Custom TCP → Port 5000 → source : Anywhere  
   6. Click Create  
   7. Now the task is running.  
10. Testing  
    1. Click on the task that is running  
    2. Confirm the status → running  
    3. Scroll down and see the Public IP address  
    4. 18.206.12.187:5000/

       