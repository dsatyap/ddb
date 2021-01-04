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

    ddb = boto3.resource('dynamodb')
    tablename = "dlt-CareerCompassRI-dev-Skipper-ProfileTable"
    #table = ddb.Table(tablename)

    files = bucket.objects.filter(
        Prefix="AWSDynamoDB/01609430713846-ba34aa1b/data/")
    for obj in files:
        print('{0}'.format(obj.key))
        print('{0} is obj'.format(obj))
        obj = bucket.Object(obj.key)
        obj_list = (obj.key.split('/'))
        obj_str = str(obj_list[-1])
        print(obj_str)
        data = io.BytesIO()
        print(data.getvalue())
    
        with gzip.GzipFile(fileobj=obj.get()["Body"]) as gzipfile:
            content = gzipfile.readlines()
        for cont in content:
            decoded_content = cont.decode()
            j = json.loads(decoded_content)
            print(j)
            print("==========================================")
            with table.batch_writer() as batch:
                batch.put_item(Item=j)
       
main()
