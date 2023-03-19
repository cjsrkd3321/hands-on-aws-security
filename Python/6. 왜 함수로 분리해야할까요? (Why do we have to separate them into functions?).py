import psutil


# 현재 메모리 사용량 출력 함수 (Current memory usage output function)
def memory_usage(message: str = "debug"):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2**20  # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.3f} MB")


def test_list():
    list_comp = [i for i in range(0, 1000000)]  # type: ignore
    memory_usage("List Comprehension")


if __name__ == "__main__":
    memory_usage("START")

    # list_comp = [i for i in range(0, 1000000)]  # type: ignore
    # memory_usage("List Comprehension")
    test_list()

    memory_usage("END")
