import json
import boto3
import os
import base64
from datetime import datetime

#Create AWS clients
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('orders')

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    for record in event['Records']:
        order = json.loads(records['body'])
        order_id = f"ORDER-{init(datetime.now().timestamp())}"

        #save order to DynamoDB
        table.put_item(
            Item={
                'order_id': order_id,
                'name': order['name'],
                'email': order['email'],
                'product': order['product'],
                'timestamp': datetime.now().isoformat()
            }
        )

        # Upload optional file to S3    
        if 'fileContent' in order and 'fileName' in order:
            file_content = base64.b64decode(order['fileContent'])
            s3.put_object(
                Bucket=os.environ['S3_BUCKET'],
                Key=f"orders/{order['fileName']}",
                Body=file_content
            )

        # Send SNS noification
        sns.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],
            Subject=' Order Processed',
            Message=f"Order for {order['name']} processed successfully. ID: {order_id}",
        )