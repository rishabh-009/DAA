import numpy as np

class DynamicIntArray:
    def __init__(self,a):
        self.data = np.zeros(1)
        self.capacity = 1
        self.N = 0
    def _resize_(self):
        assert self.N == self.capacity
        tmp = np.zeros(self.capacity*2)
        for i in range(self.capacity):
            tmp[i] = self.data[i]
        self.capacity*=2
        self.data=tmp
    def insert(self,a):
        if self.N < self.capacity:
            self.data[self.N] = a
            self.N+=1
        else: 
            self._resize_()
            self.insert(a)
    def __iter__(self):
        for i in range(self.N):
            yield int(self.data[i])

    def _resize_down_(self):
        assert self.N == self.capacity//4
        tmp = np.zeros(self.capacity//2)
        for i in range(self.capacity//4):
            tmp[i] = self.data[i]
        self.capacity//=2
        self.data=tmp
    def delete(self,a):
        if self.N>self.capacity//4:
            for i in range(self.N):
                if self.data[i] == a:
                    self.data[i] = None
                    break 
            self.N-=1
        else:
            self._resize_down_()
            self.insert(a)

        

    




