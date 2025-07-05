# PART I
# ----1
list1 = []
a = 0

while not a == 20101226:
    a = int(input("Enter the number you want to add to the list(enter 20101226 to end) > "))
    list1.append(a)

print(f"Sum of numbers in the list: {sum(list1)};")
print(f"Average number in the list: {sum(list1)//len(list1)}")

# ----2
list1 = []
a = 0

while not a == 20101226:
    a = int(input("Enter the number you want to add to the list(enter 20101226 to end) > "))
    list1.append(a)

n = int(input("Enter the number you want to count > "))
print(f"{n} appears in list {list1.count(n)} times.")

# ----3
l = list(map(int, input("Enter the numbers SEPARATELY > ").split()))
s = 0

for i in l:
    if i>=0:
        s += i

print(f"Sum of every positive number in this list is {s}.")

# ----4
indexes = []
l = list(map(int, input("Enter the numbers SEPARATELY > ").split()))

for i in l:
    if i%2 == 0:
        indexes.append(l.index(i))

print(f"Even numbers in list you entered are located at the following indexes: {', '.join(map(str, indexes))}")

# ----5
import re

digits = 0
znakoklykus = 0
sprtrs = 0

text = input("Enter the text > ")
sentences = re.split(r"[.?!]+", text)
for i in sentences:
    sentences[sentences.index(i)] = i.strip().capitalize()
print('. '.join(sentences))
for c in text:
    if c.isdigit():
        digits += 1
    elif c == "!":
        znakoklykus += 1
        sprtrs += 1
    elif c == "." or c == "," or c == "?" or c == ";":
        sprtrs +=1

print(f"There are {digits} numbers in the text.")
print(f"There are {sprtrs} separators in the text.")
print(f"There are {znakoklykus} \"!\"s in the text.")

# ----6
list1 = []
res = []
a = 0

while not a == 20101226:
    a = int(input("Enter the number you want to add to the list(enter 20101226 to end) > "))
    list1.append(a)

for i in list1:
    if i not in res and i != 20101226:
        res.append(i)

print(" ".join(map(str, res)))
