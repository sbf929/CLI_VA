"""For user authentificationm, login, and settings."""
from colorama import init, Style, Fore
init(autoreset=True)

import os
 # ----------------------------------------------------------------------------------------------------------------------------
# Connect to the SQLite database
import sqlite3
db_path = r'D:\\LearningTools\\Computer Tools\\DataScience_AI\\Python\\Practice_Projects\\Virtual_Assistant_CLI\\Memory\\memory_data\\Database\\users.db'
conn = sqlite3.connect(db_path)

if os.path.exists(db_path):
    print("Database found.")
else:
    print("Could not find database...")

print("Current working directory:", os.getcwd())
print("Database file path:", os.path.abspath('Virtual_Assistant_CLI\\Memory\\memory_data\\Database\\memory.db'))


print("Checking permissions for:", db_path)
print("Directory permissions:", oct(os.stat(db_path).st_mode))
print("File permissions:", oct(os.stat(db_path).st_mode))

# print(f"An error occurred ({e}). Couuldnot connect to database")
temp_db_path = r'D:\\LearningTools\\Computer Tools\\DataScience_AI\\Python\\Practice_Projects\\Virtual_Assistant_CLI\\Memory\\memory_data\\Database\\users.db'

# Path to your database
db_path = r'D:\LearningTools\Computer Tools\DataScience_AI\Python\Practice_Projects\Virtual_Assistant_CLI\Memory\memory_data\Database\users.db'

def test_connection(db_path):
    try:
        connection = sqlite3.connect(db_path)
        print("Database connection successful!")
        connection.close()
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
 # ----------------------------------------------------------------------------------------------------------------------------

class User():
    """Main User class."""

    def __init__(self):
        super(User). __init__()
        self.username = "User"
        self.password = None
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.name_color = Style.BRIGHT + Fore.GREEN
        self.style_reset = Style.RESET_ALL

        self.previlege = "None"

        # Authentify user:
        self.user_authentification()
    
    def user_authentification(self):
        print(self.username, self.password)

        check_for_username_query = "SELECT * FROM USERS WHERE username = ?"
        auth_query = "SELECT password FROM USERS WHERE username = ?"

        while (True):
            username_input = str(input("Enter you Username: "))
            print(self.conn)

            # Check if user exists:
            self.cursor.execute(check_for_username_query, (username_input,))
            result = self.cursor.fetchone()

            if result:
                print("Username found!")
                self.username = username_input

                while True:
                    # Perform authentification:
                    password_input = str(input("Enter the password: "))

                    self.cursor.execute(auth_query, (username_input,))
                    stored_password_result = self.cursor.fetchone()

                    if stored_password_result:
                        stored_password = stored_password_result[0]

                        if password_input == stored_password:
                            print(Fore.GREEN + "User verified.")

                            # Get the name for conversation marker:
                            self.get_username(username_input)

                            os.system('cls')
                            return

                        else:
                            print(Fore.RED + "Incorrect password.")
                
                    else:
                        print(Fore.LIGHTRED_EX + "Error fetching password.")
                        break

            else: 
                print("Username does not exist.")
                print(Fore.YELLOW + "Do you want to add user? (y/n)", end=" ")

                create = str(input()).strip().lower()

                # Create username:
                if create == "y":
                    print("Creating User.")
                    
                    # Take user details:
                    new_username = str(input(Fore.YELLOW + "Enter a username: " + Style.RESET_ALL))
                    new_pass = str(input(Fore.YELLOW + "Enter a password: " + Style.RESET_ALL))

                    self.add_user(new_username, new_pass)
                    print("User added.")

                elif create == "n":
                    print("Exiting...")
                    exit()


    def get_username(self, username):
        """Get the username from the User to use in the conversation."""
        name = str(input("Enter a username(Leave blank for defualt / -u for username): "))
        
        if name and name.strip() and not name and name.strip() == "-u":
            self.username = name

        elif name.strip() == "-u":
            print("Using username...")
            self.username = "Someone"

        else:
            print("Using Default name...")


    def add_user(self, username, password):
        """Adds a user."""

        query = "INSERT INTO USERS(username, password) VALUES (?, ?)"
        check_if_exists_query = "SELECT * FROM USERS WHERE username = ?"

        # Check if user already exists:
        self.cursor.execute(check_if_exists_query, (username,))
        found_user = self.cursor.fetchone()

        if found_user:
            print(f"Username - \"{username}\" already exists.")

        else:
            self.cursor.execute(query, (username, password))
            self.conn.commit()


    def conversation_marker(self):
        """Marks the conversation with the `username`."""
        marker = self.name_color + str(self.username) + ":" + self.style_reset
        return marker
    
    #def change_username():
    
 # ----------------------------------------------------------------------------------------------------------------------------

class Assistant():
    """##### Main assistant class.
    Parameters:
    * `name`: The name of the model. 
    * `model_type`: The type of model.
    * `desc`: Decription for the model.
    * `data_type`: Instance of the data type class that this model works with.
    * `memory_manager`: Instance of the `MemoryManager` class.
    * `processing_stacks`: List of instances of the `ProcessorStacks` class.
    * `processing_stacks_names`: List of the names for the processor_stacks. The length of both the lists should be the same.
    * `output_class`: `Assistant_Output` class instance for replying."""
    def __init__(self, name, model_type, desc, data_type,
                memory_manager, 
                processing_stacks:list, processing_stacks_names:list, 
                output_instance):
        super(). __init__()
        self.name = name

        self.name_color = Style.BRIGHT + Fore.CYAN
        self.style_reset = Style.RESET_ALL

        # User details:
        self.user_input = ''

        # Components:
        self.model_type = model_type # Type of model
        self.desc = desc # Description of the model
        self.data_type = data_type # Type of Data class being used for the model
        self.memory_manager = memory_manager # Instance of the MemoryManager class for this model
        self.output_class = output_instance # Instance of the Assistant_Output class used for this model

        # --- Preprocessing ---
        self.preprocessing_stacks = {} # For storing different processing stacks
        self.active_processing_stack = None # Active processing stack 
        # Initialize the preprocessing stacks:
        self.add_preprocessing_stacks(processing_stacks_names, processing_stacks)

    def description():
        """Returns the details of a `Assistant` instance."""

    def conversation_marker(self):
        """Marks the conversation with the `username`."""
        marker = self.name_color + str(self.name) + ":" + self.style_reset
        return marker
    

    def process_user_input(self, command):
        """Processes the user input using the active preprocessing stack."""
        if self.active_processing_stack is None:
            raise ValueError("No active preprocessing stack set.")
        
        processor = self.preprocessing_stacks.get(self.active_processing_stack)
        if processor is None:
            raise ValueError(f"Preprocessor stack '{self.active_processing_stack}' not found.")
        
        processed_text = processor.execute_processing_stack(command)
        return processed_text
    

    def add_preprocessing_stacks(self, stack_name_list, stack_list):
        """Create a preprocessing_stacks **dictionary** 
        with `processing_stacks_names` as keys and `processing_stacks` as values."""
        if len(stack_name_list) != len(stack_list):
            raise ValueError("The number of preprocessing stacks and the stack names should be the same.")
        
        for name, stack in zip(stack_name_list, stack_list):
            self.preprocessing_stacks[name] = stack
            print(f"Added --> `{name}`: {stack}")   

    def set_active_preprocessing_stack(self, stack_name):
        """Updates the active processing_stack as `stack_name` which will be used to preprocess the input."""
        if stack_name in self.preprocessing_stacks:
            self.active_processing_stack = stack_name
        else:
            raise ValueError("Preprocessor stack name is wrong.")


    def initialize_preprocessor(self):
        """Initialize the processor stack of the `TextPreprocessor` instance."""
        
    def initialize_context_processor(self):
        """"""
    
    def initialize_text_generator(self):
        """"""
    

    
import sqlite3

# Connect to the SQLite database
try:
    conn = sqlite3.connect('D:\\LearningTools\\Computer Tools\\DataScience_AI\\Python\\Practice_Projects\\Virtual_Assistant_CLI\\Memory\\memory_data\\Database\\commands.db')
    cursor = conn.cursor()
except sqlite3.Error as e:
    print(f"An error occurred ({e}). Could not connect to database")



# -------------------------------- Functions for SQL queries --------------------------------
def AddUser(username, password):
    """Adds details of user to the database."""

    query = "INSERT INTO USERS(name, password) VALUES (?, ?)"
    check_if_exists_query = "SELECT * FROM USERS WHERE name = ?"

    # Check if user already exists:
    cursor.execute(check_if_exists_query, (username,))
    found_user = cursor.fetchone

    if found_user:
        print(f"Username - \"{username}\" already exists.")

    else:
        cursor.execute(query, (username, password))

        conn.commit()

def LoadAllUsers():
    """Load the details of all the users in tha database."""


