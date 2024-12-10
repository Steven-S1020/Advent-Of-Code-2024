from copy import deepcopy

def main() -> None:

    with open('input.in', 'r', encoding='utf8') as f:
        map = [list(line.strip()) for line in f]

    map_copy = deepcopy(map)
    directions = [[-1,0], [0,1], [1,0], [0,-1]]
    distinct_positions = 1

    def find_guard(map):
        for row_idx, row in enumerate(map):
            for col_idx, char in enumerate(row):
                if char == '^':
                    return row_idx, col_idx
        return -1, -1

    start_guard_row, start_guard_col = find_guard(map)
    guard_row = start_guard_row
    guard_col = start_guard_col


    obstacle_possible = []
    flag = True
    curr_dir = 0
    while flag:
        if map[guard_row][guard_col] == '.':
            distinct_positions += 1
            map[guard_row][guard_col] = 'X'
            obstacle_possible.append([guard_row, guard_col, curr_dir % 4])

        next_row = guard_row + directions[curr_dir % 4][0]
        next_col = guard_col + directions[curr_dir % 4][1]

        if (0 <= next_row < len(map) and 0 <= next_col < len(map[0])):
            if map[next_row][next_col] == '#':
                curr_dir += 1

            guard_row += directions[curr_dir % 4][0]
            guard_col += directions[curr_dir % 4][1]

        else:
            flag = False

    guard_row = start_guard_row
    guard_col = start_guard_col

    number_of_obstacle_spots = 0
    for obstacle_test in obstacle_possible:
        map_with_obstacle = deepcopy(map_copy)
        x, y, _ = obstacle_test
        map_with_obstacle[x][y] = '#'
        visited_spots = []

        flag = True
        curr_dir = 0
        while flag:
            if [guard_row, guard_col, curr_dir % 4] in visited_spots:
                number_of_obstacle_spots += 1
                break

            visited_spots.append([guard_row, guard_col, curr_dir % 4])
            next_row = guard_row + directions[curr_dir % 4][0]
            next_col = guard_col + directions[curr_dir % 4][1]

            if (0 <= next_row < len(map_with_obstacle) and 0 <= next_col < len(map_with_obstacle[0])):
                if map_with_obstacle[next_row][next_col] == '#':
                    curr_dir += 1

                guard_row += directions[curr_dir % 4][0]
                guard_col += directions[curr_dir % 4][1]

            else:
                flag = False

    print(f'Part One: {distinct_positions}')
    print(f'Part Two: {number_of_obstacle_spots}')

if __name__ == '__main__':
    main()
