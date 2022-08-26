import pandas as pd
import numpy as np
from icecream import ic
import random
import string
n = 5
random_str = ""
k = 10
empty = []
empty2 = []
# for i in range(n):
#     (''.join(random_str += str(random.choice(string.ascii_letters)) for _ in range(k))
for x in range(k):
    empty.append(''.join(random.choice(string.ascii_letters) for _ in range(n)))     
for i in range(10):
    empty2.append((np.random.randint(10,100,size=(1,4)))) 
dictionary = dict(zip(empty,np.array(empty2)))

class Content(object):
    def __init__(self) -> None:
        pass
    def make(self) -> None :
        # print(f'id : {empty[0]}')
        # print(f'점수 : {empty2[0][0]}')
        df = pd.DataFrame.from_dict(dictionary
            ,columns=['국어','영어','수학','사회']
        )
        ic(df)

# print(np.array(empty2))
print(dictionary)
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
        
  
    def content(self):
    ''' 
        