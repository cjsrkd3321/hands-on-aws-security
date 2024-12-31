# 1. 역할 목록 반환
# 2. 사용 이력이 없는 역할 식별

import boto3

iam = boto3.client("iam")

roles = iam.list_roles()["Roles"]
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
            print(res["Arn"], res["RoleLastUsed"])
    except iam.exceptions.NoSuchEntityException:
        print(f"[X] {role_name}이 존재하지 않습니다.")
