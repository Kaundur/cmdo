import os
import datetime

class Display:
    def __init__(self):
        self.display_width = 80
        # TODO - Later this should be pulled from the database

        self.title = ['Done', 'ID', 'Title', 'Date entered', 'Due']
        self.layout = ['complete', 'id', 'title', 'date', 'due']
        self.layout_format = {'id': {'length': 5},
                              'title': {'length': 20},
                              'complete': {'length': 10},
                              'date': {'length': 25},
                              'due': {'length': 50},
                       }

    def show_list(self, todo_list):
        if todo_list:

            for row in todo_list:
                print row
            # todo_list = self.format_list(todo_list)
            # self.print_header()
            #
            # for row in todo_list:
            #     self.print_row(row)
            #
            # print '-' * self.display_width


    def format_list(self):
        pass

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_welcome(self):
        print '_________          _________'
        print '__  ____/______ _________  /_____'
        print '_  /    __  __ `__ \  __  /_  __ \ '
        print '/ /___  _  / / / / / /_/ / / /_/ /'
        print '\____/  /_/ /_/ /_/\__,_/  \____/'
        print ''
        print 'Command List'
        print "\tShow list    --list   -l"
        print "\tAdd item     --add    -a"
        print "\tRemove item  --remove -r"
        print "\tMark done    --done   -d"
