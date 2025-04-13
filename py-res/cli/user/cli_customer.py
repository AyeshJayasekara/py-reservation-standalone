
from rich.prompt import Prompt

from cli.user.customer_decorator import CustomerDecorator
from rich.console import Console
from rich.table import Table
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError

class RoomValidator(Validator):
    def validate(self, document):
        try:
            room = int(document.text)


            if room < 2025 or room > 2027:
                raise ValidationError(
                    message='Please enter a valid room number',
                    cursor_position=len(document.text))  # Move cursor to end
        except ValueError:
            raise ValidationError(
                message='Please enter a valid room number',
                cursor_position=len(document.text))  # Move cursor to end

class YearValidator(Validator):
    def validate(self, document):
        try:
            year = int(document.text)
            if year < 2025 or year > 2027:
                raise ValidationError(
                    message='Please enter a valid year',
                    cursor_position=len(document.text))  # Move cursor to end
        except ValueError:
            raise ValidationError(
                message='Please enter a valid year',
                cursor_position=len(document.text))  # Move cursor to end

class MonthValidator(Validator):
    def validate(self, document):
        try:
            month = int(document.text)
            if month < 1 or month > 12:
                raise ValidationError(
                    message='Please enter a valid month ranging from 1 to 12',
                    cursor_position=len(document.text))  # Move cursor to end
        except ValueError:
            raise ValidationError(
                message='Please enter a valid month ranging from 1 to 12',
                cursor_position=len(document.text))  # Move cursor to end


class DayValidator(Validator):
    def validate(self, document):
        try:
            day = int(document.text)
            if day < 1 or day > 31:
                raise ValidationError(
                    message='Please enter a valid day ranging from 1 to 31',
                    cursor_position=len(document.text))  # Move cursor to end
        except ValueError:
            raise ValidationError(
                message='Please enter a valid month ranging from 1 to 31',
                cursor_position=len(document.text))  # Move cursor to end


class DecoratedCliCustomer(CustomerDecorator):

    def cli_view_rooms(self):

        records = self.view_rooms()

        table = Table(title="Rooms")

        rows = [[str(el) for el in row] for row in records]
        columns = ['Room ID', 'Room Type', 'Price']

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(*row, style='bright_green')

        console = Console()
        console.print(table)
        console.input("Press enter to continue...")

    def cli_check_availability(self):
        questions = [
            {
                'type': 'input',
                'name': 'check_in_year',
                'message': 'Check In Year:'
            },
            {
                'type': 'input',
                'name': 'check_in_month',
                'message': 'Check In Month:'
            },
            {
                'type': 'input',
                'name': 'check_in_day',
                'message': 'Check In Day:'
            },
            {
                'type': 'input',
                'name': 'check_out_year',
                'message': 'Check Out Year:'
            },
            {
                'type': 'input',
                'name': 'check_out_month',
                'message': 'Check Out Month:'
            },
            {
                'type': 'input',
                'name': 'check_out_day',
                'message': 'Check Out Day:'
            }

        ]
        answers = prompt(questions)
        records = self.check_availability(answers['check_in_year'], answers['check_in_month'], answers['check_in_day'],
                                          answers['check_out_year'], answers['check_out_month'],
                                          answers['check_out_day'])

        table = Table(title="Available Rooms")

        rows = [[str(el) for el in row] for row in records]
        columns = ['Room ID', 'Room Type', 'Price']

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(*row, style='bright_green')

        console = Console()
        console.print(table)
        response = int(Prompt.ask("Enter Room ID to confirm booking or 0 to exit >", default="0"))

        if response == 0:
            return
        else:
            self.book_room(response, answers['check_in_year'], answers['check_in_month'], answers['check_in_day'],
                           answers['check_out_year'], answers['check_out_month'], answers['check_out_day'])

    def cli_book_room(self):
        questions = [
            {
                'type': 'input',
                'name': 'room_id',
                'message': 'Room ID:',
                'validate': lambda val: self.valid_room(val)
            },
            {
                'type': 'input',
                'name': 'check_in_year',
                'message': 'Check In Year:',
                'validate': YearValidator
            },
            {
                'type': 'input',
                'name': 'check_in_month',
                'message': 'Check In Month:',
                'validate': MonthValidator
            },
            {
                'type': 'input',
                'name': 'check_in_day',
                'message': 'Check In Day:',
                'validate': DayValidator
            },
            {
                'type': 'input',
                'name': 'check_out_year',
                'message': 'Check Out Year:',
                'validate': YearValidator
            },
            {
                'type': 'input',
                'name': 'check_out_month',
                'message': 'Check Out Month:',
                'validate': MonthValidator
            },
            {
                'type': 'input',
                'name': 'check_out_day',
                'message': 'Check Out Day:',
                'validate': DayValidator
            }

        ]

        while True:
            answers = prompt(questions)
            records = self.check_availability(answers['check_in_year'], answers['check_in_month'],
                                              answers['check_in_day'],
                                              answers['check_out_year'], answers['check_out_month'],
                                              answers['check_out_day'])
            for record in records:
                if int(record[0]) == int(answers['room_id']):
                    self.book_room(answers['room_id'], answers['check_in_year'], answers['check_in_month'],
                                   answers['check_in_day'],
                                   answers['check_out_year'], answers['check_out_month'], answers['check_out_day'])
                    return
            console = Console()
            console.input("Room Not Available > Press enter to try again...")

    def cli_show_reservations(self):

        records = self.show_reservations()

        table = Table(title="My Reservations")

        rows = [[str(el) for el in row] for row in records]
        columns = ['Reservation ID', 'Room Type', 'Price Per Night', 'Check In Year', 'Check In Month', 'Check In Day',
                   'Check Out Year', 'Check Out Month', 'Check Out Day']

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(*row, style='bright_green')

        console = Console()
        console.print(table)
        console.input("Press enter to continue...")

    def cli_cancel_res(self):
        records = self.show_reservations()

        table = Table(title="My Reservations")

        rows = [[str(el) for el in row] for row in records]
        columns = ['Reservation ID', 'Room Type', 'Price Per Night', 'Check In Year', 'Check In Month', 'Check In Day',
                   'Check Out Year', 'Check Out Month', 'Check Out Day']

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(*row, style='bright_green')

        console = Console()
        console.print(table)
        response = int(Prompt.ask("Enter Reservation ID to cancel booking or 0 to exit >", default="0"))

        if response == 0:
            return
        else:
            self.cancel_booking(response)

    def valid_room(self, room: 0):

        rooms = self.view_rooms()
        is_valid = False
        for r in rooms:
            if int(r[0]) == int(room):
                is_valid = True
                break

        if not is_valid:
            raise ValidationError(
                message='Please enter a valid room number')
        return True

