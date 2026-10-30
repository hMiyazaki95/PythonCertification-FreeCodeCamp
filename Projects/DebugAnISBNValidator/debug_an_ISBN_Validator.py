# Debug an ISBN Validator
# The ISBN (International Standard Book Number) is a unique identifier assigned to commercial books. It is either 10 or 13 characters long. The last character is a check digit, which is calculated from the digits before it, known as the main digits.

# Camperbot has tried to build their own ISBN validator. However, they have made a few mistakes along the way.

# In this lab, you will fix the existing code and make it function properly.

# Expected behavior: When the user runs the program, it will show the prompt Enter ISBN and length: . The user can enter the ISBN code they want to validate in ISBN,length format. Enter the ISBN without hyphens, followed by a comma and its length (10 or 13).

# Example inputs: 1530051126,10 for ISBN-10 codes. 9781530051120,13 for ISBN-13 codes.

# How to find the check digit:

# The main digits are the first 9 digits of an ISBN-10 code, or the first 12 digits of an ISBN-13 code. They must all be numbers.
# The last character is the given check digit. The expected check digit is calculated from the main digits, and the ISBN code is valid only if the two match.
# For example, in the ISBN-10 code 1530051126, the main digits are 153005112 and the given check digit is 6. In the ISBN-13 code 9781530051120, the main digits are 978153005112 and the given check digit is 0.
# You don't have to know the detailed calculation logic in this lab. The functions calculate_check_digit_10 and calculate_check_digit_13 will take care of the calculation and return the expected check digit as a string.
# The check digit for ISBN-10 codes can be a number from 0 to 9 or an uppercase letter X.
# The check digit for ISBN-13 codes can be a number from 0 to 9.
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should fix the IndentationError in the current code.
# Even if the user does not enter comma-separated values, the program should handle the IndexError without crashing.
# When the user does not enter comma-separated values, they should see the message Enter comma-separated values. in the console, and the program should terminate.
# Even if the user enters a non-numeric value for the length, the program should handle the ValueError without crashing.
# When the user enters a non-numeric value for the length, they should see the message Length must be a number. in the console, and the program should terminate.
# You should fix the off-by-one error in the validate_isbn function.
# You should fix the TypeError in the current code that occurs when the user enters a valid ISBN code.
# You should fix the IndexError in the current code when the user enters a valid ISBN code.
# Even if the user enters an incorrect ISBN code with non-numeric characters in the main digits, the program should handle the ValueError that occurs without crashing.
# When the user enters an incorrect ISBN code with non-numeric characters in the main digits, they should see the message Invalid character was found. in the console.
# When the user enters 1530051126,10, they should see the message Valid ISBN Code.
# When the user enters 9781530051120,13, they should see the message Valid ISBN Code.
# Important: you will need to comment out the main() call in the global space for the tests to run properly.

# When you complete the project, the user should see the following messages depending on the values they enter.

# ISBN Code	Length	Message	Example input
# Valid	Valid	Valid ISBN Code.	1530051126,10
# Invalid Number	Valid	Invalid ISBN Code.	1530051125,10
# Does not match specified length or left blank	Valid	ISBN-10 code should be 10 digits long. or ISBN-13 code should be 13 digits long., depending on the length they entered.	9781530051120,10 or 1530051126,13
# Contains non-numeric characters in the main digits	Valid	Invalid character was found.	15-0051126,10
# Any	Invalid Number	Length should be 10 or 13.	1530051126,9
# Any	Contains non-numeric characters or left blank	Length must be a number.	1530051125,A
# Not comma-separated	Not comma-separated	Enter comma-separated values.	1530051125
# You can use the following values to test your code manually if you would like.

# Example inputs for valid ISBN-10 codes: 1530051126,10 9971502100,10 080442957X,10

# Example inputs for valid ISBN-13 codes: 9781530051120,13 9781947172104,13

# Tests:
# Passed:1. You should comment out the call to the main function to allow for the rest of the tests to work properly.
# Passed:2. You should have a validate_isbn function.
# Passed:3. You should have a calculate_check_digit_10 function.
# Passed:4. You should have a calculate_check_digit_13 function.
# Failed:5. You should have a main function.
# Failed:6. When the user inputs values that are not comma-separated, you should see the message Enter comma-separated values. in the console.
# Failed:7. When the user inputs a non-numeric value for the length, you should see the message Length must be a number. in the console.
# Failed:8. When the user enters an incorrect ISBN code with non-numeric characters in the main digits, you should see the message Invalid character was found. in the console.
# Failed:9. When the user enters 1530051126,10, you should see the message Valid ISBN Code. in the console.
# Failed:10. When the user enters 9781530051120,13, you should see the message Valid ISBN Code.
# Failed:11. When the user enters 1530051125,10, you should see the message Invalid ISBN Code.
# Failed:12. When the user enters 9781530051120,10, you should see the message ISBN-10 code should be 10 digits long.
# Failed:13. When the user enters 1530051126,13, you should see the message ISBN-13 code should be 13 digits long.
# Failed:14. When the user enters 15-0051126,10, you should see the message Invalid character was found.
# Failed:15. When the user enters 1530051126,9, you should see the message Length should be 10 or 13.
# Failed:16. When the user enters 1530051125,A, you should see the message Length must be a number.
# Failed:17. When the user enters 1530051125, you should see the message Enter comma-separated values.
# Failed:18. When the user enters 9971502100,10, you should see the message Valid ISBN Code.
# Failed:19. When the user enters 080442957X,10, you should see the message Valid ISBN Code.
# Failed:20. When the user enters 9781947172104,13, you should see the message Valid ISBN Code.





def validate_isbn(isbn, length):
    if len(isbn, length) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    main_digits = isbn[0:length]
    given_check_digit = isbn[length]
    main_digits_list = [int(digit) for digit in main_digits]
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')
def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit
def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit
# def main():
#     user_input = input('Enter ISBN and length: ')
#     values = user_input.split(',')
#     isbn = values[0]
#     length = int(values[1])
#     if length == 10 or length == 13:
#     validate_isbn(isbn, length)
#     else:
#     print('Length should be 10 or 13.')

# main()