###################################
# cmd(ctrl) + k, cmd(ctrl) + s
# run python 검색
# Run Python File in Terminal -> Keybinding
# 원하는 키 입력
###################################

test = "test"
if test == test:
    print(test)

is_true = True
if is_true:  # not
    print(is_true)
else:
    print(False)

result = []
if not result:
    print(f"result에 값이 없습니다.")

number = 2
if number >= 2:
    print(number)
else:
    print("2보다 크지 않습니다.")

is_good, number = False, 2
if is_good and number == 2:
    print(is_good, number)
elif not is_good and number == 2:
    print(f"{is_good} and {number}")
else:
    print("?????")

l = [1, 2, 3, 4]
if 1 in l:
    print(f"{l}은 1을 포함하고 있습니다.")
else:
    print("포함하지 않습니다.")

if 10 not in l:
    print(f"{l}은 10을 포함하지 않습니다.")
else:
    print("포함합니다.")

d = {"rex": "jjang"}
if "rex" in d:
    print(f"{d}는 rex라는 키를 포함하고 있습니다.")
