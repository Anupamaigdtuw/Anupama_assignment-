
#2. Write a programme to check whether the number is odd or even.

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

odd_val = list(filter(lambda num:(num%2!=0),list1))
print("the odd values from the list:",odd_val)

even_val = list(filter(lambda num:(num%2 == 0),list1))
print("the even values from the list:",even_val)