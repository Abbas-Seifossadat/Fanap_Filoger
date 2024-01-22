import numpy as np
from utils import random_number

def create_random_array(length):
    random_array = np.array([random_number.generate_random_number() for _ in range(length)])
    return random_array
