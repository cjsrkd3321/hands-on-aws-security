# boto3
# python3 -m pip install boto3
# pip install boto3
# python3 -m pip install boto3-stubs
# pip install boto3-stubs
import boto3

from pprint import pprint

##### boto3 role(get-caller-identity) #####

# client = boto3.client("sts")
# res = client.get_caller_identity()
# print(res["UserId"], res["Arn"], res["UserId"])
# if res["Arn"].endswith("root"):
#     print("루트 계정을 사용중입니다. (You are using the root account.)")


##### boto3 user(사용자 생성/삭제) #####

client = boto3.client("iam")

# username = "rex"
# try:
#     res = client.create_user(UserName=username)
#     pprint(f"{username} 사용자가 생성되었습니다. (User created successfully.)")
# except client.exceptions.EntityAlreadyExistsException:
#     print(f"{username} 사용자가 이미 존재합니다. (User already exists.)")

# try:
#     client.delete_user(UserName=username)
#     print(f"{username} 사용자가 삭제되었습니다. (User has been deleted.)")
# except client.exceptions.NoSuchEntityException:
#     print(f"{username} 사용자가 존재하지 않습니다. (User does not exist.)")


# def del_user(client, username):
#     if not username:
#         raise Exception(f"{username} 잘못된 사용자 이름입니다. (Invalid name.)")
#     try:
#         client.delete_user(UserName=username)
#     except client.exceptions.NoSuchEntityException:
#         print("ASDF")
#         return True, None
#     except Exception as e:
#         return False, e


# print(del_user(client, ""))


##### boto3 role(역할) #####

from datetime import datetime, timezone, timedelta

now = datetime.now(timezone.utc)

client = boto3.client("iam")
roles = client.list_roles()["Roles"]
# iterator = client.get_paginator("list_roles").paginate()
# roles = [role for roles in iterator for role in roles["Roles"]]

for role in roles:
    name = role["RoleName"]
    r = client.get_role(RoleName=name)["Role"]
    last_used_date = r["RoleLastUsed"].get("LastUsedDate")

    if not last_used_date:
        print(name, "400일 내 사용 기록 없음 (No history of use in 400 days.)")
    elif (now - last_used_date) > timedelta(days=90):
        print(
            name, f"90일 내 사용 기록 없음 (No history of use in 90 days.) | {last_used_date}"
        )
    else:
        print(
            name,
            f"90일 내 사용 기록 있음 (Has a history of use within 90 days.) | {last_used_date}",
        )
