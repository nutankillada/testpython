'''
# check if any ebs volume creation happens - through CW EventBridge rule
# if yes - trigger the lambda function (lambda will need describeVolume & modifyVolume IAM permission)
# In lambda code, from the event data coming from CW EventBridge rule trigger, check the volume type
# if not gp3, modify volume type to gp3
'''

#import boto3

#ec2_client = boto3.client('ec2')

'''
lt = ['arn:aws:ec2:us-east-1:954976328253:volume/vol-0811']
lt9 = lt[0].split(":")
print(lt9[-1].split("/")[-1])
'''
'''
response = {
    'NextToken': 'string',
    'Volumes': [
        {
            'OutpostArn': 'string',
            'Iops': 123,
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            'VolumeType': 'standard',
            'FastRestored': True
        }   
    ]
}           
result = response['Volumes'][0]['VolumeType']
print(result)
'''

import boto3

def lambda_handler(event, context):

    ec2_client = boto3.client('ec2')
    #print(event)       # dictionary of vol details
    # {'version': '0', 'id': 'b6770066-2068-37b0-6787-24b286d82bc1', 'detail-type': 'EBS Volume Notification', 'source': 'aws.ec2', 'account': '954976328253', 'time': '2025-01-14T21:49:13Z', 'region': 'us-east-1', 'resources': ['arn:aws:ec2:us-east-1:954976328253:volume/vol-0811fbae1bcee29d9'], 'detail': {'result': 'available', 'cause': '', 'event': 'createVolume', 'request-id': '857036b3-aaff-4022-b5fb-b5e6de6e95d5'}}
    # required item--> 'resources': ['arn:aws:ec2:us-east-1:954976328253:volume/vol-0811fbae1bcee29d9']
    #print("----------------------------")
    #print(context)

    vol_details_resources = event['resources']  # ['arn:aws:ec2:us-east-1:954976328253:volume/vol-0811']
    vol_details = vol_details_resources[0].split(":")[-1]
    vol_id = vol_details.split("/")[-1]
    print(vol_id)

    response = ec2_client.describe_volumes(VolumeIds=[vol_id])
    vol_type = response['Volumes'][0]['VolumeType']
    print(vol_type)

    if vol_type == 'gp2':
        ec2_client.modify_volume(VolumeId=vol_id, VolumeType='gp3')
        print("Volume Type Modified from gp2 to gp3")
