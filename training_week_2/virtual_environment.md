# Виртуальные окружения в Python: Полное руководство для Middle-разработчика

## Что такое виртуальное окружение и зачем оно нужно

**Виртуальное окружение** — это изолированная среда Python, которая позволяет устанавливать пакеты и зависимости для конкретного проекта, не влияя на системную установку Python или другие проекты.

### Основные проблемы, которые решают виртуальные окружения:

- **Конфликты зависимостей**: Разные проекты могут требовать разные версии одной библиотеки
- **Загрязнение системы**: Установка пакетов в системный Python может привести к нестабильности
- **Воспроизводимость**: Гарантия одинаковых зависимостей на разных машинах
- **Безопасность**: Изоляция проектов друг от друга


## Работа с venv

### Создание и активация окружения

```bash
# Создание виртуального окружения
python -m venv myproject_env

# Активация в Linux/macOS
source myproject_env/bin/activate

# Активация в Windows
myproject_env\Scripts\activate

# Деактивация (в любой системе)
deactivate
```


### Проверка активного окружения

```bash
# Проверить, какой Python используется
which python
# или
python -c "import sys; print(sys.executable)"

# Посмотреть установленные пакеты
pip list
```


## Управление зависимостями с requirements.txt

### Создание файла зависимостей

```bash
# Сохранить текущие зависимости
pip freeze > requirements.txt

# Более продвинутый способ с pip-tools
pip install pip-tools
pip-compile requirements.in  # создает requirements.txt из requirements.in
```


### Восстановление зависимостей

```bash
# Установка зависимостей из файла
pip install -r requirements.txt

# Обновление зависимостей
pip install -r requirements.txt --upgrade
```


### Структура requirements файлов для продакшн-проектов

```
requirements/
├── base.txt          # Общие зависимости
├── development.txt   # Для разработки
├── production.txt    # Для продакшна
└── testing.txt       # Для тестирования
```

**base.txt:**

```
Django>=4.2,<5.0
psycopg2-binary>=2.9.0
celery>=5.3.0
redis>=4.5.0
```

**development.txt:**

```
-r base.txt
django-debug-toolbar>=4.0.0
pytest>=7.0.0
black>=23.0.0
flake8>=6.0.0
```

**production.txt:**

```
-r base.txt
gunicorn>=21.0.0
sentry-sdk>=1.32.0
```


## Примеры использования от простых к сложным

### Простой проект

```bash
# 1. Создание проекта
mkdir simple_project && cd simple_project
python -m venv venv
source venv/bin/activate  # Linux/macOS

# 2. Установка зависимостей
pip install requests beautifulsoup4
pip freeze > requirements.txt

# 3. Работа с проектом
python main.py
```


### Веб-приложение на Django

```bash
# 1. Настройка окружения
mkdir django_project && cd django_project
python -m venv venv
source venv/bin/activate

# 2. Установка Django и создание проекта
pip install Django>=4.2
django-admin startproject mysite .

# 3. Создание requirements структуры
mkdir requirements
echo "Django>=4.2,<5.0" > requirements/base.txt
echo "-r base.txt\ndjango-debug-toolbar" > requirements/development.txt
echo "-r base.txt\ngunicorn" > requirements/production.txt

# 4. Установка dev зависимостей
pip install -r requirements/development.txt
```


### Микросервисная архитектура

```bash
# Структура проекта
microservices/
├── user-service/
│   ├── venv/
│   ├── requirements.txt
│   └── app.py
├── order-service/
│   ├── venv/
│   ├── requirements.txt
│   └── app.py
└── docker-compose.yml
```

**Dockerfile для каждого сервиса:**

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "app.py"]
```


## Best Practices

### 1. Именование окружений

```bash
# Хорошо
python -m venv venv
python -m venv .venv
python -m venv project_name_env

# Плохо
python -m venv env1
python -m venv my_env
```


### 2. Структура проекта

```
my_project/
├── .venv/              # Виртуальное окружение
├── src/                # Исходный код
├── tests/              # Тесты
├── requirements.txt    # Зависимости
├── .gitignore         # Исключения для Git
├── README.md          # Документация
└── setup.py           # Настройки пакета
```


### 3. .gitignore для Python проектов

```gitignore
# Виртуальные окружения
venv/
.venv/
env/
ENV/

# Кэш Python
__pycache__/
*.pyc
*.pyo
*.pyd

# IDE
.vscode/
.idea/
```


### 4. Автоматизация с Makefile

```makefile
.PHONY: install dev test clean

install:
	python -m venv venv
	./venv/bin/pip install -r requirements.txt

dev:
	./venv/bin/pip install -r requirements/development.txt

test:
	./venv/bin/pytest

clean:
	rm -rf venv/
	find . -type d -name __pycache__ -delete
```


## Типовые ошибки и их решения

### 1. Забыли активировать окружение

```bash
# Проблема: пакеты устанавливаются в системный Python
pip install django

# Решение: всегда проверяйте активацию
which python  # должен показать путь к venv
```


### 2. Коммит виртуального окружения в Git

```bash
# Проблема: добавили venv/ в репозиторий
git add venv/

# Решение: удалить и добавить в .gitignore
git rm -r --cached venv/
echo "venv/" >> .gitignore
```


### 3. Конфликты версий

```bash
# Проблема: неточные версии в requirements.txt
Django
requests

# Решение: точные версии
Django==4.2.7
requests==2.31.0
```


### 4. Проблемы с путями

```python
# Проблема: хардкод путей
sys.path.append('/home/user/project/venv/lib/python3.11/site-packages')

# Решение: использование относительных путей
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
```


## Сравнение инструментов

| Инструмент | Плюсы | Минусы | Когда использовать |
| :-- | :-- | :-- | :-- |
| **venv** | Встроен в Python, простой | Базовый функционал | Простые проекты, обучение |
| **virtualenv** | Больше возможностей, поддержка старых версий | Требует установки | Legacy проекты |
| **pipenv** | Pipfile вместо requirements.txt, автоматическое управление | Медленный, сложности с CI/CD | Средние проекты |
| **poetry** | Современный, управление зависимостями и публикацией | Кривая обучения, не всегда совместим | Библиотеки, сложные проекты |

### Примеры использования альтернатив

**Poetry:**

```bash
# Инициализация проекта
poetry init
poetry add django
poetry add pytest --group dev

# Активация окружения
poetry shell

# Установка зависимостей
poetry install
```

**Pipenv:**

```bash
# Создание Pipfile
pipenv install django
pipenv install pytest --dev

# Активация
pipenv shell

# Установка из Pipfile
pipenv install --dev
```


## Интеграция с VS Code

### 1. Настройка интерпретатора

```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true
}
```


### 2. Автоматическая активация

VS Code автоматически обнаружит виртуальное окружение, если оно находится в:

- `./venv/`
- `./.venv/`
- `./env/`


### 3. Задачи для автоматизации

```json
// .vscode/tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Install dependencies",
            "type": "shell",
            "command": "${workspaceFolder}/venv/bin/pip",
            "args": ["install", "-r", "requirements.txt"]
        }
    ]
}
```


## Командная разработка

### 1. Соглашения команды

```bash
# Стандартизация Python версии
echo "python_version = '3.11'" > .python-version

# Единый способ создания окружения
make install  # или npm run install для JS-команд
```


### 2. Документация для команды

```markdown
# README.md
## Настройка окружения

1. Клонируйте репозиторий
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте: `source venv/bin/activate`
4. Установите зависимости: `pip install -r requirements/development.txt`
```


### 3. Pre-commit хуки

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```


## CI/CD интеграция

### GitHub Actions

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.9, 3.10, 3.11]
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Create virtual environment
      run: |
        python -m venv venv
        source venv/bin/activate
        echo "VIRTUAL_ENV=${VIRTUAL_ENV}" >> $GITHUB_ENV
        echo "${VIRTUAL_ENV}/bin" >> $GITHUB_PATH
    
    - name: Install dependencies
      run: |
        pip install --upgrade pip
        pip install -r requirements/testing.txt
    
    - name: Run tests
      run: pytest
```


### Docker для продакшна

```dockerfile
FROM python:3.11-slim

# Создание пользователя
RUN useradd --create-home --shell /bin/bash app
USER app
WORKDIR /home/app

# Установка зависимостей
COPY --chown=app:app requirements.txt .
RUN python -m venv venv && \
    venv/bin/pip install --upgrade pip && \
    venv/bin/pip install -r requirements.txt

# Копирование кода
COPY --chown=app:app . .

# Активация окружения и запуск
ENV PATH="/home/app/venv/bin:$PATH"
CMD ["python", "app.py"]
```


### Кэширование зависимостей

```yaml
# Кэширование pip в GitHub Actions
- name: Cache pip packages
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```


## Продвинутые техники

### 1. Множественные окружения для одного проекта

```bash
# Разные версии Python
python3.9 -m venv venv39
python3.11 -m venv venv311

# Разные конфигурации
python -m venv venv_dev
python -m venv venv_prod
```


### 2. Автоматическое переключение окружений

```bash
# Используя direnv
echo "source venv/bin/activate" > .envrc
direnv allow
```


### 3. Мониторинг зависимостей

```bash
# Проверка уязвимостей
pip install safety
safety check

# Проверка устаревших пакетов
pip list --outdated
```

Виртуальные окружения — это основа профессиональной разработки на Python. Правильное их использование обеспечивает стабильность, воспроизводимость и масштабируемость ваших проектов. Начните с простого `venv`, освойте best practices, а затем переходите к более продвинутым инструментам по мере необходимости.

