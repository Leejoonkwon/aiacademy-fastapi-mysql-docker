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
        ''' 
        
 Q4 국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성. 단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
 ic| self.id(): 'HKKHc'
ic| self.score(): 22
ic| df4:        국어  영어  수학  사회
               lDZid  57  90  55  24
               Rnvtg  12  66  43  11
               ljfJt  80  33  89  10
               ZJaje  31  28  37  34
               OnhcI  15  28  89  19
               claDN  69  41  66  74    
               
               LYawb  65  16  13  20
               QDBCw  44  32   8  29
               PZOTP  94  78  79  96
               GOJKU  62  17  75  49
'''
    def id(self):
        return [ "".join((random.choice(string.ascii_letters) 
                          for i in range(5))) for i in range(10)]
    
    def score(self):
        return np.random.randint(0,101,(10,4))
    
    def quiz_4(self) :
        ic(self.id())
        ic(self.score())
        df4 = pd.DataFrame(self.score(),
                           index = self.id(),
                           columns=['국어', '영어', '수학', '사회'])
 
        ic(df4)

