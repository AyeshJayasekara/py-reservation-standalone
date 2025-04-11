class Room:
    def __init__(self, room_id: int, room_type: str = 'UNDEFINED', price: float = 'UNDEFINED',
                 quantity_available: int = 0):
        self.room_id = room_id
        self.room_type = room_type
        self.price = price
        self.quantity_available = quantity_available
