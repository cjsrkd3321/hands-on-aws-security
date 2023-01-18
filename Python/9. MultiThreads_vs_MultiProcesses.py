import os
import csv
import time

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait


CSV_NAME = "test.csv"
CONTENTS: list = []
TOTAL_COUNTS = 1_000_000
MAX_WORKERS = 10


def create_test_csv(name):
    fp = open(name, "w")
    w = csv.writer(fp)
    for _ in range(0, TOTAL_COUNTS):
        w.writerow([1, 2, 3, 4])


def test_multi_threads():
    fp = open(CSV_NAME)
    r = csv.reader(fp)

    contents = (i for i in r)
    for content in contents:
        content == [1, 2, 3, 4]


def test_multi_processes():
    fp = open(CSV_NAME)
    r = csv.reader(fp)

    contents = (i for i in r)
    for content in contents:
        content == [1, 2, 3, 4]


def multi_threads():
    start_time = time.time()

    threads = []
    pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    for _ in range(MAX_WORKERS):
        threads.append(pool.submit(test_multi_threads))
    wait(threads)

    print(f"MULTI THREADS TIME: {time.time() - start_time:.3f}s")


def multi_processes():
    start_time = time.time()

    processes = []
    pool = ProcessPoolExecutor(max_workers=MAX_WORKERS)
    for _ in range(MAX_WORKERS):
        processes.append(pool.submit(test_multi_processes))
    wait(processes)

    print(f"MULTI PROCESSES TIME: {time.time() - start_time:.3f}s")


if __name__ == "__main__":
    if not os.path.exists(CSV_NAME):
        create_test_csv(CSV_NAME)

    multi_threads()

    multi_processes()
