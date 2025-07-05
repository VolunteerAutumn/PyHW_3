# PART I
# ----1
even = 0
odd = 0
list_ = list(map(int, input("Enter the elements of your list SEPARATELY > ").split()))

for i in list_:
	if i % 2 == 0:
		even += 1
	else:
		odd += 1

print(f"There are {even} even numbers and {odd} odd numbers.")

# ----2
list_ = list(map(int, input("Enter the elements of your list SEPARATELY > ").split()))

print(f"The biggest one is {max(list_)} and the smallest one is {min(list_)}.")

# ----3

