"""Core logic of the `TextProccesing` module."""

#---------------------------------------------------------------------------------------------------
from NLP import Command_Type
from NLP.TextProcessing.Preprocessing import preprocessor_v1 # Get any processor
#---------------------------------------------------------------------------------------------------

class TextData():
    """Base class for all **text** data processing, storage and management. Main connection between the data and the user."""
    def __init__(self):
        super().__init__()
        self.preprocessor = preprocessor_v1


    def update_current_loaded_text():
        """Used to update the text data, when a new user command is given. 
        Updates the `self.current_loaded_text` in the proccessor instance."""
        
    