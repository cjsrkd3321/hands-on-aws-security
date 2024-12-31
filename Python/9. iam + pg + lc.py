import boto3

iam = boto3.client("iam")

### PAGINATOR 적용 ###
# roles = iam.list_roles()["Roles"]
iterator = iam.get_paginator("list_roles").paginate()

### LIST COMPREHENSION 적용 ###
# for page in iterator:
#     for role in page["Roles"]:
roles = [role for page in iterator for role in page["Roles"]]
for role in roles:
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
