#Launching EC2 instance

import boto3
ec2_client = boto3.client('ec2', region_name='us-east-1')

instance = ec2_client.run_instances(
    ImageId='ami-0c94855ba95c71c99',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)

instance_id = instance['Instances'][0]['InstanceId']
print('EC2 instance created with ID:', instance_id)




#Creating EBS Volume
ec2_resource = boto3.resource('ec2', region_name='us-east-1')

volume = ec2_resource.create_volume(
    AvailabilityZone='us-east-1a',
    Size=10
)
volume_id = volume.id
print('EBS volume created with ID:', volume_id)



#Attaching EBS Volume

ec2_client.attach_volume(
    VolumeId=volume_id,
    InstanceId=instance_id,
    Device='/dev/xvdf'
)

print('EBS volume attached to the EC2 instance.')