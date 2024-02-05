import os

class Printer:
    def __init__(self, columns:int) -> None:
        self.columns = columns
    
    def __call__(self,*text) -> None:
        text = list(text)
        
        window_columns = os.get_terminal_size().columns - 1
        columns_size = window_columns // self.columns
        for i in range(len(text)):
            if len(text[i]) > columns_size:
                text[i] = text[i][:columns_size]
        
        
        for i in range(len(text)):
            print(*(str(text[i]).ljust(columns_size) for i in range(self.columns)))
