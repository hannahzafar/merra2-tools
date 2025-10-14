# Main access functions
from .config import MERRA2_ROOT
from .query import print_val_and_type
from .query import find_MERRA2_files
# from .virtualizarr import #FIX: add relevant functions here and below

# What is imported with "from merra2_tools import *"
__all__ = [
    'MERRA2_ROOT',
    'find_MERRA2_files',
    'print_val_and_type'
]
