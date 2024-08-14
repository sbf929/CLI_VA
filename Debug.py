import os
from pathlib import Path
from BASE.models import GPTv1
import inspect
from colorama import Fore

#print(GPTv1.input_preprocessor, GPTv1.preprocessing_methods)
#print(GPTv1.process_user_input("Hello, how are you?"))
input = "Hello, how are you?? Are you from America. I have to completee the project by 24 September."
print(Fore.RED + input)
print(Fore.GREEN + str(GPTv1.input_preprocessor.execute_processing_stack(input)))



exit()

def find_items(start_dir, name):
    results = []

    # Walk through the staring directory:
    for root, dirs, files in os.walk(start_dir):

        # If the given name is a directory
        if name in dirs:
            results.append((os.path.join(root, name)))
        # If the given name is a file
        if name in files:
            results.append((os.path.join(root, name)))

    return results


# Example usage
start_directory = 'D:\\'  # Starting from D:
dir_to_find = 'CS(Classes)'

print(find_items(start_directory, dir_to_find))



