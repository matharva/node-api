import boto3

client = boto3.client('xray',
                      aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                      aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                      region_name=os.getenv('AWS_DEFAULT_REGION')
                      )

ec2 = boto3.resource('ec2')
ec2.create_instances(ImageId='<ami-image-id>', MinCount=1, MaxCount=5)
