
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

    # ddb = boto3.resource('dynamodb')
    ddb_client = boto3.client('dynamodb')
    #tablename = os.environ['TABLE_NAME']
    # table = ddb.Table('test-shivam-dynamodb')

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
        # obj.download_fileobj(data)
        # data.seek(0)
        print(data.getvalue())
        
        with gzip.GzipFile(fileobj=obj.get()["Body"]) as gzipfile:
            content = gzipfile.readlines()
        for cont in content:
            json_decoded_content = json.loads(cont.decode())
            print(json_decoded_content)
            response = ddb_client.put_item(
                TableName='dlt-CareerCompassRI-dev-Skipper-ProfileTable', Item=json_decoded_content['Item'])
            print("==========================================")
        
main()
