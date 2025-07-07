
# Настройка pre-commit hooks с Black

## Введение

Pre-commit hooks с Black представляют собой мощный инструмент для автоматического форматирования Python-кода перед каждым коммитом. Это обеспечивает единообразный стиль кода в команде и предотвращает попадание неотформатированного кода в репозиторий[^1][^2].

**Основные преимущества:**

- Автоматическое форматирование кода перед коммитом
- Единообразный стиль кода в команде
- Предотвращение споров о стиле кодирования
- Улучшение читаемости и поддерживаемости кода


## Установка и базовая настройка

### Шаг 1: Установка необходимых пакетов

```bash
# Установка pre-commit и black
pip install pre-commit black

# Добавление в requirements.txt (рекомендуется)
echo "pre-commit" >> requirements-dev.txt
echo "black" >> requirements-dev.txt
```


### Шаг 2: Создание конфигурационного файла

Создайте файл `.pre-commit-config.yaml` в корне вашего проекта[^2][^3]:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        language_version: python3.11
```


### Шаг 3: Установка git hooks

```bash
# Установка pre-commit hooks в .git/hooks/
pre-commit install
```

После этого Black будет автоматически запускаться при каждом `git commit`[^2].

## Примеры конфигураций от простых к сложным

### Пример 1: Минимальная конфигурация

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
```

Эта конфигурация применяет Black с настройками по умолчанию ко всем Python-файлам[^1].

### Пример 2: Конфигурация с параметрами

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        args: [--line-length=120]
        language_version: python3.11
```

Здесь мы устанавливаем максимальную длину строки в 120 символов[^3].

### Пример 3: Конфигурация с исключениями

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        exclude: ^(migrations/|legacy_code/|third_party/)
        args: [--line-length=88, --target-version=py311]
```

Эта конфигурация исключает определенные директории от форматирования[^1].

### Пример 4: Комплексная конфигурация для продакшена

```yaml
fail_fast: true
repos:
  # Базовые проверки
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-merge-conflict
      - id: debug-statements

  # Форматирование с Black
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        args: [--line-length=88, --target-version=py311]
        exclude: ^(migrations/|docs/|scripts/legacy/)

  # Сортировка импортов
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: [--profile=black]

  # Линтинг
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        additional_dependencies: [flake8-docstrings, flake8-import-order]
```


## Интеграция с различными инструментами

### Конфигурация для работы с flake8

Создайте файл `.flake8` для совместимости с Black[^4]:

```ini
[flake8]
max-line-length = 88
extend-ignore = E203, E266, E501, W503, F403, F401
max-complexity = 18
select = B,C,E,F,W,T4,B9
```


### Конфигурация pyproject.toml для Black

```toml
[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'
exclude = '''
/(
    \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
  | migrations
)/
'''
```


## Примеры из коммерческой разработки

### Пример 1: Конфигурация для микросервиса

```yaml
# .pre-commit-config.yaml для микросервиса
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-docstring-first
      - id: requirements-txt-fixer

  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        args: [--line-length=100]
        files: ^(src/|tests/|scripts/).*\.py$

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: [--profile=black, --line-length=100]

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: [--max-line-length=100]
        additional_dependencies:
          - flake8-bugbear
          - flake8-comprehensions
          - flake8-simplify

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.0.1
    hooks:
      - id: mypy
        additional_dependencies: [types-requests, types-PyYAML]
        args: [--ignore-missing-imports]
```


### Пример 2: Конфигурация для Django проекта

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        args: [--line-length=88]
        exclude: ^(migrations/|venv/|env/)
        
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: [--profile=black, --multi-line=3]
        
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        additional_dependencies: [flake8-django]
        args: [--max-line-length=88, --exclude=migrations]

  - repo: https://github.com/adamchainz/django-upgrade
    rev: 1.13.0
    hooks:
      - id: django-upgrade
        args: [--target-version, "4.2"]
```


### Пример 3: Конфигурация для Data Science проекта

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        args: [--line-length=100]
        files: ^(src/|notebooks/.*\.py$|scripts/)

  - repo: https://github.com/nbQA-dev/nbQA
    rev: 1.6.0
    hooks:
      - id: nbqa-black
        args: [--line-length=100]
      - id: nbqa-isort
        args: [--profile=black]
      - id: nbqa-flake8
        args: [--max-line-length=100, --ignore=E203,W503]

  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: [--profile=black, --line-length=100]
```


## Работа с Poetry

### Локальная конфигурация с Poetry

```yaml
# .pre-commit-config.yaml для проектов с Poetry
repos:
  - repo: local
    hooks:
      - id: black
        name: black
        entry: poetry run black
        language: system
        types: [python]
        args: [--line-length=88]
        
      - id: isort
        name: isort
        entry: poetry run isort
        language: system
        types: [python]
        args: [--profile=black]
```

Эта конфигурация использует Poetry для запуска инструментов из виртуального окружения проекта[^5].

## Решение типичных проблем

### Проблема 1: Black изменяет файлы, но коммит не проходит

**Проблема:** Black форматирует файлы, но возвращает код ошибки, из-за чего коммит не проходит[^6].

**Решение:**

```bash
# После того как Black отформатировал файлы, добавьте их снова
git add .
git commit -m "Your commit message"
```


### Проблема 2: Конфликт с другими форматтерами

**Решение:** Настройте правильный порядок выполнения hooks:

```yaml
repos:
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
        args: [--profile=black]
        
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
```


### Проблема 3: Пропуск pre-commit hooks в экстренных случаях

```bash
# Пропуск всех hooks
git commit -m "Emergency fix" --no-verify

# Пропуск конкретного hook
SKIP=black git commit -m "Skip black formatting"
```


## Продвинутые настройки

### Кастомные аргументы для разных типов файлов

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        name: black-src
        files: ^src/
        args: [--line-length=88]
        
      - id: black
        name: black-tests
        files: ^tests/
        args: [--line-length=100]
```


### Условное выполнение hooks

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        stages: [commit, push]  # Запуск только при commit и push
```


### Интеграция с CI/CD

```yaml
# .github/workflows/pre-commit.yml
name: Pre-commit
on: [push, pull_request]
jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - uses: pre-commit/action@v3.0.0
```


## Мониторинг и обслуживание

### Обновление hooks

```bash
# Автоматическое обновление до последних версий
pre-commit autoupdate

# Ручное обновление конкретного hook
pre-commit autoupdate --repo https://github.com/psf/black
```


### Запуск hooks вручную

```bash
# Запуск всех hooks для всех файлов
pre-commit run --all-files

# Запуск конкретного hook
pre-commit run black

# Запуск hooks для конкретных файлов
pre-commit run --files src/main.py tests/test_main.py
```


## Лучшие практики для продакшена

### 1. Версионирование hooks

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0  # Используйте конкретную версию, а не 'stable'
    hooks:
      - id: black
```


### 2. Настройка для команды

```yaml
# Создайте общий конфиг для всей команды
default_language_version:
  python: python3.11

repos:
  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        args: [--line-length=88, --target-version=py311]
```


### 3. Документирование настроек

```markdown
# README.md
## Настройка разработки

1. Установите pre-commit hooks:
```

pip install -r requirements-dev.txt
pre-commit install

```

2. Запустите проверку всех файлов:
```

pre-commit run --all-files

```
```


### 4. Интеграция с IDE

Настройте ваш редактор для использования тех же настроек Black:

```json
// VS Code settings.json
{
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": ["--line-length=88"],
  "editor.formatOnSave": true
}
```


## Заключение

Настройка pre-commit hooks с Black является критически важной практикой для профессиональной разработки на Python. Это обеспечивает:

- **Консистентность кода** в команде
- **Автоматизацию** процесса форматирования
- **Предотвращение** попадания неотформатированного кода в репозиторий
- **Улучшение** качества кода и его читаемости

Начните с простой конфигурации и постепенно добавляйте дополнительные инструменты по мере необходимости. Помните, что правильно настроенные pre-commit hooks экономят время команды и улучшают качество кодовой базы.

<div style="text-align: center">⁂</div>

[^1]: https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/

[^2]: https://pre-commit.com

[^3]: https://dev.to/emmo00/how-to-setup-black-and-pre-commit-in-python-for-auto-text-formatting-on-commit-4kka

[^4]: https://sineadobrien.com/tech/code/python-black-and-flake8-pre-commit-hooks/

[^5]: https://smhk.net/note/2023/09/poetry-pre-commit-hooks/

[^6]: https://stackoverflow.com/questions/58398995/black-as-pre-commit-hook-always-fails-my-commits

[^7]: https://github.com/psf/black/issues/3073

[^8]: https://github.com/jidicula/pre-commit-black

[^9]: https://github.com/psf/black/issues/1857

[^10]: https://graphite.dev/guides/implementing-pre-commit-hooks-to-enforce-code-quality

[^11]: https://www.reddit.com/r/Python/comments/npnfq3/installing_and_using_black_for_code_formatting/

[^12]: https://www.reddit.com/r/ExperiencedDevs/comments/144fcqo/what_are_your_precommit_hooks/

[^13]: https://black.readthedocs.io/en/stable/integrations/source_version_control.html

[^14]: https://dev.to/pratyushcode/streamlining-your-python-workflow-with-black-ruff-github-actions-and-pre-commit-hooks-nk2

[^15]: https://gist.github.com/mattrasband/fa8c07a1c63d685f4796c439089ef3ab

[^16]: https://www.pythonsnacks.com/p/pre-commit-hooks-python

