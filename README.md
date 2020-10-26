# Тестовое задание для JetLend


Выполненое тестовое задание для компании JetLend.

## Модели

* Investor - описывает модель инвестора.
* Passport - описывает модель паспорта, имеет внешний ключ к модели Investor.
* Document - содержит внешний ключ к модели Investor, определяет квалифицирующий докумет.
* Qualification - объект модели создается при помощи post_save сигнала, сразу же после загрузки инвестором своих паспортых данных. Имеет 4 вида состояния, которые подразумевают выполение определенных действий (загрузка паспортных дынных, принятие условий, продолжение квалификации с/без загрузки подтверждающего документа. Cодержит внешний ключ к модели Investor.

## Конечные точки API

Все endpoints являются стандартыми, сгенерироваными DefaultRouter.

* api/investors/ - GET запрос отобразит список инвесторов/POST запрос создаст нового инвестора.
* api/investors/[id] - PUT запрос внесет изменения в объект/DELETE удалит.
* api/passports/
* api/passports/[id]
* api/documents/
* api/documents/[id]
* api/qualifications/
* api/qualifications/[id]


## Пример сценария

1. Создадим нового Инвестора:
   ````
   curl --location --request POST '127.0.0.1:8000/api/investors/' \
        --form 'first_name=Иванов' \
        --form 'last_name=Иван' \
        --form 'patponymic=Иванович'>
   ````
2. Загрузим паспортные данные:
	````
   curl --location --request POST '127.0.0.1:8000/api/passports/' \
		--form 'investor=1' \
		--form 'serial=5555' \
		--form 'number=555555' \
		--form 'date_of_birth=2020-01-01' \
		--form 'place_of_birth=Какой-то текст' \
		--form 'date_of_issue=2020-01-01' \
		--form 'issued_by=Какой-то текст' \
		--form 'code_subdivision=111' \
		--form 'registration_address=Какой-то текст' \
		--form 'screen_part1=@/home/dcontm/dev/111.png' \
		--form 'screen_part2=@/home/dcontm/dev/112.png'
   ````
3. Инвестор принимает условия:
	````
   curl --location --request PUT '127.0.0.1:8000/api/qualifications/1/' \
		--form 'state=ST2' \
		--form 'accept_rules=true' \
		--form 'investor=1'
   ````
4. Завершение квалификации без загрузки файла:
   ````
   curl --location --request PUT '127.0.0.1:8000/api/qualifications/1/' \
		--form 'state=ST3' \
		--form 'accept_rules=true' \
		--form 'investor=1'
   ````
