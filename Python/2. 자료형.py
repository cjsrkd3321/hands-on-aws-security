### 불리안(boolean, 참과 거짓) ###
boolean = True
print(boolean)
boolean = False
print(boolean)

### 문자열(string) ###
string = "test"
print(type(string))
string += " good"
print(string)
print(string.find("test"))
print(string.startswith("t"))
print(string.endswith("1"))
print(string[0])

### 숫자(number) ###
number = 1
print(type(number), number)
number += 10  # number = number + 10 같은 의미
print(number)

### 리스트(list) ###
contents = ["apple", "banana", "carrot"]
print(type(contents), contents)
contents += ["donut"]
print(contents)
contents.append("egg")
print(contents)
print(contents.count("egg"))
print(
    contents[0],  # 첫번째 값
    contents[0:2],  # 첫번째 ~ 두번째 값
    contents[:-1],  # 마지막 이전까지 값
    contents[::2],  # 첫번째부터 2칸 간격 값
)
contents.clear()
print(contents)

### 사전(dictionary, 딕셔너리) ###
dictionary = {}
print(type(dictionary), dictionary)
dictionary["key"] = "value"
print(dictionary)
dictionary[1] = 2
print(dictionary)
print(
    dictionary.items(),
    dictionary.keys(),
    dictionary.values(),
)
# print(dictionary["no"])
print(dictionary.get("no", "yes"), dictionary)
print(dictionary.pop(1, "yes"))
print(dictionary)

### 튜플(tuple) ###
t = ()
print(type(t), t)
t = (1,)
print(type(t), t)
print(t[0])
t += (2, 3)  # 추가 되는 것 처럼 보이지만, 실제로는 새롭게 만들어지는 것임
print(t)

### None ###
print(type(None), None)

### 타입 변환 ###
print(int("1"))
# print(int("d"))
print(str(12512512512))
print(type(tuple([])))
print(type(list(())))
print(list({1: 2}))  # 키만 추출
