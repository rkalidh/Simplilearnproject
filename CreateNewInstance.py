## This script will work for creating instances in aws and taking backup of instance
import boto3
s=boto3.Session(region_name="ca-central-1")
ec2 = s.resource('ec2')
client=boto3.client('ec2')
#backup=client.create_image(InstanceId='i-03c68b7e21265640a',Name='Linux-serverbackup')
#ids=['i-0ccdd37d704f9b949','i-0db86a801f4577460']
for instance in ec2.instances.all():
    print(instance.id,instance.state)
#ec2.instances.filter(InstanceIds=ids).terminate()
#ec2.instances.filter(InstanceIds=ids).start()
#print("Succesfully Started")
#Below code is to create New Linux instance
instances = ec2.create_instances(
    ImageId='ami-07423fb63ea0a0930', 
    MinCount=1, 
    MaxCount=1,
    KeyName="ec2-keypair",
    InstanceType="t2.micro"
)
print("Successfully Created")
#print("Successfully backedup")




