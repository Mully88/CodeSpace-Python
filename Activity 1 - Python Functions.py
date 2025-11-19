# Python program with two functions:
# 1. show_list() - to display the content of the list
# 2. find_max() - to find the maximum value in the list

# Function to show the content of the list
def show_list(lst):
    # Print the list content
    print("The content of the list is:", lst)

# Function to find the maximum value in the list
def find_max(lst):
    # Use the built-in max() function to get the largest element
    maximum_value = max(lst)
    # Print the maximum value
    print("The max value in the list:", maximum_value)

# Sample list
numbers = [10, 2, 3, 4, 7]

# Call the functions with the sample list
show_list(numbers)
find_max(numbers)
