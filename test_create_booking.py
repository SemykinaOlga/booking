import pytest

import booking
import data
import helper


def test_success_create_book_with_three_symbol():
    # AAA = Arrange Act Assert
    # Arrange
    body = helper.get_body_creating_book('firstname', "aaa")

    # Act
    actual_status_code = booking.create_booking(body).status_code
    expected_status_code = 200

    # Assert
    assert actual_status_code == expected_status_code, \
        f"Неверный статус код. Ожидаем {expected_status_code}, получили {actual_status_code}"


@pytest.mark.parametrize("totalprice",
                         [
                             pytest.param(
                                 "12300000", id="1.1.1 Big amount"
                             ),
                             pytest.param(
                                 "1", id="1.1.2 Small amount"
                             ),
                             pytest.param(
                                 "0.001", id="1.1.3 Decimal amount"
                             ),
                         ]
                         )
def test_success_create_book_with_valid_total(totalprice):
    # AAA = Arrange Act Assert
    # Arrange
    body = helper.get_body_creating_book('totalprice', totalprice)

    # Act
    actual_status_code = booking.create_booking(body).status_code
    expected_status_code = 200

    # Assert
    assert actual_status_code == expected_status_code, \
        f"Неверный статус код. Ожидаем {expected_status_code}, получили {actual_status_code}"

def test_success_delete_status_code():
    # Arrange
    body = data.body_create_booking.copy()
    create_book_res = booking.create_booking(body)
    id = create_book_res.json()['bookingid']

    # Act
    actual_assert_code = booking.delete_booking(id).status_code
    expected_assert_code = 201

    # Assert
    assert actual_assert_code == expected_assert_code

