import boto3
import json
import os

def main():
    client = boto3.client('s3')
    s3 = boto3.resource("s3")
    bucket = s3.Bucket("careercompassri-test-deploy")
    print (bucket)
    bucket.get_available_subresources()
    response = client.get_bucket_policy(Bucket='careercompassri-test-deploy')
    print (response)
main()
