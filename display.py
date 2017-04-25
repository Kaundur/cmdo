
class Display:
    def __init__(self):
        self.display_width = 80
        # TODO - Later this should be pulled from the database
        self.title = ['ID', 'Title', 'Details', 'Date']
        self.layout = ['id', 'title', 'details', 'date']
        self.layout_format = {'id': {'length': 5},
                              'title': {'length': 20},
                              'details': {'length': 30},
                              'date': {'length': 25},
                       }

        self.row_layout = self.generate_layout()


    def show_list(self, todo_list):

        if (todo_list):
            todo_list = self.format_list(todo_list)
            self.print_header()

            for row in todo_list:
                self.print_row(row)

            print '-' * self.display_width

    def print_header(self):

        print '='*self.display_width
        row = ''
        for i, row_item in enumerate(self.layout):
            value = self.title[i]
            row += self.row_layout[i].format(value)
        print row
        print '=' * self.display_width

    def print_row(self, data):
        row = ''
        for i, row_item in enumerate(self.layout):
            # print data
            item_length = self.layout_format[row_item]['length']
            if row_item in data:
                value = self.truncate_string(data[row_item], item_length)
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
        # TODO - Should be moved to outside the dal
        # Format the return of the database into an array of dictionaries
        formatted_list = []
        for row in todo_list:
            formatted_list.append({'id': row[0], 'date': row[1], 'title': row[2]})
        return formatted_list