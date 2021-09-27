import datetime
class Console():
    
    show_debug = True
    show_log = True
    show_warnings = True
    show_errors = True
    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    @staticmethod
    def separator():
        print(f"{Console.BOLD}==================================================================================================================={Console.ENDC}")
    
    @staticmethod
    def log(msg, module="MAIN"):
        now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        print(f"[{now}][LOG][{module}]: {msg}")
        
    @staticmethod
    def warn(msg, module="MAIN"):
        now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        print(f"{Console.WARNING}[{now}][WARNING][{module}]: {msg}{Console.ENDC}")
        
    @staticmethod
    def debug_log(msg, module="MAIN"):
        now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        print(f"{Console.OKBLUE}[{now}][DEBUG][{module}]: {msg}{Console.ENDC}")
        
    @staticmethod
    def err(msg, module="MAIN"):
        now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        print(f"{Console.FAIL}[{now}][WARNING][{module}]: {msg}{Console.ENDC}")