from typing import Any

class Inventory:
    def __init__(self, max_size:int=-1) -> None:
        self.max_size = max_size
        
        self.inventoryDict:dict[Any:int] = {}
        self.totalItemAmount:int = 0
        self.itemList:list[Any] = []
        
    def __getitem__(self, index) -> Any:
        return self.inventoryDict.get(index, 0)
    
    def __len__(self) -> int:
        return self.totalItemAmount
    
    def update(self) -> None:
        
        self.itemList = list(self.inventoryDict.keys())
            
        self.totalItemAmount = 0
        for key, value in self.inventoryDict.items():
            if value == 0:
                self.inventoryDict.pop(key)
            else:
                self.totalItemAmount += value
    
    def addItem(self, item:Any, amount:int=1) -> None:
            if self.max_size > 0 and self.totalItemAmount + amount <= self.max_size:
                if item in self.inventoryDict:
                    self.inventoryDict[item] += amount
                else:
                    self.inventoryDict[item] = amount
                self.update()
            else:
                raise OverflowError("Inventory does not have enough space.")

    
    def removeItem(self, item:Any, amount:int=1) -> None:
        if item in self.inventoryDict:
            if self.inventoryDict[item] >= amount:
                self.inventoryDict[item] -= amount
                self.update()
            else:
                raise ValueError("Not enough of that item in inventory.")
        else:
            raise ValueError("Item not in inventory.")
        
    def exist(self, item:Any) -> bool:
        return item in self.inventoryDict
