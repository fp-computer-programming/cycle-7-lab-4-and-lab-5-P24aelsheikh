"""
Create a Python file named lab_7-4.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Copy your lab 7-2 code into the file
Add 4 test cases to the end of the file, with comments
Ensure your lab runs accurately
"""
def find_sum(num1, num2):
    # Add the arguments passed to num1 and num2 and store them in a new variable num_sum
    num_sum = num1 + num2
    
    # Return num_sum
    return num_sum

# Test Case 1: 111 + 222
result1 = find_sum(111, 222)
print("Test Case 1: The sum is:", result1)

# Test Case 2: -5 + 5
result2 = find_sum(-5, 5)
print("Test Case 2: The sum is:", result2)

# Test Case 3: 0 + 0
result3 = find_sum(0, 0)
print("Test Case 3: The sum is:", result3)

# Test Case 4: 3.14 + 2.86
result4 = find_sum(3.14, 2.86)
print("Test Case 4: The sum is:", result4)
"""
________________________________________________________________________________

Create a Python file named lab_7-5.py


Copy the code from your labs 6-5 through 6-8
Turn each of the programs into a function
Add 4 test cases to the functions
Ensure your code runs accurately


"""
def find_min_max(input_list):
    unique_numbers = set(input_list)
    if len(unique_numbers) < 2:
        return "error: list does not meet specifications"

    min_value = min(input_list)
    max_value = max(input_list)

    return min_value, max_value

# Test cases for find_min_max
test_case1 = [3, 1, 7, 4, 5, 1, 10]
test_case2 = [8, 2, 6, 4, 7, 9, 11]
test_case3 = [5, 5, 5, 5, 5]
test_case4 = [2, 2, 4, 6, 8, 10]

print("Test Case 1:", find_min_max(test_case1))
print("Test Case 2:", find_min_max(test_case2))
print("Test Case 3:", find_min_max(test_case3))
print("Test Case 4:", find_min_max(test_case4))

def construct_word_list():
    word1 = input("Enter the first unique word: ")
    word2 = input("Enter the second unique word: ")
    word3 = input("Enter the third unique word: ")
    word4 = input("Enter the fourth unique word: ")
    word5 = input("Enter the fifth unique word: ")

    word_list = [word1, word2, word3, word4, word5]

    length_list = [len(word) for word in word_list]

    print("User input words:", word_list)
    print("Length of words at corresponding indices:", length_list)

# Test cases for construct_word_list
construct_word_list()

def double_numeric_values():
    num1 = float(input("Enter the first numeric value: "))
    num2 = float(input("Enter the second numeric value: "))
    num3 = float(input("Enter the third numeric value: "))
    num_list = [num1, num2, num3]
    doubled_list = [int(2 * num) for num in num_list]
    print("User input values:", num_list)
    print("Doubled values as integers:", doubled_list)

# Test cases for double_numeric_values
double_numeric_values()

def check_numbers():
    num1 = int(input("Enter the first numeric value: "))
    num2 = int(input("Enter the second numeric value: "))
    num3 = int(input("Enter the third numeric value: "))

    num_list = [num1, num2, num3]

    is_all_even = all(num % 2 == 0 for num in num_list)
    is_all_odd = all(num % 2 != 0 for num in num_list)

    if is_all_even:
        print("All numbers are even.")
    elif is_all_odd:
        print("All numbers are odd.")
    else:
        print("Numbers are mixed (both even and odd).")

# Test cases for check_numbers
check_numbers()
