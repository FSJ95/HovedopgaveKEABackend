import logging
import boto3
import json
from botocore.exceptions import ClientError
import io

def upload_file(content, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """ 

    AWS_ACCESS_KEY_ID = 'AKIAZIPZIJIZYAAYD3VL'
    AWS_SECRET_ACCESS_KEY = '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'
    REGION_NAME = 'eu-north-1'

    S3_RESOURCE = boto3.resource('s3',
                                aws_access_key_id=AWS_ACCESS_KEY_ID,
                                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                region_name=REGION_NAME)

    S3_CLIENT = boto3.client('s3',
                            aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            region_name=REGION_NAME)

    BUCKET_SRC = S3_RESOURCE.Bucket(bucket)

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = content

    # Upload the file
    try:
        S3_CLIENT.put_object(Body=content, Bucket=bucket, Key=object_name, ACL='public-read')
    except ClientError as e:
         logging.error(e)
         return False


    return True

def delete_upload_from_amazon(upload_id):
    return None
