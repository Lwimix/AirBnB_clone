#!/usr/bin/python3
""" This is the console module
It contains our console, which we use for remote
management and debugging
It contains HBNBCommand class which inherits from Cmd class
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ The HBNBCommand class
    It acts as our console
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ The EOF method
        Enables for smooth exiting (Ctrl+d)
        """
        return True

    def help_EOF(self):
        """ Helper for EOF
        Prints help for EOF
        """
        print("Exits console when Ctrl+d is hit")

    def postloop(self):
        """ The postloop method overridden
        Adds a newline after exiting (Ctrl+d)
        """
        print()

    def do_quit(self, line):
        """ The Quit method
        Exits program
        """
        sys.exit()

    def help_quit(self):
        """ Helper for quit
        Prints help instructions for quit
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """ The emptyline method overridden
        Deals with empty lines
        """
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
