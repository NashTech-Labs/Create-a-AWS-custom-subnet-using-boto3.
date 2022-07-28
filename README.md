## Create a AWS custom subnet using boto3.

#### A subnet is a range of IP addresses in your VPC. You can attach AWS resources, such as EC2 instances and RDS DB instances, to subnets. You can create subnets to group instances together according to your security and operational needs. You can follow this [link](https://docs.aws.amazon.com/quicksight/latest/user/vpc-subnets.html) to know more.

-------------

**Files:** 
```
    custom_create_subnet.py
```

## Apply the script

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command to create a custom subnet.

        python3 custom_create_subnet.py
