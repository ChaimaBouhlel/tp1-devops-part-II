def calculate_sum_of_array(arr):
        int_arr = [int(x) for x in arr]
        array_sum = sum(int_arr)
        return array_sum

# Get input from the user
input_array = input("Enter the array elements separated by spaces: ").split()

# Calculate and print the sum of the array
result = calculate_sum_of_array(input_array)
if result is not None:
    print("Sum of array elements:", result)
