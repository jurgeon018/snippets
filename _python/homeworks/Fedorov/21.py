# Упражнение 21.1
# Разработайте программного бота, работающего по принципу клиент-серверного
# взаимодействия.
# 1. Идея бота: переводчик иностранных слов, бот-анекдотов и пр. (можно предлагать
# собственные идеи).
# 2. Разработайте систему команд для общения с ботом.
# 3. Реализацию необходимо построить с использованием шаблона MVC.
# 4. Оконный интерфейс tkinter.


# Упражнение 21.2
# Разработайте распределенную систему мониторинга удаленных хостов:
# Каждый хост (операционная система на выбор разработчика) содержит программу-
# агента, который собирает информацию о текущем состоянии системы, например,
# контроль запуска определенных служб (контролируемые службы выбираются на
# усмотрение разработчика, можно реализовать выбор службы для мониторинга через
# конфигурационный файл). Необходимо задействовать максимальные возможности Python
# для работы с операционными системами.
# На хосте производится сбор основных действий агента и результатов мониторинга
# (время, состояние и пр.). Через определенные интервалы времени агенты отправляют
# информацию на центральный сервер мониторинга. Сервер мониторинга опрашивает
# агентов, в ответ получает информацию о текущем состоянии системы. На сервере
# мониторинга производится логирование основных действий и результатов сбора
# информации (IP-адрес хоста, время и пр.). Итоговый результат сбора информации
# представляется в виде таблицы или (желательно) графика.
# При реализации системы необходимо задействовать возможности библиотек языка
# программирования Python (os, xmlrpclib и пр.). В качестве хранилища данных можно
# использовать текстовые файлы собственного формата, XML-формат, БД (MySQL, SQLite).


# Упражнение 21.3
# Разработайте веб-форму (HTML+PHP) для запроса имени пользователя и пароля из
# базы данных (MySQL). Пароль состоит из цифр от 1 до 5. Используются GET-запросы.
# При правильном вводе пароля веб-сервис направляет на страницу, которая содержит
# «секретную» текстовую строку или ссылку на файл, содержащий «секретную» текстовую
# строку.
# Написать скрипт на языке Python, который создает текстовый файл, содержащий
# словарь возможных паролей, и на основании созданного словаря перебирает пароли
# («перебор по словарю») веб-формы. В случае подбора правильного пароля программа
# считывает и выводит на экран «секретную» текстовую строку.
# Построить график зависимости длины пароля от времени перебора.
