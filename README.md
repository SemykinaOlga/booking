# Тесты на проверку сервиса booking.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest

https://restful-booker.herokuapp.com/apidoc/

спрашиваем, какие есть две проблемы в программировании? )
создаем функцию create booking

создаем переменную
печатаем статус код

создаем хелпер и функцию подмены в body
печатаем боди
печатаем статус код


загружаем pytest  pip install pytest


создаем тест без assert

вопрос, что проверяет наш тест?

создаем тест c asserT 
 assert actual_status_code == expected_status_code, \
        f"Неверный статус код. Ожидаем {expected_status_code}, получили {actual_status_code}"
		
запускаем через гуй, 
запускаем через терминал

	

паттерн автотестирования AAA Arrange Act Assert


параметризация
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

delete

создаем функцию  обнаруживаем что нужен токен
создаем data для хидер
создаем функцию для получения токена

копируем хидер с новым токеном



def delete_booking(id):
    headers = data.header_with_token.copy()
    headers["Cookie"] = 'token=' + get_token()
    return requests.delete(url=configuration.URL + configuration.DELETE + str(id), headers=headers)


def get_token():
    token = requests.post(url=configuration.URL + configuration.CREATE_TOKEN, json=data.user_body).json()["token"]
    return token
	
	


https://restful-booker.herokuapp.com/apidoc/


создаем README.md
оздаем .gitignore
создаем requirementes





