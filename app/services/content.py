from matplotlib.cbook import flatten
import pandas as pd
import numpy as np
from icecream import ic
import random
import string
n = 5
random_str = ""
k = 10
empty = []

# for i in range(n):
#     (''.join(random_str += str(random.choice(string.ascii_letters)) for _ in range(k))
for x in range(k):
    empty.append(''.join(random.choice(string.ascii_letters) for _ in range(n)))     

random2 = np.array(np.concatenate(np.random.randint(10,100,size=(10,4))).tolist()).reshape(-1,4)
print(random2)

dictionary = dict(zip(empty,random2))
a = random.sample(range(0,100), 4)
class Content(object):
    def __init__(self) -> None:
        pass
    def make(self):
        ic(self.id())
        ic(self.score())[0]
        df4 = pd.DataFrame.from_dict({self.id():self.score()}, orient='index', columns=['국어', '영어', '수학', '사회'])
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
# print(np.array(empty2))
print(a)
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
        