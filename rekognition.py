import csv 
import boto3

with open('rekognition_credentials.csv', 'r') as input: 
    next(input)
    # skips first row & then reads from second 
    reader = csv.reader(input)
    for line in reader: 
        access_key_id = line[2]
        secret_access_key = line[3]

photo = 'water_bottle.jpeg'
# we must convert to base..byte 

client = boto3.client('rekognition', 
                        aws_access_key_id = access_key_id, 
                        aws_secret_access_key = secret_access_key)

# Method when storing images locally
with open(photo, 'rb') as source_image: 
    source_bytes = source_image.read()

response = client.detect_labels(Image = {'Bytes': source_bytes},
                                MaxLabels = 2, 
                                MinConfidence = 95)
                                # only show labels which have confidence of at least 95% 
                    
print(response)

# Method when storing images in S3 ##############################################

#response = client.detect_labels(Image = {'S3Object': {
#        'Bucket': 'bucket_name',
#        'Name' : photo}},
#        # photo name saved above, or specify in quotations ''
#        MaxLabels = 2, 
#        MinConfidence = 95)

# print(response)