import boto3
import json
import os
import gzip
import io

def main():
    s3 = boto3.resource("s3")
    bucket = s3.Bucket("careercompassri-test-deploy")
    print (bucket)
    
    ddb = boto3.resource('dynamodb')
    #tablename = os.environ['TABLE_NAME']
    #table = ddb.Table(tablename)
    
    files = bucket.objects.filter(Prefix="AWSDynamoDB/01609430713846-ba34aa1b/data/")
    for obj in files:
        print('{0}'.format(obj.key))
        obj = bucket.Object(obj.key)
        print ('{0} is obj'.format(obj))
        obj_list = (obj.key.split('/'))
        obj_str = str(obj_list[-1])
        print (obj_str)
        data = io.BytesIO()
        obj.download_fileobj(data)
        with gzip.open(data.getvalue(), "r") as fin:
            content = fin.read()
            j = json.loads (content.decode('utf-8'))
            print(type(j)) 

main()
