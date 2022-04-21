Проект «AMENIEL»

Описание: Сайт кофейни с дополнительными функциями администрирования для сотрудников и руководства. 
Для запуска проекта:
Выполните комманды:

docker-compose build

docker-compose run web python /usr/src/djangoProject/manage.py migrate

docker-compose run --rm djangoProject python manage.py createsuperuser

	- POSTGRES_USER=root
	- POSTGRES_PASSWORD=postgres
	
docker-compose up

Адрес проекта:
http://127.0.0.1:8000/

Нажмите по очереди:
Шаг 1
Шаг 2
Шаг 3
Шаг 4

Все готово к работе!!!
