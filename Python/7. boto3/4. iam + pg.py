import boto3

iam = boto3.client("iam")

### PAGINATOR 적용 ###
# roles = iam.list_roles()["Roles"]
iterator = iam.get_paginator("list_roles").paginate()
for roles in iterator:
    for role in roles["Roles"]:
        if role["Path"].startswith(
            (
                "/aws-reserved/",
                "/service-role/",
                "/aws-service-role/",
            )
        ):
            continue

        role_name = role["RoleName"]

        try:
            res = iam.get_role(RoleName=role_name)["Role"]
            if not res["RoleLastUsed"]:
                print(res["Arn"])
        except iam.exceptions.NoSuchEntityException:
            print(f"[X] {role_name}이 존재하지 않습니다.")
