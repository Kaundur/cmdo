#!/usr/bin/python
import sys
import argparse

import display
import dal


class TodoList:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='')

        self.dal = dal.DAL()

        self.display = display.Display()

        self.parser.add_argument('-l', '--list', help="", action="store_true")
        self.parser.add_argument('-a', '--add', help="", type=str)
        self.parser.add_argument('--due', help="", type=str)
        self.parser.add_argument('-r', '--remove', help="", type=int)
        self.parser.add_argument('-d', '--done', help="", type=int)
        self.parser.add_argument('-t', '--debug', help="",  action="store_true")
        args = self.parser.parse_args()

        if self.check_arguments(args):
            self.handle_arguments(args)
        else:
            self.display.display_welcome()

        self.dal.close_connection()

    def check_arguments(self, args):
        any_arg_set = False
        for arg in vars(args):
            if getattr(args, arg):
                any_arg_set = True
                break
        return any_arg_set


    def handle_arguments(self, args):

        if args.list:
            self.display_list()
        if args.add:
            due_date = None
            if args.due:
                due_date = args.due

            self.dal.add_to_cmdo_list(args.add, due_date)
        if args.remove:
            self.dal.remove_by_id(args.remove)
        if args.done:
            self.dal.mark_as_done(args.done)
            self.display_list()
        if args.debug:
            self.dal.dump_database()


    def display_list(self):
        cmdo_list = self.dal.get_cmdo_list()
        self.display.show_list(cmdo_list)

td_list = TodoList()


