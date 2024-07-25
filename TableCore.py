from typing import Any, Self

class Table:
    def __init__(self,rows:int,columns:int, default_value) -> None:
        self.rows = rows
        self.columns = columns
        self.default_value = default_value
        
        self.grid = [[default_value for _ in range(rows)] for _ in range(columns)]
        
        self.iter_index = 0
        
    def __str__(self) -> str:
        toReturn = ""
        max_len = max(len(str(value)) for row in self.grid for value in row)
        for row in self.grid:
            for value in row:
                toReturn += str(value).center(max_len+1)
            toReturn += "\n"
        return toReturn

    def __getitem__(self,index)-> Any:
        row, col = index
        return self.grid[row][col]
    
    def __setitem__(self,index,value) -> None:
        row, col = index
        self.grid[row][col] = value
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Table):
            return self.grid == other.grid
        else:
            return False
    
    def __iter__(self) -> Self:
        return self
    
    def __next__(self) -> Any:
        if self.iter_index < self.rows * self.columns:
            row = self.iter_index // self.columns
            col = self.iter_index % self.columns
            self.iter_index += 1
            return self[row, col]
        else:
            raise StopIteration
    
    def fill(self, value:Any=None) -> None:
        if value == None:
            value = self.default_value
        for row in self.grid:
            for i in range(len(self.row)):
                row[i] = value
    
    def sum(self) -> int | float:
        if isinstance(self.default_value, (int, float)):
            return sum(sum(row) for row in self.grid)
        else:
            raise ValueError("Sum is only possible with numeric value (int or float).")
    
    def copy(self) -> Self:
        copied_table = Table(self.rows, self.columns, self.default_value)
        for i in range(self.rows):
            for j in range(self.columns):
                copied_table[i, j] = self[i, j]
        return copied_table
    
    def is_empty(self) -> bool:
        return all(all(value == self.default_value for value in row) for row in self.grid)