def find_next_empty(puzzle):
    # find the next row and column on the puzzle that is not filled
    # rep with -1
    # using 0-8 for indices

    for(r) in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c

    return None, None       #if there are no empty places in the puzzle


def is_valid(puzzle, guess, row, col):
    # figures if guess is valid

    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals= []
    # col_vals= [puzzle[i][col] for i in range(9(]
    for i in range(9):
        col_vals.append(puzzle[i][col])
        if guess in col_vals:
            return False

    # then square
    # find where 3x3 square starts
    # iterate over the 3 values in the row/colum

    row_start= (row // 3) * 3
    col_start= (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # meaning checks passed
    return True



def solve_sudoku(puzzle):

    # puzzle is a list of lists
    # each inner list is a row in sudoku puzzle
    # return whether a solution exists
    # mutate puzzle to be the solution (if it exists)

    # step 1: choose somewhere on the puzzle to make a guess

    row,col = find_next_empty(puzzle)

    if row is None:
        return True

    # step 2: if there is a place tu put a number, then we make a guess

    for guess in range(1,10):
        #step 3: checking if it's a valid guess
        if is_valid(puzzle, row, col):
            # step 4: place the guess on the puzzče
            puzzle[row][col] = guess
            # step 5: recursively to call the puzzle
            if solve_sudoku(puzzle):
                return True
    # step 6: if not valid OR if the guess doesn't solve the puzzle
    # backtrack and trying a new number
    puzzle[row][col] = -1       # reset the guess

    # step 7: if none of the numbers work, then the puzzle is unsolvable
    return False


if __name__ == '__main__':
    example_board = [
        [5, 3, 0,   0, 7, 0,    0, 0, 0],
        [6, 0, 0,   1, 9, 5,    0, 0, 0],
        [0, 9, 8,   0, 0, 0,    0, 6, 0],
        [8, 0, 0,   0, 6, 0,    0, 0, 3],
        [4, 0, 0,   8, 0, 3,    0, 0, 1],
        [7, 0, 0,   0, 2, 0,    0, 0, 6],
        [0, 6, 0,   0, 0, 0,    2, 8, 0],
        [0, 0, 0,   4, 1, 9,    0, 0, 5],
        [0, 0, 0,   0, 8, 0,    0, 7, 9]
    ]

    for i in range(3):
        for j in range(3):
            matrix = [row[j * 3:(j + 1) * 3] for row in example_board[i * 3:(i + 1) * 3]]
            print(matrix)
            print()



