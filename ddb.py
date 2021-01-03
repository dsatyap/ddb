import boto3
import json
import os
import gzip

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
        print (obj.key.split('/'))[-1]
        f = obj.key.split('/')[-1]
        print (f)
    
    with gzip.open("AWSDynamoDB/01609430713846-ba34aa1b/data/5lc3kqepyu6sjo64cbdpb2xfmu.json.gz", "r") as fin:
        data = fin.read()
        j = json.loads (data.decode('utf-8'))
        print (type(j))

main()
