"""Contains the all the models that are instance of the `BaseClasses.Assistant` class."""
from BaseClasses.Accounts import Assistant
import NLP.TextProcessing
import NLP.TextProcessing.Spelling_Checker
from NLP.TextProcessing.TP_Core import TextData

from Memory.memory_manager import gpt_v1_Memory
from BaseClasses.Assistant import gpt_generation

from colorama import Fore
from NLP.TextProcessing.Preprocessing import TextPreprocessor, PreprocessingStack, preprocessor_v1, preprocessor_v1_ner, preprocessor_v1_pos
# --------------------------------------------------------------------------------------------------------------------------------------
GPTv1 = Assistant(name = "GPTv1", model_type="Text",                        # Name and dexcription of the model
                  desc  = "Good at text generation", data_type=TextData,    # Type of the data it handles
                  memory_manager = gpt_v1_Memory,                           # Memory manager
                  processing_stacks = [preprocessor_v1_ner, preprocessor_v1_pos], 
                  processing_stacks_names = ["NER", "POS"],
                  output_instance = gpt_generation)                         # Output instance
# --------------------------------------------------------------------------------------------------------------------------------------

print(GPTv1.preprocessing_stacks)

print(GPTv1.active_processing_stack)
GPTv1.set_active_preprocessing_stack('POS')
print(GPTv1.active_processing_stack)

print()
print(GPTv1.process_user_input("Hllo, wher ar yu from??? I am fro India."))