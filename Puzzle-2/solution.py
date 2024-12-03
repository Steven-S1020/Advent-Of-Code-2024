from itertools import pairwise, starmap
from operator import sub

def main() -> None:
    totalSafe = 0
    extraSafe = 0

    with open('input.in', 'r', encoding='utf8') as f:
        for line in f:
            levels = list(map(int, line.split()))

            if ((levels == sorted(levels, reverse=True)) or (levels == sorted(levels))) and not any(map(lambda x: (abs(x) > 3) or (x == 0), list(starmap(sub, pairwise(levels))))):
                totalSafe += 1

            else:
                for i in range(len(levels)):
                    newLevels = levels[:i] + levels[i + 1:]
                    if ((newLevels == sorted(newLevels, reverse=True)) or (newLevels == sorted(newLevels))) and not any(map(lambda x: (abs(x) > 3) or (x == 0), list(starmap(sub, pairwise(newLevels))))):
                        extraSafe += 1
                        break

            print(list(levels))

        print(f'Part One: {totalSafe} reports are safe')
        print(f'Part Two: {totalSafe + extraSafe} reports are safe')


if __name__ == '__main__':
    main()
