import boto3

# Change BUCKET_NAME to your bucket name and
# KEY_NAME to the name of a file in the directory where you'll run the curl command.
BUCKET_NAME = 'lanzaaz-test-bucket-9ad988'
KEY_NAME = 'filetoupload.pdf'

s3 = boto3.client('s3')

resp = s3.generate_presigned_post(
    Bucket=BUCKET_NAME,
    Key=KEY_NAME,
    Fields=None,
    Conditions=None,
    ExpiresIn=300
)

resp['fields']['file'] = '@{key}'.format(key=KEY_NAME)

form_values = "\n    ".join(["-F {key}={value} \\".format(key=key, value=value)
                        for key, value in resp['fields'].items()])

print('CURL COMMAND: \n')
print('curl -v {form_values}\n    {url}'.format(form_values=form_values, url=resp['url']))
print()
