import sys
import __main__
from PyQt5.uic import *
from pmg_qt import *
from project import __version__, __program__
#__main__.pymol_argv = [ 'pymol', '-q', sys.argv ]
#print("Argument List:",
#       str(sys.argv))
import pymol
print(f"Welcome to {__program__}, version {__version__}!")
sys.exit(pymol.launch())
#pymol.finish_launching()
