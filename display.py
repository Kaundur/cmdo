import os
import datetime

import term


class Display:
    def __init__(self):
        self.display_width = 80
        # TODO - Later this should be pulled from the database

        self.layout = ['rowid', 'complete', 'title', 'due']
        self.layout_format = {'rowid': {'length': 5},
                              'title': {'length': 30},
                              'complete': {'length': 10},
                              'date': {'length': 25},
                              'due': {'length': 15},
                              'priority': {'length': 10},
                              'description': {'length': 40}
                       }

    def print_row(self, data):
        row = ''
        for layout in self.layout:
            if layout in self.layout_format and layout in data:
                value = data[layout]
                layout_format = self.layout_format[layout]
                layout_length = layout_format['length']
                # Truncate first, as color formatting counts towards char number
                value = self.format_value(value, layout)
                value = self.truncate_value(value, layout_length)
                value = self.color_value(value, layout)
                row += value
        print row

    def color_value(self, value, item):
        if item == 'due':
            if 'ago' in value:
                value = term.color(value, 'DANGER')
            elif 'Yesterday' in value:
                value = term.color(value, 'DANGER')
            elif 'Today' in value:
                value = term.color(value, 'WARNING')
            elif 'Tomorrow' in value:
                value = term.color(value, 'OK')
        return value

    def format_value(self, value, item):
        if item == 'complete':
            if value:
                value = '[x]'
            else:
                value = '[ ]'
        elif item == 'due':
            if value is not None:
                value = self.__get_date(value)
            else:
                value = ''
        return value

    def truncate_value(self, value, format_length):
        if len(str(value)) > format_length:
            value = (value[:format_length-3] + '...')
        return ('{:<' + str(format_length) + '}').format(value)

    def show_list(self, todo_list):
        self.clear_terminal()
        self.display_logo()
        if todo_list:
            for row in todo_list:
                self.print_row(row)
        else:
            self.display_welcome()


    def display_details(self, row):
        self.print_row(row)
        if row['description'] is not None and row['description'] != '':
            print "\t"+row['description']
        else:
            print "\tNo description added. Add a description using --description ID description"

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_welcome(self):
        print 'Command List'
        print "\tShow list    --list   -l"
        print "\tAdd item     --add    -a"
        print "\tRemove item  --remove -r"
        print "\tMark done    --done   -d"

    def display_logo(self):
        print '_________          _________'
        print '__  ____/______ _________  /_____'
        print '_  /    __  __ `__ \  __  /_  __ \ '
        print '/ /___  _  / / / / / /_/ / / /_/ /'
        print '\____/  /_/ /_/ /_/\__,_/  \____/'
        print ''

    def __get_date(self, date_string):
        # TODO - need to handle multiple formats of date
        item_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        today = datetime.date.today()

        delta = item_date.date() - today


        if delta.days < 0:
            if delta.days == -1:
                return 'Yesterday'
            return str(abs(delta.days)) + ' days ago'


        if item_date.date() == datetime.date.today():
            return 'Today'

        elif item_date.date() == datetime.date.today() + datetime.timedelta(days=1):
            return 'Tomorrow'
        else:
            # Check if the day is during the next few days, return day name if so
            for i in range(2, 7):
                if item_date.date() == datetime.date.today() + datetime.timedelta(days=i):
                    return item_date.date().strftime("%A")
        return date_string
