import json
import boto3
import os

sqs = boto3.client('sqs')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        if not body.get('name') or not body.get('email') or not body.get('product'):
            return {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST"
                },
                "body": json.dumps({"message": "Missing required fields"})
            }

        sqs.send_message(
            QueueUrl=os.environ['SQS_URL'],
            MessageBody=json.dumps(body),
            MessageGroupId="orderGroup1"
        )

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({"message": "Order received successfully"})
        }
    
    except Exception as e:
        print("ERROR:", str(e))  # <-- This will show in CloudWatch Logs
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"message": "Internal Server Error"})
        }

