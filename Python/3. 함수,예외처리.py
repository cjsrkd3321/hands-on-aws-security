# 함수
# def 함수명():
#     코드


def print_test():
    print("test1234")


def print_is_two(number):
    if number == 2:
        print(number)


# a = 2
# print_is_two(a)

# b = 3
# print_is_two(b)

# c = 2
# print_is_two(c)


# 예외처리

# 1 / 0
# int("ASDF")

# try:
#     1 / 0
# except ZeroDivisionError as e:
#     print(e)

# try:
#     int("!@#")
# except ValueError as e:
#     print(e)

# try:
#     1 / 0
# except Exception as e:
#     print(e)


# def del_user():
#     try:
#         delete_user(name="rex")
#     except NoSuchUserException as e:
#         return True
#     except Exception as e:
#         return False


def convert_str_to_int(value):
    try:
        int(value)
    except ValueError:
        raise Exception(f"{value} 는 숫자 변환이 불가능합니다.")


print(convert_str_to_int("ASDF"))
