
import boto3
import json
import os
import gzip
import io
# import simplejson
import re


def main():
    s3 = boto3.resource("s3")
    bucket = s3.Bucket("careercompassri-test-deploy")
    print(bucket)

    ddb_client = boto3.client('dynamodb')
    
    files = bucket.objects.filter(
        Prefix="AWSDynamoDB/01609430713846-ba34aa1b/data/")
    for obj in files:
        print('{0}'.format(obj.key))
        print('{0} is obj'.format(obj))
        obj = bucket.Object(obj.key)
        
        
        with gzip.GzipFile(fileobj=obj.get()["Body"]) as gzipfile:
            content = gzipfile.readlines()
        for cont in content:
            json_decoded_content = json.loads(cont.decode())
            print(json_decoded_content)
            response = ddb_client.put_item(
                TableName='dlt-CareerCompassRI-dev-Skipper-ProfileTable', Item=json_decoded_content['Item'])
            print("==========================================")
        
main()
