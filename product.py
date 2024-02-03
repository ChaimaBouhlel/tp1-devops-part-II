def calculate_product(arr):
    result = 1
    for num in arr:
        result *= num
    return result

def main():
        input_str = input("Enter the array elements separated by spaces: ")
        input_arr = list(map(int, input_str.split()))
        
        # Check if the array is not empty
        if len(input_arr) == 0:
            print("Error: Please enter at least one element in the array.")
        else:
            # Calculate and print the product of array elements
            product = calculate_product(input_arr)
            print("Product of array elements:", product)

if __name__ == "__main__":
    main()
