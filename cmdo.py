#!/usr/bin/python
import sys
import argparse

import display
import dal


class TodoList:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='')
        # args = self.parser.parse_args()

        self.dal = dal.DAL()

        self.display = display.Display()

        self.parser.add_argument("add", help="", type=str)
        args = self.parser.parse_args()
        print args.add
        #
        # parser = argparse.ArgumentParser()
        # parser.add_argument("square", help="display a square of a given number",
        #                     type=int)
        # args = parser.parse_args()
        # print args.square ** 2


        # self.handle_arguments()

        self.dal.close_connection()


    def handle_arguments(self, args):
        if len(args) == 2:
            if args[1] == "list":
                todo_list = self.dal.get_list()
                self.display.show_list(todo_list)
            # This shouldnt be a function, should be called on first run
            if args[1] == "createTable":
                self.dal.create_table()
        if len(args) == 3:
            if args[1] == "add":
                self.dal.add_to_list(args[2])

            if args[1] == "remove":
                self.dal.remove_by_id(args[2])



td_list = TodoList()


