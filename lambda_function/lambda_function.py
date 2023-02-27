import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket_name = os.environ['BUCKET_NAME']
    bucket = s3.Bucket(bucket_name)
    
    # Upload a file to the bucket
    with open('/tmp/report.txt', 'w') as f:
        f.write('Report data')
    bucket.upload_file('/tmp/report.txt', 'report.txt')
    
    # Delete all files in the bucket
    for obj in bucket.objects.all():
        obj.delete()
    
    # Check if any files remain in the bucket
    if len(list(bucket.objects.all())) > 0:
        sns = boto3.client('sns')
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:123456789012:my-topic',
            Message='Lingering files found in S3 bucket!'
        )
