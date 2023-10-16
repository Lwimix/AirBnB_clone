#!/usr/bin/python3
""" This is the console module
It contains our console, which we use for remote
management and debugging
It contains HBNBCommand class which inherits from Cmd class
"""
import json
import cmd
import sys
from models.base_model import BaseModel


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
        print()

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
        print()

    def emptyline(self):
        """ The emptyline method overridden
        Deals with empty lines
        """
        return

    def do_create(self, args):
        """ The create method
        It creates a new instance of BaseModel
        """
        my_args = args.split()
        try:
            if len(my_args) != 1:
                raise TypeError()
            if eval(my_args[0]):
                instance = BaseModel()
                instance.save()
                print(instance.id)
        except TypeError:
            if len(my_args) == 0:
                print('** class name missing **')
            else:
                pass
            return
        except NameError:
            print("** class doesn't exist **")
            return

    def help_create(self):
        """ Helper for create
        Prints help for create
        """
        print("Create a new instance of BaseModel")
        print()

    def do_show(self, args):
        """ The show method
        Prints the string rep of an instance based on the class name and id
        """
        my_args = args.split()
        try:
            if len(my_args) != 2:
                raise TypeError()
            model, mod_id = my_args
            with open("./file.json") as f:
                my_dict = json.load(f)
            for key, value in my_dict.items():
                if mod_id in key:
                    my_inst = BaseModel(**my_dict[key])
                    print(my_inst)
                    return
            print("** no instance found **")
        except TypeError:
            if len(my_args) == 0:
                print("** class name missing **")
            elif len(my_args) == 1:
                try:
                    if eval(my_args[0]):
                        pass
                except NameError:
                    print("** class doesn't exist **")
                    return
                print("** instance id missing **")
            else:
                pass
        except json.JSONDecodeError:
            return
        except FileNotFoundError:
            print("** no instance found **")

    def help_show(self):
        """ Helper for show
        Prints help for show
        """
        print("Prints string of instance using class name and id")
        print()

    def do_destroy(self, args):
        """ The destroy method
        Deletes an instance based on the class name and id
        """
        my_args = args.split()
        try:
            if len(my_args) != 2:
                raise TypeError()
            model, mod_id = my_args
            try:
                with open("./file.json", 'w') as f:
                    my_dict = json.load(f)
                for key, value in my_dict.items():
                    if mod_id in key:
                        del my_dict[key]
                        return
                print("** no instance found **")
            except json.JSONDecodeError:
                pass
        except TypeError:
            if len(my_args) == 0:
                print("** class name missing **")
            elif len(my_args) == 1:
                try:
                    if eval(my_args[0]):
                        pass
                except NameError:
                    print("** class doesn't exist **")
                    return
                print("** instance id missing **")

    def help_destroy(self):
        """ Helper for destroy
        Prints help for destroy
        """
        print("Delete instance using class name and id")
        print()

    def do_all(self, args):
        """ The all method
        Prints all string rep of all instances based/not on the class name
        """
        my_args = args.split()
        try:
            if len(my_args) != 1:
                raise TypeError()
            model = my_args[0]
            try:
                if eval(model):
                    with open('file.json', 'r') as f:
                        my_dict = json.load(f)
                    for key, value in my_dict.items():
                        if model in key:
                            my_inst = BaseModel(**my_dict[key])
                            print(str(my_inst))
            except NameError:
                print("** class doesn't exist **")
                return
        except TypeError:
            if len(my_args) == 0:
                try:
                    with open('file.json', 'r') as f:
                        my_dict = json.load(f)
                        my_inst = BaseModel(**my_dict)
                        print(str(my_inst))
                except json.JSONDecodeError:
                    pass
            else:
                pass
            return
        except json.JSONDecodeError:
            pass

    def help_all(self):
        """ Helper for all
        Prints help for all
        """
        print("Print all instances as strings")
        print()

    def do_update(self):
        """ The update method
        Updates instance based on class name & id by adding/updating attribute
        """
        my_args = args.split()
        try:
            if len(my_args) != 4:
                raise TypeError()
            model, mod_id, attrib, attrib_value = my_args
            try:
                if eval(my_args[0]):
                    pass
            except NameError:
                print("** class doesn't exist **")
                return
        except TypeError:
            if len(my_args) == 0:
                print("** class name missing **")
            elif len(my_args) == 1:
                print("** instance id missing **")
            elif len(my_args) == 2:
                print("** attribute name missing **")
            elif len(my_args) == 3:
                print("** value missing **")
            else:
                pass
            return

    def help_update(self):
        """ Helper for update
        Prints help for update
        """
        print("Update instance by adding/updating attributes")
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
