import pandas as pd
from icecream import ic
import numpy as np
a = np.random.randint(10,100,size=(1,3))[0]
b = np.random.randint(10,100,size=(1,3))[0]


class PandasRandom(object):
    def __init__(self) -> None:
        pass
    def create(self) -> None:
        df = pd.DataFrame.from_dict({'0':a,'1':b },
                               orient='index',columns=['0','1','2'])
        ic(df)

