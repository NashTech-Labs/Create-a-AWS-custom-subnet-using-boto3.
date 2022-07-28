# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_resource = boto3.resource("ec2", region_name=AWS_REGION)

# this is the configuration for subnet
def custom_subnet(az, vpc_id, cidr_block):
    """
    Creates a custom subnet with the specified configuration.
    """
    try:
        response = vpc_resource.create_subnet(TagSpecifications=[
            {
                'ResourceType': 'subnet',
                'Tags': [{
                    'Key': 'Name',
                    'Value': 'custom-subnet'
                }]
            },
        ],
                                              AvailabilityZone=az,
                                              VpcId=vpc_id,
                                              CidrBlock=cidr_block)

    except ClientError:
        logger.exception(f'Could not create a custom subnet.')
        raise
    else:
        return response


if __name__ == '__main__':
    
    # CIDR_BLOCK = '192.168.1.0/20'
    CIDR_BLOCK = input('Enter the CIDR ')
    # VPC_ID = 'vpc-00720462142847955'
    VPC_ID = input('Enter the VPC ID')
    # AZ = 'ap-south-1a'
    AZ = input('Enter the availability zone')
    logger.info(f'Creating a custom Subnet...')
    custom_subnet = custom_subnet(AZ, VPC_ID, CIDR_BLOCK)
    logger.info(f'Wow !!, Your Custom Subnet is created with Subnet ID: {custom_subnet.id}')