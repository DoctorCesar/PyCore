from dataclasses import dataclass
from typing import Any

@dataclass
class Table:
    rows: int
    columns: int
    default_value: Any

    def __post_init__(self):
        self.grid = [[self.default_value for _ in range(self.columns)] for _ in range(self.rows)]
        
    def __str__(self) -> str:
        result = ""
        maxlen = max(len(str(value)) for row in self.grid for value in row) + 2
        for row in self.grid:
            for value in row:
                result +="".join(f'{value: ^{maxlen}}')
            result += "\n"
        return result
    
    def __getitem__(self,index):
        row,col = index
        return self.grid[row][col]
            
    def __setitem__(self,index,value):
        row,col = index
        self.grid[row][col] = value
    
    def fill(self, value: Any = None):
        if value == None:
            value = self.default_value
        for row in self.grid:
            for i in range(self.columns):
                row[i] = value

    def sum(self):
        if isinstance(self.default_value, (int, float)):
            return sum(sum(row) for row in self.grid)
        else:
            raise ValueError("Sum is only possible with numeric value (int or float).")

    def copy(self):
        new_table = Table(self.rows, self.columns, self.default_value)
        for i in range(self.rows):
            for j in range(self.columns):
                new_table[i, j] = self[i, j]
        return new_table

    def is_empty(self):
        return all(all(value == self.default_value for value in row) for row in self.grid)