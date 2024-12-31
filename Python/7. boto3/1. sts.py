import boto3

sts = boto3.client("sts")

res = sts.get_caller_identity()
print(res["Account"], res["Arn"], res["UserId"])

if res["Arn"].endswith("root"):
    print("[X] ROOT 사용 중")
else:
    print(f"[O] ROOT가 아닙니다. 현재: {res['Arn']}")
