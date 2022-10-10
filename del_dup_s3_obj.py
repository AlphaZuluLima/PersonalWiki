#!/usr/bin/env python3
import boto3
import argparse
import json
import collections
import pprint
import os
import sys



os.system("")


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

#print(style.BLUE + "Hello, World!" + style.RESET)
#print(f"{style.GREEN}Hello, World!{style.RESET}")



parser = argparse.ArgumentParser('Find duplicate objects in an aws s3 bucket')
parser.add_argument('--bucket', dest='myBucket', default='yourBucketName', help='S3 Bucket to search')

cliArgs = parser.parse_args() 

myBucket = cliArgs.myBucket

# Create an s3 client
s3 = boto3.client('s3')

# Create a reusable Paginator
paginator = s3.get_paginator('list_objects')

# Create a PageIterator from the Paginator
page_iterator = paginator.paginate(Bucket=myBucket)

dict_of_etag_size_tuples = {}
 
for page in page_iterator:
    contents = page['Contents']
    for obj in contents:
        #print(json.dumps(obj, indent=4, default=str))
        S3key = obj['Key']
        ETag = obj['ETag']
        Size = obj['Size']
        etag_size_tuple = (ETag,Size)
        dict_of_etag_size_tuples[S3key] = etag_size_tuple

val_map = collections.defaultdict(list)
for k,v in dict_of_etag_size_tuples.items():
    val_map[v].append(k)

#pprint.pprint(val_map)

val_map = dict(val_map)

list_of_s3keys_to_delete = []

print('\n' * 3)

for k,v in val_map.items():
    if len(v) > 1:
        #for filename in v:
        #    print(filename + ' :   ' + str(k[0]) + ' ' + str(k[1]))
        #print('\n' * 3)
        dup_list_size = len(v)
        for itemnumber in range(1,len(v)):
            print(f"{style.BLUE}{v[itemnumber]}{style.RESET} is a duplicate of {style.GREEN}{v[0]}{style.RESET}")
            list_of_s3keys_to_delete.append(v[itemnumber])
        print()

print('\n' * 3)
print('The following objects will be deleted from S3 should you choose to proceed...\n')
for s3key in list_of_s3keys_to_delete:
    print(f"{style.RED}{s3key}{style.RESET}")

print('\n' *3)

proceed_with_deletion = input("Type 'yes' if would you like to proceed with deletion of the files from S3.\nAny other response will abort.\n\n")

if proceed_with_deletion == 'yes':
    print(f"\n\n\nProceeding with deletion of files from S3\n\n\n")
    for s3key in list_of_s3keys_to_delete:
        s3.delete_object(Bucket=myBucket, Key=s3key)
else:
    print(f"\n\n\nAborting\n\n\n")

