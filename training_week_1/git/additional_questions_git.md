# 1. "pull request"
# 2. "GitFlow"
# 3. "GitHub Flow"
# 4. "SLA"
# 5. "GitHub Actions для автоматизации"
# 6. "Настройка branch protection rules"
# 7. "issues"
# 8. "Git hooks". 
# 9. "upstream"
# 10. "fork
# 11. "force push"


## **1. Pull Request (PR) - основа командной разработки**

Pull Request - это механизм предложения изменений в проект[^1]. Представь, что ты работаешь над новой функцией в отдельной ветке и хочешь добавить свои изменения в основную ветку проекта.

**Жизненный цикл PR:**

1. **Создание ветки** - ты создаешь feature-ветку от main
2. **Разработка** - пишешь код, делаешь коммиты
3. **Создание PR** - открываешь pull request для ревью
4. **Код-ревью** - коллеги проверяют твой код
5. **Исправления** - вносишь правки по комментариям
6. **Мерж** - изменения добавляются в основную ветку[^1]

**Практический пример:**
Допустим, ты работаешь в команде над интернет-магазином. Тебе поручили добавить функцию "Избранные товары":

```bash
# 1. Создаешь ветку
git checkout -b feature/favorites-functionality

# 2. Пишешь код, делаешь коммиты
git add .
git commit -m "Add favorites model and database migration"
git commit -m "Implement add/remove favorites API endpoints"
git commit -m "Add favorites UI components"

# 3. Пушишь ветку
git push origin feature/favorites-functionality

# 4. Создаешь PR через GitHub интерфейс
```

**Хороший PR должен содержать:**

- Описательное название: "Add user favorites functionality"
- Детальное описание изменений
- Скриншоты UI изменений
- Ссылки на связанные задачи
- Чек-лист для ревьюера[^1]


## **2. GitFlow - стратегия для больших проектов**

GitFlow - это модель ветвления для проектов с регулярными релизами[^2]. Она создана для команд, которые выпускают версии продукта по расписанию.

**Структура веток в GitFlow:**

**Main/Master ветка** - только стабильный код для продакшена
**Develop ветка** - интеграционная ветка для разработки
**Feature ветки** - для новых функций (от develop)
**Release ветки** - подготовка к релизу (от develop)
**Hotfix ветки** - критические исправления (от main)

**Практический пример:**
Представь, что ты работаешь в банке над мобильным приложением. У вас релизы каждый месяц:

```bash
# Инициализация GitFlow
git flow init

# Работа над новой функцией "Перевод по QR-коду"
git flow feature start qr-transfer
# ... разработка ...
git flow feature finish qr-transfer

# Подготовка релиза версии 2.1.0
git flow release start 2.1.0
# ... тестирование, исправление багов ...
git flow release finish 2.1.0

# Критический баг в продакшене
git flow hotfix start critical-security-fix
# ... исправление ...
git flow hotfix finish critical-security-fix
```

**Когда использовать GitFlow:**

- Большие команды (10+ разработчиков)
- Регулярные релизы по расписанию
- Необходимость поддерживать несколько версий
- Высокие требования к стабильности


## **3. GitHub Flow - простота для быстрой разработки**

GitHub Flow - упрощенная альтернатива GitFlow для команд с непрерывной интеграцией[^3]. Основной принцип: main ветка всегда готова к деплою.

**Процесс GitHub Flow:**

1. **Создай ветку** от main с описательным именем[^3]
2. **Делай коммиты** с понятными сообщениями
3. **Открой PR** для обсуждения изменений
4. **Проведи ревью** с командой
5. **Задеплой** для тестирования
6. **Смержи** в main после одобрения[^3]

**Практический пример:**
Ты работаешь в стартапе над SaaS продуктом с ежедневными деплоями:

```bash
# 1. Создаешь ветку для исправления бага
git checkout -b fix-user-registration-validation

# 2. Исправляешь баг
git add .
git commit -m "Fix email validation in user registration"

# 3. Пушишь и создаешь PR
git push origin fix-user-registration-validation
# Создаешь PR через GitHub

# 4. После ревью и тестов - мерж
# 5. Автоматический деплой в продакшен
```

**Преимущества GitHub Flow:**

- Простота понимания
- Быстрые циклы разработки
- Подходит для непрерывной интеграции
- Меньше веток = меньше конфликтов


## **4. SLA - гарантии качества сервиса**

SLA (Service Level Agreement) - это договор между поставщиком услуг и клиентом, определяющий уровень сервиса[^4]. В контексте GitHub - это гарантии доступности и производительности.

**Основные элементы SLA:**

- **Время доступности** (uptime) - обычно 99.9%
- **Время отклика** - максимальное время ответа сервиса
- **Время восстановления** - как быстро исправляются проблемы
- **Штрафы** - что происходит при нарушении SLA[^4]

**Практический пример GitHub SLA:**

```
GitHub Enterprise SLA:
- Uptime: 99.95% в месяц
- Время отклика API: < 200ms для 95% запросов
- Поддержка: ответ в течение 8 часов для критических проблем
- Компенсация: скидка 25% при uptime < 99.0%
```

**Почему это важно для разработчика:**

- Понимание надежности инфраструктуры
- Планирование работы с учетом возможных простоев
- Выбор подходящего тарифного плана


## **5. GitHub Actions - автоматизация рабочих процессов**

GitHub Actions - это CI/CD платформа для автоматизации задач разработки[^5]. Она позволяет автоматически запускать код при определенных событиях.

**Основные концепции:**

- **Workflow** - автоматизированный процесс
- **Job** - набор шагов, выполняемых на одном runner
- **Step** - отдельная задача в job
- **Action** - переиспользуемая единица кода

**Практический пример - CI/CD для Node.js приложения:**

```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test
    
    - name: Run linter
      run: npm run lint

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to production
      run: |
        echo "Deploying to production..."
        # Команды для деплоя
```

**Автоматизация PR процесса:**

```yaml
# Автоматическое добавление PR в проект
name: Add PR to Project
on:
  pull_request:
    types: [ready_for_review]

jobs:
  add-to-project:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/add-to-project@v0.4.0
      with:
        project-url: https://github.com/orgs/myorg/projects/1
        github-token: ${{ secrets.ADD_TO_PROJECT_PAT }}
```


## **6. Branch Protection Rules - защита важных веток**

Branch Protection Rules - это настройки, которые защищают важные ветки от случайных или некачественных изменений[^6].

**Основные правила защиты:**

- **Require pull request reviews** - обязательное ревью перед мержем
- **Require status checks** - успешное прохождение CI/CD
- **Require branches to be up to date** - актуальность ветки
- **Restrict pushes** - ограничение прямых push'ей
- **Require signed commits** - подписанные коммиты[^6]

**Практический пример настройки:**

```bash
# Защита main ветки через GitHub CLI
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":["ci/tests","ci/lint"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":2}' \
  --field restrictions=null
```

**Настройки для коммерческого проекта:**

- **Main ветка:** минимум 2 ревью, прохождение всех тестов, актуальность
- **Develop ветка:** минимум 1 ревью, прохождение тестов
- **Feature ветки:** прохождение линтера и базовых тестов

**Паттерны защиты веток:**

```
main - полная защита
develop - средняя защита  
feature/* - базовая защита
hotfix/* - ускоренная процедура
release/* - строгие проверки
```


## **7. Issues - система управления задачами**

Issues - это встроенная в GitHub система отслеживания задач, багов и улучшений. Это центральное место для обсуждения работы над проектом.

**Типы Issues:**

- **Bug reports** - сообщения об ошибках
- **Feature requests** - предложения новых функций
- **Tasks** - рабочие задачи
- **Questions** - вопросы по проекту

**Практический пример Bug Report:**

```markdown
# Bug: Пользователь не может войти с валидным email

## Описание
При попытке входа с корректным email и паролем система выдает ошибку "Invalid credentials"

## Шаги воспроизведения
1. Открыть страницу /login
2. Ввести email: user@example.com
3. Ввести пароль: correctPassword123
4. Нажать "Sign In"

## Ожидаемое поведение
Пользователь должен войти в систему

## Фактическое поведение
Появляется ошибка "Invalid credentials"

## Окружение
- Browser: Chrome 120.0
- OS: macOS 14.0
- App version: 2.1.3

## Дополнительная информация
Проблема появилась после обновления до версии 2.1.3
```

**Связывание Issues с PR:**

```bash
# В сообщении коммита или описании PR
git commit -m "Fix login validation issue

Fixes #123"
# Автоматически закроет issue #123 при мерже
```


## **8. Git Hooks - автоматизация Git операций**

Git Hooks - это скрипты, которые автоматически выполняются при определенных Git событиях. Они позволяют автоматизировать проверки и действия.

**Типы хуков:**

- **pre-commit** - перед коммитом
- **commit-msg** - проверка сообщения коммита
- **pre-push** - перед отправкой на сервер
- **post-receive** - на сервере после получения изменений

**Практический пример pre-commit хука:**

```bash
#!/bin/sh
# .git/hooks/pre-commit

echo "Running pre-commit checks..."

# Проверка линтером
npm run lint
if [ $? -ne 0 ]; then
  echo "❌ Linting failed. Please fix errors before committing."
  exit 1
fi

# Запуск тестов
npm test
if [ $? -ne 0 ]; then
  echo "❌ Tests failed. Please fix tests before committing."
  exit 1
fi

# Проверка форматирования
npm run format:check
if [ $? -ne 0 ]; then
  echo "❌ Code formatting issues found. Run 'npm run format' to fix."
  exit 1
fi

echo "✅ All pre-commit checks passed!"
```

**Хук для проверки сообщений коммитов:**

```bash
#!/bin/sh
# .git/hooks/commit-msg

commit_regex='^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .{1,50}'

if ! grep -qE "$commit_regex" "$1"; then
    echo "❌ Invalid commit message format!"
    echo "Format: type(scope): description"
    echo "Example: feat(auth): add login validation"
    exit 1
fi
```

**Установка хуков через Husky (для Node.js проектов):**

```json
// package.json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged",
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
  },
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": ["eslint --fix", "prettier --write"]
  }
}
```


## **9. Upstream - связь с оригинальным репозиторием**

Upstream - это ссылка на оригинальный репозиторий, от которого был создан форк. Это критически важно для синхронизации изменений.

**Концепция upstream:**

- **Origin** - твой форк репозитория
- **Upstream** - оригинальный репозиторий
- **Local** - локальная копия на твоей машине

**Практический пример работы с upstream:**

```bash
# 1. Клонируешь свой форк
git clone https://github.com/yourusername/awesome-project.git
cd awesome-project

# 2. Добавляешь upstream
git remote add upstream https://github.com/original-owner/awesome-project.git

# 3. Проверяешь настройки remote
git remote -v
# origin    https://github.com/yourusername/awesome-project.git (fetch)
# origin    https://github.com/yourusername/awesome-project.git (push)
# upstream  https://github.com/original-owner/awesome-project.git (fetch)
# upstream  https://github.com/original-owner/awesome-project.git (push)

# 4. Синхронизируешь с upstream
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

**Рабочий процесс с upstream:**

```bash
# Ежедневная синхронизация
git fetch upstream
git rebase upstream/main
git push --force-with-lease origin main

# Создание feature ветки от актуального upstream
git checkout -b feature/new-functionality upstream/main
```


## **10. Форк - независимая копия репозитория**

Форк - это полная копия репозитория в твоем GitHub аккаунте. Это основа для контрибуций в open source проекты.

**Зачем нужны форки:**

- Контрибуции в чужие проекты
- Экспериментирование без риска
- Создание собственной версии проекта
- Обучение на реальном коде

**Практический пример контрибуции:**
Допустим, ты хочешь исправить баг в популярной библиотеке:

```bash
# 1. Форкаешь репозиторий через GitHub интерфейс

# 2. Клонируешь свой форк
git clone https://github.com/yourusername/popular-library.git
cd popular-library

# 3. Настраиваешь upstream
git remote add upstream https://github.com/maintainer/popular-library.git

# 4. Создаешь ветку для исправления
git checkout -b fix-memory-leak

# 5. Исправляешь баг
# ... код ...
git add .
git commit -m "Fix memory leak in data processing module"

# 6. Пушишь в свой форк
git push origin fix-memory-leak

# 7. Создаешь PR в оригинальный репозиторий
```

**Синхронизация форка:**

```bash
# Регулярное обновление форка
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# Обновление feature ветки
git checkout fix-memory-leak
git rebase upstream/main
git push --force-with-lease origin fix-memory-leak
```


## **11. Force Push - принудительная отправка изменений**

Force push - это принудительная перезапись истории в удаленном репозитории. Это мощный, но опасный инструмент.

**Когда используется force push:**

- После rebase feature ветки
- Исправление ошибок в коммитах
- Squashing коммитов
- Изменение истории в личных ветках

**Безопасный force push:**

```bash
# Вместо опасного git push --force
git push --force-with-lease origin feature-branch
```

**Практический пример:**

```bash
# Ситуация: нужно исправить сообщение последнего коммита
git commit --amend -m "Fix typo in user validation logic"

# Обычный push не сработает
git push origin feature-branch
# error: failed to push some refs

# Нужен force push
git push --force-with-lease origin feature-branch
```

**Правила безопасного force push:**

1. **Никогда не делай force push в shared ветки** (main, develop)
2. **Используй --force-with-lease** вместо --force
3. **Предупреждай команду** о планируемом force push
4. **Создавай backup ветки** перед сложными операциями

**Пример создания backup:**

```bash
# Создание резервной копии
git branch backup-feature-branch

# Выполнение rebase
git rebase -i HEAD~3

# Force push с предосторожностями
git push --force-with-lease origin feature-branch

# Если что-то пошло не так
git reset --hard backup-feature-branch
```

**Альтернативы force push:**

```bash
# Вместо изменения истории - создание нового коммита
git revert <commit-hash>
git push origin feature-branch

# Создание новой ветки вместо force push
git checkout -b feature-branch-v2
git push origin feature-branch-v2
```

Помни: force push может потерять работу коллег, поэтому всегда используй его осторожно и только в личных ветках!

Это основы, которые должен знать каждый разработчик для работы в команде. Есть вопросы по какой-то из тем?

<div style="text-align: center">⁂</div>

[^1]: https://www.pagerduty.com/resources/continuous-integration-delivery/learn/what-is-a-pull-request/

[^2]: https://www.edrawmax.com/article/gitflow-diagram.html

[^3]: https://www.w3schools.com/git/git_github_flow.asp?remote=github

[^4]: https://www.manageengine.com/products/service-desk/automation/what-is-service-level-agreement-sla.html

[^5]: https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/automating-projects-using-actions

[^6]: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule

[^7]: file.csv

[^8]: https://www.semanticscholar.org/paper/ca16ab513fa6299e1024ba6d9780254fe1118209

[^9]: https://docs.github.com/articles/about-pull-requests

[^10]: https://www.atlassian.com/git/tutorials/making-a-pull-request

[^11]: https://www.pullrequest.com/blog/writing-a-great-pull-request-description/

[^12]: https://docs.github.com/articles/creating-a-pull-request

[^13]: https://ieeexplore.ieee.org/document/8952330/

[^14]: https://dl.acm.org/doi/10.1145/3387940.3391503

[^15]: https://ieeexplore.ieee.org/document/11024482/

[^16]: https://ieeexplore.ieee.org/document/8813275/

[^17]: https://link.springer.com/10.1007/s10664-022-10143-4

[^18]: https://globalizationandhealth.biomedcentral.com/articles/10.1186/s12992-024-01019-x

[^19]: https://www.frontiersin.org/articles/10.3389/feart.2021.700550/full

[^20]: https://www.aaem.pl/Expectations-of-patients-with-hepatitis-C-from-family-physicians-a-Polish-example,157357,0,2.html

[^21]: https://ieeexplore.ieee.org/document/9474402/

