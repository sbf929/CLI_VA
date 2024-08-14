# Virtual Assistant (CLI):

### 1. About the files:

`main.py`: Entry position for all the functions. This is the main running script.  
**`> BaseClasses`**:  
    |  
    |____`Accounts.py`:   
    |____`User.py`  
    |____`Assistant.py`:  
    |____`user_command.py`:   
    |____ **`> user_command_types`**:  
            |  
            |____`guide_commands.py`

**`> Basics`**:
**`> DL`**:
**`> Memory`**:
**`> NLP`**:
**`> OS`**:





### 2. Classes (custom made):
______
#### I. `BaseClasses`: Contain the base classes for the user and the virtual assistant.
1. `User`: Main user class for authentification, personalization, etc. Different instances of this class represent differnt users.
    * `Command`: All input given by the user has to be converted into this class. This class subclasses `str`. Instances of this class is used to language processing, memory storage and management, DL model training
    * `user_commands`: Class for the *flags* that can to used by the user to give commands explicitly. 

2. `Assistant`: Main class for Assistants. Different instances of this class represent differnt assistants who have different memories.
    * `Assistant_Output`: All replies given by the assistants should be of this class 

#### II. `NLP`: 

#### III. `Memory`: Module for Memory management.
1. `Memory`: All memories should be of this type. This class subclasses `str`.

