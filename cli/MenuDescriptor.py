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

    reservation_menu = [
                    'Create Reservation',
                    'Display Reservation Information'
    ]

    customer_fields = [ 'Full Name', 'E-mail', 'Phone']
    hotel_fields = ['Hotel Name', 'Address', 'E-mail', 'Phone']
    reservation_fields = ['Room Number', 'Reservation Date']