

class FileManager:
    def __init__(self, file):
        self.file = open(file, 'r', encoding='utf-8')
        self.size = 0
        self.gamma = 0
        self.noise = []
        self.table = []

    def read_param(self):
        # Read size
        line = self.file.readline()
        while line[0:1] == '#' or line == '\n':
            line = self.file.readline()
        self.size = int(line.split('#')[0].strip())

        # Read gamma
        line = self.file.readline()
        while line[0:1] == '#' or line == '\n':
            line = self.file.readline()
        self.gamma = float(line.split('#')[0].strip())

        # Read noise
        line = self.file.readline()
        while line[0:1] == '#' or line == '\n':
            line = self.file.readline()
        for noise in line.split('#')[0].strip().split(','):
            self.noise.append(float(noise))

        # Read table
        line = self.file.readline()
        while line[0:1] == '#' or line == '\n':
            line = self.file.readline()
        while line is not '':
            row = []
            for col in line.split('#')[0].strip().split(','):
                if col == 'X':
                    col = None
                else:
                    col = float(col)
                row.append(col)
            self.table.append(row)
            line = self.file.readline()



def test():
    fm = FileManager('D:\\PyProject\\AI_MDP\\AI_MDP\\examples\\i1.txt')
    fm.read_param()


test()