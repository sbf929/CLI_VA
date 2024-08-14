"""Contains the base classes for the Virtual Assistant."""
from BaseClasses import User, Accounts

class Assistant_Output():

    def __init__(self) -> None:
        self.user = ''
        self.user_command = ''
        self.reply = 'This is a reply' # This variable will be given as output. Use the other classes to manipulate this

    def error():
        """Gives the details of an error occurrance."""

    def Reply(self):
        """Returns the entire reply content."""
        return self.reply
    
    def create_reply(self, content):
        """Creates a reply. (Reassigning the `reply` attribute.)"""
        self.reply = content
    
    def update_reply(self, content):
        """Update the `reply` attributes`. Only adds the given `content` to it."""
        self.reply = self.reply + content





gpt_generation = Assistant_Output()
