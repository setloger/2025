# Этот файл содержит основную логику для создания и управления логами

# Импорт стандартных библиотек пайтон

import json     # Для работы с JSON форматом (сериализация данных в строку)
from datetime import datetime       # Для получения текущего времени и даты
from typing import List, Dict, Any, Optional        # Для аннотации типов
# (подсказки IDE)
from enum import Enum       # Для создания перечислений (константы с именами)


class LogLevel(Enum):
    """
    Перечисление уровней логирования
    Enum - это класс для создания именованных констант
    Каждый уровень имеет свое назначение:
    - DEBUG: детальная информация для отладки
    - INFO: общая информация о работе программы
    - WARNING: предупреждение о потенциальных проблемах
    - ERROR: ошибки, которые не останавливают программу
    """
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'


class SimpleLogger:
    """
    Основной класс логгера - центральная система для записи логов
    Этот класс координирует работу всех компонентов логирования
    """
    def __init__(self, name: str = 'SimpleLogger'):
        # Имеет аннотацию типа str, указывающую, что ожидается строковое
        # значение
        """
        Конструктор класса вызывается при создании нового объекта логгера

        Args:
            name: имя логгера (по умолчанию "SimpleLogger")
        """
        self.name = name    # Сохраняем имя для идентификации
        # List['LogHandler'] - это аннотация типа, означающая "список объектов
        # типа LogHandler"
        self.handlers: List['LogHandler'] = []  # Список обработчиков (куда
        # отправлять логи)

    def add_handler(self, handler: 'LogHandler'):
        """
        Добавляет обработчик логов в список
        Обработчик определяет, куда будут отправляться сообщения (консоль,
        файл, etc)

        Args:
            handler: объект обработчика, который умеет записывать логи
        """
        self.handlers.append(handler)

    def log(self, level: LogLevel, message: str, extra: Optional[Dict] = None):
        """Основной метод логирования"""
        log_record = {
            'timestamp': datetime.now().strftime('%Y-%m-%d-%H:%M:%S'),
            'level': level.value,
            'logger': self.name,
            'message': message,
            'extra': extra or {}
        }

        # Отправляем во все обработчики
        for handler in self.handlers:
            handler.write(log_record)

    def debug(self, message: str, **kwards):
        """Логирование отладочной инфомарции"""
        self.log(LogLevel.DEBUG, message, kwards)

    def into(self, message: str, **kwards):
        """Логирование общей информации"""
        self.log(LogLevel.INFO, message, kwards)

    def warning(self, message: str, **kwards):
        """Логирование предупреждений"""
        self.log(LogLevel.WARNING, message, kwards)

    def error(self, message: str, **kwards):
        """Логирование ошибок"""
        self.log(LogLevel.ERROR, message, kwards)
