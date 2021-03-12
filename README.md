### Требования
Python 3.8

### Установка зависимостей
> pip install -r requirements.txt

### Запуск тестов
> pytest -v -s tests

Дополнительные параметры:
1. Окружение (по умолчанию prod, можно добавить новые в файле conftest.py)
> --server=prod
2. Браузер (по умолчанию chrome)
> --browser=firefox 
3. Таймаут (по умолчанию 10 сек)
> --timeout=20 

### Дополнительно 
При возникновении ошибки: 
> ModuleNotFoundError: No module named 'helpers'

В терминал ввести команду:
> export PYTHONPATH=./