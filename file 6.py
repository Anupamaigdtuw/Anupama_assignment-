#12. write a program  that calculate the sum of the digits of a given number.

number = int(input("Enter a number : "))
sum_digit = 0
for digit in number:
    sum_digit += int(digit)
    return sum_digits
print("The sum of the digits of is:" sum_digit)