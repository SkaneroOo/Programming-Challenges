from random import randint
def tttrand(board):
    temple=['1','2','3','4','5','6','7','8','9']
    rand=randint(1,len(board)-1)
    if board[rand] in temple:
        return(rand)
    else:
        while board[rand] not in temple:
            rand = randint(1, len(board)-1)
        return(rand)

#    def battleshiprand(board):
