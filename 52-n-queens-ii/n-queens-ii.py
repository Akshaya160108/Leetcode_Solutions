def isvalid(row,col,board,n):
    tempr=row
    tempc=col
    #top move
    while tempr>=0:
        if board[tempr][tempc]=='Q':
            return False
        tempr-=1
    tempr=row
    #topright diagonal
    while tempr>=0 and tempc<n and tempc>=0 and tempr<n:
        if board[tempr][tempc]=='Q':
            return False
        tempr-=1
        tempc+=1
    tempr=row
    tempc=col
    #top left diagonal
    while tempr>=0 and tempc<n and tempc>=0 and tempr<n:
        if board[tempr][tempc]=='Q':
            return False
        tempr-=1
        tempc-=1
    return True

def solve(row,board,all_possibilities,n):
    if row==n:
        all_possibilities.append(["".join(row) for row in board])
        return
    for col in range(n):
        if isvalid(row,col,board,n):
            board[row][col]='Q'
            solve(row+1,board,all_possibilities,n)
            board[row][col]='.'

class Solution:
    def totalNQueens(self, n: int) -> int:
        all_possibilities=[]
        board=[['.']*n for _ in range(n)]
        solve(0,board,all_possibilities,n)
        return len(all_possibilities)