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