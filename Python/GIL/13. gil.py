from concurrent.futures import ThreadPoolExecutor, wait

import sys
import time


MAX_WORKERS = 10
LOAD_BALANCE = 10
TOTAL_COUNTS = 10_000_000

# GIL 확인 시간을 변경하면?
# sys.setswitchinterval(0.005)


def count(n):
    while n > 0:
        n -= 1


# SINGLE THREAD
start_time = time.time()

count(TOTAL_COUNTS)

print(f"SINGLE THREAD ELAPSED TIME: {time.time() - start_time:.5f}s")

# MULTI THREADS
start_time = time.time()

threads = []
pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)
for _ in range(MAX_WORKERS):
    threads.append(pool.submit(count, TOTAL_COUNTS))
wait(threads)

print(f"MULTI THREADS ELAPSED TIME: {time.time() - start_time:.5f}s")

# MULTI THREADS by LOAD_BALANCE
start_time = time.time()

threads = []
pool = ThreadPoolExecutor(max_workers=MAX_WORKERS * LOAD_BALANCE)
for _ in range(MAX_WORKERS * LOAD_BALANCE):
    threads.append(pool.submit(count, TOTAL_COUNTS / LOAD_BALANCE))
wait(threads)

print(f"MULTI THREADS by LOAD_BALANCE ELAPSED TIME: {time.time() - start_time:.5f}s")
