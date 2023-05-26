Поиск Автомобиля - это веб-приложение, которое позволяет пользователям искать ближайшие доступные автомобили для транспортировки. Оно предоставляет функции создания запросов на перевозку грузов, управления автомобилями и отслеживания статуса груза.

Возможности
Создание и управление запросами на перевозку грузов.
Добавление и обновление информации об автомобилях.
Расчет ближайших автомобилей для транспортировки груза.
Отслеживание статуса груза и просмотр расстояний до автомобилей.
Интеграция с API Google Maps для визуализации местоположения.
Используемые технологии
Django: Python веб-фреймворк для разработки бэкенда.
Django REST Framework: Набор инструментов для создания RESTful API.
PostgreSQL: Реляционная база данных для хранения данных.
Docker: Платформа контейнизации для удобного развертывания.

Начало работы
Эти инструкции помогут вам настроить проект Поиск Автомобиля на вашем локальном компьютере для разработки и тестирования.

Предварительные требования
Docker: Установите Docker Desktop в зависимости от вашей операционной системы.
Установка
Клонируйте репозиторий:

bash
Copy code
git clone <repository-url>
Перейдите в директорию проекта:

bash
Copy code
cd car_search
Соберите Docker образ и запустите контейнеры:

Copy code
docker-compose up
Дождитесь запуска контейнеров и доступности приложения.

Откройте веб-приложение Поиск Автомобиля в вашем браузере:

arduino
Copy code
http://localhost:8000
Использование
Зарегистрируйте новую учетную запись или войдите в существующую.
Создайте запросы на перевозку грузов, указав места загрузки и доставки, вес и описание.
Управляйте информацией об автомобилях, добавляйте, обновляйте или удаляйте данные об автомобилях.
Отслеживайте статус груза и просматривайте ближайши