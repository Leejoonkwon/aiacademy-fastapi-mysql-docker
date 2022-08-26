class Grade(object):
    def __init__(self,name,kor,eng,math) -> None:
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.avg = 0.0
    
    def set_avg(self): # assignment 은 변수 정의
        self.avg = (self.kor + self.eng + self.math) / 3
        
    def get_avg(self): # get 은 ruturn 이 나와야한다.
        return self.avg
