1 / 0
int("ASDF")

# try:
#     1 / 0
# except ZeroDivisionError as e:
#     print(f"{e} 예외 발생!")

# try:
#     int("ASDF")
# except ValueError as e:
#     print(f"{e} 예외 발생!")

# try:
#     1 / 0
# except Exception as e:
#     print(e)
# finally:
#     print(
#         "무조건 실행됩니다.",
#         "예외 발생 여부와 상관없이 꼭!!!",
#         "처리해야 하는 코드를 넣어주세요.",
#         sep=" ",
#     )

# # 1. 예외처리 추가해보기
# # 2. 예외처리 후 새로운 예외 발생시키기
# while True:
#     print(1)
#     try:
#         value = int(input("1을 입력하면 종료됩니다: "))
#     except ValueError:
#         raise Exception("문자열을 입력하시면 안돼요!")
#     if value == 1:
#         break
