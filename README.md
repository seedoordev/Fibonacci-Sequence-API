### Описание API

Первый эндпоинт API на POST запрос принимает параметр, валидирует сериализатором и добавляет задачу в очередь.

А на GET запрос возвращает список задач, содержащий для каждой из них:

- текущий статус;
- дата и время начала задачи;
- дата и время ее завершения;
- время выполнения, которое должно быть вычисляемой дельтой в серилизаторе объекта, а не хранится в БД;
- параметр, с которым задача запускалась.

Второй эндпоинт, который по идентификатору задачи будет возвращать все то же, что и в списке, а так же результат задачи, если он имеется. В качестве результата в БД записывается полученный ряд чисел.

### Запуск

API упаковано в докер. Для запуска клонируйте себе удалённый репозиторий:

- `git clone https://github.com/seedoordev/Fibonacci-Sequence-API.git`

и в корневой папке проекта выполните команды:
- `docker-compose up -d --build`
- `docker-compose exec app python testtask/manage.py migrate --noinput`

### Документация

Для создания таска на рассчёт последовательности чисел необходимо перейти по url `http://127.0.0.1:8000/api/numbers/` и оптправить POST запрос с json следующего формата:
```
{
   "parameter": N
}
```
где N - уровень (положительное число), до которого надо выполнить расчет.
 
Для просмотра списка задач необходимо отправить GET запрос на тот же url.

Для просмотра конкретной задачи необходимо отправить GET запрос на url `http://127.0.0.1:8000/api/numbers/N`, где N - глубина задачи (и, по совместительству, её первичный ключ).