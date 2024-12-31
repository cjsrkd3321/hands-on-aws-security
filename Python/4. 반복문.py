# while, for

while True:
    print(1)
    value = int(input("1을 입력하면 종료됩니다: "))
    if value == 1:
        break

# count = 10
# while count >= 5:
#     print(count, end=" ")
#     count -= 1

# for i in "string":
#     print(i)

# for i in [1, 2, 3, 4]:
#     print(i)

# for i in range(100):
#     print(i, end=" ")

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}")

# for i in range(1, 10):
#     if i != 2:  # 2단만 출력
#         continue
#     for j in range(1, 10):
#         if j > 2:  # 2까지 곱한 결과만 출력
#             break
#         print(f"{i} * {j} = {i * j}")
