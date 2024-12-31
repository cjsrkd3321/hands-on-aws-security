from concurrent.futures import ThreadPoolExecutor, as_completed

import boto3
import time


def get_role_last_used_date(role_name):
    iam = boto3.client("iam")
    try:
        res = iam.get_role(RoleName=role_name)["Role"]
        return role_name, res["RoleLastUsed"]
    except iam.exceptions.NoSuchEntityException:
        return None, None


if __name__ == "__main__":
    start_time = time.time()

    iam = boto3.client("iam")

    iterator = iam.get_paginator("list_roles").paginate()
    roles = [role for page in iterator for role in page["Roles"]]

    ### No MultiThreads ###
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
        name, last_used_date = get_role_last_used_date(role_name)
        if not last_used_date and name:
            print(name)

    # ### Yes MultiThreads ###
    # threads = []
    # pool = ThreadPoolExecutor()

    # for role in roles:
    #     if role["Path"].startswith(
    #         (
    #             "/aws-reserved/",
    #             "/service-role/",
    #             "/aws-service-role/",
    #         )
    #     ):
    #         continue
    #     threads.append(pool.submit(get_role_last_used_date, role["RoleName"]))

    # for future in as_completed(threads):
    #     name, last_used_date = future.result()
    #     if not last_used_date and name:
    #         print(name)

    print(f"ELAPSED TIME: {time.time() - start_time:.3f}s")
