import TicTacToe 
import Player
from view import *


class Control:

    def __init__(self):
        
        self.cellNumbers=set(range(1,10))
     
        self.player1 = self.enterPlayer('X')
        self.player2 = self.enterPlayer('O')
        self.ticTacToe = TicTacToe.TicTacToe()
        self.startGame()

    def enterPlayer(self, s):
        p = Player.Player(0, input('Player '+s+'\nEnter your name :'), s)
        return p

    def enterCell(self, msg):
       
        i = input(msg)
        if not i.isnumeric():
             return self.enterCell('Erorr!!  Enter a cell number corectly:')
        try:
            i= int(i)
            self.cellNumbers.remove(i)
            return i
             
        except:
            return self.enterCell('You should choose one of these numbers '+str(self.cellNumbers)+': ')

    tics= lambda self: len(self.cellNumbers)
    def swichTurn(self):

        if self.tics() % 2 == 1:
            return self.player1
        return self.player2

    def playerTurn(self, p):

        show("\n\n{s}{s}{s}>>> Player {S}: {n} <<<{s}{s}{s}\n--- Put {S} ---".format(n=p.name.upper(), s=p.shape.lower(),S=p.shape))
        view(self.ticTacToe.board)
        i = self.enterCell('Enter cell number: ')
        isWin = self.ticTacToe.changeByNumber(i, p.shape)
        
       # view(self.ticTacToe.board)
     #   print (self.ticTacToe.loop(p.shape))

        if isWin:
            show('*************')
            self.end('** {n} is Win **\n*************\n'.format(n=p.name))

        elif self.tics() < 1:
            self.end('Eqwal!! no winer ..... \n')
        else:
            self.playerTurn(self.swichTurn())

    def startGame(self):
        self.ticTacToe
        self.playerTurn(self.player1)
        
    def end(self,msg):
        
        view(self.ticTacToe.board)
        
        show(msg)
        
        c=input('Press enter to restart or q to quit ...')
        if c.capitalize()!='Q':
         self.__init__()
        
show('********************************')
show('********************************')
show('*** Welcom in TicTacToe Game ***')
show('********************************')
show('********************************')
show('***************** X ************')
show('****** X ***************** X ***')
show('*************** O **************')
show('**** O *************************')
show('***************** X ************')
show('***** X ************************')
show('************ O ********* O *****')
show('********************************')



Control()
