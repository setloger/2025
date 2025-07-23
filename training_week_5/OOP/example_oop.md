# Структурированная подготовка к собеседованию: ООП в Python для Middle-разработчика

## 🎯 Прогрессивная система обучения: от простого к сложному

### Уровень 1: Основы классов и объектов

#### Простой пример: Базовый класс

```python
class User:
    """Простой класс пользователя"""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def get_info(self):
        return f"Пользователь: {self.name} ({self.email})"

# Использование
user = User("Иван Петров", "ivan@example.com")
print(user.get_info())  # Пользователь: Иван Петров (ivan@example.com)
```

**Пояснение:** Базовая структура класса с конструктором и методом. Это фундамент для понимания объектов.

#### Усложнение: Атрибуты класса vs экземпляра

```python
class Employee:
    """Сотрудник компании"""
    
    # Атрибуты класса
    company_name = "TechCorp"
    total_employees = 0
    
    def __init__(self, name, position, salary):
        # Атрибуты экземпляра
        self.name = name
        self.position = position
        self.salary = salary
        self.employee_id = self._generate_id()
        
        # Увеличиваем счетчик сотрудников
        Employee.total_employees += 1
    
    def _generate_id(self):
        """Защищенный метод для генерации ID"""
        import random
        return f"EMP{random.randint(1000, 9999)}"
    
    @classmethod
    def get_company_info(cls):
        """Метод класса для получения информации о компании"""
        return f"Компания: {cls.company_name}, Сотрудников: {cls.total_employees}"
    
    @staticmethod
    def calculate_annual_bonus(salary, performance_rating):
        """Статический метод для расчета бонуса"""
        bonus_rates = {1: 0.05, 2: 0.10, 3: 0.15, 4: 0.20, 5: 0.25}
        return salary * bonus_rates.get(performance_rating, 0)

# Демонстрация
emp1 = Employee("Анна Смирнова", "Python Developer", 120000)
emp2 = Employee("Петр Иванов", "DevOps Engineer", 110000)

print(Employee.get_company_info())  # Компания: TechCorp, Сотрудников: 2
print(f"Бонус Анны: {Employee.calculate_annual_bonus(120000, 4)}")  # 24000.0
```

**Коммерческий контекст:** В реальных проектах такой подход используется для управления сотрудниками в HR-системах, где нужно отслеживать общую статистику и индивидуальные данные.

### Уровень 2: Инкапсуляция и валидация данных

#### Продакшн-пример: Система управления заказами

```python
from datetime import datetime
from enum import Enum
from typing import List, Optional

class OrderStatus(Enum):
    """Статусы заказа"""
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class Product:
    """Продукт в каталоге"""
    
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self._price = None
        self._stock = None
        
        # Используем сеттеры для валидации
        self.price = price
        self.stock = stock
    
    @property
    def price(self) -> float:
        """Цена продукта"""
        return self._price
    
    @price.setter
    def price(self, value: float):
        """Установка цены с валидацией"""
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом")
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        if value > 1000000:
            raise ValueError("Цена слишком высокая")
        self._price = float(value)
    
    @property
    def stock(self) -> int:
        """Количество на складе"""
        return self._stock
    
    @stock.setter
    def stock(self, value: int):
        """Установка количества с валидацией"""
        if not isinstance(value, int):
            raise TypeError("Количество должно быть целым числом")
        if value < 0:
            raise ValueError("Количество не может быть отрицательным")
        self._stock = value
    
    @property
    def is_available(self) -> bool:
        """Проверка доступности товара"""
        return self._stock > 0
    
    def reserve(self, quantity: int) -> bool:
        """Резервирование товара"""
        if quantity <= self._stock:
            self._stock -= quantity
            return True
        return False

class Order:
    """Заказ клиента с полной бизнес-логикой"""
    
    def __init__(self, order_id: str, customer_email: str):
        self.order_id = order_id
        self.customer_email = customer_email
        self._status = OrderStatus.PENDING
        self._items = []
        self._created_at = datetime.now()
        self._updated_at = self._created_at
        self._total_amount = 0.0
    
    @property
    def status(self) -> OrderStatus:
        """Текущий статус заказа"""
        return self._status
    
    @property
    def total_amount(self) -> float:
        """Общая сумма заказа"""
        return self._total_amount
    
    @property
    def items_count(self) -> int:
        """Количество позиций в заказе"""
        return len(self._items)
    
    def add_item(self, product: Product, quantity: int) -> str:
        """Добавление товара в заказ"""
        if self._status != OrderStatus.PENDING:
            raise ValueError(f"Нельзя изменять заказ в статусе {self._status.value}")
        
        if not product.is_available:
            return f"Товар {product.name} недоступен"
        
        if quantity > product.stock:
            return f"Недостаточно товара {product.name} на складе"
        
        # Резервируем товар
        if product.reserve(quantity):
            item = {
                'product': product,
                'quantity': quantity,
                'unit_price': product.price,
                'total_price': product.price * quantity
            }
            self._items.append(item)
            self._total_amount += item['total_price']
            self._updated_at = datetime.now()
            return f"Добавлено {quantity} x {product.name}"
        
        return "Ошибка при резервировании товара"
    
    def confirm_order(self) -> str:
        """Подтверждение заказа"""
        if self._status != OrderStatus.PENDING:
            return f"Заказ уже в статусе {self._status.value}"
        
        if not self._items:
            return "Нельзя подтвердить пустой заказ"
        
        self._status = OrderStatus.CONFIRMED
        self._updated_at = datetime.now()
        return f"Заказ {self.order_id} подтвержден на сумму {self._total_amount:.2f}"
    
    def cancel_order(self) -> str:
        """Отмена заказа с возвратом товара на склад"""
        if self._status in [OrderStatus.SHIPPED, OrderStatus.DELIVERED]:
            return "Нельзя отменить отправленный или доставленный заказ"
        
        # Возвращаем товары на склад
        for item in self._items:
            item['product']._stock += item['quantity']
        
        self._status = OrderStatus.CANCELLED
        self._updated_at = datetime.now()
        return f"Заказ {self.order_id} отменен"
    
    def get_order_summary(self) -> dict:
        """Получение сводки по заказу"""
        return {
            'order_id': self.order_id,
            'customer': self.customer_email,
            'status': self._status.value,
            'items_count': self.items_count,
            'total_amount': self._total_amount,
            'created_at': self._created_at.isoformat(),
            'updated_at': self._updated_at.isoformat()
        }

# Демонстрация использования
laptop = Product("LAPTOP001", "MacBook Pro", 150000, 5)
mouse = Product("MOUSE001", "Wireless Mouse", 2500, 20)

order = Order("ORD-2025-001", "customer@example.com")
print(order.add_item(laptop, 1))  # Добавлено 1 x MacBook Pro
print(order.add_item(mouse, 2))   # Добавлено 2 x Wireless Mouse
print(order.confirm_order())      # Заказ ORD-2025-001 подтвержден на сумму 155000.00

print(f"Остаток ноутбуков: {laptop.stock}")  # 4
print(order.get_order_summary())
```

**Коммерческое применение:** Такая система используется в e-commerce платформах (Wildberries, Ozon), где критически важна валидация данных и управление состоянием заказов.

### Уровень 3: Наследование и полиморфизм

#### Продакшн-пример: Система уведомлений

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List
import json
import logging

class NotificationChannel(ABC):
    """Абстрактный базовый класс для каналов уведомлений"""
    
    def __init__(self, name: str):
        self.name = name
        self.is_enabled = True
        self.retry_count = 3
        self.delivery_stats = {'sent': 0, 'failed': 0}
    
    @abstractmethod
    def send(self, recipient: str, message: str, **kwargs) -> bool:
        """Абстрактный метод отправки уведомления"""
        pass
    
    @abstractmethod
    def validate_recipient(self, recipient: str) -> bool:
        """Валидация получателя"""
        pass
    
    def send_with_retry(self, recipient: str, message: str, **kwargs) -> bool:
        """Отправка с повторными попытками"""
        if not self.is_enabled:
            logging.warning(f"Канал {self.name} отключен")
            return False
        
        if not self.validate_recipient(recipient):
            logging.error(f"Некорректный получатель: {recipient}")
            return False
        
        for attempt in range(self.retry_count):
            try:
                if self.send(recipient, message, **kwargs):
                    self.delivery_stats['sent'] += 1
                    logging.info(f"Уведомление отправлено через {self.name}")
                    return True
            except Exception as e:
                logging.warning(f"Попытка {attempt + 1} неудачна: {e}")
        
        self.delivery_stats['failed'] += 1
        logging.error(f"Не удалось отправить уведомление через {self.name}")
        return False
    
    def get_stats(self) -> Dict[str, Any]:
        """Статистика доставки"""
        total = self.delivery_stats['sent'] + self.delivery_stats['failed']
        success_rate = (self.delivery_stats['sent'] / total * 100) if total > 0 else 0
        
        return {
            'channel': self.name,
            'enabled': self.is_enabled,
            'sent': self.delivery_stats['sent'],
            'failed': self.delivery_stats['failed'],
            'success_rate': f"{success_rate:.1f}%"
        }

class EmailNotification(NotificationChannel):
    """Уведомления по email"""
    
    def __init__(self, smtp_server: str, port: int = 587):
        super().__init__("Email")
        self.smtp_server = smtp_server
        self.port = port
        self.from_address = "noreply@company.com"
    
    def validate_recipient(self, recipient: str) -> bool:
        """Валидация email адреса"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, recipient))
    
    def send(self, recipient: str, message: str, subject: str = "Уведомление", **kwargs) -> bool:
        """Отправка email (имитация)"""
        # В реальности здесь был бы код для SMTP
        logging.info(f"EMAIL: {subject} -> {recipient}")
        logging.debug(f"Сервер: {self.smtp_server}:{self.port}")
        
        # Имитация случайных сбоев
        import random
        if random.random() < 0.1:  # 10% вероятность сбоя
            raise Exception("SMTP connection failed")
        
        return True
    
    def send_html(self, recipient: str, html_content: str, subject: str) -> bool:
        """Отправка HTML email"""
        return self.send_with_retry(recipient, html_content, subject=subject, content_type="html")

class SMSNotification(NotificationChannel):
    """SMS уведомления"""
    
    def __init__(self, api_key: str, provider: str = "Twilio"):
        super().__init__("SMS")
        self.api_key = api_key
        self.provider = provider
        self.max_length = 160
    
    def validate_recipient(self, recipient: str) -> bool:
        """Валидация номера телефона"""
        import re
        # Простая валидация международного формата
        pattern = r'^\+[1-9]\d{1,14}$'
        return bool(re.match(pattern, recipient))
    
    def send(self, recipient: str, message: str, **kwargs) -> bool:
        """Отправка SMS"""
        if len(message) > self.max_length:
            logging.warning(f"Сообщение обрезано до {self.max_length} символов")
            message = message[:self.max_length-3] + "..."
        
        logging.info(f"SMS: {message[:50]}... -> {recipient}")
        logging.debug(f"Провайдер: {self.provider}")
        
        # Имитация API вызова
        import random
        if random.random() < 0.05:  # 5% вероятность сбоя
            raise Exception("SMS API rate limit exceeded")
        
        return True

class PushNotification(NotificationChannel):
    """Push уведомления для мобильных приложений"""
    
    def __init__(self, firebase_key: str):
        super().__init__("Push")
        self.firebase_key = firebase_key
        self.supported_platforms = ["ios", "android"]
    
    def validate_recipient(self, recipient: str) -> bool:
        """Валидация device token"""
        # Упрощенная валидация токена устройства
        return len(recipient) > 50 and recipient.isalnum()
    
    def send(self, recipient: str, message: str, title: str = "Уведомление", 
             platform: str = "android", **kwargs) -> bool:
        """Отправка push уведомления"""
        if platform not in self.supported_platforms:
            raise ValueError(f"Неподдерживаемая платформа: {platform}")
        
        payload = {
            'to': recipient,
            'notification': {
                'title': title,
                'body': message
            },
            'platform': platform
        }
        
        logging.info(f"PUSH: {title} -> {recipient[:20]}...")
        logging.debug(f"Payload: {json.dumps(payload, ensure_ascii=False)}")
        
        import random
        if random.random() < 0.03:  # 3% вероятность сбоя
            raise Exception("Firebase service unavailable")
        
        return True

class NotificationService:
    """Сервис управления уведомлениями"""
    
    def __init__(self):
        self.channels: List[NotificationChannel] = []
        self.default_channels = []
    
    def add_channel(self, channel: NotificationChannel, is_default: bool = False):
        """Добавление канала уведомлений"""
        self.channels.append(channel)
        if is_default:
            self.default_channels.append(channel)
        logging.info(f"Добавлен канал: {channel.name}")
    
    def send_notification(self, recipients: Dict[str, str], message: str, 
                         channels: List[str] = None, **kwargs) -> Dict[str, bool]:
        """Отправка уведомления через указанные каналы"""
        if channels is None:
            active_channels = self.default_channels
        else:
            active_channels = [ch for ch in self.channels if ch.name in channels]
        
        results = {}
        
        for channel in active_channels:
            channel_name = channel.name
            recipient = recipients.get(channel_name.lower())
            
            if recipient:
                success = channel.send_with_retry(recipient, message, **kwargs)
                results[channel_name] = success
            else:
                logging.warning(f"Нет получателя для канала {channel_name}")
                results[channel_name] = False
        
        return results
    
    def broadcast_notification(self, message: str, **kwargs) -> Dict[str, int]:
        """Массовая рассылка (имитация)"""
        # В реальности здесь была бы работа с базой данных пользователей
        test_recipients = {
            'email': 'user@example.com',
            'sms': '+79001234567',
            'push': 'device_token_123abc' + 'x' * 50
        }
        
        results = self.send_notification(test_recipients, message, **kwargs)
        
        summary = {'successful': 0, 'failed': 0}
        for success in results.values():
            if success:
                summary['successful'] += 1
            else:
                summary['failed'] += 1
        
        return summary
    
    def get_all_stats(self) -> List[Dict[str, Any]]:
        """Статистика по всем каналам"""
        return [channel.get_stats() for channel in self.channels]

# Демонстрация полиморфизма в действии
def setup_notification_system():
    """Настройка системы уведомлений"""
    # Создаем различные каналы
    email_channel = EmailNotification("smtp.company.com", 587)
    sms_channel = SMSNotification("api_key_12345", "Twilio")
    push_channel = PushNotification("firebase_key_67890")
    
    # Создаем сервис и добавляем каналы
    notification_service = NotificationService()
    notification_service.add_channel(email_channel, is_default=True)
    notification_service.add_channel(sms_channel, is_default=True)
    notification_service.add_channel(push_channel, is_default=False)
    
    return notification_service

# Использование
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

service = setup_notification_system()

# Отправка уведомления конкретному пользователю
recipients = {
    'email': 'john.doe@example.com',
    'sms': '+79001234567',
    'push': 'device_token_abc123' + 'x' * 50
}

results = service.send_notification(
    recipients, 
    "Ваш заказ готов к получению!",
    subject="Уведомление о заказе",
    title="Заказ готов"
)

print("Результаты отправки:", results)

# Массовая рассылка
broadcast_results = service.broadcast_notification(
    "Новая акция! Скидка 20% на все товары до конца недели!",
    subject="Специальное предложение",
    title="Акция"
)

print("Результаты массовой рассылки:", broadcast_results)

# Статистика
print("\nСтатистика каналов:")
for stats in service.get_all_stats():
    print(f"- {stats['channel']}: {stats['success_rate']} успешных доставок")
```

**Коммерческое применение:** Подобные системы используются в крупных сервисах (Яндекс, Mail.ru, банки) для отправки уведомлений пользователям через различные каналы с отслеживанием доставки.

### Уровень 4: Продвинутые паттерны и архитектура

#### Enterprise-пример: Система обработки платежей

```python
from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
import uuid
import logging
from decimal import Decimal

class PaymentStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"
    CANCELLED = "cancelled"

class Currency(Enum):
    RUB = "RUB"
    USD = "USD"
    EUR = "EUR"

@dataclass
class PaymentRequest:
    """Запрос на платеж"""
    amount: Decimal
    currency: Currency
    description: str
    customer_id: str
    order_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class PaymentResult:
    """Результат обработки платежа"""
    success: bool
    transaction_id: Optional[str] = None
    error_message: Optional[str] = None
    provider_response: Optional[Dict[str, Any]] = None

class PaymentProvider(ABC):
    """Абстрактный провайдер платежей"""
    
    def __init__(self, name: str, supported_currencies: List[Currency]):
        self.name = name
        self.supported_currencies = supported_currencies
        self.is_enabled = True
        self.commission_rate = Decimal('0.03')  # 3%
        self.min_amount = Decimal('1.00')
        self.max_amount = Decimal('1000000.00')
    
    @abstractmethod
    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        """Обработка платежа"""
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id: str, amount: Decimal) -> PaymentResult:
        """Возврат платежа"""
        pass
    
    @abstractmethod
    def get_payment_status(self, transaction_id: str) -> PaymentStatus:
        """Получение статуса платежа"""
        pass
    
    def validate_request(self, request: PaymentRequest) -> Optional[str]:
        """Валидация запроса"""
        if not self.is_enabled:
            return f"Провайдер {self.name} отключен"
        
        if request.currency not in self.supported_currencies:
            return f"Валюта {request.currency.value} не поддерживается"
        
        if request.amount < self.min_amount:
            return f"Сумма меньше минимальной ({self.min_amount})"
        
        if request.amount > self.max_amount:
            return f"Сумма превышает максимальную ({self.max_amount})"
        
        return None
    
    def calculate_commission(self, amount: Decimal) -> Decimal:
        """Расчет комиссии"""
        return amount * self.commission_rate

class SberPayProvider(PaymentProvider):
    """Провайдер Сбербанка"""
    
    def __init__(self, merchant_id: str, secret_key: str):
        super().__init__("SberPay", [Currency.RUB])
        self.merchant_id = merchant_id
        self.secret_key = secret_key
        self.api_url = "https://api.sberbank.ru/payment"
        self.commission_rate = Decimal('0.025')  # 2.5%
    
    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        """Обработка платежа через Сбербанк"""
        validation_error = self.validate_request(request)
        if validation_error:
            return PaymentResult(False, error_message=validation_error)
        
        try:
            # Имитация API вызова к Сбербанку
            transaction_id = f"sber_{uuid.uuid4().hex[:12]}"
            
            # Симуляция обработки
            import random
            if random.random() < 0.95:  # 95% успешных платежей
                logging.info(f"Платеж {transaction_id} успешно обработан через {self.name}")
                return PaymentResult(
                    success=True,
                    transaction_id=transaction_id,
                    provider_response={
                        "provider": self.name,
                        "merchant_id": self.merchant_id,
                        "amount": str(request.amount),
                        "currency": request.currency.value
                    }
                )
            else:
                return PaymentResult(
                    success=False,
                    error_message="Недостаточно средств на карте"
                )
        
        except Exception as e:
            logging.error(f"Ошибка при обработке платежа: {e}")
            return PaymentResult(False, error_message=str(e))
    
    def refund_payment(self, transaction_id: str, amount: Decimal) -> PaymentResult:
        """Возврат платежа"""
        refund_id = f"refund_{uuid.uuid4().hex[:12]}"
        logging.info(f"Возврат {refund_id} для транзакции {transaction_id}")
        return PaymentResult(True, transaction_id=refund_id)
    
    def get_payment_status(self, transaction_id: str) -> PaymentStatus:
        """Получение статуса платежа"""
        # Имитация проверки статуса
        return PaymentStatus.COMPLETED

class YooKassaProvider(PaymentProvider):
    """Провайдер ЮKassa (Яндекс)"""
    
    def __init__(self, shop_id: str, secret_key: str):
        super().__init__("YooKassa", [Currency.RUB, Currency.USD, Currency.EUR])
        self.shop_id = shop_id
        self.secret_key = secret_key
        self.api_url = "https://api.yookassa.ru/v3/payments"
        self.commission_rate = Decimal('0.029')  # 2.9%
    
    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        """Обработка платежа через ЮKassa"""
        validation_error = self.validate_request(request)
        if validation_error:
            return PaymentResult(False, error_message=validation_error)
        
        try:
            transaction_id = f"yoo_{uuid.uuid4().hex[:12]}"
            
            # Симуляция обработки
            import random
            if random.random() < 0.97:  # 97% успешных платежей
                logging.info(f"Платеж {transaction_id} успешно обработан через {self.name}")
                return PaymentResult(
                    success=True,
                    transaction_id=transaction_id,
                    provider_response={
                        "provider": self.name,
                        "shop_id": self.shop_id,
                        "amount": str(request.amount),
                        "currency": request.currency.value
                    }
                )
            else:
                return PaymentResult(
                    success=False,
                    error_message="Платеж отклонен банком"
                )
        
        except Exception as e:
            logging.error(f"Ошибка при обработке платежа: {e}")
            return PaymentResult(False, error_message=str(e))
    
    def refund_payment(self, transaction_id: str, amount: Decimal) -> PaymentResult:
        """Возврат платежа"""
        refund_id = f"yoo_refund_{uuid.uuid4().hex[:12]}"
        logging.info(f"Возврат {refund_id} для транзакции {transaction_id}")
        return PaymentResult(True, transaction_id=refund_id)
    
    def get_payment_status(self, transaction_id: str) -> PaymentStatus:
        """Получение статуса платежа"""
        return PaymentStatus.COMPLETED

class PaymentRouter:
    """Роутер для выбора оптимального провайдера платежей"""
    
    def __init__(self):
        self.providers: List[PaymentProvider] = []
        self.provider_priorities: Dict[str, int] = {}
        self.fallback_enabled = True
    
    def add_provider(self, provider: PaymentProvider, priority: int = 1):
        """Добавление провайдера с приоритетом"""
        self.providers.append(provider)
        self.provider_priorities[provider.name] = priority
        logging.info(f"Добавлен провайдер {provider.name} с приоритетом {priority}")
    
    def get_best_provider(self, request: PaymentRequest) -> Optional[PaymentProvider]:
        """Выбор лучшего провайдера для запроса"""
        suitable_providers = []
        
        for provider in self.providers:
            if (provider.is_enabled and 
                request.currency in provider.supported_currencies and
                provider.min_amount <= request.amount <= provider.max_amount):
                suitable_providers.append(provider)
        
        if not suitable_providers:
            return None
        
        # Сортируем по приоритету и комиссии
        suitable_providers.sort(
            key=lambda p: (
                -self.provider_priorities.get(p.name, 0),  # Высокий приоритет
                p.calculate_commission(request.amount)      # Низкая комиссия
            )
        )
        
        return suitable_providers[0]
    
    def process_payment_with_fallback(self, request: PaymentRequest) -> PaymentResult:
        """Обработка платежа с fallback на другие провайдеры"""
        suitable_providers = [
            p for p in self.providers 
            if (p.is_enabled and 
                request.currency in p.supported_currencies and
                p.min_amount <= request.amount <= p.max_amount)
        ]
        
        if not suitable_providers:
            return PaymentResult(
                False, 
                error_message="Нет доступных провайдеров для данного платежа"
            )
        
        # Сортируем по приоритету
        suitable_providers.sort(
            key=lambda p: -self.provider_priorities.get(p.name, 0)
        )
        
        last_error = None
        
        for provider in suitable_providers:
            try:
                logging.info(f"Попытка обработки через {provider.name}")
                result = provider.process_payment(request)
                
                if result.success:
                    return result
                else:
                    last_error = result.error_message
                    logging.warning(f"Провайдер {provider.name} отклонил платеж: {last_error}")
                    
            except Exception as e:
                last_error = str(e)
                logging.error(f"Ошибка провайдера {provider.name}: {e}")
                continue
        
        return PaymentResult(
            False,
            error_message=f"Все провайдеры недоступны. Последняя ошибка: {last_error}"
        )

class PaymentService:
    """Основной сервис обработки платежей"""
    
    def __init__(self):
        self.router = PaymentRouter()
        self.transaction_log: List[Dict[str, Any]] = []
        self.daily_limits: Dict[str, Decimal] = {}
        self.processed_today: Dict[str, Decimal] = {}
    
    def setup_providers(self):
        """Настройка провайдеров"""
        # Добавляем провайдеров с разными приоритетами
        sber_provider = SberPayProvider("merchant_123", "secret_key_sber")
        yoo_provider = YooKassaProvider("shop_456", "secret_key_yoo")
        
        self.router.add_provider(yoo_provider, priority=2)  # Высокий приоритет
        self.router.add_provider(sber_provider, priority=1)  # Средний приоритет
        
        # Устанавливаем дневные лимиты
        self.daily_limits["default"] = Decimal('100000.00')  # 100k рублей в день
    
    def process_payment(self, request: PaymentRequest) -> PaymentResult:
        """Обработка платежа с логированием и проверками"""
        # Проверяем дневные лимиты
        today = datetime.now().date()
        daily_key = f"{request.customer_id}_{today}"
        
        current_daily_amount = self.processed_today.get(daily_key, Decimal('0'))
        daily_limit = self.daily_limits.get(request.customer_id, self.daily_limits["default"])
        
        if current_daily_amount + request.amount > daily_limit:
            return PaymentResult(
                False,
                error_message=f"Превышен дневной лимит ({daily_limit})"
            )
        
        # Обрабатываем платеж
        result = self.router.process_payment_with_fallback(request)
        
        # Логируем транзакцию
        transaction_log_entry = {
            'timestamp': datetime.now().isoformat(),
            'customer_id': request.customer_id,
            'amount': str(request.amount),
            'currency': request.currency.value,
            'success': result.success,
            'transaction_id': result.transaction_id,
            'error': result.error_message
        }
        self.transaction_log.append(transaction_log_entry)
        
        # Обновляем дневной лимит при успешном платеже
        if result.success:
            self.processed_today[daily_key] = current_daily_amount + request.amount
        
        return result
    
    def get_transaction_history(self, customer_id: str, 
                               days: int = 30) -> List[Dict[str, Any]]:
        """Получение истории транзакций клиента"""
        cutoff_date = datetime.now() - timedelta(days=days)
        
        return [
            log for log in self.transaction_log
            if (log['customer_id'] == customer_id and 
                datetime.fromisoformat(log['timestamp']) > cutoff_date)
        ]
    
    def get_daily_statistics(self) -> Dict[str, Any]:
        """Получение дневной статистики"""
        today = datetime.now().date()
        today_transactions = [
            log for log in self.transaction_log
            if datetime.fromisoformat(log['timestamp']).date() == today
        ]
        
        successful = [t for t in today_transactions if t['success']]
        failed = [t for t in today_transactions if not t['success']]
        
        total_amount = sum(Decimal(t['amount']) for t in successful)
        
        return {
            'date': today.isoformat(),
            'total_transactions': len(today_transactions),
            'successful_transactions': len(successful),
            'failed_transactions': len(failed),
            'total_amount': str(total_amount),
            'success_rate': f"{len(successful) / len(today_transactions) * 100:.1f}%" if today_transactions else "0%"
        }

# Демонстрация использования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Создаем и настраиваем сервис
payment_service = PaymentService()
payment_service.setup_providers()

# Обрабатываем различные платежи
test_payments = [
    PaymentRequest(
        amount=Decimal('1500.00'),
        currency=Currency.RUB,
        description="Оплата заказа #12345",
        customer_id="customer_001",
        order_id="order_12345"
    ),
    PaymentRequest(
        amount=Decimal('50.00'),
        currency=Currency.USD,
        description="Подписка Premium",
        customer_id="customer_002"
    ),
    PaymentRequest(
        amount=Decimal('25000.00'),
        currency=Currency.RUB,
        description="Покупка ноутбука",
        customer_id="customer_001"
    )
]

print("=== Обработка платежей ===")
for i, payment_request in enumerate(test_payments, 1):
    print(f"\nПлатеж {i}:")
    result = payment_service.process_payment(payment_request)
    
    if result.success:
        print(f"✅ Успешно: {result.transaction_id}")
    else:
        print(f"❌ Ошибка: {result.error_message}")

# Статистика
print("\n=== Дневная статистика ===")
stats = payment_service.get_daily_statistics()
for key, value in stats.items():
    print(f"{key}: {value}")

# История транзакций
print("\n=== История транзакций customer_001 ===")
history = payment_service.get_transaction_history("customer_001")
for transaction in history:
    status = "✅" if transaction['success'] else "❌"
    print(f"{status} {transaction['amount']} {transaction['currency']} - {transaction.get('error', 'Успешно')}")
```

**Коммерческое применение:** Такая архитектура используется в финтех-компаниях (Тинькофф, Сбербанк, ЮMoney) для обработки миллионов платежей в день с высокой надежностью и возможностью переключения между провайдерами.

## 🎯 Ключевые принципы для собеседования

### 1. **Демонстрация прогрессии сложности**

- Начинайте с простых примеров
- Постепенно добавляйте сложность
- Объясняйте, почему нужно усложнение


### 2. **Связь с реальными задачами**

- Всегда приводите примеры из продакшена
- Объясняйте бизнес-логику
- Показывайте понимание масштабирования


### 3. **Архитектурное мышление**

- Обосновывайте выбор паттернов
- Показывайте понимание trade-offs
- Демонстрируйте знание SOLID принципов


### 4. **Практические навыки**

- Пишите рабочий код
- Добавляйте обработку ошибок
- Включайте логирование и мониторинг

Этот подход поможет продемонстрировать на собеседовании не только знание синтаксиса Python, но и понимание того, как ООП применяется для решения реальных бизнес-задач в коммерческой разработке.

