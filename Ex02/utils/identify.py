import numpy as np

def win_or_fail(array):
    max_value = np.max(array)
    if max_value > 70:
        return "Congratulations, you win! The maximum value is: " + str(max_value)
    else:
        return "Sorry, you lose. The maximum value is: " + str(max_value)
