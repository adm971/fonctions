# setup.py
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"  

build_exe_options = {
    "packages": ["pygame", "random", "sys"],  
    "include_files": [] 
}

setup(
    name="Fonctions",
    version="1.0",
    description="Faire des fonctions",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)

# python setup.py build