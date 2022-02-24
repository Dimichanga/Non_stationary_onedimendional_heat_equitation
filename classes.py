class Boundary:
    def __init__(self, table=[]):
        self.table=table

    def set_boundary(self, str):
        with open(str, "r") as f:
            for line in f:
                self.table.append([float(x) for x in line.split()]) # 0 - time, 1 - temperature

    def get(self,x): # Function interpolation
        N = len(self.table)
        if x >= self.table[N-1][0]:
            val = self.table[N-1][1]
        else:
            i = 0
            while self.table[i][0] < x:
                i+=1
            val = self.table[i-1][1] + ((self.table[i][1] - self.table[i-1][1]) / (self.table[i][0] - self.table[i-1][0])) * (x - self.table[i-1][0])
        return val
   
class time_:
    def __init__(self,step=0,actual=0,duration=0,output=0, n=0):
        self.step = step
        self.actual = actual
        self.duration = duration
        self.output = output
        self.n = n

    def set_step(self, x):
        self.step = x

    def set_n(self):
        self.n = self.output / self.step #coef for output of data

class geometry:
    def __init__(self, length=0):
        self.length = length 

    def set_geometry(self, str):
        with open(str, "r") as f:
            self.length = float(f.read())

    def get_geometry(self):
        return self.lenght


