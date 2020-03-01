#slove the game
from easyAI import id_solve

class GameOfBones( TwoPlayersGame ):
    def __init__(self, players):
        self.players = players
        self.pile = 20 # start with 20 bones in the pile
        self.nplayer = 1 # player 1 starts

    def possible_moves(self): return ['1','2','3']
    def make_move(self,move): self.pile -= int(move) # remove bones.
    def win(self): return self.pile<=0 # opponent took the last bone ?
    def is_over(self): return self.win() # Game stops when someone wins.
    def show(self): print ("%d bones left in the pile"%self.pile)
    def scoring(self): return 100 if self.win() else 0 # For the AI

        
r,d,m = id_solve(GameOfBones, ai_depths=range(2,20), win_score=100)

tt = TT()

GameOfBones.ttentry = lambda game : game.pile # key for the table
r,d,m = id_solve(GameOfBones, range(2,20), win_score=100, tt=tt)

game = GameOfBones( [  AI_Player( tt ), Human_Player() ] )
history = game.play() # you will always lose this game :)
1

