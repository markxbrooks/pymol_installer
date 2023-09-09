import os
import sys
from pathlib import Path
pyinstaller_cmd=r"pyinstaller.exe -w -i pymol.ico --paths=venv\Lib\site-packages --noupx --noconfirm -n biotoolkit-pymol --clean main.py"
os.system(pyinstaller_cmd)
inno_exe = r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe"
cwd = os.getcwd()
inno_input_file = os.path.join(cwd,"pymol.iss")
inno_cmd = rf'"{inno_exe}" {inno_input_file}'
print(inno_cmd)
os.system(inno_cmd)

