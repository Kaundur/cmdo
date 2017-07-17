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

    def print_row(self, data):
        row = ''
        for layout in self.layout:
            if layout in self.layout_format and layout in data:
                value = data[layout]
                layout_format = self.layout_format[layout]
                layout_length = layout_format['length']
                # item_length = self.layout_format[layout_format]['length']
                # row_layout.append('{:<' + str(item_length) + '}')
                row += ('{:<'+str(layout_length)+'}').format(value)
        print row


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
