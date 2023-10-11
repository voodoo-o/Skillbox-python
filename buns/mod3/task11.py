k = 3
board = [input().strip() for _ in range(k)]
winner = 'Ничья'

for i in range(k):
    if all(board[i][j] == 'X' for j in range(k)) or all(board[j][i] == 'X' for j in range(k)):
        winner = 'X'
        break
    elif all(board[i][j] == 'O' for j in range(k)) or all(board[j][i] == 'O' for j in range(k)):
        winner = 'O'
        break
    elif all(board[i][i] == 'X' for i in range(k)) or all(board[i][k - i - 1] == 'X' for i in range(k)):
        winner = 'X'
        break
    elif all(board[i][i] == 'O' for i in range(k)) or all(board[i][k - i - 1] == 'O' for i in range(k)):
        winner = 'O'
        break
    
print(winner)
