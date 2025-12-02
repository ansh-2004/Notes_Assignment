# Auto Scaling Groups - Scaling Strategies

- Manual Scaling : When we update the size of a Auto Scaling Group manually. For eg, we changed the capacity from one to two or back from two to one. 
- Dynamic Scaling : Respond to changing demand automatically. We have different types of scaling policies within Dynamic Scaling
    - Simple/Step Scaling 
        - Whenever a cloudwatch alarm is triggered for example you say whenever the average CPU utilization of all my EC2 instances goes over 70% for five minutes, then add two units to capacity to my ASG
        - Or when another alarm for example, say whenever the CPU utilization is less than 30% for 10 minutes, then remove one unit of capacity in my ASG.
        - This is simple/step scaling because we define the trigger and define how many units we add or remove. 
    - Target Tracking Scaling 
        - Example , i want the average CPU utilization of all the EC2 instances in my ASG  to stay around 40% on average and then the ASG will scale automatically to make sure that you stay around that target of 40%
    - Scheduled Scaling
        - This is when we know that changes are going to happen ahead of time. 
        - So we anticipate a scaling based on known users patterns.
        - For example, we know that on Friday at 5:00 PM, People are going to do sports betting maybe who knows,before the soccer game,so increase the minimum capacity to 10 EC2 instances in my ASG at 5:00 pm on Friday
- Predictive Scaling
    - Uses Machine Learning to predict future traffic ahead of time so there's some algorithms that will look at the past traffic patterns,and it will forecast what will happen to traffic based on the past patterns.
    - It is called predictive because we predict what the load will be over time, and may be the load is just on a daily basis, it peaks on three hours
    - It will automatically provision the right number of EC2 instances in advance to match that predicted period.
    - This is helpful when you have time-based patterns and you just want to have an easy, without any intervention type of scaling