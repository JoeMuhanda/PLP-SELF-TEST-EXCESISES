# Part 1
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for num in num_list:
  print(num)

# Part 2
for num in num_list:
  if num > 45:
    print(num)

# Part 3
for num in num_list:
  if num > 45:
    print("Over 45")
  else:
    print("Under 45")

# Part 4
for i, num in enumerate(num_list):
  if num == 36:
    print("Number found at position: ", i)

# Part 5
count = 0
for num in num_list:
  if num == 36:
    print("Number found at position: ", i)
    count += 1

# Part 6
print(count)

# Part 7
count = 0
for num in num_list:
  if num == 36:
    print("Number found at position: ", i)
    count += 1
    break

# Part 8
print(count)


# Part II
# Program to guess a number between 1 to 9

