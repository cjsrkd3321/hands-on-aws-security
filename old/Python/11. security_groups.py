import boto3
import botocore


def create_ingress_rule(ec2, sg_id, protocol, from_port, to_port, cidr_ip):
    return ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        CidrIp=cidr_ip,
        FromPort=from_port,
        ToPort=to_port,
        IpProtocol=protocol,
    )["SecurityGroupRules"][0]["SecurityGroupRuleId"]


def delete_ingress_rule(ec2, sg_id, sgr_id):
    return ec2.revoke_security_group_ingress(
        GroupId=sg_id, SecurityGroupRuleIds=[sgr_id]
    )["Return"]


def delete_security_group(ec2, sg_id):
    try:
        ec2.delete_security_group(GroupId=sg_id)["_return"]
        return True
    except botocore.exceptions.ClientError as e:
        code = e.response["Error"]["Code"]
        if code == "DependencyViolation":
            return False


if __name__ == "__main__":
    ec2 = boto3.client("ec2")
    iterator = ec2.get_paginator("describe_security_groups").paginate()
    sgs = [sg for sgs in iterator for sg in sgs["SecurityGroups"]]
    for sg in sgs:
        sg_id = sg["GroupId"]
        print(sg_id, sg["GroupName"])
        sgr_id = create_ingress_rule(ec2, sg_id, "tcp", 80, 80, "1.1.1.1/32")
        print(delete_ingress_rule(ec2, sg_id, sgr_id))
        print(delete_security_group(ec2, sg_id))
