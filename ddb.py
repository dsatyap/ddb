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
        obj_list = (obj.key.split('/'))
        obj_str = str(obj_list[-1])
        print (obj_str)

        contents = io.BytesIO()
        bucket.download_fileobj(obj.key, contents)
        contents.seek(0)
        with gzip.open(contents.getvalue(), "r") as fin:
    
        #with gzip.open(obj_str, "r") as fin:
            data = fin.read()
            j = json.loads (data.decode('utf-8'))
            print (type(j))

main()
