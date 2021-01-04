
import boto3
import json
import os
import gzip
import io


def main():
    s3 = boto3.resource("s3")
    bucket = s3.Bucket("careercompassri-test-deploy")
    print(bucket)

    ddb = boto3.resource('dynamodb')
    #tablename = os.environ['TABLE_NAME']
    #table = ddb.Table(tablename)

    files = bucket.objects.filter(Prefix="AWSDynamoDB/01609430713846-ba34aa1b/data/")
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
        # with gzip.open(data.getvalue(), "rb") as fin:
        #     content = fin.read()
        #     print(content)
        #     j = json.loads(content.decode('utf-8'))
        #     print(type(j))
        with gzip.GzipFile(fileobj=obj.get()["Body"]) as gzipfile:
            content = gzipfile.read()
            j = json.loads(content.decode('utf-8'))
        print(type(content))


main()
