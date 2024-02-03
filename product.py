def calculate_product(arr):
    # Calculate the product of array elements
    result = 1
    for num in arr:
        # Multiply each element with the result
        result *= num
    return result
print("This is product.py")

def main():
        # Get input from the user
        input_str = input("Enter the array elements separated by spaces: ")
        input_arr = list(map(int, input_str.split()))
        
        # Check if the array is not empty
        if len(input_arr) == 0:
            print("Error: Please enter at least one element in the array.")
        else:
            # Calculate and print the product of array elements
            product = calculate_product(input_arr)
            print("Product of array elements:", product)

print("This is product.py")
if __name__ == "__main__":
    main()
