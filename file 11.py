
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