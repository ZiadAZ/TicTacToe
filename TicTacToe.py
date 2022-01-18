
class TicTacToe:
    
    

    def __init__(self):

        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def isWin(arr): return arr[0] == arr[1] == arr[2]

    def checkDiameter(arr, row, column):

        if (row+column) % 2 != 0:
            return

        def cell(index):
            a = [arr[i][j] for (i, j) in index]

            return TicTacToe.isWin(a)

        mainDiameterCells = ((0, 0), (1, 1), (2, 2))
        crossDiameterCells = ((0, 2), (1, 1), (2, 0))
        if (row, column) in mainDiameterCells:
            main = cell(mainDiameterCells)
            if main:
                return True
        if (row, column) in crossDiameterCells:
            return cell(crossDiameterCells)

    def changeByNumber(self, number, shape):

        for row in range(3):
            for column in range(3):
                if self.board[row][column] == number:
                    return self.changeCell(row, column, shape)

    def changeCell(self, row, column, shape):
        def columns(column): return [row[column] for row in self.board]
        self.board[row][column] = shape

        return TicTacToe.checkDiameter(self.board, row, column) or TicTacToe.isWin(self.board[row]) or TicTacToe.isWin(columns(column))

    def loop(self, s):

        for r in range(3):
            for c in range(3):
                if self.board[r][c] != s or self.board[c][r] != s:
                    continue
                    return s
        return -1
