import csv 
import boto3

with open('rekognition_credentials.csv', 'r') as input: 
    next(input)
    # skips first row & then reads from second 
    reader = csv.reader(input)
    for line in reader: 
        access_key_id = line[2]
        secret_access_key = line[3]

photos = ['fridge1.png', 'fridge2.png', 'fridge3.png', 'fridge4.png', 'fridge5.png']

client = boto3.client('rekognition', 
                        aws_access_key_id = access_key_id, 
                        aws_secret_access_key = secret_access_key)

# Method when storing images locally
for photo in photos: 
    with open(photo, 'rb') as source_image: 
        source_bytes = source_image.read()
    response = client.detect_labels(Image = {'Bytes': source_bytes},
                                    MaxLabels = 3, 
                                    MinConfidence = 95)
                                # only show labels which have confidence of at least 95% 
    print("The main response label is: ", response['Labels'][0]['Name'],", ", "with a Confidence of", response['Labels'][0]['Confidence'] )


