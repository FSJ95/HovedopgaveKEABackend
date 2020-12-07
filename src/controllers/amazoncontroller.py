import logging
import boto3
from botocore.exceptions import ClientError

AWS_ACCESS_KEY_ID = 'AKIAZIPZIJIZYAAYD3VL'
AWS_SECRET_ACCESS_KEY = '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'
REGION_NAME = 'eu-north-1'
BUCKET = 'keabucket'

def getClient():
    return boto3.client('s3',
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                        region_name=REGION_NAME)

def upload_file(content, file_name=None):
    """Upload a file to an S3 bucket

    :param content: content to upload
    :param bucket: Bucket to upload to
    :param file_name: S3 object name. If not specified then content is used
    :return: True if file was uploaded, else False
    """ 

    # If S3 object_name was not specified, use file_name
    if file_name is None:
        file_name = content[0:20] + '.json'

    # Upload the file
    try:
        getClient().put_object(Body=content, Bucket=BUCKET, Key=file_name, ACL='public-read')
    except ClientError as e:
         logging.error(e)
         return False


    return True

def delete_upload_from_amazon(upload_id):

    #retrieve filename from upload id instead of this:
    file_name = upload_id

    try:
        getClient().delete_object(Bucket=BUCKET, Key=file_name)
    except ClientError as e:
         logging.error(e)
         return False
    return True
                        
