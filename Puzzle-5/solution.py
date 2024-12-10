from collections import defaultdict
from itertools import takewhile, dropwhile
from functools import cmp_to_key

def main() -> None:

    sum_correct = 0
    sum_incorrect = 0
    rules = defaultdict(list)

    def valid_updates(update):
        already_seen = []

        for num in update:
            if rules.get(num) == 'None':
                already_seen.append(num)

            elif not any(val in rules.get(num) for val in already_seen):
                already_seen.append(num)

            else:
                return False
        return True



    with open('input.in', 'r', encoding='utf8') as f:
        lines = [line.strip() for line in f]

    rules_temp = map(lambda x: x.split('|'), (takewhile(lambda x: x != '', lines)))

    for k, v in rules_temp:
        rules[int(k)].append(int(v))

    updates_temp = dropwhile(lambda x: x != '', lines)
    next(updates_temp)
    updates = list(map(lambda x: list(map(int, x)), map(lambda x: x.split(','), (updates_temp))))

    for update in updates:
        if valid_updates(update):
            sum_correct += update[len(update) // 2]

        else:
            update.sort(key=cmp_to_key(lambda a, b: -1 if a in rules[b] else 1))
            sum_incorrect += update[len(update) // 2]

    print(sum_correct)
    print(sum_incorrect)

if __name__ == '__main__':
    main()
