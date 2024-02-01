import os
from typing import Any
import inquirer

class Menu:
    def __init__(self, message:str,*choices:Any, clear:bool=True) -> None:
        self.message = message
        for i in choices:
            if isinstance(i, SubMenu):
                i.commit(self)
        
        self.choices = list(choices)
        self.clear = clear
    
    def __call__(self) -> Any | None:
        if self.clear:
            os.system('cls' if os.name == 'nt' else 'clear')
                        
        choicesDict = {i.text : i for i in self.choices}
        
        question = [inquirer.List("menu",self.message,choices=[i.text for i in self.choices])]
        answer = choicesDict[inquirer.prompt(question)["menu"]]
        print(f"Answer: {type(answer)}")
        if isinstance(answer,SubMenu):
            print("SubMenu")
            return answer()
        elif isinstance(answer, Parent):
            print("Parent")
            return answer.parent_menu()
        elif isinstance(answer, Output):
            print("Output")
            return answer.output_code
            

class SubMenu:
    def __init__(self, text:str, message:str, *choices:Any, clear:bool=True) -> None:
        self.text = text
        self.message = message
        
        for i in choices:
            if isinstance(i, SubMenu):
                i.commit(self)
        
        self.choices = list(choices)
        self.clear = clear
        
    def commit(self, parent_menu):
        self.choices.insert(0, Parent(parent_menu))
        
    def __call__(self):
        if self.clear:
            os.system('cls' if os.name == 'nt' else 'clear')
            
        choicesDict = {i.text : i for i in self.choices}
        
        question = [inquirer.List("menu",self.message,choices=[i.text for i in self.choices])]
        answer = choicesDict[inquirer.prompt(question)["menu"]]
        if isinstance(answer,SubMenu):
            return answer()
        elif isinstance(answer, Parent):
            return answer.parent_menu()
        elif isinstance(answer, Output):
            return answer.output_code

class Parent:
    def __init__(self, parent_menu:Menu|SubMenu):
        self.text = "<---"
        self.parent_menu = parent_menu


class Output:
    def __init__(self, text:str ,output_code:Any):
        self.text = text
        self.output_code = output_code
