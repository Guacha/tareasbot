import datetime


class Console:

    def __init__(self, module_name: str,
                 debug: bool = True,
                 log: bool = True,
                 warnings: bool = True,
                 errors: bool = True):
        self.module = module_name
        self.show_debug = debug
        self.show_log = log
        self.show_warnings = warnings
        self.show_errors = errors

        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKCYAN = '\033[96m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

    def separator(self):
        print(
            f"{self.BOLD}========================================================================================"
            f"========================================================================================{self.ENDC}")

    def log(self, msg):
        now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        print(f"[{now}][LOG][{self.module}]: {msg}")

    def warn(self, msg):
        now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        print(f"{self.WARNING}[{now}][WARNING][{self.module}]: {msg}{self.ENDC}")

    def debug_log(self, msg):
        now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        print(f"{self.OKBLUE}[{now}][DEBUG][{self.module}]: {msg}{self.ENDC}")

    def err(self, msg, module="MAIN"):
        now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
        print(f"{self.FAIL}[{now}][WARNING][{module}]: {msg}{self.ENDC}")
