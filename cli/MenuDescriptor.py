class MenuDescriptor:
    def __init__(self):
        pass

    root_menu = ['Customer','Hotel', 'Reservation']

    customer_menu = [
                    'Create Customer',
                    'Display Customer Information'
    ]

    hotel_menu = [
                    'Create Hotel',
                    'Delete Hotel',
                    'Display Hotel Information',
                    'Modify Hotel Information',
                    'Reserve a Room',
                    'Cancel a Reservation'
    ]

    reservation_menu = [
        'Create a Reservation(Customer, Hotel)',
        'Cancel a Reservation'
    ]

    customer_fields = [ 'Full Name', 'E-mail', 'Phone']