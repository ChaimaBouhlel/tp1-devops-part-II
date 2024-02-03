def calculate_product(arr):
    result = 1
    for num in arr:
        print("Multiplying", result, "by", num)
        result *= num
    return result

def main():
    # Read input array from the user
    try:
        input_str = input("Enter the array elements separated by spaces: ")
        input_arr = list(map(int, input_str.split()))
        print("Input array:", input_arr)
        # Check if the array is not empty
        if len(input_arr) == 0:
            print("Error: Please enter at least one element in the array.")
            print("Error: Please enter at least one element in the array.")
        else:
            # Calculate and print the product of array elements
            product = calculate_product(input_arr)
            print("Product of array elements:", product)
    except ValueError:
        print("Error: Please enter valid integers in the array.")

if __name__ == "__main__":
    main()
