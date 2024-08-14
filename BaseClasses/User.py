""" Contains the main class for command and other dependencies. """
# Reqired Modules:
from NLP import Command_Type
from BaseClasses import Accounts


class Command(str):
    """Main class for all commands given by the user. Any command given by the user should of this this class."""
    
    def __init__(self, command_text: str) -> None:
        super(Command, self).__init__()
        self.type = Command_Type.Unknown
        self.content = command_text
        self.username = 'conversation_marker'

    def mark_conversation(self):
        print(f"{self.username}:", end=" ")
        
    def get_command_type(self, types = Command_Type.command_type):
        """Required to get the type of comannd. For the types of command, check `Command_Type.py`."""

    def process_command(self):
        """Process the command to extract information."""

    def help():
        """Get help."""

    def set_type(self, type_code: int):
        """For setting the command type **explicitly** based on `type_code`."""

        Command_Type.set_command_type(self.type, type_code)




def convert_to_command(input: str) -> Command:
    """ Converts the input given by the user in `Command` type."""
    command = Command(input)

    return command
