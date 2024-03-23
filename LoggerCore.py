import colorama as cl
from time import strftime

cl.init(autoreset=True)

class Logger:
    def __init__(self,logLevel: int = 1, * ,showTime: bool = True, timeSyntax:str ="[%Y-%m-%d %H:%M:%S]",fileDirectory:str="", displayInConsole:bool=True) -> None:
        self.logLevel = logLevel
        self.showTime = showTime
        self.timeSyntax = timeSyntax
        self.fileDirectory = fileDirectory
        self.displayInConsole = displayInConsole

    def debug(self, msg: str):
        if self.showTime:
            currentTime = strftime(self.timeSyntax)
        else:
            currentTime = ""
        
        if self.fileDirectory and self.logLevel <= 1:
            with open(self.fileDirectory, "a") as f:
                f.write(f"[DBUG]{currentTime} -> {msg}\n")
        
        if self.displayInConsole and self.logLevel <= 1:
            print(f"{cl.Fore.LIGHTCYAN_EX}[DBUG]{currentTime} -> {msg}")

    def info(self, msg: str):
        if self.showTime:
            currentTime = strftime(self.timeSyntax)
        else:
            currentTime = ""

        if self.fileDirectory and self.logLevel <= 2:
            with open(self.fileDirectory, "a") as f:
                f.write(f"[INFO]{currentTime} -> {msg}\n")

        if self.displayInConsole and self.logLevel <= 2:
            print(f"{cl.Fore.LIGHTGREEN_EX}[INFO]{currentTime} -> {msg}")

    def warn(self, msg: str):
        if self.showTime:
            currentTime = strftime(self.timeSyntax)
        else:
            currentTime = ""

        if self.fileDirectory and self.logLevel <= 3:
            with open(self.fileDirectory, "a") as f:
                f.write(f"[WARN]{currentTime} -> {msg}\n")

        if self.displayInConsole and self.logLevel <= 3:
            print(f"{cl.Fore.YELLOW}[WARN]{currentTime} -> {msg}")

    def crit(self, msg: str):
        if self.showTime:
            currentTime = strftime(self.timeSyntax)
        else:
            currentTime = ""

        if self.fileDirectory and self.logLevel <= 4:
            with open(self.fileDirectory, "a") as f:
                f.write(f"[CRIT]{currentTime} -> {msg}\n")

        if self.displayInConsole and self.logLevel <= 4:
            print(f"{cl.Back.RED}{cl.Fore.BLACK}[CRIT]{currentTime} -> {msg}")

class MultiLogger:
    def __init__(self,*loggers):
        self.loggers = loggers
    
    def debug(self, msg: str):
        for logger in self.loggers:
            logger.debug(msg)
    
    def info(self, msg: str):
        for logger in self.loggers:
            logger.info(msg)
    
    def warn(self, msg: str):
        for logger in self.loggers:
            logger.warn(msg)
    
    def crit(self, msg: str):
        for logger in self.loggers:
            logger.crit(msg)