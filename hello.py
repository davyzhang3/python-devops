import boto3


def myS3Buckets():
    s3 = boto3.client("s3")
    all_my_S3_buckets = s3.list_buckets()
    print("A list of my buckets:")
    for bucket in all_my_S3_buckets['Buckets']:
        print(bucket['Name'])
        

def simpleAdd(x, y):
    return x+y

if __name__ == "__main__":
    myS3Buckets()
    print("I modified sth on github")
    # a new comment
