def check_winner(board, player):
    if any(all(board[i][j] == player for j in range(3)) for i in range(3)):
        return True
    if any(all(board[i][j] == player for i in range(3)) for j in range(3)):
        return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[2-i][i] == player for i in range(3)):
        return True
    return False
    

if __name__ == "__main__":
    board = list()
    board.append(input().split())
    board.append(input().split())
    board.append(input().split())
    print(check_winner(board, input()))