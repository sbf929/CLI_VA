"""Contains `MemoryProcessor` class that can be used to create memory processor."""
from NLP.TextProcessing.Spelling_Checker import Autocorrect
#from NLP.TextProcessing.Summary import 
import spacy
mlp = spacy.load("en_core_web_sm")

class MemoryProcessor():
    """Uses different available models to process memory."""
    def __init__(self, *args, **kwargs):
        self.args = list(args)


    def memory_processor_stack(self,input):
        """Processing stack based on the given processors (`*args`)."""
        for processor in self.args:
            input = processor(input)

        return input


text_memory_processor = MemoryProcessor(Autocorrect)

print(text_memory_processor.memory_processor_stack("cn you hlp me out?"))