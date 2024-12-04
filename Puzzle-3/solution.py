from functools import reduce
from operator import mul
import re

def main() -> None:
    expressionP1 = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
    expressionP2 = r'mul\([0-9]{1,3},[0-9]{1,3}\)|don\'t\(\)|do\(\)'


    with open('input.in', 'r', encoding='utf8') as f:
        entireFile = f.read()

    matchesP1 = re.findall(expressionP1, entireFile)
    productsP1 = [x.strip('mul()').split(',') for x in matchesP1]
    totalP1 = sum(reduce(mul, map(int, x)) for x in productsP1)

    # Part Two
    mulFlag = True
    productsP2 = []
    matchesP2 = re.findall(expressionP2, entireFile)
    for match in matchesP2:
        match match:
            case 'don\'t()':
                mulFlag = False
            case 'do()':
                mulFlag = True
            case _:
                if mulFlag:
                    productsP2.append(match.strip('mul()').split(','))

    totalP2 = sum(reduce(mul, map(int, x)) for x in productsP2)

    print(f'Part One: {totalP1}')
    print(f'Part Two: {totalP2}')

if __name__ == '__main__':
    main()
