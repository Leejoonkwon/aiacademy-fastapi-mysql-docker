import numpy as np
class Classifier(object):
    def __init__(self,name,score1,score2,score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    def name(self):
        return self.name
    def score(self):
        return np.mean(self.score1 + self.score2 + self.score3)
 
        
    
    
 
    
    
