import argparse
from game import NumpyGame

def generate_and_check(length):
    analyzer = NumpyGame()
    random_result = analyzer.create_random_array(length)
    result_message = analyzer.win_or_fail(random_result)
    print(result_message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Numpy Game Analyzer App')
    parser.add_argument('length', type=int, help='Length of the random array')
    args = parser.parse_args()

    generate_and_check(args.length)