import numpy as np

def generate_random_array():
    while True:
        try:
            a = int(input("Enter the lower bound: "))
            b = int(input("Enter the upper bound: "))
            l = int(input("Enter the length of the array: "))
            if a >= b:
                print("Upper bound must be greater than lower bound. Please try again.")
                continue
            elif l <= 0:
                print("Length of the array must be a positive integer. Please try again.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    random_array = np.random.randint(a, b, size=l)
    return random_array