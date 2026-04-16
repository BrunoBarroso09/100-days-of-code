import subprocess
import os

class TerminalClear:
    @staticmethod
    def clear():
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)