#Question 1
def hello_name():
    user_name = input("Enter your username: ")
    print(f"Hello {user_name}!")

# Call the function
hello_name()

#Question 2
def first_odds():
    for number in range(1, 101, 2):
        print(number)

# Call the function to print odd numbers from 1 to 100
first_odds()

#Question 3
def max_num_in_list(a_list):
    if not a_list:
        return None  # Return None for empty lists

    max_number = a_list[0]  # Initialize max_number with the first element of the list

    for number in a_list:
        if number > max_number:
            max_number = number

    return max_number

# Example usage:
my_list = [3, 8, 1, 6, 9, 4, 2, 7]
result = max_num_in_list(my_list)
print(f"The maximum number in the list is: {result}")

#Question 4
def is_leap_year(a_year):
    # Leap year conditions
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year_to_check = int(input("What is the year?"))
result = is_leap_year(year_to_check)
print(f"{year_to_check} is a leap year: {result}")

#Question 5
def is_consecutive(a_list):
    if len(a_list) < 2:
        return False  # Lists with less than two elements cannot have consecutive numbers

    sorted_list = sorted(a_list)  # Sort the list

    for i in range(len(sorted_list) - 1):
        if sorted_list[i] + 1 != sorted_list[i + 1]:
            return False

    return True

# Example usage:

# Initialize an empty list
consecutive_list = []

# Get user input for the number of integers
n = int(input("Enter the number of integers: "))

# Use a loop to input individual integers
for i in range(n):
    num = int(input(f"Enter integer {i + 1}: "))
    consecutive_list.append(num)

print("List of integers:", consecutive_list)

result_consecutive = is_consecutive(consecutive_list)

if result_consecutive == True:
    print(f"{consecutive_list} are consecutive: {result_consecutive}")
else:
    print(f"{consecutive_list} are non-consecutive: {result_consecutive}")

