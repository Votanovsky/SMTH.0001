# SMTH.0001 — проект Drames Studio™

### Тут я буду писать TODOs и также оставлю инструкцию
---

### Инструкция по установке зависимостей:

#### venv
Для того, чтобы рабочая среда твоего компьютера не засорялась лишними пакетами, лучше использовать виртуальную среду. Для этого:
1. скачай python3 по [этой ссылке](https://www.python.org/downloads/release/python-3100/);
2. находясь в корневом каталоге проекта, пропиши в терминале команду: `virtualenv venv`;
4. после успешного завершения процесса смени активный профиль терминала на (venv) с помощью команды: ``
3. посмотри файл **_dependencies.txt_**, там собраны все пакеты, которые нужно скачать; устанавливаются они командой `pip install <название пакета без указания ==версия>`

#### npm
В папке /app/static/ есть node_modules с установленными tailwindcss three, webpack и image-webpack-loader; package.json и package-lock.json содержат всю информацию для установки зависимостей для этих модулей.

Для установки зависимостей:
1. перейди в папку статических файлов: `cd app/static/`;
2. пропиши `npm install`

### TODOs:
#### BACK
1. Создать рабочую ветку — *(сделано)*
2. Настроить админку — *(прогресс 25%)*
3. Настроить роутер и контроллер — *(прогресс 40%)*
4. Заполнить бд начальными данными — *(прогресс 1%)*
5. Связать клиент с сервером с помощью Fetch API — *(требуется выполнение предыдущих задач)*
6. Проверить проект и приступить к отладке перед сдачей — *(требуется выполнение предыдущих задач)*