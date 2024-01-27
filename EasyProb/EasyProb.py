import random
from typing import Any


class Ponderable:
    def __init__(self, ponderate_dict:dict[Any:int]) -> None:
        
        self.ponderate_dict = ponderate_dict
        
        self.ponderate_list = []
        for key,value in ponderate_dict.items():
            for _ in range(value): self.ponderate_list.append(key) 
    
        self.total = sum(ponderate_dict.values())
    
    def __eq__(self):
        return self.ponderate_dict == self.ponderate_dict
    
    def random(self):
        return random.choice(self.ponderate_list)
    
    def randomList(self,amount:int=1) -> list[Any]:
        toReturn = []
        for _ in range(amount): toReturn.append(random.choice(self.ponderate_list))
        return toReturn
    
    def randomDict(self,amount:int=1) -> dict[Any:int]:
        toReturn = {}
        for _ in range(amount):
            element = random.choice(self.ponderate_list)
            toReturn[element] = toReturn.get(element,0)+1
        return toReturn
    
    def probability(self):
        toReturn = {}
        for key, value in self.ponderate_dict.items():
            toReturn[key] = value/self.total
        return toReturn
    
    def size(self):
        return len(self.ponderate_list)


