
import pytest
import boto3
#import s3Buckets
from hello import simpleAdd

def test_simpleAdd():
    assert 5 == simpleAdd(2,3)