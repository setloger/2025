
# Интенсивный план обучения Cloud-native разработка на Yandex Cloud (7-10 дней)

## Структура 10-дневного интенсивного курса

### **Дни 1-2: Основы Cloud-native и Yandex Cloud**

#### **День 1: Введение в Cloud-native архитектуру**

- **Теория (3 часа)**: Принципы cloud-native разработки, микросервисы vs монолит
- **Практика (5 часов)**: Настройка Yandex Cloud аккаунта, изучение консоли управления[^1]
- **Проект**: Развертывание простого Django приложения с использованием Yandex Cloud Apps[^1]
- **Критерии оценки**: Успешное развертывание первого приложения в облаке


#### **День 2: Serverless архитектура**

- **Теория**: Yandex Cloud Functions, API Gateway, Serverless Containers[^2]
- **Практика**: Создание serverless функций на Python, настройка API Gateway[^2]
- **Проект**: Разработка URL shortener с использованием serverless технологий[^2]
- **Критерии оценки**: Функциональное serverless приложение с API


### **Дни 3-4: Контейнеризация и Kubernetes**

#### **День 3: Docker и контейнеризация**

- **Теория**: Docker основы, создание образов, оптимизация размера
- **Практика**: Контейнеризация Python приложений, работа с Yandex Container Registry[^3]
- **Проект**: Создание multi-stage Docker образа для FastAPI приложения
- **Критерии оценки**: Оптимизированный Docker образ размером <100MB


#### **День 4: Managed Service for Kubernetes**

- **Теория**: Kubernetes основы, pods, services, deployments
- **Практика**: Создание Kubernetes кластера в Yandex Cloud, развертывание приложений[^3]
- **Проект**: Развертывание микросервисной архитектуры в Kubernetes[^3]
- **Критерии оценки**: Работающий кластер с автоматическим масштабированием


### **Дни 5-6: Микросервисы и интеграции**

#### **День 5: Архитектура микросервисов**

- **Теория**: Service mesh, межсервисное взаимодействие, паттерны отказоустойчивости
- **Практика**: Создание системы микросервисов с использованием FastAPI
- **Проект**: E-commerce платформа с отдельными сервисами для пользователей, заказов, платежей[^4]
- **Критерии оценки**: Независимо развертываемые микросервисы с API


#### **День 6: Интеграция с облачными сервисами**

- **Теория**: Object Storage, Managed PostgreSQL, Redis, Message Queue
- **Практика**: Интеграция приложения с облачными базами данных и хранилищами
- **Проект**: Система обработки изображений с автоматическим изменением размера[^1]
- **Критерии оценки**: Полная интеграция с облачными сервисами


### **Дни 7-8: Мониторинг и безопасность**

#### **День 7: Мониторинг и логирование**

- **Теория**: Yandex Monitoring, Cloud Logging, метрики приложений
- **Практика**: Настройка мониторинга и алертов для приложений[^2]
- **Проект**: Система сбора метрик с визуализацией в Grafana[^2]
- **Критерии оценки**: Полноценная система мониторинга с алертами


#### **День 8: Безопасность и соответствие требованиям**

- **Теория**: Yandex Security Deck, управление доступом, шифрование данных[^5]
- **Практика**: Настройка IAM, анализ безопасности с помощью DSPM[^5]
- **Проект**: Защищенное API с JWT авторизацией и Smart Web Security[^2]
- **Критерии оценки**: Приложение с enterprise-уровнем безопасности


### **Дни 9-10: CI/CD и Production-ready решения**

#### **День 9: CI/CD пайплайны**

- **Теория**: GitLab CI/CD, автоматизация развертывания, canary releases
- **Практика**: Создание полного CI/CD пайплайна для микросервисов[^2]
- **Проект**: Автоматизированный пайплайн с тестированием и развертыванием[^2]
- **Критерии оценки**: Полностью автоматизированный процесс доставки кода


#### **День 10: Production optimization и масштабирование**

- **Теория**: Горизонтальное и вертикальное масштабирование, оптимизация производительности[^3]
- **Практика**: Настройка автоскейлинга, load testing, оптимизация ресурсов[^3]
- **Проект**: Production-ready система с автоматическим масштабированием
- **Критерии оценки**: Система выдерживает нагрузку 1000+ RPS


## Ключевые проекты

### **Проект 1: Serverless URL Shortener (Дни 1-2)**

- **Технологии**: Yandex Cloud Functions, API Gateway, Object Storage[^2]
- **Функционал**: Сокращение URL с аналитикой переходов
- **Демонстрирует**: Навыки serverless разработки


### **Проект 2: Микросервисная E-commerce платформа (Дни 3-6)**

- **Технологии**: Kubernetes, FastAPI, PostgreSQL, Redis[^3][^4]
- **Функционал**: Управление товарами, заказами, пользователями
- **Демонстрирует**: Архитектурные навыки и работу с контейнерами


### **Проект 3: Система мониторинга и безопасности (Дни 7-8)**

- **Технологии**: Yandex Monitoring, Security Deck, Grafana[^2][^5]
- **Функционал**: Сбор метрик, анализ безопасности, алерты
- **Демонстрирует**: Навыки DevOps и безопасности


### **Проект 4: CI/CD пайплайн с автоскейлингом (Дни 9-10)**

- **Технологии**: GitLab CI/CD, Kubernetes HPA, Load Balancer[^3][^2]
- **Функционал**: Автоматическое тестирование, развертывание, масштабирование
- **Демонстрирует**: Production-ready навыки


## Образовательные ресурсы

### **Официальная документация Yandex Cloud**

- Yandex Cloud Apps - для быстрого развертывания приложений[^1]
- Managed Kubernetes tutorials - для работы с контейнерами[^3]
- Serverless tutorials - для изучения serverless технологий[^2]


### **Практические материалы**

- GitHub репозитории с примерами кода от Yandex Cloud[^6]
- Официальные туториалы по интеграции сервисов[^2]
- Документация по специализациям партнеров[^6]


### **Дополнительные ресурсы**

- Kubernetes официальная документация
- Docker best practices
- Microservices patterns


## Система контроля прогресса

### **Ежедневные цели**

| День | Основная цель | Ключевые метрики |
| :-- | :-- | :-- |
| 1-2 | Освоение serverless | Работающее serverless приложение |
| 3-4 | Контейнеризация | Kubernetes кластер с приложением |
| 5-6 | Микросервисы | 3+ независимых сервиса |
| 7-8 | Мониторинг и безопасность | Полная система мониторинга |
| 9-10 | CI/CD и production | Автоматизированный пайплайн |

### **Критерии оценки**

1. **Техническая реализация**: Работоспособность всех компонентов
2. **Архитектурные решения**: Применение cloud-native принципов
3. **Безопасность**: Соответствие требованиям enterprise
4. **Производительность**: Способность выдерживать нагрузку

## Специфика Yandex Cloud

### **Уникальные возможности**

- **Yandex Cloud Apps**: Развертывание приложений одним кликом[^1]
- **Security Deck**: Комплексная платформа безопасности с AI[^5]
- **Интеграция с YandexGPT**: Для анализа безопасности и мониторинга[^5]


### **Специализации партнеров**

- **Infrastructure**: Миграция и настройка инфраструктуры[^6]
- **DevOps**: Создание микросервисной архитектуры[^6]
- **ML \& AI**: Интеллектуальные решения[^6]
- **Data Platform**: Корпоративные хранилища данных[^6]


## Признаки готовности к cloud-native разработке

### **Технические навыки**

- Самостоятельное проектирование облачной архитектуры
- Создание и управление Kubernetes кластерами
- Настройка CI/CD пайплайнов с автоматическим тестированием
- Реализация принципов безопасности на уровне enterprise


### **Практические результаты**

- Портфолио с 4 cloud-native проектами
- Опыт работы с serverless и контейнерными технологиями
- Знание специфики Yandex Cloud сервисов
- Понимание принципов масштабирования и мониторинга


### **Готовность к сертификации**

После завершения курса вы будете готовы к получению сертификации Yandex Cloud и участию в программах партнерских специализаций[^6], что откроет доступ к дополнительным бонусам и проектам стоимостью до 150,000 рублей.

<div style="text-align: center">⁂</div>

[^1]: https://yandex.cloud/en/services/cloud-apps

[^2]: https://yandex.cloud/en/docs/tutorials/serverless/

[^3]: https://yandex.cloud/en/docs/managed-kubernetes/tutorials/

[^4]: https://cloud.yandex.com/en/solutions/retail

[^5]: https://yandex.cloud/en/services/security-deck

[^6]: https://github.com/yandex-cloud/docs/blob/master/en/partner/specializations/index.md

[^7]: https://www.semanticscholar.org/paper/b79b77619dc71515587e138e55fd75b417954790

[^8]: https://www.globalknowledge.com/us-en/course/185595/cloud-native-development-bootcamp-cn-252/

[^9]: https://slashdot.org/software/p/Yandex-Cloud/alternatives

[^10]: https://www.vldb.org/pvldb/vol15/p3548-yan.pdf

[^11]: https://eajournals.org/ejcsit/vol13-issue-5-2025/aiops-transforming-management-of-large-scale-distributed-systems/

[^12]: https://webofproceedings.org/proceedings_series/article/artId/1789.html

[^13]: http://converter-magazine.info/index.php/converter/article/view/337

[^14]: https://ojs.bbwpublisher.com/index.php/IEF/article/view/7694

[^15]: https://www.revistaelite.itsqmet.edu.ec/index.php/elite/article/view/89

[^16]: https://www.emerald.com/insight/content/doi/10.1108/XJM-09-2020-0111/full/html

[^17]: http://ird.gov.ua/sep/doi/sep2023.02.050

[^18]: https://isprs-annals.copernicus.org/articles/IV-5/421/2018/

[^19]: http://pediatrics.aappublications.org/lookup/doi/10.1542/peds.147.3_MeetingAbstract.979

[^20]: https://yandex.cloud/en/services/cloud-registry

[^21]: https://www.slideteam.net/yandex-cloud-saas-platform-implementation-guide-cl-mm.html

[^22]: https://yandex.cloud/en/docs/overview/sdk/quickstart

[^23]: https://ehp.niehs.nih.gov/doi/10.1289/ehp.116-a245

[^24]: https://yandex.cloud/en/docs/getting-started/individuals/service-plan

[^25]: https://openmetal.io/resources/blog/serverless-computing-understanding-when-and-why-to-use-it/

[^26]: https://yandex.cloud/en-ru/cloud-boost

[^27]: https://training.linuxfoundation.org/training/introduction-to-serverless-on-kubernetes-lfs157/

[^28]: https://www.brandeis.edu/online/academics/course-descriptions/rseg-167.html

[^29]: https://fullscale.io/blog/cloud-architecture-best-practices-2025/

