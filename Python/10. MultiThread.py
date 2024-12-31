from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import requests  # pip install requests


# 숫자 더하기
def cpu_task():
    total = 0
    for i in range(20_000_000):
        total += i


def run_cpu_tasks(num_tasks):
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=num_tasks) as executor:
        futures = [executor.submit(cpu_task) for _ in range(num_tasks)]
        as_completed(futures)

    end_time = time.time()
    print(f"[CPU 작업 결과 (총 {num_tasks}개)]")
    print(f"CPU 작업 총 소요 시간: {end_time - start_time:.2f}초")


# 웹 요청
def io_task(url):
    requests.get(url)


def run_io_tasks(num_tasks, urls):
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=num_tasks) as executor:
        futures = [executor.submit(io_task, url) for url in urls]
        as_completed(futures)

    end_time = time.time()
    print(f"[I/O 작업 결과 (총 {num_tasks}개)]")
    print(f"I/O 작업 총 소요 시간: {end_time - start_time:.2f}초")


def main():
    num_tasks = 5  # 1 ~ 5

    run_cpu_tasks(num_tasks)

    urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.python.org",
        "https://www.wikipedia.org",
    ]
    run_io_tasks(num_tasks, urls)


if __name__ == "__main__":
    main()
