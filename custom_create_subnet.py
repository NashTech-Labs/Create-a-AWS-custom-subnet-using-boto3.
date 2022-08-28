# By MuZakkir Saifi
# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError

REGION = input("Please enter the REGION: ")
Tag=input("Enter the tag name: ")
Tag_Value=input("Enter the tag value: ")
# this is the configration for the logger_for

logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

client = boto3.resource("ec2", region_name=REGION)

# this is the configuration for subnet
def custom_subnet(az, id, block):

    try:
        response = client.create_subnet(TagSpecifications=[
            {
                'ResourceType': 'subnet',
                'Tags': [{
                    'Key': Tag,
                    'Value': Tag_Value
                }]
            },
        ],
                                              AvailabilityZone=az,
                                              VpcId=id,
                                              CidrBlock=block)

    except ClientError:
        logger_for.exception(f'Oops sorry, Your custom subnet can not created:')
        raise
    else:
        return response


if __name__ == '__main__':
    BLOCK = input('Enter the CIDR Block:  ')
    ID = input('Enter the VPC ID: ')
    Zone = input('Enter the availability zone:  ')
    logger_for.info(f'Please wait your custom Subnet is creating...')
    custom_subnet = custom_subnet(Zone, ID, BLOCK)
    logger_for.info(f'Wow !!, Your Custom Subnet is created with Subnet ID: {custom_subnet.id}')