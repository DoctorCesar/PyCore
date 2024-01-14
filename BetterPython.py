import os
import sys
import time
import string
import secrets
import inspect
from colorama import init, Fore, Back, Style


init()

def commonList(list1,list2,returnCommon=False):
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

def clear():
    os.system('cls')

def write(text, delay=0.075,back=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if back:
        print()

def embed(text: str, fore=Fore.WHITE, back=Back.BLACK):
    colorDict = {"red":Fore.RED,
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
    return(colorDict[fore] + colorDict[back] + text + Style.RESET_ALL)

def prompt(type="str",text=">>>"):
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

def password(length=8):
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

def title(title :str):
    os.system(f'title {title}')

def windowSize(lenght,height):
    os.system(f'mode con: cols={lenght} lines={height}')

def getFunctionParameters():
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