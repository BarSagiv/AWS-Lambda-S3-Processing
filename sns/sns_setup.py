import boto3

# Initialize SNS client
sns = boto3.client('sns')

def create_sns_topic():
    response = sns.create_topic(Name='S3FileUploadTopic')
    topic_arn = response['TopicArn']
    print(f"SNS Topic ARN: {topic_arn}")
    return topic_arn

def subscribe_to_sns(topic_arn, email):
    sns.subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint=email
    )
    print(f"Subscribed {email} to topic {topic_arn}")

# Example usage:
topic_arn = create_sns_topic()
subscribe_to_sns(topic_arn, 'barsagiv8@gmail.com')
