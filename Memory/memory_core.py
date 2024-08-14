""" For saving, managing, accessing and removing memories. Also contains `Memory` class."""
import json
from NLP.TextProcessing.Spelling_Checker import Autocorrect # For autocorrecting, to avoid same key - pair values
import sqlite3
from BaseClasses import User # For getting commands
from datetime import datetime
# -------------------------------------------------------------------------------------------------------------------------
conn = sqlite3.connect("Memory\\memory_data\\Database\\memory.db")
# -------------------------------------------------------------------------------------------------------------------------

memory_file = 'Memory/memory_data/memory.json'

class BaseMemory:
    """Memory class. All memories should be of this class."""
    def __init__(self, data:User.Command | str, database_code: int) :
        super().__init__()

        # Loading memory
        self.data = data
        self.db_code = database_code
        self.memory_tables = ["memory_unknown", "memory_personal", "memory_tasks", "memory_info"]
        self_db_base_memory = "memory_base"

        # Database:
        self.db_path = ''
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = conn.cursor()
        self.columns = ["value", "summary"]
        self.table = ''

        # Memory
        self.base_memory = "This will have a basic summarization of the command."
        self.memory_type = "unknown"

        self.memory_id = '' # FIXED FOR ALL TYPES
        self.current_datetime = datetime.now()
        self.memory_date = self.current_datetime.strftime("%Y-%m-%d") # FIXED FOR ALL TYPES
        self.memory_time = self.current_datetime.strftime("%H:%M:%S") # FIXED FOR ALL TYPES


    def create_memory_table(self, table_name, cols):
        
        column_def = ", ".join([f"{col} TEXT" for col in cols]) # Default to TEXT

        create_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, date VARCHAR(15), {column_def});"

        # Table does not exists:
        self.cursor.execute(create_query)

        print(f"Table created: {table_name}")
        print(f"Columns added: {cols}")

        self.conn.commit()

    def insert_memory_rows(self, table_name, columns, rows):
        """Add the values for an entire row in the table."""
        placeholders = ", ".join(["?" for _ in columns])
        insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"

        self.cursor.executemany(insert_query, rows)
        self.conn.commit()


    def convert_to_command(self):
        """Convert the given content to type `User.Command` of it is of type `str`."""

    def load_memory(self, memory_type):
        """Loads the memory based on `self.db_code`. Has to be initialized. """

    def save_memory(self):
        """Save the current state of memory to a database or other storage."""

    def update_memory(self):
        """	Update the existing memory data."""

    def process_memory(self):
        """Process the memory data."""

    def get_memory_type(self):
        """Return the type or class name of the memory."""

        # Use the getType() function from User.Command


class personal_memory(BaseMemory):
    """Memory class for personal memories."""
    def __init__(self, data:User.Command | str ,database_code: int, memory_id='', memory_date='', memory_time=''):
        super().__init__(data, database_code)
        self.details = []
        self.relation = None

class task_memory(BaseMemory):
    """Memory class for scheduling and executing tasks."""
    def __init__(self, data:User.Command | str ,database_code: int, memory_id='', memory_date='', memory_time=''):
        super().__init__(data, database_code)
        self.actions = []
        self.details = []

class info_memory(BaseMemory):
    """Memory class for information."""
    def __init__(self, data:User.Command | str ,database_code: int, memory_id='', memory_date='', memory_time=''):
        super().__init__(data, database_code)
        self.memory_type = "info"
        self.topics = []
        self.content = ""


class unknown_memory(BaseMemory):
    """Memories with unknown type."""
    def __init__(self, data:User.Command | str ,database_code: int):
        super().__init__(data, database_code)
        self.memory_type = "unknown"

    def change_memory_type(self, specialized_class):
        """Convert a memory into one of the specialized types."""
        if specialized_class not in [personal_memory, task_memory, info_memory]:
            print("Invalid memory type.")

            return None

        specialized_instance = specialized_class(self.data, self.db_code, self.memory_id, self.memory_date, self.memory_time)
        # Copying the relevant and permanent attributes:

        return specialized_instance


memory = unknown_memory(data = "Hello i am soumyajit", database_code = 1)
personal_mem = memory.change_memory_type(info_memory)

if personal_mem:
    print(f"Memory type: {type(memory), memory.memory_type} --> time: {memory.memory_time}\nMemory type: {type(personal_mem), personal_mem.memory_type} --> time: {personal_mem.memory_time}\n")


