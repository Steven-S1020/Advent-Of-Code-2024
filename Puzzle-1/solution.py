def main() -> None:
    list1 = []
    list2 = []

    with open('input.txt', 'r', encoding='utf8') as f:
        for line in f:
            id1, id2 = map(int, line.split())
            list1.append(id1)
            list2.append(id2)

    list1.sort()
    list2.sort()
    sum = 0

    for i in range(len(list1)):
        sum += abs(list1[i] - list2[i])

    print(f'Part One: {sum}\n')

    score = 0

    for id in list1:
        score += id * list2.count(id)

    print(f'Part Two: {score}')

if __name__ == '__main__':
    main()
