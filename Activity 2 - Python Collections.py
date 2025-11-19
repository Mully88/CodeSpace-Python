# Python program to calculate the average value of list elements

# Define the sample list with both positive and negative numbers
numbers = [20, 30, 25, 35, -16, 60, -100]

# Calculate the sum of all elements in the list
total = sum(numbers)

# Find the number of elements in the list using len()
count = len(numbers)

# Calculate the average by dividing the total sum by the count
average = total / count

# Print the result formatted to one decimal place using format specifier {:.1f}
print("Average value of the list elements is :", "{:.1f}".format(average))
