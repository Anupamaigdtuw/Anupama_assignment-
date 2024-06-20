#Assignment
#1.  write a program that takes two numbers as input and prints their sum.
# taking input from the user

'''num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))
sum = num1 + num2

print("The sum of {} and {} is {}".format(num1,num2,sum))
#or 
num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))
sum = num1 + num2

print("The sum of num1 and num2 is :", sum )

#2. Write a programme to check whether the number is odd or even.

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

odd_val = list(filter(lambda num:(num%2!=0),list1))
print("the odd values from the list:",odd_val)

even_val = list(filter(lambda num:(num%2 == 0),list1))
print("the even values from the list:",even_val)

# 3. write a programme for that ask the user for their name and then prints a message

username = input("Enter your user name.....!! ")
print("Good morning:",username )
import math

#4.write a programme that calculates factorial of a given number.

num = int(input("Enter a positive number...."))
factorial_value = int(input(math.factorial(num)))
print("The factorial value:",num)

# 10. Write a programme that converts string into upper case

list_stud= [ "rishika" ,"sakshi","saminaz", "suditi", "manika "]
proc_list_stud = list(map(lambda stud : stud.upper(),list_stud))
print("The processesd list:",proc_list_stud)

#12. write a program  that calculate the sum of the digits of a given number.

number = int(input("Enter a number : "))
sum_digit = 0
for digit in number:
    sum_digit += int(digit)
    return sum_digits
print("The sum of the digits of is:" sum_digit)

#11. write a program that generates first n numbers of fibonacci sequqence



def fibonacci_sequence(n):
    fib_sequence = []

    # Handle the base cases
    if n >= 1:
        fib_sequence.append(0)
    if n >= 2:
        fib_sequence.append(1)

    # Generate Fibonacci sequence
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence


# Example usage:
n = 10  # Replace with any positive integer
sequence = fibonacci_sequence(n)
print(f"The first {n} numbers of the Fibonacci sequence are:")
print(sequence)

# write a program in which the user ask for your birth year and then calculate your age .
import datetime

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age

# Get user input for birth year
birth_year = int(input("Enter your birth year: "))

# Calculate age
age = calculate_age(birth_year)

# Display the age
print(f"You are {age} years old.")

 # 17 write a program that coverts a given string to titl case.
list_stud= [ "rishika" ,"sakshi","saminaz", "suditi", "manika "]
proc_list_stud = list(map(lambda stud : stud.title(),list_stud))
print("The processesd list:",proc_list_stud)

#22. write a program in python that returns  the min and max  values in a list of numbers number

list1 = [1,45,23,7,14,23,78,46,90]
res = max(list1)
print("maximum value is :",res)

res1 = min(list1)
print("minimum value is :",res1)

# 21. write a program that counts the occurrences of a specific element in a list
def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage:
my_list = [1, 2, 3, 4, 2, 2, 3, 1, 2]
element_to_count = 1
occurrences = count_occurrences(my_list, element_to_count)

print(f"The element {element_to_count} appears {occurrences} times in the list.")

 # 20.write a program that takes a list  of numbers and return their sum

my_list = [1,5,7,2,3,6,19,34]
res = sum(my_list)
print(" The sum of the numbers in given list :",res)

#
import csv
data_list = [
    ["University","student name "," year"," department"],
    ["DU"," Khushi","2nd","Maths" ],
    ["DU"," Ojasvani","2nd","Maths"],
    ["BHU"," urvi ","2nd","Maths"]
]
with open('firstfile.csv', 'w', newline='') as file:
     writer = csv.writer(file,delimiter='|')
     writer.writerows(data_list)




