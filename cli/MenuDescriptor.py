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
                    'Display Hotel Information'
    ]

    # 'Reserve a Room',
    # 'Cancel a Reservation'

    reservation_menu = [
        'Create a Reservation (Customer, Hotel)',
        'Cancel a Reservation'
    ]

    customer_fields = [ 'Full Name', 'E-mail', 'Phone']
    hotel_fields = ['Hotel Name', 'Address', 'E-mail', 'Phone']
