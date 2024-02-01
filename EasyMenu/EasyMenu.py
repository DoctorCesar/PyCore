from typing import Any
import inquirer

class Menu:
    def __init__(self, message:str,*choices:Any) -> None:
        self.message = message
        for i in choices:
            if isinstance(i, SubMenu):
                i.commit(self)
        
        self.choices = choices
    
    def __call__(self) -> Any | None:
        
        choicesDict = {i.text : i for i in self.choices}
        
        question = [inquirer.List("menu",self.message,choices=[i.text for i in self.choices])]
        answer = choicesDict[inquirer.prompt(question)["menu"]]
        if isinstance(answer,SubMenu):
            return answer()
        elif isinstance(answer, Parent):
            return answer.parent_menu()
        elif isinstance(answer, Output):
            return answer.output_code
            

class SubMenu:
    def __init__(self, text:str, message:str, *choices:Any):
        self.text = text
        self.message = message
        
        for i in choices:
            if isinstance(i, SubMenu):
                i.commit(self)
        
        self.choices = list(choices)
        
    def commit(self, parent_menu):
        self.choices.insert(0, Parent(parent_menu))
        
    def __call__(self):
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
