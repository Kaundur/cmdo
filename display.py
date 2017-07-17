import os
import datetime

class Display:
    def __init__(self):
        self.display_width = 80
        # TODO - Later this should be pulled from the database

        # self.title = ['ID', 'Done' 'Title', 'Date entered', 'Due']
        self.layout = ['rowid', 'complete', 'priority', 'title', 'due', 'date']
        self.layout_format = {'rowid': {'length': 5},
                              'title': {'length': 20},
                              'complete': {'length': 10},
                              'date': {'length': 25},
                              'due': {'length': 50},
                              'priority': {'length': 10}
                       }

    def print_row(self, data):
        row = ''
        for layout in self.layout:
            if layout in self.layout_format and layout in data:
                value = data[layout]
                layout_format = self.layout_format[layout]
                layout_length = layout_format['length']
                value = self.format_value(value, layout)
                row += self.truncate_value(value, layout_length)
        print row

    def format_value(self, value, item):
        if item == 'complete':
            if value:
                value = '[x]'
            else:
                value = '[ ]'
        return value

    def truncate_value(self, value, format_length):
        return ('{:<' + str(format_length) + '}').format(value)

    def show_list(self, todo_list):
        if todo_list:
            for row in todo_list:
                self.print_row(row)

        else:
            pass
            # TODO - Display empty message

            # todo_list = self.format_list(todo_list)
            # self.print_header()
            #
            # for row in todo_list:
            #     self.print_row(row)
            #
            # print '-' * self.display_width



    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_welcome(self):
        self.clear_terminal()
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
