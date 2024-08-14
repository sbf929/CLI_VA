"""Contains methods for creating, removing, manilupating, listing and other such methods for files and folders."""

import os
from pathlib import Path
import argparse

# ================================================== For file path ==================================================

def SearchFileOrFolder(start_dir, name:str) -> list:
    """Returns the all of the folder or file with `name` from `start_dir`."""
    results = [] # Initialize the results list



def GetPath(path_list: SearchFileOrFolder, n:int):
    """Returns the **path** at `n`th position in the `path_list`. Returns `None` if `path_list` is empty. 
    This is the base function to be used in every other function. This gives the Absosulte path, which can be properly used."""

    if len(path_list) > 0:
        # Check if file path exists:
        if path_list[n] exists:
            return path_list[n]
    
    else:
        return None

# ================================================== Details ==================================================
    
def GetFileSize(path:str = None):
    """Retrieves the size of the given file at the `path`."""
    

        
def FindAllFileWithExtension():

def FilePermission():

def GetDetails():

def LastModification():

# ================================================== Creating, Deleting and Manipulating files and folders ==================================================

def RenameFileOrFolder():
    """Renames the given path or `file`"""

def RemoveFileOrFolder():

def CreateFileOrFolder():

# ================================================== Manipulating Working Directory ==================================================

def GetCurrentDirectory():

def ChangeDirectory():

def ListItemsInDirectory():

def GetFileExtension():

# ================================================== Environment Variables ==================================================

def EnvironmentVariable():