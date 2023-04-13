from Board import BoardUtility
import random
import copy

class Player:
    def __init__(self, player_piece):
        self.piece = player_piece

    def play(self, board):
        return 0


class RandomPlayer(Player):
    def play(self, board):
        return [random.choice(BoardUtility.get_valid_locations(board)), random.choice([1, 2, 3, 4]), random.choice(["skip", "clockwise", "anticlockwise"])]


class HumanPlayer(Player):
    def play(self):
        move = input("row, col, region, rotation\n")
        move = move.split()
        return [[int(move[0]), int(move[1])], int(move[2]), move[3]]

class TreeDepth():

    def __init__(self,depthlim,board,min_max,piece,row,col,region,rotation):
        self.piece=piece
        self.depthlim=depthlim
        self.board=board
        self.subTree={}
        self.min_max=1 if min_max==0 else 0
        self.row=row
        self.col = col
        self.region = region
        self.rotation = rotation
        self.nodeValue=0
        self.subtrees=[]
    @staticmethod
    def make_move1(game_board, row, col, region, rotation, piece):
        """
        make a new move on the board
        row & col: row and column of the new move
        piece: 1 for first player. 2 for second player
        """

        assert game_board[row][col] == 0
        game_board[row][col] = piece
        BoardUtility.rotate_region(game_board, region, rotation)
    def utility_Func(self,board, player_piece1,min_max):
        """
        piece:  1 or 2.
        return: True if the player with the input piece has won.
                False if the player with the input piece has not won.
        """
        player_piece=player_piece1 if min_max == 1 else (2 if player_piece1 == 1 else 1)
        player_piece2=player_piece1 if min_max == 0 else (2 if player_piece1 == 1 else 1)
        ROWS=len(board)
        COLS=len(board)
        UtilityFunc=0
        utilharif=0
        # checking horizontally
        for c in range(2):
            for r in range(ROWS):
                thisUtil=0
                if board[r][c] == player_piece:
                    thisUtil=thisUtil+1
                elif board[r][c] != 0:
                    thisUtil =-10000
                if board[r][c + 1] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r][c+1] != 0:
                    thisUtil =-10000
                if board[r][c + 2] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r][c+2] != 0:
                    thisUtil =-10000
                if board[r][c + 3] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r][c+3] != 0:
                    thisUtil =-10000
                if board[r][c + 4] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r][c+4] != 0:
                    thisUtil =-10000
                if thisUtil>UtilityFunc:
                    UtilityFunc=thisUtil

                thisUtil = 0
                if board[r][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c] != 0:
                    thisUtil = -10000
                if board[r][c + 1] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c + 1] != 0:
                    thisUtil = -10000
                if board[r][c + 2] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c + 2] != 0:
                    thisUtil = -10000
                if board[r][c + 3] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c + 3] != 0:
                    thisUtil = -10000
                if board[r][c + 4] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c + 4] != 0:
                    thisUtil = -10000
                if thisUtil > utilharif:
                    utilharif = thisUtil

        # checking vertically
        for r in range(2):
            for c in range(COLS):
                thisUtil=0
                if board[r][c] == player_piece:
                    thisUtil=thisUtil+1
                elif board[r][c] != 0:
                    thisUtil =-10000
                if board[r + 1][c] == player_piece:
                    thisUtil=thisUtil+1
                elif board[r+1][c] != 0:
                    thisUtil =-10000
                if board[r + 2][c] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r+2][c] != 0:
                    thisUtil =-10000
                if board[r + 3][c] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r+3][c] != 0:
                    thisUtil =-10000
                if board[r + 4][c] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r+4][c] != 0:
                    thisUtil =-10000
                if thisUtil > UtilityFunc:
                    UtilityFunc = thisUtil

                thisUtil=0
                if board[r][c] == player_piece2:
                    thisUtil=thisUtil+1
                elif board[r][c] != 0:
                    thisUtil =-10000
                if board[r + 1][c] == player_piece2:
                    thisUtil=thisUtil+1
                elif board[r+1][c] != 0:
                    thisUtil =-10000
                if board[r + 2][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r+2][c] != 0:
                    thisUtil =-10000
                if board[r + 3][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r+3][c] != 0:
                    thisUtil =-10000
                if board[r + 4][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r+4][c] != 0:
                    thisUtil =-10000
                if thisUtil > utilharif:
                    utilharif = thisUtil

        # checking diagonally
        for c in range(COLS - 4):
            for r in range(4, ROWS):
                thisUtil=0
                if board[r][c] == player_piece:
                    thisUtil=thisUtil+1
                elif board[r][c] != 0:
                    thisUtil =-10000
                if board[r - 1][c + 1] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-1][c+1] != 0:
                    thisUtil =-10000
                if board[r - 2][c + 2] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-2][c+2] != 0:
                    thisUtil =-10000
                if board[r - 3][c + 3] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-3][c+3] != 0:
                    thisUtil =-10000
                if board[r - 4][c + 4] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-4][c+4] != 0:
                    thisUtil =-10000
                if thisUtil > UtilityFunc:
                    UtilityFunc = thisUtil

                thisUtil = 0
                if board[r][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c] != 0:
                    thisUtil = -10000
                if board[r - 1][c + 1] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 1][c + 1] != 0:
                    thisUtil = -10000
                if board[r - 2][c + 2] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 2][c + 2] != 0:
                    thisUtil = -10000
                if board[r - 3][c + 3] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 3][c + 3] != 0:
                    thisUtil = -10000
                if board[r - 4][c + 4] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 4][c + 4] != 0:
                    thisUtil = -10000
                if thisUtil > utilharif:
                    utilharif = thisUtil

        # checking diagonally
        for c in range(4, COLS):
            for r in range(4, ROWS):
                thisUtil=0
                if board[r][c] == player_piece:
                    thisUtil =thisUtil+1
                elif board[r][c] != 0:
                    thisUtil =-10000
                if board[r - 1][c - 1] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-1][c-1] != 0:
                    thisUtil =-10000
                if board[r - 2][c - 2] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-2][c-2] != 0:
                    thisUtil =-10000
                if board[r - 3][c - 3] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-3][c-3] != 0:
                    thisUtil =-10000
                if board[r - 4][c - 4] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-4][c-4] != 0:
                    thisUtil =-10000
                if thisUtil > UtilityFunc:
                    UtilityFunc = thisUtil

                thisUtil = 0
                if board[r][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c] != 0:
                    thisUtil = -10000
                if board[r - 1][c - 1] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 1][c - 1] != 0:
                    thisUtil = -10000
                if board[r - 2][c - 2] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 2][c - 2] != 0:
                    thisUtil = -10000
                if board[r - 3][c - 3] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 3][c - 3] != 0:
                    thisUtil = -10000
                if board[r - 4][c - 4] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 4][c - 4] != 0:
                    thisUtil = -10000
                if thisUtil > utilharif:
                    utilharif = thisUtil
        return [UtilityFunc ,utilharif]
    def make_sub_tree(self):
        if self.depthlim>0:
            rotate = [ "anticlockwise","clockwise", "skip"]
            for reg in [1,2,3,4]:
                for rot in rotate:
                    validcell = BoardUtility.get_valid_locations(self.board)
                    for cell in validcell:
                        copy_board = copy.deepcopy(self.board)
                        TreeDepth.make_move1(copy_board, cell[0], cell[1], reg, rot,self.piece )
                        subtr=TreeDepth(self.depthlim-1,copy_board,self.min_max,self.piece if self.min_max==0 else (2 if self.piece==1 else 1 ),cell[0], cell[1], reg, rot)
                        subtr.make_sub_tree()
                        self.subTree[subtr]=subtr.nodeValue
                        self.subtrees.append(subtr)

            self.nodeValue=max(self.subTree.values()) if self.min_max else min(self.subTree.values())
        else :
            utils=self.utility_Func(self.board,self.piece,self.min_max)
            self.nodeValue=utils[0]
            harif=utils[1]
            if harif>=3:
                self.nodeValue=self.nodeValue-1000











class MiniMaxPlayer(Player):
    def __init__(self, player_piece, depth=5):
        super().__init__(player_piece)
        self.depth = depth
        self.depth=1


    def play(self, board):
        row = -1
        col = -1
        region = -1
        rotation = -1
        # Todo: implement minimax algorithm
        selftree=TreeDepth(self.depth,board,0,self.piece,row,col,region,rotation)
        selftree.make_sub_tree()
        dic=selftree.subTree
        max=0
        subtreee = copy.deepcopy(selftree)
        for i in dic:
            if i.nodeValue==selftree.nodeValue:
                subtreee=i

        row =subtreee.row
        col = subtreee.col
        region=subtreee.region
        rotation=subtreee.rotation

        return [[row, col], region, rotation]

















class ProbTreeDepth():
    def __init__(self,depthlim,board,min_max,piece,row,col,region,rotation,prob_stochastic):
        self.piece=piece
        self.depthlim=depthlim
        self.board=board
        self.subTree={}
        self.min_max=1 if min_max==0 else 0
        self.row=row
        self.col = col
        self.region = region
        self.rotation = rotation
        self.nodeValue=0
        self.subtrees=[]
        self.prob_stochastic=prob_stochastic
    @staticmethod
    def make_move1(game_board, row, col, region, rotation, piece):
        """
        make a new move on the board
        row & col: row and column of the new move
        piece: 1 for first player. 2 for second player
        """

        assert game_board[row][col] == 0
        game_board[row][col] = piece
        BoardUtility.rotate_region(game_board, region, rotation)
    def utility_Func(self,board, player_piece1,min_max):
        """
        piece:  1 or 2.
        return: True if the player with the input piece has won.
                False if the player with the input piece has not won.
        """
        player_piece=player_piece1 if min_max == 1 else (2 if player_piece1 == 1 else 1)
        player_piece2=player_piece1 if min_max == 0 else (2 if player_piece1 == 1 else 1)
        ROWS=len(board)
        COLS=len(board)
        UtilityFunc=0
        utilharif=0
        # checking horizontally
        for c in range(2):
            for r in range(ROWS):
                thisUtil=0
                if board[r][c] == player_piece:
                    thisUtil=thisUtil+1
                elif board[r][c] != 0:
                    thisUtil =-10000
                if board[r][c + 1] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r][c+1] != 0:
                    thisUtil =-10000
                if board[r][c + 2] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r][c+2] != 0:
                    thisUtil =-10000
                if board[r][c + 3] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r][c+3] != 0:
                    thisUtil =-10000
                if board[r][c + 4] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r][c+4] != 0:
                    thisUtil =-10000
                if thisUtil>UtilityFunc:
                    UtilityFunc=thisUtil

                thisUtil = 0
                if board[r][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c] != 0:
                    thisUtil = -10000
                if board[r][c + 1] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c + 1] != 0:
                    thisUtil = -10000
                if board[r][c + 2] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c + 2] != 0:
                    thisUtil = -10000
                if board[r][c + 3] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c + 3] != 0:
                    thisUtil = -10000
                if board[r][c + 4] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c + 4] != 0:
                    thisUtil = -10000
                if thisUtil > utilharif:
                    utilharif = thisUtil

        # checking vertically
        for r in range(2):
            for c in range(COLS):
                thisUtil=0
                if board[r][c] == player_piece:
                    thisUtil=thisUtil+1
                elif board[r][c] != 0:
                    thisUtil =-10000
                if board[r + 1][c] == player_piece:
                    thisUtil=thisUtil+1
                elif board[r+1][c] != 0:
                    thisUtil =-10000
                if board[r + 2][c] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r+2][c] != 0:
                    thisUtil =-10000
                if board[r + 3][c] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r+3][c] != 0:
                    thisUtil =-10000
                if board[r + 4][c] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r+4][c] != 0:
                    thisUtil =-10000
                if thisUtil > UtilityFunc:
                    UtilityFunc = thisUtil

                thisUtil=0
                if board[r][c] == player_piece2:
                    thisUtil=thisUtil+1
                elif board[r][c] != 0:
                    thisUtil =-10000
                if board[r + 1][c] == player_piece2:
                    thisUtil=thisUtil+1
                elif board[r+1][c] != 0:
                    thisUtil =-10000
                if board[r + 2][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r+2][c] != 0:
                    thisUtil =-10000
                if board[r + 3][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r+3][c] != 0:
                    thisUtil =-10000
                if board[r + 4][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r+4][c] != 0:
                    thisUtil =-10000
                if thisUtil > utilharif:
                    utilharif = thisUtil

        # checking diagonally
        for c in range(COLS - 4):
            for r in range(4, ROWS):
                thisUtil=0
                if board[r][c] == player_piece:
                    thisUtil=thisUtil+1
                elif board[r][c] != 0:
                    thisUtil =-10000
                if board[r - 1][c + 1] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-1][c+1] != 0:
                    thisUtil =-10000
                if board[r - 2][c + 2] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-2][c+2] != 0:
                    thisUtil =-10000
                if board[r - 3][c + 3] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-3][c+3] != 0:
                    thisUtil =-10000
                if board[r - 4][c + 4] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-4][c+4] != 0:
                    thisUtil =-10000
                if thisUtil > UtilityFunc:
                    UtilityFunc = thisUtil

                thisUtil = 0
                if board[r][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c] != 0:
                    thisUtil = -10000
                if board[r - 1][c + 1] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 1][c + 1] != 0:
                    thisUtil = -10000
                if board[r - 2][c + 2] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 2][c + 2] != 0:
                    thisUtil = -10000
                if board[r - 3][c + 3] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 3][c + 3] != 0:
                    thisUtil = -10000
                if board[r - 4][c + 4] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 4][c + 4] != 0:
                    thisUtil = -10000
                if thisUtil > utilharif:
                    utilharif = thisUtil

        # checking diagonally
        for c in range(4, COLS):
            for r in range(4, ROWS):
                thisUtil=0
                if board[r][c] == player_piece:
                    thisUtil =thisUtil+1
                elif board[r][c] != 0:
                    thisUtil =-10000
                if board[r - 1][c - 1] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-1][c-1] != 0:
                    thisUtil =-10000
                if board[r - 2][c - 2] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-2][c-2] != 0:
                    thisUtil =-10000
                if board[r - 3][c - 3] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-3][c-3] != 0:
                    thisUtil =-10000
                if board[r - 4][c - 4] == player_piece:
                    thisUtil = thisUtil + 1
                elif board[r-4][c-4] != 0:
                    thisUtil =-10000
                if thisUtil > UtilityFunc:
                    UtilityFunc = thisUtil

                thisUtil = 0
                if board[r][c] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r][c] != 0:
                    thisUtil = -10000
                if board[r - 1][c - 1] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 1][c - 1] != 0:
                    thisUtil = -10000
                if board[r - 2][c - 2] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 2][c - 2] != 0:
                    thisUtil = -10000
                if board[r - 3][c - 3] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 3][c - 3] != 0:
                    thisUtil = -10000
                if board[r - 4][c - 4] == player_piece2:
                    thisUtil = thisUtil + 1
                elif board[r - 4][c - 4] != 0:
                    thisUtil = -10000
                if thisUtil > utilharif:
                    utilharif = thisUtil
        return [UtilityFunc ,utilharif]

    def make_sub_tree(self):
        if self.depthlim > 0:
            rotate = ["anticlockwise", "clockwise", "skip"]
            for reg in [1, 2, 3, 4]:
                for rot in rotate:
                    validcell = BoardUtility.get_valid_locations(self.board)
                    for cell in validcell:
                        copy_board = copy.deepcopy(self.board)
                        TreeDepth.make_move1(copy_board, cell[0], cell[1], reg, rot, self.piece)
                        subtr = ProbTreeDepth(self.depthlim - 1, copy_board, self.min_max,
                                          self.piece if self.min_max == 0 else (2 if self.piece == 1 else 1), cell[0],
                                          cell[1], reg, rot,self.prob_stochastic)
                        subtr.make_sub_tree()
                        self.subTree[subtr] = subtr.nodeValue
                        self.subtrees.append(subtr)

            randint=random.uniform(0, 1)
            #print(randint)
            self.nodeValue = (max(self.subTree.values()) if self.min_max else min(self.subTree.values())) if randint>self.prob_stochastic else random.choice(list(self.subTree.values()))
        else:
            utils = self.utility_Func(self.board, self.piece, self.min_max)
            self.nodeValue = utils[0]
            harif = utils[1]
            if harif >= 3:
                self.nodeValue = self.nodeValue = -1000


class MiniMaxProbPlayer(Player):
    def __init__(self, player_piece, depth=5, prob_stochastic=0.1):
        super().__init__(player_piece)
        self.depth = depth
        self.depth=1
        self.prob_stochastic = prob_stochastic

    def play(self, board):
        row = -1
        col = -1
        region = -1
        rotation = -1
        # Todo: implement minimaxProb algorithm

        selftree = ProbTreeDepth(self.depth, board, 0, self.piece, row, col, region, rotation,self.prob_stochastic)
        selftree.make_sub_tree()
        dic = selftree.subTree
        max = 0
        subtreee = copy.deepcopy(selftree)
        for i in dic:
            if i.nodeValue == selftree.nodeValue:
                subtreee = i
        row = subtreee.row
        col = subtreee.col
        region = subtreee.region
        rotation = subtreee.rotation


        return [[row, col], region, rotation]
