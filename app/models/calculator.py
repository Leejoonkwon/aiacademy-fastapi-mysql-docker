class Calculator(object):
    def __init__(self,first,second):
        self.first = first # 괄호가 없는 건 속성
        self.second = second
        pass
    
    def sum(self) : #괄호가 있는 건 method
        return self.first + self.second
    
    def sub(self) :
        return self.first - self.second
    
    def mul(self) :
        return self.first * self.second
    
    def div(self) :
        return self.first / self.second
  