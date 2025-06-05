# Solving the N Queens problem with Exhaustive search (depth-first).
# Compare the four approaches for solving the N-Queens problem with
# N = 10, N = 30,  N = 50, N = 100, and N = 200 in terms of computational time and efficiency.
import time
from operator import index


# Programmer: Keven Quevedo - Date 4/June/25


def solve_n_queens(n):
    results = [] # stores all valid build sol
    board = [-1] * n  # stores q positions

    # position check safety
    def is_valid(row, col): # checks to see if placement is good
        for prev_row in range(row):
            # this prevents two queens in the same col
            if board[prev_row] == col or \
               abs(board[prev_row] - col) == abs(prev_row - row):# this prevents two queens diagonally
                return False # false if either position isn;t safe
        return True # true is position is safe

    # depth first search
    def dfs(row):
        if row == n: # if row has queen then add to results
            results.append(build_solution(board)) # using append
            return
        for col in range(n):
            if is_valid(row, col): # calls func to check if queen placement is vaild
                board[row] = col # since valid placement, store placement
                dfs(row + 1) # move to next row + 1
                board[row] = -1  # backtrack

    # builds the output
    def build_solution(board):
        solution = [] # stores the final output
        for row in board:
            line = ['.'] * n # how long each line shown be according to n
            line[row] = 'Q' # changes dot to Q
            solution.append(''.join(line)) # combines the line results and appends it into solution variable

        return solution

    dfs(0) # calls the func at row 0 to start process
    return results # output


if __name__ == "__main__":
    n = [4,9] # tests all these n queens problems
    print("Solving N-Queen problem for these {0}".format(n))
    for nums in n:
        print(f"Solving N-Queens for N = {nums}")
        start = time.time()
        solutions = solve_n_queens(nums)
        end = time.time()
        print(f"Total solutions found: {len(solutions)} \nonly showing 2 solutions:")
        print(f"Time taken: {end - start:.2f} seconds")
        #if len(solutions) <= 20:  # Only print board layouts if solution set is small
        for index, solution in enumerate(solutions[:2]):
            print(f"\nSolution #{index + 1}:")
            for row in solution:
                print(row)
        print("\n" + "-" * 60 + "\n")
