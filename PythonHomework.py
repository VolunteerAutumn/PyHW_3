# PART II (why did you assign the exact same task lmfao)
# ----1
nl = map(int, input("Enter the numbers separated with spaces (\" \") > ").split())
en = 0
on = 0

for i in nl:
	if i % 2 == 0:
		en += 1
	elif i % 2 != 0:
		on += 1

print(f"There are {en} even numbers and {on} odd numbers")

# ----2
nl = list(map(int, input("Enter the numbers separated with spaces (\" \") > ").split()))
print(f"The biggest one is {max(nl)} and the smallest one is {min(nl)}")

# ----3
import random as r
nl = []
min_pos = 100
max_neg = -100
zeros = 0
for i in range(0, r.randint(8, 15)):
	nl.append(r.randint(-100, 100))
print(f"We have a list: {nl}")
for number in nl:
	if number < 0:
		if number > max_neg:
			max_neg = number
	elif number > 0:
		if number < min_pos:
			min_pos = number
	elif number == 0:
		zeros += 1
print(f"In this list, {min_pos} is the smallest positive number, {max_neg} is the largest negative number.")
print(f"The list has {zeros} zeros.")

# ----4
nums = list(map(int, input("Enter all the numbers of the list you want to create > ").split()))
c = int(input("Enter a coefficient > "))
filtered_nums = []
for i in nums:
    if i >= c:
        filtered_nums.append(i)
print(f"The result is: {' '.join(map(str, filtered_nums))}")

# ----5
kkk = input("Enter the equation (ex. 23+12) > ")
print(f"Result of {kkk} is {int(eval(kkk))}")

# ----6
starting_list = list(map(int, input("Enter the numbers of the list (separate with ' ') > ").split()))
filler_list = []
result = []
filler_number_index = 0

for i in starting_list:
	if i >= 0:
		filler_list.append(i)

filler_list.sort()

for num in starting_list:
	if num < 0:
		result.append(num)
	else:
		result.append(filler_list[filler_number_index])
		filler_number_index += 1
print(f"Result: {', '.join(map(str, result))}")

# PART III
# ----1
l = list(map(int, input("Enter da list yuh > ").split()))
count = 0

for i in range(0, len(l)):
	if l[i] > l[i-1]:
		count += 1

print(f"There are {count} elements that are bigger than the previous one.")

# ----2
l = list(map(int, input("Enter da list yuh > ").split()))
resl = []

for i in l:
	if l.count(i) == 1:
		resl.append(i)
		
print(f"filtered list is {resl}.")

# ----3
requested_list = list(map(int, input("Enter da list yuh > ").split()))

max_length = 1
curr_length = 1
start = 0
max_sequence_start = 0

for i in range(1, len(requested_list)):
	if requested_list[i] > requested_list[i - 1]:
		curr_length += 1
	else:
		if curr_length > max_length:
			max_length = curr_length
			max_sequence_start = start
		curr_length = 1
		start = i

if curr_length > max_length:
	max_length = curr_length
	max_sequence_start = start

longest_sequence = requested_list[max_sequence_start:max_sequence_start + max_length]

print(f"length of dat sequence: {max_length}")
print(f"sequence: {longest_sequence}")

# ----4
requested_list = list(map(int, input("Enter da list yuh > ").split()))
shift = int(input("Howd'ya want to shift da list (enter the number you want to shift it by) > "))

for i in range(shift):
	requested_list.insert(0, requested_list[-1])
	requested_list.pop(-1)
	
print(f"Result: {requested_list}")

# ----5
import random as r

length = r.randint(10, 16)

random_list_1 = [r.randint(-100, 100) for _ in range(length)]
random_list_2 = [r.randint(-100, 100) for _ in range(length)]

print(f"""Random lists are:
1. {random_list_1}
2. {random_list_2}""")

res_list1 = random_list_1 + random_list_2
res_list2 = []
res_list3 = []
res_list4 = []

for i in range(len(res_list1)):
    # Add to res_list2 if not already there (no repeats) (I'm adding these to stay focused cuz I WANNA FCKING SLEEP {&#x1FAE0})
    if res_list1[i] not in res_list2:
        res_list2.append(res_list1[i])

    # Check for elements from random_list_1 in random_list_2 (only for i in first list)
    if i < length and random_list_1[i] in random_list_2 and random_list_1[i] not in res_list3:
        res_list3.append(random_list_1[i])

    # Add unique elements (appear exactly once in combined list)
    if res_list1.count(res_list1[i]) == 1 and res_list1[i] not in res_list4:
        res_list4.append(res_list1[i])

res_list5 = [max(res_list1), min(res_list1)]

print(f"Combined lists: {res_list1}")
print(f"Without repeating elements: {res_list2}")
print(f"With the elements that appear in both lists: {res_list3}")
print(f"Unique elements: {res_list4}")
print(f"Biggest and smallest: {res_list5}")

# ----6
REQlist = list(map(int, input("Enter numbers of the list separated by spaces > ").split()))
result = []

while REQlist:
	result.append(min(REQlist))
	REQlist.remove(min(REQlist))
	if not REQlist:
		break
	result.append(max(REQlist))
	REQlist.remove(max(REQlist))

print(f"Result: {result}")
