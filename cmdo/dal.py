import sqlite3
import datetime
import os
import sys


class DAL:
    def __init__(self):
        self.database_name = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'cmdo.db')
        self.database_connection = sqlite3.connect(self.database_name)
        self.initalise_database()

    def initalise_database(self):
        self.create_main_table()

    def create_main_table(self):
        cursor = self.database_connection.cursor()

        cursor.execute('''CREATE TABLE if not exists todo_list
                      (date TIMESTAMP DEFAULT (datetime('now','localtime')),
                      title text,
                      priority int,
                      due DATE,
                      description text DEFAULT '',
                      complete BOOLEAN NOT NULL CHECK (complete IN (0, 1)) DEFAULT (0)
                      )''')
        self.database_connection.commit()

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_cmdo_list(self):
        self.database_connection.row_factory = self.dict_factory
        cursor = self.database_connection.cursor()
        cursor.execute("select rowid, * FROM todo_list")
        return cursor.fetchall()

    def _format_list(self, cmdo_list, format):
        # Formats the array into a dictionary, could this be built in?
        rows = []
        for sql_row in cmdo_list:
            row = {}
            for i, column in enumerate(format):
                row[column] = sql_row[i]
            rows.append(row)
        return rows

    def add_description(self, item_id, description):
        try:
            item_id = int(item_id)
            cursor = self.database_connection.cursor()
            description = ' '.join(description)

            cursor.execute("UPDATE todo_list SET description = ? WHERE rowid = ?", (description, item_id,))
            self.database_connection.commit()

        except ValueError:
            print('ID of item should be the first element supplied to description')

    def add_due_date(self, item_id, date_due):
        try:
            item_id = int(item_id)
            cursor = self.database_connection.cursor()
            date = self._get_date_from_string(date_due)
            cursor.execute("UPDATE todo_list SET due = ? WHERE rowid = ?", (date, item_id,))
            self.database_connection.commit()

        except ValueError:
            print('ID of item should be the first element supplied to due')
    # TODO
    # def clean_database(self):
    #
    #     # TODO - Archive everything marked as done
    #     # Should also accept ids, then only archive that item
    #     # Should prompt user on mass archive
    #     pass

    def get_item_description(self, rowid):
        self.database_connection.row_factory = self.dict_factory
        cursor = self.database_connection.cursor()
        cursor.execute("select rowid, * FROM todo_list WHERE rowid = ?", (rowid, ))
        # There can only be one
        return cursor.fetchone()

    def add_to_cmdo_list(self, message, due_date, description_elements, priority=0):
        message = ' '.join(message)
        cursor = self.database_connection.cursor()

        date = None
        if due_date:
            # Assume that the first element is the date if its passed in with the --add flag
            date = self._get_date_from_string(due_date[0])

        description = ''
        if description_elements:
            # If description is passed in with add ignore the id field. Assume that it isn't included
            description = ' '.join(description_elements)

        cursor.execute("INSERT INTO todo_list (title, priority, due, description) VALUES (?, ?, ?, ?)", (message, priority, date, description,))

        self.database_connection.commit()

    def _get_date_from_string(self, date_string):
        # item_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        today = datetime.date.today()

        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if date_string.lower() == 'today':
            return today
        if date_string.lower() == 'tomorrow':
            return today+datetime.timedelta(days=1)
        if date_string.lower() in days:
            for i in range(1, 8):
                next_day = today + datetime.timedelta(days=i)
                next_day_string = next_day.strftime("%A")
                if date_string.lower() == next_day_string.lower():
                    return next_day
        try:
            date = datetime.datetime.strptime(date_string, '%d-%b')
            date = date.replace(year=today.year)
            # If date is in the past, then add a year to put it in the future
            if date.date() - today:
                date = date.replace(year=today.year + 1)
            return date.strftime("%Y-%m-%d")
        except ValueError:
            pass
        try:
            date = datetime.datetime.strptime(date_string, '%d-%b-%Y')
            return date.strftime("%Y-%m-%d")
        except ValueError:
            pass
        # TODO - Should handle unknown date here

        return date_string

    def remove_by_id(self, item_id):
        cursor = self.database_connection.cursor()
        cursor.execute("DELETE FROM todo_list WHERE rowid = ?", (item_id,))
        self.database_connection.commit()

    def vacuum_id(self):
        self.database_connection.execute("VACUUM")

    def mark_as_done(self, item_id):
        cursor = self.database_connection.cursor()
        cursor.execute("UPDATE todo_list SET complete = 1 WHERE rowid = ?", (item_id,))
        self.database_connection.commit()

    def mark_as_undone(self, item_id):
        cursor = self.database_connection.cursor()
        cursor.execute("UPDATE todo_list SET complete = 0 WHERE rowid = ?", (item_id,))
        self.database_connection.commit()

    # For debug
    def dump_database(self):
        cursor = self.database_connection.cursor()
        cmdo_list = cursor.execute('SELECT * FROM todo_list')
        for row in cmdo_list:
            print(row)

    def close_connection(self):
        self.database_connection.close()

