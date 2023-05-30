# jewerly_website
Website-project for programming subject realised in ITMO University


Для теста эндпоинтов:

1. Создание виртуального окружения `python3 -m venv venv` -> Активация `venv\Scripts\activate.bat` - windows, `source venv/bin/activate` - Linux/MacOS;
2. Установка зависимостей `pip install -r requirements.txt`
3. Ввести команду `uvicorn src.main:app --reload` для запуска локального сервера. Если стандартный порт занят, то добавить флаг `--port номер порта`
4. Можно перейти на локальный сервер через ссылку в терминале или вручную. Для просмотра эндпоинтов в конце нужно добавить `/docs`, т.е. это будет выглядеть примерно так: `http://localhost:8000/docs`
