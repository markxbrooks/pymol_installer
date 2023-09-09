import __main__
from project import __version__, __program__
__main__.pymol_argv = [ 'pymol', '-q' ]
import pymol
pymol.finish_launching()
print(f"Welcome to {__program__}, version {__version__}!")
