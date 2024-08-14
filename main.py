""" This is a practice project for creating a Command Line Interface (CLI) Virtual Assistant."""
# Libraries:
from BaseClasses import Assistant, User
from BaseClasses import Accounts
from BASE.models import GPTv1
from NLP.TextProcessing.Preprocessing import preprocessor_v1_ner, preprocessor_v1_pos

from colorama import init, Fore, Style
# ------------------------------------------------------------------------------------------------------------------------
#### Load model and user:
#from BASE.models import 
# ------------------------------------------------------------------------------------------------------------------------

init(autoreset=True)

def main():
    """ Main function. Entry point for all other function. """
    exe = True
    
    # Create an instance of both classes:
    user_instance = Accounts.User()

    # Continously prompt user for input:
    while (exe):
        print(user_instance.conversation_marker(), end = " ")
        user_input = input()

        Command = User.convert_to_command(user_input) # Get the user input and convert to to Command type.

        # Give the command to the Assistant instance:
        GPTv1.user_input = Command.content
        GPTv1.output_class.create_reply('') # INitializing the output

        # Update the reply:
        #GPTv1.output_class.create_reply(GPTv1.execute_processing_stack(Command.content)) #GPTv1.process_user_input(Command.content)
        #print(assistant_instance.process_user_input())
        
        # Get the output:
        GPTv1.set_active_preprocessing_stack('NER')
        GPTv1.output_class.update_reply(f"NER preprocessing stack: {GPTv1.active_processing_stack} --> {GPTv1.process_user_input(Command.content)}\n")
        GPTv1.set_active_preprocessing_stack("POS")
        GPTv1.output_class.update_reply(f"POS preprocessing stack:{GPTv1.active_processing_stack} --> {GPTv1.process_user_input(Command.content)}\n")
        #GPTv1.output_class.update_reply(f"processing stack dict:{GPTv1.process_user_input(Command.content)}\n")

        output = GPTv1.output_class.Reply()

        print(GPTv1.conversation_marker(), end = " ")
        print(output, type(Command.content))

        if "exit" in user_input:
            content = "Have a great day..."
            print(GPTv1.conversation_marker(), end = " ")
            print("Have a great day")
            exe = False


if __name__ == "__main__":
    main()
    