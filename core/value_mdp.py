from utils.file_manager import FileManager
from core.node import Node
import time
import copy
import os


class ValueMDP:
    def __init__(self, file):
        fm = FileManager(file)
        fm.read_param()
        self.size = fm.size
        self.gamma = fm.gamma
        self.noise = fm.noise
        self.table = fm.table
        self.count = 0

    def run(self, restrict, pt=False):
        up_n = self.noise[0]
        left_n = self.noise[1]
        right_n = self.noise[2]
        if len(self.noise) > 3:
            down_n = self.noise[3]
        else:
            down_n = 0

        # Init table
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.table[row][col] is None:
                    self.table[row][col] = Node(0, 0, 0, 0, terminal=False)
                else:
                    value = self.table[row][col]
                    self.table[row][col] = Node(value, value, value, value, terminal=True)

        self.print_table()
        print()

        stable = False
        while not stable:
            r = 0
            c = 0
            temp_table = copy.deepcopy(self.table)
            for row in temp_table:
                for col in row:
                    col: Node
                    if col.terminal is not True:
                        # Relative up (Main direction always is up)
                        for i in range(0, 4):
                            col.set_dir(i)
                            col.score[i] = self.gamma * (self.find(r, c, col.d_up) * up_n
                                                         + self.find(r, c, col.d_left) * left_n
                                                         + self.find(r, c, col.d_right) * right_n
                                                         + self.find(r, c, col.d_down) * down_n)
                        col.go_opt_dir()
                    c += 1
                c = 0
                r += 1

            # Check stable
            delta = 0
            for row in range(0, self.size):
                for col in range(0, self.size):
                    delta += temp_table[row][col].opt_score - self.table[row][col].opt_score
            if delta < restrict:
                stable = True

            self.table = temp_table

            if pt is True:
                self.print_table()
                time.sleep(0.5)
                print()
            self.count += 1

    def find(self, row, col, direction):
        if direction == 0:
            row -= 1
            if row < 0:
                row = 0
            score = self.table[row][col].opt_score
        elif direction == 1:
            col -= 1
            if col < 0:
                col = 0
            score = self.table[row][col].opt_score
        elif direction == 2:
            col += 1
            if col >= self.size:
                col -= 1
            score = self.table[row][col].opt_score
        elif direction == 3:
            row += 1
            if row >= self.size:
                row -= 1
            score = self.table[row][col].opt_score
        return score

    def print_table(self):
        for row in self.table:
            for col in row:
                print('%.2f\t' % col.opt_score, end='')
            print()

    def print_dir(self):
        for row in self.table:
            for col in row:
                col: Node
                if col.terminal is True:
                    if col.opt_score > 0:
                        print('%.0f   \t' % col.opt_score, end='')
                    elif col.opt_score <= 0:
                        print('%.0f   \t' % col.opt_score, end='')
                else:
                    if col.opt_dir == 0:
                        print('↑ \t\t', end='')
                    elif col.opt_dir == 1:
                        print('← \t\t', end='')
                    elif col.opt_dir == 2:
                        print('→ \t\t', end='')
                    elif col.opt_dir == 3:
                        print('↓ \t\t', end='')
            print()


def test():
    v_mdp = ValueMDP('D:\\PyProject\\AI_MDP\\AI_MDP\\examples\\i5.txt')
    start = time.time()
    v_mdp.run(0.01, pt=False)
    end = time.time()
    v_mdp.print_table()
    v_mdp.print_dir()
    print('time cost: ', end - start)
    print('iterations: ', v_mdp.count)

test()