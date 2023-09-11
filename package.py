import os
import sys
# from biotoolkit.strutils import replace_text_in_new_file
# from biotoolkit.project import __version__
# from biotoolkit.config import BIOTOOLKIT_PATH
from pathlib import Path
from distutils.dir_util import copy_tree
inno_exe = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
cwd = os.getcwd()
inno_input_file = os.path.join(cwd,"pymol.iss")
inno_cmd = rf'"{inno_exe}" {inno_input_file}'
print(inno_cmd)
os.system(inno_cmd)

