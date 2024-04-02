def solve_eight_queens(n):
  """
  Solves the 8-Queens problem using backtracking.

  Args:
      n: Size of the chessboard (8x8 in this case).

  """
  def safe(row, col):
    # Check if a queen can be placed at (row, col) without conflicts
    for i in range(col):
      if board[row][i] == 1 or abs(row - queens[i]) == abs(col - i):
        return False
    return True

  board = [[0 for _ in range(n)] for _ in range(n)]  # Chessboard representation
  queens = [-1] * n  # Keeps track of queen positions in each column

  def backtrack(col):
    # Backtracking function to find a solution
    if col >= n:
      return True  # Reached the end of the board, solution found
    for i in range(n):
      if safe(i, col):
        board[i][col] = 1
        queens[col] = i
        if backtrack(col + 1):
          return True
        board[i][col] = 0  # Backtrack if placement doesn't lead to a solution
        queens[col] = -1
    return False

  if backtrack(0):
    return queens  # Return solution if found
  else:
    return None  # No solution exists

# Example usage
solution = solve_eight_queens(8)
if solution:
  print("Solution:", solution)
else:
  print("No solution exists for the 8-Queens problem.")