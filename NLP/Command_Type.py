""" Contains the base classes for the types of user input. 
Also contains function to check the type of command given by user. """

command_type = {'unknown': 0,
                'command line': 1,
                'conversation': 2, 
                'info': 3, 
                'task': 4}

class Unknown():
    """Unkown type of command. Has functions to extensively process this type, to get the real type of the command."""


class CMD():
    """Base class for executing 'os' commands."""

    def __init__(self) -> None:
        "C"
        
        
class Conversation():
    """Base class for normal conversation **(Chatbot)**."""

    def __init__(self, ) -> None:
        super().__init__()


class Information():
    """Base class for providing **Information**."""

class Task():
    """Base class for setting simple tasks."""


def set_command_type(existing_type, code: int):

    if code == 1:
        existing_type.type = CMD

    elif code == 2:
        existing_type.type = Conversation

    elif code == 3:
        existing_type.type = Information
    
    elif code == 4:
        existing_type.type = Task

    else:
        print("Invalid type.")
