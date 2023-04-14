
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

def guess_number():
  target_number = 5
  while True:
    try:
      user_guess = int(input("Enter a guess between 1 and 9: "))
      if user_guess == target_number:
        print("Well guessed!")
        break
    except ValueError:
      print("Invalid input. Enter a number between 1 and 9.")

guess_number()
