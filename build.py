import os
import sys
from pathlib import Path
from distutils.dir_util import copy_tree
from project import __version__, __program__
#sys.path.insert(0, os.path.abspath('.'))
# PYTHONPATH="C:\Evotec\env\Lib\site-packages"
# export PYTHONPATH
#
print(f"Welcome to {__program__} version " + __version__ + " build system")
destination_path_1 = f"dist\\pymol"
destination_path_2 = rf"build\\pymol"
rm_cmd = rf'rm -r "{destination_path_1}"'
#os.system(rm_cmd)
rm_cmd = rf'rm -r "{destination_path_2}"'
#os.system(rm_cmd)
pyinstaller_cmd=r"pyinstaller.exe -w -i pymol.ico --paths=venv\Lib\site-packages --noupx --noconfirm -n pymol --clean main.py"
os.system(pyinstaller_cmd)

dir_list = ["pymol"]
dest_dir = "dist/pymol" 
for directory in dir_list:
    for directory in dir_list:
        copy_tree(directory, dest_dir + r"/" + directory)

inno_exe = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
cwd = os.getcwd()
inno_input_file = os.path.join(cwd,"pymol.iss")
inno_cmd = rf'"{inno_exe}" {inno_input_file}'
print(inno_cmd)
#os.system(inno_cmd)

