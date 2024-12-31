# cmd(ctrl) + k, cmd(ctrl) + s
# run python 검색
# Run Python File in Terminal -> Keybinding
# 원하는 키 입력

# 반복문 (Repeat)
# while True:
#     print(1)
#     break

# a = 5
# while a >= 5:
#     a -= 1
#     print(a)

# for i in [1, 2, 3, 4, 5, 6]:
#     print(i)

# for i in range(1, 10):
#     for j in range(1, 10):
#         # continue
#         print(f"{i} * {j} = {i * j}")
#     # continue
#     # break

# 제어문(조건문) (Control(Condition))
# test = "asdf"
# b = 2
# c = False
# if not c:
#     print("종료합니다.")

# d = [1]
# if 2 not in d:
#     print(d)

# if test == "asdf" or b == 1:
#     print(test)
# elif test == "zxcv":
#     print("ASDF")
# else:
#     print("ELSE")

# List comprehension
# a = [1, 2, 3, 4]
# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append(i)

# b = [i for i in a if i % 2 == 0]

# print(b)

# Assignment Expression (Walrus expression)
# l = [1, 2, 3, 4, 5, 6]
# c = len(l)
# if c > 5:
#     print("TEST")
# if (c := len(l)) > 5:
#     print(c)

# while True:
#     data = f.read(128)
#     if not data:
#         break
#     print(data)

# while (data := f.read(128)):
#     print(data)
