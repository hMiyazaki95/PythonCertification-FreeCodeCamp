# Create a variable named base_price to store the base price of the movie ticket and set its value to 15. Create another variable named age to store the user's age and set its value to 21.
base_price = 15
age = 21

# Create a variable named seat_type to store the type of seat the user has selected and set its value to the string Gold. Create another variable named show_time to store the show time of the movie and set its value to the string Evening.
# Remember to surround both values with either single or double quotes.
seat_type = 'Gold'
show_time = "Evening"

# In this step, you will check if the user is eligible to book a movie ticket based on their age.
# Create an if statement to check if age is greater than 17. Inside the body of the if statement, print User is eligible to book a ticket. This will print the message only when the user's age is greater than 17.
# Remember to indent the body of the if statement and surround the message with single or double quotes inside the print() call.
if age > 17:
    print("User is eligible to book a ticket")
# Create an if statement to check if age is greater than or equal to 21. Inside the body of the if statement, print User is eligible for Evening shows.
if age >= 21:
    print('User is eligible for Evening shows')
# Now, add an else clause to your if statement and print User is not eligible for Evening shows inside the else body. This will print only when the condition in the if statement is false.
else: print('User is not eligible for Evening shows')

# Create a variable named is_member to indicate whether the user is a member and set its value to True.
# Below the is_member variable create another variable named is_weekend to indicate whether the movie show is on a weekend and sets its value to False. Do not surround the value with quotes.
# is_member = True
is_member = False
is_weekend = False

# The user qualifies for a membership discount if they are a member.
# Create a variable named discount and set its value to 0. This will store the discount the user gets on the movie ticket.
discount = 0
# Create an if statement to check if is_member is truthy. Inside the body of the if statement, update the discount value to 3 and print User qualifies for membership discount to the terminal.
# if is_member:
#     discount = 3
#     print('User qualifies for membership discount')
# You should also handle the case when the user does not qualify for a membership discount.

# Add an else clause to your if statement and print User does not qualify for membership discount inside the else body.
# else: 
#     print('User does not qualify for membership discount')
# You also want to display the updated value of discount. Below the if...else statement, use the print() call to display a message that shows Discount: followed by the updated value of discount. Then, check the output in the terminal.
# print('Discount:', discount)

# The membership discount should only apply to members if their age is greater than or equal to 21.
# Use the and operator to combine the existing condition of your if statement with another condition checking if age is greater than or equal to 21.
# Use the and operator to combine the existing condition of your if statement with another condition checking if age is greater than or equal to 21.
if is_member and age >= 21 :
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Now change the value of the is_member variable to False as the user is not a member.
# After that, you will see that the discount value now remains 0, because both conditions must be satisfied for the discount to apply.

# Now create a variable named extra_charges and set it to 0. This will represent extra charges to apply to the movie ticket on weekends.
extra_charges = 0

# Then, create an if statement to check if is_weekend is truthy. Inside the body of if statement, update the extra_charges value to 2 and print Extra charges will be applied in the terminal.
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')

# Now, add an else clause to your if statement and print No extra charges will be applied inside the else body. This will print the message only when the extra charges condition is false.
# Then, below the else clause, use the print() call to display a message that shows Extra charges: followed by the updated value of extra_charges and check the output in the terminal.
else: print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# Extra charges should also apply if the show is in the evening. 
# Use the or operator to combine the existing condition of your 
# if statement with a second condition checking if show_time is equal to the string Evening.


# Now you will check if the user satisfies the conditions to book a movie ticket. Users with age 21 or above can always book tickets without any restrictions.
# Create an if statement to check if age is greater than or equal to 21. Inside the body of the if statement, print Ticket booking condition satisfied to the terminal.
# Then, add an else clause to your if statement and print Ticket booking failed due to restrictions inside the else body.


# Users between 18 and 21 can book tickets, but only when the show_time is not Evening.
final_price = 0
# Use the and operator to build an expression checking if age is greater than or equal to 18 and show_time is not Evening. Use the or operator to combine it with the existing condition of the last if statement. Do not create new variables.
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)
    final_price = base_price + extra_charges + service_charges - discount
    print('Final price of ticket:', final_price)
    
else:
    print('Ticket booking failed due to restrictions')
# There is one more exception to the booking rules. Users between 18 and 21 can book evening shows if they are members.
# When multiple logical operators are used in an if statement, conditions joined with and are evaluated before conditions joined with or. Parentheses () are used in Python to group conditions and control the order in which they are evaluated.
# Now, add another condition to your existing if statement using the or operator to check if is_member is truthy. Use the parentheses () to group the show_time != 'Evening' and is_member conditions together as shown in the above example.

# Nested if
# Now you will calculate service charges based on the type of seat the user has selected.
# Still inside your last if statement body, create a variable named service_charges and set it to 0.
# Then, create a nested if statement to check if seat_type is equal to Premium. Inside the body of the if statement, update the service_charges value to 5.

#elif
# if condition1:
#    # Code to execute if condition1 is True
# elif condition2:
#    # Code to execute if condition1 is False and condition2 is True
# else:
#    # Code to execute if all conditions are False

# Add an elif statement to your if...else statement and check if seat_type is equal to Gold. Inside the body of the elif statement, update the value of service_charges to 3.

# Below the if...elif..else statement, use the print() call to display a message that shows Service charges: followed by the updated value of service_charges. Then, check the output in the terminal.



# In this final step, you will calculate the final price of the movie ticket using the values calculated in the previous steps.

# The final ticket price is calculated by adding the extra charges and service charges to the base price, and then subtracting the discount.

# At the bottom of your last if statement body, calculate the final price of the ticket and store it in a variable named final_price.

# Finally, print a message that shows Final price of ticket: followed by the value of final_price.

