board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
turn = 0
curPlayer = ""

gameRunning = True


def printBoard():
    for i in range(0, 9, 3):
        print(board[i:i+3])


def checkWin(curPlayer) -> bool:
    win = [curPlayer]*3

    for i in range(3):
        if board[i::3] == win:
            return False

    for i in range(0, 9, 3):
        if board[i:i+3] == win:
            return False

    diagnalOptionOne = [board[2], board[4], board[6]]
    diagnalOptionTwo = [board[0], board[4], board[8]]
    if win == diagnalOptionOne or win == diagnalOptionTwo:
        return False

    return True


def checkDraw(curPlayer) -> bool:
    """
    if it is turn 7 then next turn is always final turn.
    CheckDraw should only check for draw. But maybe make difference between current and next turn.
    """
    if turn == 8:
        print("Draw")
        return False
    if turn == 7:
        # TODO do i need to make a copy of board or can I just append and it doesn't change the value outside this method?
        pass

    # TODO implement Draw -> maybe 1 turn before final turn/when it is clear a draw is inplace
    return True


def getPlayerMove(curPlayer) -> int:
    while True:
        printBoard()
        move = int(input("Give move num: "))
        if move < 9 and move > -1:
            if board[move] not in ["X", "O"]:
                break
    return move


def getAIMove() -> int:

    pass


def minimax(state, max_turn):
    # TODO implement a Minimax algorithm
    # TODO improve minimax algorithm with alpha beta pruning
    if state == 0:
        return 1 if max_turn else -1


def getOtherPlayer(curPlayer):
    player1, player2 = "X", "O"
    return player1 if curPlayer == player2 else player2


def playerHandler(curPlayer):
    player1, player2 = "X", "O"

    if curPlayer == player1:
        return player2
    return player1


while gameRunning:
    curPlayer = playerHandler(curPlayer)

    print(curPlayer)

    # if curPlayer == player1:
    move = getPlayerMove(curPlayer)
    # else:
    #     move = getAIMove()

    board[move] = curPlayer

    # TODO if next players have no more chance of winning then end game.
    # TODO don't end game if player wins on next move, as player might make wrong move
    # TODO possibly end game if next player only can make 1 move and it would be the winning move.
    if not checkWin(curPlayer):
        print(f"{curPlayer} wins!")
        gameRunning = False

    if not checkDraw(curPlayer):
        print("It's a draw!")
        gameRunning = False

    turn += 1
