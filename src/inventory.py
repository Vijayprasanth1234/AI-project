import boto3
import os

def list_ec2_instances():
    region = os.getenv("AWS_REGION", "us-east-1")
    ec2 = boto3.client("ec2", region_name=region)
    resp = ec2.describe_instances()
    instances = []
    for r in resp["Reservations"]:
        for i in r["Instances"]:
            instances.append(i)
    return instances
