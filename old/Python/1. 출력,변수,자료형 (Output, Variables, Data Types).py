# 출력 (output)
print("HELLO WORLD!")

# 변수 (variables)
variable = "test"

# 기본 자료형 (default data type)
# 숫자(number)
a = 1
a = a + 1
a += 1

# 문자열(string)
b = "string"
b += "asdf"
b.find("str")
b.startswith("str")
b.endswith("ing")
b[0]

# 불리안(boolean)
c = True
c = False

# 리스트(list)
d = []
d += [2]
d.append(1)
d.clear()
d.count(1)
d.extend([1])
d[0]
d[1:]
d[-1]
d = [1, 2, 3, 4]
d[::2]

# 사전(dictionary)
e: dict = {}
# e += {1:2}
e[1] = 2
e.items()
e.keys()
e.values()
e["asdf"]
e.get("asdf", None)
e.pop("asdf", "asdf")

# 튜플(tuple)
f = ()
# f2 = (1)
f3 = (1,)
f3[0]

# None
None

# 출력 포맷팅 (formatting)
print("asdf")
print("%s" % "asdf")
print("{}".format("asdf"))
test = "asdf"
print(f"{test}")

# 타입 변환 (type conversion)
type(None)
type(1)
int(1)
int("asdf")
str(123)
tuple([])
list(())
list({1: 2, 3: 4})

# 튜플은 추가가 안된다고 하지 않았나요? (Didn't you say you can't add tuples?)
l: list = []
id(l)
l.append(1)
id(l)
l += [2]
id(l)

t: tuple = ()
id(t)
t += (1,)
id(t)
