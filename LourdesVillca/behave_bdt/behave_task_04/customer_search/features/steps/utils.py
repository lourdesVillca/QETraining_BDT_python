client_list = {1001: "Lourdes", 1002: 'Alvaro', 1003: 'Juana', 1004: 'Bruno'}
price_list = {1001: 45.6, 1002: 1300, 1003: 550.67, 1004: 340}


def get_client_id(client_name):
    for key, value in client_list.items():
        if value == client_name:
            return key

