from concurrent.futures import ThreadPoolExecutor, wait

import time
import hashlib


MAX_WORKERS = 10
MESSAGE = b"rex" * (2**29)  # 1.5GB


def compute(message):
    hashlib.sha256(message).digest()


# SINGLE THREAD
start_time = time.time()

compute(MESSAGE)

print(f"SINGLE THREAD ELAPSED TIME: {time.time() - start_time:.5f}s")

# MULTI THREADS
start_time = time.time()

threads = []
pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)
for _ in range(MAX_WORKERS):
    threads.append(pool.submit(compute, MESSAGE))
wait(threads)

print(f"MULTI THREADS ELAPSED TIME: {time.time() - start_time:.5f}s")
