import colorama as cl
from time import strftime

cl.init(autoreset=True)

class Logger:
    def __init__(self,
                logLevel: int = 1,
                *,showTime: bool = True,
                timeSyntax:str ="[%Y-%m-%d %H:%M:%S]",
                fileDirectory:str="",
                displayInConsole:bool=True,
                titleDict:dict={"debug":"[DBUG]","info":"[INFO]","warn":"[WARN]","crit":"[CRIT]"},
                colorDict:dict={"debug":cl.Fore.LIGHTCYAN_EX,"info":cl.Fore.LIGHTGREEN_EX,"warn":cl.Fore.YELLOW,"crit":cl.Back.RED + cl.Fore.BLACK}) -> None:
        
        self.logLevel = logLevel
        self.showTime = showTime
        self.timeSyntax = timeSyntax
        self.fileDirectory = fileDirectory
        self.displayInConsole = displayInConsole
        self.titleDict = titleDict
        self.colorDict = colorDict

    def debug(self, msg: str):
        if self.showTime:
            currentTime = strftime(self.timeSyntax)
        else:
            currentTime = ""
        
        if self.fileDirectory and self.logLevel <= 1:
            with open(self.fileDirectory, "a") as f:
                f.write(f"{self.titleDict["debug"]}{currentTime} -> {msg}\n")
        
        if self.displayInConsole and self.logLevel <= 1:
            print(f"{self.colorDict["debug"]}{self.titleDict["debug"]}{currentTime} -> {msg}")

    def info(self, msg: str):
        if self.showTime:
            currentTime = strftime(self.timeSyntax)
        else:
            currentTime = ""

        if self.fileDirectory and self.logLevel <= 2:
            with open(self.fileDirectory, "a") as f:
                f.write(f"{self.titleDict["info"]}{currentTime} -> {msg}\n")

        if self.displayInConsole and self.logLevel <= 2:
            print(f"{self.colorDict["info"]}{self.titleDict["info"]}{currentTime} -> {msg}")

    def warn(self, msg: str):
        if self.showTime:
            currentTime = strftime(self.timeSyntax)
        else:
            currentTime = ""

        if self.fileDirectory and self.logLevel <= 3:
            with open(self.fileDirectory, "a") as f:
                f.write(f"{self.titleDict["warn"]}{currentTime} -> {msg}\n")

        if self.displayInConsole and self.logLevel <= 3:
            print(f"{self.colorDict["warn"]}{self.titleDict["warn"]}{currentTime} -> {msg}")

    def crit(self, msg: str):
        if self.showTime:
            currentTime = strftime(self.timeSyntax)
        else:
            currentTime = ""

        if self.fileDirectory and self.logLevel <= 4:
            with open(self.fileDirectory, "a") as f:
                f.write(f"{self.titleDict["crit"]}{currentTime} -> {msg}\n")

        if self.displayInConsole and self.logLevel <= 4:
            print(f"{self.colorDict["crit"]}{self.titleDict["crit"]}{currentTime} -> {msg}")

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