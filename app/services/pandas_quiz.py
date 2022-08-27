from icecream import ic
import pandas as pd
import numpy as np
import random
import string
class PandasQuiz(object):
    def __init__(self) -> None:
        pass
    
    '''
        Q1. 다음 결과 출력
           a  b  c
        1  1  3  5
        2  2  4  6
        ic| df1:    a  b  c
                 1  1  3  5
                 2  2  4  6
    '''
    def quiz_1(self) -> None :
        df1 = pd.DataFrame.from_dict(
          { '1' :  [1 , 3 , 5],
            '2' :  [2 , 4 , 6]},
          orient='index',
          columns=['a','b','c'])
        ic(df1)
    def quiz_2(self) -> None :
        df2 = pd.DataFrame.from_dict({'1': [1, 2, 3],'2': [4, 5, 6],'3': [7, 8, 9],
                                      '4': [10, 11, 12]},orient='index',columns=['A','B','C'])
        ic(df2)   
    def quiz_3(self) -> None :
        df3 = pd.DataFrame.from_dict({'0':np.random.randint(10,100,size=3),
                                    '1':np.random.randint(10,100,size=3) },
                               orient='index',columns=['0','1','2'])
        ic(df3)  
    def quiz_4(self) -> None :
        ic(self.id())
        ic(self.score())
        df4 = pd.DataFrame.from_dict({self.id():self.score()},
                                     orient='index', columns=['국어', '영어', '수학', '사회'])
        for i in range(8):
            df4 = pd.concat([df4,pd.DataFrame.from_dict({self.id():self.score()}, 
                                                        orient='index', columns=['국어', '영어', '수학', '사회'])],axis=0)
        ic(df4)
    def id(self):
        rand_str = ''
        for i in range(5):
            rand_str += str(random.choice(string.ascii_letters))
        return rand_str
    
    def score(self):
        return random.sample(range(0,100), 4)