from cli.user.admin_decorator import AdminDecorator
from PyInquirer import prompt
from rich.console import Console
from rich.table import Table

from core.reservation.booking import Booking
from core.reservation.room import Room


class DecoratedCliAdmin(AdminDecorator):

    def cli_add_room(self):
        while (True):

            questions = [
                {
                    'type': 'input',
                    'name': 'room_id',
                    'message': 'Room ID:'
                },
                {
                    'type': 'list',
                    'name': 'room_type',
                    'message': 'Room Type:',
                    'choices': ['Single', 'Double', 'Suite'],
                    'filter': lambda val: val.upper()
                },
                {
                    'type': 'input',
                    'name': 'price',
                    'message': 'Price:'
                }

            ]
            answers = prompt(questions)
            room = Room(answers['room_id'], answers['room_type'], answers['price'])
            if self.add_room(room):
                return True
            else:
                questions = [
                    {
                        'type': 'confirm',
                        'message': 'Room already exists, Try again? ',
                        'name': 'confirm',
                        'default': True,
                    },
                ]

                answer = prompt(questions)

                if not answer['confirm']:
                    return False

    def cli_remove_room(self):
        questions = [
            {
                'type': 'input',
                'name': 'room_id',
                'message': 'Remove Room with ID:'
            }
        ]
        answer = prompt(questions)
        room_id = answer['room_id']
        questions = [
            {
                'type': 'confirm',
                'message': 'Do you want to remove room ' + room_id,
                'name': 'confirm',
                'default': False,
            },
        ]

        answer = prompt(questions)

        if answer['confirm']:

            self.remove_room(Room(room_id, '', 0))
        else:
            return

    def cli_edit_room(self):
        questions = [
            {
                'type': 'input',
                'name': 'room_id',
                'message': 'Room ID:'
            },
            {
                'type': 'list',
                'name': 'room_type',
                'message': 'Room Type:',
                'choices': ['Single', 'Double', 'Suite'],
                'filter': lambda val: val.upper()
            },
            {
                'type': 'input',
                'name': 'price',
                'message': 'Price:'
            }
        ]
        answers = prompt(questions)
        room = Room(answers['room_id'], answers['room_type'], answers['price'])
        self.edit_room(room)

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

    def cli_view_bookings(self):
        records = self.view_bookings()

        table = Table(title="Reservations")

        rows = [[str(el) for el in row] for row in records]
        columns = ['Reservation ID', 'Room ID', 'Email', 'Room Type', 'Price Per Night', 'Check In', 'Check Out']

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(*row, style='bright_green')

        console = Console()
        console.print(table)
        console.input("Press enter to continue...")

    def cli_delete_booking(self):
        questions = [
            {
                'type': 'input',
                'name': 'reservation_id',
                'message': 'Remove Reservation with ID:'
            }
        ]
        answer = prompt(questions)
        res_id = answer['reservation_id']
        questions = [
            {
                'type': 'confirm',
                'message': 'Do you want to Reservation ' + res_id,
                'name': 'confirm',
                'default': False,
            },
        ]

        answer = prompt(questions)

        if answer['confirm']:
            booking = Booking(res_id, '', '', '',
                              '', '', '', '', '')
            self.delete_booking(booking)
        else:
            return
