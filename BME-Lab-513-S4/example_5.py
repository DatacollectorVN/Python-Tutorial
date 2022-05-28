import sys
sys.path.append("../")
from maths import square, sum
def main():
    x = 2
    x_square = square(x)
    print(f'x_square = {x_square}')
    y = 4
    sum_ = sum(x, y)
    print(f'sum_ = {sum_}')
if __name__ == '__main__':
     main()