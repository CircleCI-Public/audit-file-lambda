import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
import json 

s3_client = boto3.client('s3')

def log_events(file_path):
	with open(file_path) as batch:
		for eventline in batch.readlines():
			eventjson = json.loads(eventline)
			print("Read Audit Event ID: {}, type: {}".format(eventjson['id'], eventjson['action']))
        

##
# Receives an S3 Event record, and determines if it is an audit file
##
def handler(event, context):
	print("Running event")
	for record in event['Records']:
		bucket = record['s3']['bucket']['name']
		key = unquote_plus(record['s3']['object']['key'])
		if key.startswith('audit-logs'):
			download_path = '/tmp/{}'.format(uuid.uuid4())
			s3_client.download_file(bucket, key, download_path)
			log_events(download_path)
