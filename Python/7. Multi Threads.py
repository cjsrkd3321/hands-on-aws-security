from concurrent.futures import ThreadPoolExecutor, as_completed
from botocore.config import Config

import boto3
import time

# client : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html
# resource, session : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html?highlight=multithreading#multithreading-or-multiprocessing-with-resources
def get_role_last_used_date(iam, role_name):
    role = iam.get_role(RoleName=role_name)["Role"]
    return role_name, role["RoleLastUsed"]


if __name__ == "__main__":
    start_time = time.time()

    iam = boto3.client("iam", config=Config(max_pool_connections=1000))
    roles = iam.list_roles()["Roles"]

    # No MultiThreads
    # for role in roles:
    #     r = iam.get_role(RoleName=role["RoleName"])["Role"]
    #     print(r["RoleName"], r["RoleLastUsed"])

    # Yes MultiThreads
    threads = []
    pool = ThreadPoolExecutor(max_workers=len(roles))

    for role in roles:
        threads.append(pool.submit(get_role_last_used_date, iam, role["RoleName"]))

    for future in as_completed(threads):
        name, last_used_date = future.result()
        print(name, last_used_date)

    print(f"ELAPSED TIME: {time.time() - start_time:.3f}s")
