import psutil  # pip install psutil
import os
import csv

CSV_NAME = "test.csv"


# 현재 메모리 사용량 출력 함수
def memory_usage(message="debug"):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2**20  # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.3f} MB")


def create_test_csv(name):
    fp = open(name, "w")
    w = csv.writer(fp)
    for _ in range(0, 1_000_000):  # 컴퓨터 사양에 따라 조절해주세요.
        w.writerow([1, 2, 3, 4])


###############################################
# 1. List Comprehension vs Generator Expression
###############################################
# memory_usage("START")

# list_comp = [i for i in range(0, 1_000_000)]
# memory_usage("List Comprehension")

# print(list_comp[-1])  # 인덱싱 가능

# # gen_exp = (i for i in range(0, 1_000_000))
# # memory_usage("Generator Expression")

# # print(gen_exp[-1])  # 인덱싱 불가능

# memory_usage("END")


###############################################
# 2. Read a file
###############################################
# if not os.path.exists(CSV_NAME):
#     create_test_csv(CSV_NAME)

# fp = open(CSV_NAME)
# r = csv.reader(fp)
# list_comp = [i for i in r]
# list_comp = [tuple(i) for i in r]
# memory_usage("List Comprehension(Read a File)")

# gen_exp = (i for i in r)
# for i in gen_exp:
#     print(i)
#     break
# memory_usage("Generator Expression(Read a File)")

memory_usage("END")
