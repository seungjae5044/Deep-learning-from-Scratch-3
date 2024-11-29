import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        ouput = Variable(y)
        return ouput
    def forward(self, x):
        raise NotImplementedError()

class Square(Function):
    def forward(self, x):
        return x ** 2

if __name__ == "__main__":
    x = Variable(np.array(10))
    f = Square()
    y = f(x)
    print(type(y))
    print(y.data)


