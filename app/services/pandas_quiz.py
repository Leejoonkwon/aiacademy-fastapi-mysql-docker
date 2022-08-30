from icecream import ic
from jsonschema import draft4_format_checker
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
    ''' 
    Q5 원하는 과목 점수만 출력하시오. (만약 국어라고 입력하면 아래와 같이 출력됨)
        hVoGW    93
        QkpKK    25
        oDmky    82
        qdTeX    51
        XGzWk    34
        PAwgj    85
        vnTmB    28
        wuxIm    58
        AOQFG    32
        jHChe    59
        Name: 국어, dtype: int64
        '''

    def quiz_5(self,subject):
        self.subject = subject
        df5 = pd.DataFrame(self.score(),
                           index = self.id(),
                           columns=['국어', '영어', '수학', '사회'])[f'{self.subject}']
        ic(df5)
    ''' 
    Q6 원하는 학생점수만 출력하시오. (아이디가 랜덤이므로 맨 위에 학생점수 출력으로 대체함)
        lDZid  57  90  55  24
    '''
    def quiz_6(self):
        df6 = pd.DataFrame(self.score(),
                           index = self.id(),
                           columns=['국어', '영어', '수학', '사회'])
        ic(df6.iloc[[0]])
    '''
    Q7 각 학생들의 점수의 총합과 마지막 행은 과목총점 추가해서 출력
        ic| df5:  국어   영어   수학   사회   과학    총점
                 hVoGW   93   44   14   94   86   331
                 QkpKK   25   54   29   10    8   126
                 oDmky   82   65   31   31    2   211
                 qdTeX   51   56   56    3   13   179
                 XGzWk   34   32   67   48   23   204
                 PAwgj   85   24   16    8   22   155
                 vnTmB   28   80   52   43   48   251
                 wuxIm   58   94   93   54   83   382
                 AOQFG   32   50   95    1   52   230
                 jHChe   59   37   80   27   39   242
                 과목총점   547  536  533  319  376  2311
''' 
    def quiz_7(self):
        random_num = np.random.randint(0,101,(10,5))
        df7 = pd.DataFrame(random_num,index=self.id(),
                           columns=['국어','영어','수학','사회','과학'])
        df7['총점'] = df7.sum(axis=1)
        df7.loc['과목총점']= df7.sum(axis=0)
        ic(df7)
       


