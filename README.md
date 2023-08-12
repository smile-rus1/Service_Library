# Service_Library
---
### Стек приложения:
  * python 3.11
  * django 4.2.4
  * SQLite

### Для клонирования с репозитория
---
__git clone https://github.com/smile-rus1/Service_Library.git__
---
### Установка:
 * Создайте виртуальное окружение
  ---
  py -m venv env
  ---
* Далее активируйте его
  ---
  env\Scripts\activate
  ---
* После установите все зависимости:
  ---
  pip install -r requirements.txt
  ---
### Работа с системой
Для запуска проекта в корне проекта пропишите
---
* env\Scripts\activate
* cd config
* py manage.py runserver
---
###### После перейдите по ip 
127.0.0.1:8000

#### Для того чтобы добавлять книги в БД нужно войти в админ панель по url
---
http://127.0.0.1:8000/admin/
---
Далее в поля написать 
Имя пользователя -> admin
Пароль -> 11111111
#### Для того чтобы зайти как читатель нужно перейти по url
---
http://127.0.0.1:8000/login/
---
