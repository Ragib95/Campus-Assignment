import json

data = open('json.txt')
data_parsed = json.load(data)
print 'bucket name:', data_parsed['Records'][0]['s3']['bucket']['name']
print 'eTag:', data_parsed['Records'][0]['s3']['object']['eTag']