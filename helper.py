import data


def get_body_creating_book(field, name):
    body = data.body_create_booking.copy()
    body[field] = name
    return body

