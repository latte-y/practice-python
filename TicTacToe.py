matrixSize = int(input('何目並べで遊ぶ？＞'))
print(f'===============================\n=           {matrixSize}目並べ           =\n===============================')


def printBoardIndex(matrixSize):
    for i in range(matrixSize*matrixSize):
        print(i, end=' ')
        if i % matrixSize == matrixSize - 1:
            print('')

def printBoard(boardElement, gridIdex, matrixSize):
    for i in range(matrixSize*matrixSize):
        print(boardElement[i], end=' ')
        if i % matrixSize == matrixSize - 1:
            print('')

# initial condition
print('下記のマス目の数字を使用して対戦します。\n')
printBoardIndex(matrixSize)

turn = 1
player = {'player2':'X', 'player1':'O'}
boardElement = []
for i in range(matrixSize*matrixSize):
    boardElement.append('*')

while True:

    print(f'\n\"{list(player.keys())[turn%2]}\"のターン (turn={turn})')

    try:
        gridIndex = int(input('どこを指定しますか？＞'))
        boardElement[gridIndex] = list(player.values())[turn%2]
        print(boardElement)
        
        printBoard(boardElement, gridIndex, matrixSize)

        # 揃ったか判定
        # hogehoge()

        turn += 1

    except:
        print('指定された範囲内でindexを指定してください。')
