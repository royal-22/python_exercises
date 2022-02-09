  def isValidSudoku(self, board: List[List[str]]) -> bool:
      N = 9

      # row
      for r in range(N): 
          row = [c for c in board[r] if c!="."]
          if len(row) != len(set(row)) : return False
      #col 

      for c in range(N):
          col = [board[r][c] for r in range(N) if board[r][c] != "."]
          if len(col) != len(set(col)) : return False
      #subbox
      def helper(R, C):
          l = set()
          for r in range(R, R+3):
              for c in range(C, C+3):
                  if board[r][c] == ".": 
                      continue
                  if board[r][c] not in l: 
                      l.add(board[r][c])
                  else: 
                      return False
          return True

      for r in range(0, N, 3):
          for c in range(0, N, 3):
              if not helper(r, c): return False
      return True
