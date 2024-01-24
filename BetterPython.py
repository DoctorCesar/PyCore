from colorama import Fore, Back, Style; import colorama
from typing import Any
import inspect
import secrets
import string
import time
import sys
import os


colorama.init()

def commonList(list1,list2,returnCommon=False) -> tuple[bool,list[int]] | tuple[bool,None]:
    common = []
    for position in list1:
        if position in list2:    
            if returnCommon:
                common.append(position)
            else:
                return(True)
    if returnCommon:
        if common != []:
            return(True,common)
        else:
            return(False,None)
    else:    
        return(False)

def clear() -> None:
    os.system('cls')

def write(text, delay=0.075,back=True) -> None:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if back:
        print()

def embed(text: str, fore:str="white", back:str="black") -> str:
    foreDict = {"red":Fore.RED,
                "green":Fore.GREEN,
                "yellow":Fore.YELLOW,
                "blue":Fore.BLUE,
                "magenta":Fore.MAGENTA,
                "cyan":Fore.CYAN,
                "white":Fore.WHITE,
                "black":Fore.BLACK,
                "lightred":Fore.LIGHTRED_EX,
                "lightgreen":Fore.LIGHTGREEN_EX,
                "lightyellow":Fore.LIGHTYELLOW_EX,
                "lightblue":Fore.LIGHTBLUE_EX,
                "lightmagenta":Fore.LIGHTMAGENTA_EX,
                "lightcyan":Fore.LIGHTCYAN_EX,
                "lightwhite":Fore.LIGHTWHITE_EX,
                "reset":Style.RESET_ALL}
    backDict = {"red":Back.RED,
                "green":Back.GREEN,
                "yellow":Back.YELLOW,
                "blue":Back.BLUE,
                "magenta":Back.MAGENTA,
                "cyan":Back.CYAN,
                "white":Back.WHITE,
                "black":Back.BLACK,
                "lightred":Back.LIGHTRED_EX,
                "lightgreen":Back.LIGHTGREEN_EX,
                "lightyellow":Back.LIGHTYELLOW_EX,
                "lightblue":Back.LIGHTBLUE_EX,
                "lightmagenta":Back.LIGHTMAGENTA_EX,
                "lightcyan":Back.LIGHTCYAN_EX,
                "lightwhite":Back.LIGHTWHITE_EX,
                "reset":Style.RESET_ALL}
    return(foreDict[fore] + backDict[back] + text + Style.RESET_ALL)

def prompt(type="str",text=">>>") -> str | int | float:
    while True:
        if type=="str":
            return(str(input(text)))
        if type=="int":
            try:
                return(int(input(text)))
            except:
                print(embed("Value must be an integer",Fore.RED))
        if type=="float":
            try:
                return(float(input(text)))
            except: 
                print(embed("Value must be a number", Fore.RED))

def password(length=8) -> str:
    char = string.ascii_letters + string.digits + string.punctuation + " "
    while True:
        password = ''.join(secrets.choice(char) for _ in range(length))
        password_list = list(password)
        if length >= 4:
            if (commonList(password_list,list(string.ascii_lowercase))
            and commonList(password_list,list(string.ascii_uppercase))
            and commonList(password_list,list(string.digits))
            and commonList(password_list,list(string.punctuation))):
                
                break
            else:
                break
    return(password)

def title(title :str) -> None:
    os.system(f'title {title}')

def windowSize(lenght,height) -> None:
    os.system(f'mode con: cols={lenght} lines={height}')

def getFunctionParameters() -> dict[str, Any]:
    calling_frame = inspect.currentframe().f_back
    name_parent_function = calling_frame.f_code.co_name
    parameters = inspect.signature(calling_frame.f_globals[name_parent_function]).parameters
    parameters_value = {name: calling_frame.f_locals[name] for name in parameters}
    return parameters_value

def pnumber(n,roundPrecision:int=3,valueLetter:dict={1000:'K',10**6:'M',10**9:'B',10**12:'T'}) -> str:
    if not (type(n) == float or type(n) == int):
        raise TypeError('Parameter should be a float or an integer')
    toReturn = ''
    for key,value in valueLetter.items():
        if n >= key:
            toReturn = f'{round(n/key,roundPrecision)}{value}'
        else:
            break
    return toReturn

def spaceship(val1:int|float, val2:int|float) -> int:
    if val1 == val2:
        return 0
    elif val1 > val2:
        return 1
    else:
        return -1

def spsh(val1:int|float, val2:int|float) -> int: # Alias for spaceship
    return spaceship(val1,val2)

class ToPrintClass:
    def __init__(self,text:Any) -> None:
        self.text = str(text)
    
    def __str__(self) -> str:
        return self.text
    
    def get(self) -> Any:
        return self.text
    
    def set(self,value) -> None:
        self.text = value

    def add(self, value) -> None:
        self.text += value

    def c(self) -> None:
        print(self.text)
    
    def commit(self) -> None:
        print(self.text)

toPrint = ToPrintClass("")


if __name__ == '__main__':
    write("Hello there !")
    time.sleep(1)
    clear()

    write(embed("This is a python module, it can't work alone. You must import it in your python project. To do this add: ",
                Fore.RED),0.05)
    write(embed("from BetterPython import * ",Fore.CYAN),0.05)
    write(embed("or ",Fore.RED),0.05)
    write(embed("import BetterPython",Fore.CYAN),0.05)
    write(embed("at the begging of your python file",Fore.RED),0.05)

    print()

    write(embed("This window will close after 5 seconds"), 0.05)
    print()
    write(".....",1)

    exit()