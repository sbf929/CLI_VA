"""Main memory manager."""
from BaseClasses import User

from Memory import memory_core
from Memory import memory_processor

class MemoryManager():
    """Manages all the the interaction with memory."""
    def __init__(self):
        self.command = 'Some command by the user.'
        self.memory_processors = [] # Processors used for processing the memory.
        self.memory = None # Instance of one of the memory types from `memory_core`

    def ScanMemory():
        """Scans the entire given database."""

    def get_new_memory(self, command):
        """Updates the `self.command` attribute."""
        self.command = command

    def StoreMemory(self, memory):
        """Entrypoint for all memories."""
        stored_memory = memory_core.unknown_memory(self.command, 0)
        return stored_memory
    

gpt_v1_Memory = MemoryManager()