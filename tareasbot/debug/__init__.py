import datetime

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


class Console:
    """Class that allows simple pretty printing to console for logging/Debugging purposes"""

    def __init__(self, module_name: str,
                 debug: bool = True,
                 log: bool = True,
                 warnings: bool = True,
                 errors: bool = True):
        """
        Constructor for a Console class object. Each module (Ideally) should have their own console object, such that
        each class has ease of use for pretty printing with module, and configuration for debug/warning/error level
        filtering
        Args:
            module_name (string): A String that represents the module that owns the console object
            debug (bool): Signal if the console should print debug messages. Default True
            log (bool): Signal if the console should print log messages. Default True
            warnings (bool): Signal if the console should print warning messages. Default True
            errors (bool): Signal if the console should print error messages. Default True
        """
        self.module = module_name
        self.show_debug = debug
        self.show_log = log
        self.show_warnings = warnings
        self.show_errors = errors

    @staticmethod
    def separator():
        """
        Function to print a console separator, useful if printing multiple log messages all at once and you need to
        split them
        """
        print(
            f"{BOLD}========================================================================================"
            f"========================================================================================{ENDC}")

    def log(self, msg: str):
        """
        Function to pretty print log messages to console. Log messages are messages to know of system-level function
        calls, Like database operations.
        Args:
            msg (str): The message to be printed
        """
        if self.show_log:
            now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
            print(f"[{now}][LOG][{self.module}]: {msg}")

    def warn(self, msg: str):
        """
        Function to pretty print warning messages to console. Warning messages are messages meant to convey programmer
        level details of missing/incomplete features in a system call or drawbacks of using a specific implementation

        Args:
            msg (str): The message to be pretty printed
        """
        if self.show_warnings:
            now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
            print(f"{WARNING}[{now}][WARNING][{self.module}]: {msg}{ENDC}")

    def debug_log(self, msg: str):
        """
        Function to pretty print debug messages to console. Debug messages are meant to let the dev know where the bot
        process is during any given operation, usually are more detailed and give useful techincal information as well

        Args:
            msg (str): The message to be pretty printed
        """
        if self.show_debug:
            now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
            print(f"{OKBLUE}[{now}][DEBUG][{self.module}]: {msg}{ENDC}")

    def err(self, msg: str):
        """
        Function to pretty print error messages to console. Error messages differ from exceptions in that they convey a
        non terminating errors during code logic or execution.
        Args:
            msg: The message to be pretty printed
        """
        if self.show_errors:
            now = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
            print(f"{FAIL}[{now}][WARNING][{self.module}]: {msg}{ENDC}")
