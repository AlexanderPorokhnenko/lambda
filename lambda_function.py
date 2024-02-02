import csv
import requests
import boto3
import time


def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    with open('/tmp/cat_facts.csv', 'w', newline='') as fileobj:
        writer = csv.writer(fileobj)
        header = ["id", "fact", "timestamp"]
        writer.writerow(header)
        for i in range(10):
            response = requests.get("https://catfact.ninja/fact")
            if response.status_code == 200:
                writer.writerow([i,response.json()['fact'], int(time.time()) ])
    return s3.Bucket(event["bucket_name"]).upload_file('/tmp/cat_facts.csv', event["filename"])
