from board import Board
from square import Square

class TicTacBoard(Board):
    
    def __init__(self):
        self.n_cols = 3
        self.n_rows = 3
        self.nums = []
        self._set_up_nums()

    def _set_up_nums(self):
        for i in range(self.n_cols):
            new_row = []
            for j in range(self.n_rows):
                new_row.append(Square())
            self.nums.append(new_row)

    def play(self):
        current_player = 1
        while not self.check_winner():
            print("Player", current_player, "make a choice (x,y)")
            choice = input("x,y:")
            choice = choice.split(",")
            x, y = int(choice[0]), int(choice[1])
            if self.nums[x][y].status == 0:
                self.nums[x][y].status = current_player
            else:
                print("There's already a piece here, try again")
                continue
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1
            print(self)

    def check_winner(self):
        # Check horizontal
        for i in range(self.n_cols):
            first = self.nums[i][0].status
            if first == 0:
                return False
            for j in range(self.n_rows):
                if self.nums[i][j].status != first:
                    break
                if j == self.n_cols-1:
                    return True
        # Check vertical
        for i in range(self.n_cols):
            first = self.nums[0][i].status
            if first == 0:
                return False
            for j in range(self.n_rows):
                if self.nums[j][i].status != first:
                    break
                if j == self.n_cols-1:
                    return True
        return False

    def _set_up_elems(self):
        raise NotImplementedError

    def solve(self):
        raise NotImplementedError


if __name__ == "__main__":
    testboard = TicTacBoard()
    testboard.play()

