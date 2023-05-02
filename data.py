body_create_booking = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 500,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2023-05-01",
        "checkout": "2023-12-01"
    },
    "additionalneeds": "Breakfast"
}

user_body = {
    "username": "admin",
    "password": "password123"
}

header_with_token = {
    "Cookie": "token"
}
