
from pathlib import Path

# Absolute path :: Ex : C:\Program Files\Microsoft

# Relative path :: Ex : Pycharm jeita dekte pari oida

# path = Path("ecommarce")
# print(path.exists())


# path = Path("eamils")
# print(path.mkdir())    # make directory = mkdir
# print(path.rmdir())   #rmdir = remove directory
"""
path = Path()
path.glob('*') # For all file search
path.glob('*.*') # For all file search
path.glob('*.py') # For all Python file search
path.glob('*.xls') # For all excel file search
"""

path = Path()
for file in path.glob('*.py'):
    print(file)
