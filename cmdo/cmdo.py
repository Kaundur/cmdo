import argparse

import dal
import display
import term


class TodoList:
    def __init__(self):

        self.parser = argparse.ArgumentParser(description='')

        self.dal = dal.DAL()

        self.display = display.Display()

        self.parser.add_argument('-add', help="Add a new item to Cmdo", type=str, nargs="+")

        self.parser.add_argument('-remove', help="Remove item", type=int)
        self.parser.add_argument('-done', help="Mark item as done", type=int)
        self.parser.add_argument('-undone', help="Mark item as not done", type=int)  # Revert done
        # should be 0 or 1 arg here
        self.parser.add_argument('-view', help="View list or view item", type=int, nargs='*')

        self.parser.add_argument('-description', help="Add description to item", nargs="*")
        self.parser.add_argument('-due', help="Add due date to item", nargs="*")

        self.parser.add_argument('-welcome', help="Display welcome message", action="store_true")

        self.parser.add_argument('-vacuum', help="Vacuum database ids", action="store_true")
        self.parser.add_argument('-debug', help="Dump database to screen", action="store_true")


        # TODO
        # self.parser.add_argument('--clean', help="")

        args = self.parser.parse_args()
        if self.check_arguments(args):
            self.handle_arguments(args)
        else:
            # If view is empty itll go here
            self.display_list()

        self.dal.close_connection()
        term.reset_terminal()
        return

    def check_arguments(self, args):
        any_arg_set = False
        for arg in vars(args):
            if getattr(args, arg):
                any_arg_set = True
                break
        return any_arg_set


    def handle_arguments(self, args):
        display_list = False
        # TODO - Display list is happening too many times here, it could be called multiple times depending on the operation
        if args.add:
            # TODO - Should handle description here as well
            self.dal.add_to_cmdo_list(args.add, args.due, args.description)
            display_list = True
        elif args.description:
            # Split the args into the id and description
            self.dal.add_description(args.description[0], args.description[1::])
        elif args.due:
            self.dal.add_due_date(args.due[0], args.due[1])

        if args.remove:
            self.dal.remove_by_id(args.remove)
            display_list = True

        if args.done:
            self.dal.mark_as_done(args.done)
            display_list = True
        if args.undone:
            self.dal.mark_as_undone(args.undone)
            display_list = True

        if args.debug:
            self.dal.dump_database()
        if args.vacuum:
            self.dal.vacuum_id()
            display_list = True

        if args.welcome:
            self.display.display_welcome()

        # TODO
        # if args.clean:
        #     self.dal.clean_database()
        if args.view:
            self.display_details(args.view[0])
        if display_list:
            self.display_list()

    def display_details(self, item_id):
        self.display.display_details(self.dal.get_item_description(item_id))

    def display_list(self):
        cmdo_list = self.dal.get_cmdo_list()
        self.display.show_list(cmdo_list)


def run_cmdo():
    TodoList()
