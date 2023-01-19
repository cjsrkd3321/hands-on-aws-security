import boto3
import botocore


class SecurityGroup:
    def __init__(self, ec2, sg):
        self.ec2 = ec2
        self.__sg_id = sg["GroupId"]
        self.__sg_name = sg["GroupName"]

    def create_ingress_rule(self, protocol, from_port, to_port, cidr_ip):
        return self.ec2.authorize_security_group_ingress(
            GroupId=self.__sg_id,
            CidrIp=cidr_ip,
            FromPort=from_port,
            ToPort=to_port,
            IpProtocol=protocol,
        )["SecurityGroupRules"][0]["SecurityGroupRuleId"]

    def delete_ingress_rule(self, sgr_id):
        return self.ec2.revoke_security_group_ingress(
            GroupId=self.__sg_id, SecurityGroupRuleIds=[sgr_id]
        )["Return"]

    def delete(self):
        try:
            self.ec2.delete_security_group(GroupId=self.__sg_id)["_return"]
            return True
        except botocore.exceptions.ClientError as e:
            code = e.response["Error"]["Code"]
            if code == "DependencyViolation":
                return False

    @property
    def id(self):
        return self.__sg_id

    @property
    def name(self):
        return self.__sg_name


if __name__ == "__main__":
    ec2 = boto3.client("ec2")
    iterator = ec2.get_paginator("describe_security_groups").paginate()
    sgs = [sg for sgs in iterator for sg in sgs["SecurityGroups"]]
    for _sg in sgs:
        sg = SecurityGroup(ec2, _sg)
        sgr_id = sg.create_ingress_rule("tcp", 80, 80, "1.1.1.1/32")
        sg.delete_ingress_rule(sgr_id)
        print(sg.delete())
        print(sg.id)
        print(sg.name)
