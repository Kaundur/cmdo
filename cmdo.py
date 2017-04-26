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
        self.parser.add_argument('-r', '--remove', help="", type=str)
        args = self.parser.parse_args()
        self.handle_arguments(args)

        self.dal.close_connection()


    def handle_arguments(self, args):
        
        if args.list:
            cmdo_list = self.dal.get_cmdo_list()
            self.display.show_list(cmdo_list)

        if args.add:
            self.dal.add_to_cmdo_list(args.add)
        if args.remove:
            self.dal.remove_by_id(args.remove)

td_list = TodoList()


