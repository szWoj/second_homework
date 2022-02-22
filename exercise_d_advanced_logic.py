# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_int = []
for num in numbers:
    if num % 2 == 0:
        even_int.append(num)
print(even_int)


# 2. Print the difference between the largest and smallest value:
min_val = min(numbers)
max_val = max(numbers)
difference = max_val - min_val
print(f"Difference between the largest and smallest value: {difference}")

# 3. Print True if the list contains a 2 next to a 2 somewhere.
for i in range(0, len(numbers)):
    if numbers[i] == numbers[i-1] and numbers[i] == 2:
        print(True)

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
sum = 0
six_mode = False

for number in numbers:
    if number != 6 and six_mode == False:
        sum = sum + number

    elif number == 6:
        six_mode = True
        continue
    elif number == 7 and six_mode == True:
        six_mode = False
        continue
print(sum)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







