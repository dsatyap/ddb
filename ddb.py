import boto3
import json
import os

def main():
    
    s3 = boto3.resource("s3")
    bucket = s3.Bucket("careercompassri-test-deploy")
    print (bucket)

main()
