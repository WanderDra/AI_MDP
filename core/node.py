
class Node:
    def __init__(self, up, left, right, down, terminal=False):
        self.opt_dir = 0        # up = 0, left = 1, right = 2, down = 3
        self.up = up
        self.left = left
        self.right = right
        self.down = down
        self.score = [up, left, right, down]
        self.opt_dir_score = self.score
        self.terminal = terminal
        self.opt_score = None
        self.go_opt_dir()
        self.d_up = 0
        self.d_left = 1
        self.d_right = 2
        self.d_down = 3

    def set_dir(self, direction):
        self.opt_dir = direction
        if self.opt_dir == 0:
            self.up = self.score[0]
            self.d_up = 0
            self.left = self.score[1]
            self.d_left = 1
            self.right = self.score[2]
            self.d_right = 2
            self.down = self.score[3]
            self.d_down = 3
        elif self.opt_dir == 1:
            self.up = self.score[1]
            self.d_up = 1
            self.left = self.score[3]
            self.d_left = 3
            self.right = self.score[0]
            self.d_right = 0
            self.down = self.score[2]
            self.d_down = 2
        elif self.opt_dir == 2:
            self.up = self.score[2]
            self.d_up = 2
            self.left = self.score[0]
            self.d_left = 0
            self.right = self.score[3]
            self.d_right = 3
            self.down = self.score[1]
            self.d_down = 1
        elif self.opt_dir == 3:
            self.up = self.score[3]
            self.d_up = 3
            self.left = self.score[2]
            self.d_left = 2
            self.right = self.score[1]
            self.d_right = 1
            self.down = self.score[0]
            self.d_down = 0

        self.opt_dir_score = [self.up, self.left, self.right, self.down]

    def go_opt_dir(self):
        self.set_dir(self.score.index(max(self.score)))
        self.opt_score = self.up


