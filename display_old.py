import os
import datetime
import termcolor


class Display:
    def __init__(self):
        self.display_width = 80
        # TODO - Later this should be pulled from the database
        #self.title = ['ID', 'Title', 'Details', 'Date']
        self.title = ['Done', 'ID', 'Title', 'Date entered', 'Due']
        #self.layout = ['id', 'title', 'details', 'date']
        self.layout = ['complete', 'id', 'title', 'date', 'due']
        self.layout_format = {'id': {'length': 5},
                              'title': {'length': 20},
                              #'details': {'length': 30},
                              'complete': {'length': 10},
                              'date': {'length': 25},
                              'due': {'length': 50},
                       }

        self.row_layout = self.generate_layout()

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

        # self.parser.add_argument('-l', '--list', help="", action="store_true")
        # self.parser.add_argument('-a', '--add', help="", type=str)
        # self.parser.add_argument('-r', '--remove', help="", type=int)
        # self.parser.add_argument('-d', '--done', help="", type=int)

        # TODO - Should list commands
        # TODO - should show that database was created

    def show_list(self, todo_list):
        if (todo_list):
            todo_list = self.format_list(todo_list)
            self.print_header()

            for row in todo_list:
                self.print_row(row)

            print '-' * self.display_width

    def print_header(self):
        self.clear_terminal()
        # print '='*self.display_width
        row = ''
        for i, row_item in enumerate(self.layout):

            value = self.title[i]
            row += self.row_layout[i].format(value)
        print row
        # print '=' * self.display_width

    def print_sub_header(self):
        pass
        # This should display the grouping
        # if there isnt any grouping, dont show this

    def print_row(self, data):
        row = ''
        for i, row_item in enumerate(self.layout):
            item_length = self.layout_format[row_item]['length']
            if row_item in data:
                value = data[row_item]
                if row_item == 'complete':
                    if value == 0:
                        value = '[ ]'
                    else:
                        value = '[x]'
                if row_item == 'due':

                    # print datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S.%f")
                    item_date = datetime.datetime.strptime(value, "%Y-%m-%d")

                    # print datetime.datetime.strptime(value, "%Y-%d-%m %H:%M:%S.%f")
                    if item_date.date() == datetime.date.today():
                        value = '<Today>'
                        # value = '<'+value+'>'
                        # value = termcolor.colored(value, 'red')
                        # # Seems to reset to green. could add a config to set this
                        # termcolor.RESET()

                else:
                    value = self.truncate_string(value, item_length)
            else:
                value = ''
            row += self.row_layout[i].format(value)
        print row

    def generate_layout(self):
        row_layout = []
        for layout_item_name in self.layout:
            item_length = self.layout_format[layout_item_name]['length']
            row_layout.append('{:<' + str(item_length) + '}')
        return row_layout


    def truncate_string(self, value, length):
        # print value, length
        if len(str(value)) > length:
            value = value[:length-3] + '...'
        return value


    def format_list(self, todo_list):
        # Format the return of the database into an array of dictionaries
        # TODO - Is there a better way of doing this?
        formatted_list = []
        for row in todo_list:
            # TODO - Is this really the best way of doing this
            # This means we need to link the format three times, seems really bad
            formatted_list.append({'id': row[0], 'date': row[1], 'title': row[2], 'complete': row[4], 'due': row[5]})
        return formatted_list

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
