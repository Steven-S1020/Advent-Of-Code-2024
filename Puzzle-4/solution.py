def main() -> None:
    grid = []
    word = 'XMAS'
    directions = [[0,1], [1,1], [1, 0], [1,-1], [0, -1], [-1,-1], [-1,0], [-1,1]]
    total_words = 0
    x_words = 0

    with open('input.in', 'r', encoding='utf8') as f:
        for line in f:
            grid.append(list(line.strip()))

    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            for i in range(len(directions)):
                d_row = directions[i][0]
                d_col = directions[i][1]

                found = True
                for j in range(len(word)):
                    new_row = row + j * d_row
                    new_col = col + j * d_col
                    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                        found = False
                        break

                    if grid[new_row][new_col] != word[j]:
                        found = False
                        break
                if found:
                    total_words += 1

            if row + 2 < rows and col + 2 < cols:
                if (grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]) == 'MAS' or (grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]) == 'SAM':
                    if (grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2]) == 'MAS' or (grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2]) == 'SAM':
                        x_words += 1

    print(f'Part One: {total_words}')
    print(f'Part Two: {x_words}')

if __name__ == '__main__':
    main()
