# project-aws-lambda-s3-processing
![Image](https://github.com/user-attachments/assets/a1bed561-9294-47c6-92d2-93e4312aea90)

# Overview

This project provides an automated serverless solution for processing files uploaded to an S3 bucket using AWS Lambda. The Lambda function is triggered whenever a new file is uploaded to the designated S3 bucket. It processes the file, performs necessary transformations, and logs the results. The solution also includes integration with CloudWatch for monitoring Lambda execution and SNS for failure notifications.

The goal of this project is to automate file processing tasks (such as text file parsing or data transformation) in a scalable and cost-effective manner using AWS services. You can extend the processing logic within the Lambda function to suit various use cases, such as data filtering, transformation, or integration with other AWS services like DynamoDB or S3.




# Project Structure
## lambda/
Contains the main Lambda function (lambda_function.py) responsible for processing files from S3

## sns/
Contains the script (sns_topic_setup.py) to create an SNS topic and send notifications when an alarm is triggered.

## cloudwatch/
Contains the script (cloudwatch_alarm_setup.py) to create CloudWatch alarms to monitor Lambda function performance.

## config/
Contains configuration files for the Lambda function, such as S3 bucket names or API keys, in config.json.

# Setup Instructions
AWS account: You need an AWS account to deploy the resources.
AWS CLI: Install and configure the AWS CLI on your machine to deploy resources.
IAM Permissions: Make sure the IAM role associated with Lambda has the necessary permissions for S3, SNS, CloudWatch, etc.

![Image](https://github.com/user-attachments/assets/a9bb7021-2dad-4ba9-94c2-c20f98068e7e)

## Step 1: Set Up AWS Lambda
The first step is to set up the Lambda function in your AWS account. Go to the AWS Lambda Console and create a new Lambda function. Select Author from Scratch, give the function a name like S3FileProcessor, and choose the Python 3.x runtime. Ensure the IAM role assigned to the Lambda has the necessary permissions for S3, CloudWatch, and SNS.

After creating the Lambda function, you need to upload the code from the lambda/ folder. You can do this by selecting the Upload from option in the Lambda console and choosing .zip file. Upload the zipped lambda_function.py file.
![Image](https://github.com/user-attachments/assets/7c1e0723-197c-413d-aa5b-244ca0a1fa52)

## Step 2: Set Up S3 Bucket
Next, create an S3 bucket where the files will be uploaded. You can name it something like datastoragebarsagiv. In the S3 console, go to the Properties tab of your bucket and enable event notifications. Set the event to trigger the Lambda function whenever an ObjectCreated event occurs. Make sure that the Lambda execution role has permissions for s3:GetObject and s3:ListBucket.
![Image](https://github.com/user-attachments/assets/1f2fac94-c7ba-4e31-b6de-ed4fdfecffa1)


## Step 3: Set Up SNS
If you want to receive notifications when something goes wrong with the Lambda function, you can set up an SNS topic. Create an SNS topic called LambdaFailureNotifications in the AWS SNS Console. After creating the topic, subscribe to it by adding your email address or other notification methods. Ensure the Lambda function has permissions to publish messages to the SNS topic. The failure notifications can be configured in the sns/ folder by using the sns_topic_setup.py script.
![Image](https://github.com/user-attachments/assets/87cb124a-e28d-43d0-a171-1cf781ee2032)


## Step 4: Set Up CloudWatch Alarms
To monitor the Lambda function's health, set up a CloudWatch alarm. Go to the AWS CloudWatch Console and create an alarm for the Lambda Errors metric. Set a threshold to trigger an alarm when the error count exceeds a certain limit, such as more than 5 errors within 5 minutes. Link the alarm to the SNS topic you created earlier so you get notified when the alarm is triggered.

![Image](https://github.com/user-attachments/assets/72ab8c41-dfcf-4cb0-8d07-7fcff9f7e45e)
![Image](https://github.com/user-attachments/assets/83a67959-36d9-4d78-b8d6-df246fe9f029)
![Image](https://github.com/user-attachments/assets/46927cdf-3730-4611-9686-ea20bb61fbe8)


## Step 5: Test the Setup
Once everything is configured, upload a test file (such as a .txt file) to your S3 bucket. This should trigger the Lambda function, and you can verify the function's execution by checking CloudWatch Logs. If everything works as expected, you should see log entries showing that the file was processed. If you've set up SNS, you will receive a notification in case of any failure.

![Image](https://github.com/user-attachments/assets/973f97c9-856b-401a-872a-1297e07e6441)
