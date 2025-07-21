# Этот файл содержит классы, которые определяют, куда записывать логи

import json
from abc import ABC, abstractmethod


class LogHandler(ABC):
    @abstractmethod
    def write(self, log_record: dict):
        pass


class ConsoleHandler(LogHandler):

    def __init__(self, colored: bool = True):
        self.colored = colored

        self.colors = {
            'DEBUG': '\033[36m',    # Голубой цвет
            'INFO': '\033[32m',     # Зеленый цвет
            'WARNING': '\033[33m',  # Желтый цвет
            'ERROR': '\033[31m',    # Красный цвет
            'RESET': '\033[0m'      # Сброс цвета к стандартному
        }

    def write(self, log_record: dict):
        level = log_record['level']
        timestamp = log_record['timestamp']
        message = log_record['message']


