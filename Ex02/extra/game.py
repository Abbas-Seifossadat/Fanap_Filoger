import numpy as np

class NumpyGame:
    """
    It is an ObjectOrientedProgramming.

    This class contains functions to analyze the numpy game according to exercise 2.

    Attributes:
        None
    ------------------------------------------
    """

    def __init__(self):
        pass

    def generate_random_number(self):
        """
        In generate_random_number Function Generates a random number between 0 and 100.

        Args:
            None

        Returns:
            int: A random integger number between 0 and 100.
        ------------------------------------------
        """
        return np.random.randint(0, 101)

    def create_random_array(self, length):
        """
        In create_random_array Function Creates an array of random numbers.

        Args:
            length (int): The length of the random array.

        Returns:
            numpy.ndarray: An array of random numbers.
        ---------------------------------------------
        """
        random_array = np.array([self.generate_random_number() for _ in range(length)])
        return random_array

    def win_or_fail(self, array):
        """
        win_or_fail Function determines wins or fails based on the array's maximum value.

        Args:
            array (numpy.ndarray): The input array of random numbers.

        Returns:
            str: A message indicating whether the player has won or failed based on the maximum value in the array.
        """
        max_value = np.max(array)
        if max_value > 70:
            return "Congratulations, you win! The maximum value is: " + str(max_value)
        else:
            return "Sorry, you lose. The maximum value is: " + str(max_value)


# Create an instance of the class
analyzer = NumpyGame()
print(NumpyGame.__doc__)
print(NumpyGame.generate_random_number.__doc__)
print(NumpyGame.create_random_array.__doc__)
print(NumpyGame.win_or_fail.__doc__)

# example
"""
try:
    length = int(input("Please Enter a Number: "))
    random_result = analyzer.create_random_array(length)
    print("Random array: ", random_result)
    result_message = analyzer.win_or_fail(random_result)
    print(result_message)
except ValueError:
    print('Error!\n', 'Please enter a valid integer!')
"""
