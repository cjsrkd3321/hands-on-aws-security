# 1. 특정 태그를 갖고 있는 VPC 존재하는지 확인
# 2. 없는 경우 VPC 생성
# 3. 있는 경우 VPC 삭제

import boto3

ec2 = boto3.client("ec2")

vpcs = ec2.describe_vpcs(
    Filters=[
        {
            "Name": "tag:Name",
            "Values": [
                "main-vpc",
            ],
        },
    ],
)["Vpcs"]

if not vpcs:
    res = ec2.create_vpc(
        CidrBlock="10.0.0.0/16",
        TagSpecifications=[
            {
                "ResourceType": "vpc",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "main-vpc",
                    },
                ],
            },
        ],
    )
    print(res["Vpc"])
else:
    res = ec2.delete_vpc(VpcId=vpcs[0]["VpcId"])
    print(res)
