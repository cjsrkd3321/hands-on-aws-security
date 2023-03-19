import psutil
import os
import csv

CSV_NAME = "test.csv"

# 현재 메모리 사용량 출력 함수 (Current memory usage output function)
def memory_usage(message: str = "debug"):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2**20  # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.3f} MB")


def create_test_csv(name):
    fp = open(name, "w")
    w = csv.writer(fp)
    for _ in range(0, 10000000):
        w.writerow([1, 2, 3, 4])


if not os.path.exists(CSV_NAME):
    create_test_csv(CSV_NAME)


###############################################
# 1. List Comprehension vs Generator Expression
###############################################
memory_usage("START")

# list_comp = [i for i in range(0, 1000000)]  # type: ignore
# memory_usage("List Comprehension")

# print(list_comp[-1])  # 인덱싱 가능 (indexable)

# gen_exp = (i for i in range(0, 1000000))
# memory_usage("Generator Expression")

# print(gen_exp[-1])  # 인덱싱 불가능 (Unable to index)

# memory_usage("END")


###############################################
# 2. Read a file
###############################################
fp = open(CSV_NAME)
r = csv.reader(fp)
# list_comp = [i for i in r]  # type: ignore
# list_comp = [tuple(i) for i in r]  # type: ignore
# memory_usage("List Comprehension(Read a File)")

gen_exp = (i for i in r)  # type: ignore
for i in gen_exp:
    print(i)
    break
memory_usage("Generator Expression(Read a File)")

memory_usage("END")
