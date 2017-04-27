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
        self.parser.add_argument('-r', '--remove', help="", type=int)
        self.parser.add_argument('-d', '--done', help="", type=int)
        args = self.parser.parse_args()
        self.handle_arguments(args)

        self.dal.close_connection()


    def handle_arguments(self, args):

        if args.list:
            self.display_list()
        if args.add:
            self.dal.add_to_cmdo_list(args.add)
        if args.remove:
            self.dal.remove_by_id(args.remove)
        if args.done:
            self.dal.mark_as_done(args.done)
            self.display_list()

    def display_list(self):
        cmdo_list = self.dal.get_cmdo_list()
        self.display.show_list(cmdo_list)

td_list = TodoList()


