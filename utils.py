# utils.py

from enum import Enum

class Color(Enum):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def print_colored(text, color: Color):
    print(f"{color.value}{text}{Color.RESET.value}")
