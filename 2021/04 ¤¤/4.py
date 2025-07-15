def bingo(inputfile):
    with open(inputfile) as data:
        nums = data.readline().split(',')
        rows = [x.split() for x in data.readlines() if x.split()]

    boards = []
    for i in range(0, len(rows), 5):
        board, cols = [], [{}, {}, {}, {}, {}]
        for x in rows[i:i+5]:
            board.append({y: 0 for y in x})
            for z in x:
                cols[x.index(z)][z] = 0
        board.extend(cols)
        boards.append(board)

    '''i, winner, sums = 0, [], []
    while not winner and i < len(nums):
        num = nums[i]
        for board in boards:
            for bingo in board:
                if num in bingo:
                    bingo[num] = 1
                    if all(bingo.values()):
                        winner.append(boards.index(board))
                        combined_board = {k: v for x in board for k, v in x.items()}
                        sums.append(sum(int(x)
                                    for x in combined_board if not combined_board[x] and x != num) * int(num))
        i += 1
    return sums, winner'''

    # del 2

    i, winsum, winners = 0, 0, set()
    while not winsum and i < len(nums):
        num = nums[i]
        for board in boards:
            if boards.index(board) not in winners:
                for bingo in board:
                    if num in bingo:
                        bingo[num] = 1
                        if all(bingo.values()):
                            winners.add(boards.index(board))
                            if len(winners) == len(boards):
                                combined_board = {k: v for x in board for k, v in x.items()}
                                winsum = sum(
                                    int(x) for x in combined_board if not combined_board[x] and x != num) * int(num)
        i += 1
    return winsum


print(bingo('4-input.txt'))
