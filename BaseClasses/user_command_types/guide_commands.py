"""Contains the command to help and guide the user."""
from typing import Callable

class Help():
    def __init__(self):
        super(help).__init__()
        
        # Initialize the flags:
        self.help_tag = "--h"
        self.manual_tag = "--m"

    def command_help(self, function: Callable, tag):
        """Get help for a particular command (`function`)"""
        return function.__doc__
    
    def manual(tag):
        """Returns the entire manual."""


