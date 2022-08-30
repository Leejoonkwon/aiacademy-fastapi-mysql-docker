from dataclasses import dataclass
@dataclass
class Context:
    path: str
    fname:str
    train:object
    test:object
    id:str
    label:str
    
    @property
    def path(self) -> str: return self._path
    
    @path.setter
    def path(self,path):self._path = path
    
    @property
    def fname(self) -> str: return self.fname
    
    @fname.setter
    def fname(self,fname):self.fname = fname
    
    @property
    def train(self) -> object : return self.train
    
    @train.setter
    def train(self,train):self.train = train
    
    @property
    def test(self) -> object : return self.test
    
    @test.setter
    def test(self,test):self.test = test
    
    @property
    def id(self) -> str : return self.id
    
    @id.setter
    def id(self,id) :self.id = id
    
    @property
    def label(self) -> str : return self.label
    
    @label.setter
    def label(self,label): self.label = label




