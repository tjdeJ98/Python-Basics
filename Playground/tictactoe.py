board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
turn = 0
curPlayer = ""
player1, player2 = "X", "O"

gameRunning = True


def printBoard():
    for i in range(0, 9, 3):
        print(board[i:i+3])


def checkWin(player, board_item) -> bool:
    win = [player]*3
    if turn == 7:
        pass

    if turn > 4:
        for i in range(3):
            if board_item[i::3] == win:
                return False

        for i in range(0, 9, 3):
            if board_item[i:i+3] == win:
                return False

        # doesnt check the board copy
        diagnalOptionOne = [board_item[2], board_item[4], board_item[6]]
        diagnalOptionTwo = [board_item[0], board_item[4], board_item[8]]
        if win == diagnalOptionOne or win == diagnalOptionTwo:
            return False

    return True


def checkDraw() -> bool:
    if turn == 9:
        print("Draw")
        return False

    return True


def getPlayerMove() -> int:
    while True:
        printBoard()
        move = int(input("Give move num: "))
        if move < 9 and move > -1:
            if board[move] not in ["X", "O"]:
                break
    return move


def getAIMove() -> int:

    pass


def minimax(state: int, max_turn: int):
    # TODO implement a Minimax algorithm
    # TODO improve minimax algorithm with alpha beta pruning
    if state == 0:
        return 1 if max_turn else -1


def getOtherPlayer(curPlayer: str):
    return player1 if curPlayer == player2 else player2


def playerHandler(player: str):
    if player == player1:
        return player2
    return player1


def startDrawWinCheck(player: str, board_item: list) -> bool:
    if not checkWin(player, board_item):
        print(f"{player} wins!")
        return False

    if not checkDraw():
        print("It's a draw!")
        return False
    return True


if __name__ == "__main__":
    while gameRunning:
        curPlayer = playerHandler(curPlayer)

        print(curPlayer)
        if turn == 7:
            board_copy = board
            otherPlayer = getOtherPlayer(curPlayer)

            for i in range(len(board_copy)):
                if not board_copy[i]:
                    board_copy[i] = otherPlayer

            gameRunning = startDrawWinCheck(otherPlayer, board_copy)

        # if curPlayer == player1:
        move = getPlayerMove()
        # else:
        #     move = getAIMove()

        board[move] = curPlayer

        # TODO don't end game if player wins on next move, as player might make wrong move
        print(turn)

        gameRunning = startDrawWinCheck(curPlayer, board)
        turn += 1
