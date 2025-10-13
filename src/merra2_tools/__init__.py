# Main access functions
from .query import find_MERRA2_files
# from .virtualizarr import #FIX: add relevant functions here and below

# What is imported with "from merra2_tools import *"
__all__ = [
    'find_MERRA2_files',
]
