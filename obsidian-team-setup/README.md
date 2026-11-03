# Настройка и использование Obsidian + opencode для команды

Эта инструкция поможет каждому члену команды настроить рабочее окружение для работы с базой знаний ithive через Obsidian и opencode.

---

## 1. Установка Obsidian

### macOS

1. Перейди на [obsidian.md](https://obsidian.md)
2. Нажми **Download for Mac**
3. Открой скачанный `.dmg` файл
4. Перетащи **Obsidian.app** в папку **Applications**
5. Запусти Obsidian из Applications

### Windows

1. Перейди на [obsidian.md](https://obsidian.md)
2. Нажми **Download for Windows**
3. Запусти скачанный `.exe` установщик
4. Следуй инструкциям установщика
5. Запусти Obsidian

> Obsidian бесплатен для личного использования. Регистрация не обязательна, но рекомендуется для синхронизации.

---

## 2. Установка opencode

### macOS

**Через Homebrew (рекомендуется):**

```bash
# Если Homebrew не установлен, сначала установи его:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Установи opencode:
brew install opencode
```

**Вручную:**

1. Скачай последнюю версию с [GitHub Releases](https://github.com/anomalyco/opencode/releases)
2. Распакуй архив
3. Перемести бинарник в `/usr/local/bin/`:
   ```bash
   mv opencode /usr/local/bin/
   chmod +x /usr/local/bin/opencode
   ```

### Windows

**Через Scoop (рекомендуется):**

```powershell
# Если Scoop не установлен:
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex

# Установи opencode:
scoop install opencode
```

**Вручную:**

1. Скачай последнюю версию с [GitHub Releases](https://github.com/anomalyco/opencode/releases) (файл `.zip` для Windows)
2. Распакуй архив в удобную папку, например `C:\opencode\`
3. Добавь папку в PATH:
   - Открой **Параметры** → **Система** → **О системе** → **Дополнительные параметры системы**
   - Нажми **Переменные среды**
   - В разделе **Пользовательские переменные** найди `Path`, нажми **Изменить**
   - Добавь путь к папке с opencode
4. Перезапусти терминал и проверь:
   ```powershell
   opencode --version
   ```

---

## 3. Копирование проекта Obsidian

Вам предоставлен архив с готовой базой знаний.

### Шаги:

1. **Скачай архив** с проектом Obsidian (файл `.zip`)
2. **Распакуй архив** в удобную папку:
   - **macOS:** `/Users/ТВОЕ_ИМЯ/Documents/Obsidian`
   - **Windows:** `C:\Users\ТВОЕ_ИМЯ\Documents\Obsidian`
3. Убедись, что после распаковки структура папки выглядит так:
   ```
   Obsidian/
   ├── Instructions/
   ├── Modules/
   ├── Test Cases/
   ├── Templates/
   ├── MOC - Инструкции.md
   ├── MOC - Модули.md
   └── ...
   ```

> **Важно:** Запомни полный путь к папке Obsidian — он понадобится для настройки субагентов.

---

## 4. Открытие папки Obsidian

### macOS и Windows

1. Запусти **Obsidian**
2. Нажми **Open folder as vault**
3. Выбери папку `Obsidian`, которую ты распаковал на шаге 3
4. Vault откроется со всей структурой и файлами

---

## 5. Подключение субагентов с глобальной областью видимости

Субагенты подключаются через глобальную конфигурацию opencode, чтобы они были доступны в любом проекте.

> **Работаете в Cursor или Claude Code?** Этот раздел можно пропустить: субагенты
> `qa-teacher` и `qaithive` уже лежат в корне репозитория в `.cursor/agents/` и
> `.claude/agents/`. См. раздел 9.

### Шаг 1: Найди свою глобальную папку opencode

- **macOS:** `~/.config/opencode/` (или `/Users/ТВОЕ_ИМЯ/.config/opencode/`)
- **Windows:** `%APPDATA%\opencode\` (или `C:\Users\ТВОЕ_ИМЯ\AppData\Roaming\opencode\`)

### Шаг 2: Создай папку для агентов

```bash
# macOS
mkdir -p ~/.config/opencode/agent

# Windows (PowerShell)
New-Item -ItemType Directory -Force -Path "$env:APPDATA\opencode\agent"
```

### Шаг 3: Скопируй файлы субагентов

Скопируй файлы из папки `agents/` (которая идёт в архиве) в глобальную папку `agent/`:

```bash
# macOS — скопируй все три файла:
cp obsidian-indexer.md ~/.config/opencode/agent/
cp qa-teacher.md ~/.config/opencode/agent/
cp qaithive.md ~/.config/opencode/agent/

# Windows (PowerShell):
Copy-Item obsidian-indexer.md "$env:APPDATA\opencode\agent\"
Copy-Item qa-teacher.md "$env:APPDATA\opencode\agent\"
Copy-Item qaithive.md "$env:APPDATA\opencode\agent\"
```

### Шаг 4: Укажи путь к своему Obsidian vault

Открой файл `~/.config/opencode/agent/obsidian-indexer.md` в любом текстовом редакторе.

Найди строку:

```
`/Users/YOUR_USERNAME/Documents/Obsidian`
```

Замени `YOUR_USERNAME` на своё имя пользователя:

- **macOS:** `/Users/aleksandr/Documents/Obsidian`
- **Windows:** `C:\Users\aleksandr\Documents\Obsidian`

> **Важно:** Путь должен быть точным. Если vault лежит в другом месте, укажи свой полный путь.

### Шаг 5: Проверь что субагенты подключены

Запусти opencode в любом проекте:

```bash
opencode
```

Введи `/agents` — ты должен увидеть три субагента:
- `obsidian-indexer`
- `qa-teacher`
- `qaithive`

---

## 6. Подключение других нейросетей к opencode

opencode поддерживает различные AI-провайдеры. По умолчанию используется бесплатная модель **qwen3.6-plus-free**.

### Добавление API-ключа

Создай или отредактируй файл `~/.config/opencode/opencode.jsonc`:

```bash
# macOS
nano ~/.config/opencode/opencode.jsonc

# Windows
notepad %APPDATA%\opencode\opencode.jsonc
```

### Пример конфигурации с несколькими провайдерами

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "openai": {
      "apiKey": "sk-...",
      "models": {
        "gpt-4o": {
          "name": "gpt-4o",
          "provider": "openai"
        },
        "gpt-4o-mini": {
          "name": "gpt-4o-mini",
          "provider": "openai"
        }
      }
    },
    "anthropic": {
      "apiKey": "sk-ant-...",
      "models": {
        "claude-sonnet-4-20250514": {
          "name": "claude-sonnet-4-20250514",
          "provider": "anthropic"
        }
      }
    },
    "qwen": {
      "apiKey": "your-qwen-api-key",
      "models": {
        "qwen3.6-plus-free": {
          "name": "qwen3.6-plus-free",
          "provider": "qwen"
        }
      }
    }
  }
}
```

### Переключение модели в opencode

Внутри opencode используй команду:

```
/model qwen3.6-plus-free
```

или

```
/model gpt-4o
```

### Бесплатные модели

- **qwen3.6-plus-free** — бесплатная, рекомендуется для работы с субагентами
- Другие бесплатные модели зависят от провайдера — проверяй документацию opencode

---

## 7. Описание субагентов и их задачи

### @obsidian-indexer

**Задача:** Индексирует инструкции в Obsidian vault.

> База индексируется автоматически раз в сутки в 10:00 UTC.
> Новые и изменённые инструкции из source-репозитория обрабатываются
> нейросетью без ручного вмешательства. Ручная индексация через
> субагент нужна только для исключительных случаев.

**Что делает:**
- Анализирует контент инструкций
- Определяет модуль и тему
- Создаёт файлы с wikilinks, тегами и properties
- Обновляет MOC-файлы и файлы модулей

**Что НЕ делает:**
- Не создаёт тест-кейсы и чек-листы (это делает @qaithive)

**Когда использовать:**
- Когда нужно добавить новую инструкцию в базу знаний
- Когда нужно обновить существующую инструкцию

---

### @qa-teacher

**Задача:** Отвечает на вопросы по модулям ithive, используя базу знаний Obsidian.

**Что делает:**
- Отвечает на вопросы по настройке модулей
- Объясняет как работает функциональность
- Даёт пошаговые инструкции
- Показывает связи между модулями

**Что НЕ делает:**
- Не создаёт, не редактирует и не удаляет файлы
- Не запускает bash-команды

**Когда использовать:**
- Когда нужно быстро узнать как что-то настроить
- Когда нужен ответ на вопрос по функциональности модуля
- Когда нужно найти связь между модулями

---

### @qaithive

**Задача:** Создаёт чек-листы проверок для QA на основе задачи и базы знаний Obsidian.

**Что делает:**
- Анализирует условие задачи
- Изучает базу знаний Obsidian
- Создаёт детальные чек-листы с техниками тест-дизайна
- Сохраняет чек-листы в папку `Test Cases/` (по запросу)

**Что включает чек-лист:**
- Позитивные проверки (Happy Path)
- Негативные проверки
- Граничные значения
- Интеграционные проверки
- UI/UX проверки
- Регрессионные проверки

**Когда использовать:**
- Когда нужно составить чек-лист для новой фичи
- Когда нужен чек-лист регрессионного тестирования
- Когда нужно проверить баг-фикс

---

## 8. Как пользоваться субагентами в работе

### Вызов субагента

В opencode субагенты вызываются через `@` в сообщении:

```
@obsidian-indexer проиндексируй инструкцию по модулю HelpDesk
```

```
@qa-teacher как настроить уведомления в HelpDesk?
```

```
@qaithive создай чек-лист для проверки создания тикета в HelpDesk
```

### Типичные сценарии работы

#### Сценарий 1: Добавление новой инструкции

1. Скопируй текст инструкции
2. В opencode напиши:
   ```
   @obsidian-indexer [вставь инструкцию]
   ```
3. Субагент создаст файл в `Instructions/`, обновит MOC и файл модуля

#### Сценарий 2: Вопрос по модулю

1. В opencode напиши:
   ```
   @qa-teacher как покрасить фон виджета на главной странице?
   ```
2. Субагент найдёт ответ в базе знаний и даст развёрнутый ответ

#### Сценарий 3: Создание чек-листа

1. В opencode напиши:
   ```
   @qaithive задача: добавить возможность экспорта тикетов в CSV в модуле HelpDesk. Создай чек-лист и сохрани его.
   ```
2. Субагент изучит базу знаний, создаст чек-лист и сохранит в `Test Cases/`

#### Сценарий 4: Комплексная проверка

1. Сначала проиндексируй новую инструкцию:
   ```
   @obsidian-indexer [инструкция]
   ```
2. Затем задай вопрос по ней:
   ```
   @qa-teacher как работает экспорт в CSV?
   ```
3. Затем создай чек-лист:
   ```
   @qaithive создай чек-лист для проверки экспорта в CSV
   ```

### Полезные команды opencode

| Команда | Описание |
|---------|----------|
| `/agents` | Показать доступных субагентов |
| `/model` | Переключить модель |
| `/help` | Показать справку |
| `@имя-субагента` | Вызвать конкретного субагента |

### Советы

- Всегда указывай **модуль** в запросе — это поможет субагенту быстрее найти нужную информацию
- Если субагент не может определить модуль — он спросит тебя
- Для индексации больших документов — разбивай их на логические части
- Субагенты используют **wikilinks** `[[ ]]` для связей — это работает только в Obsidian

---

## 9. Cursor и Claude Code — субагенты уже в репозитории

Субагенты `qa-teacher` и `qaithive` лежат в корне этого репозитория в двух форматах,
поэтому после клонирования ничего вручную создавать не нужно:

```
qa-knowledge-base/
├── .cursor/
│   └── agents/
│       ├── qa-teacher.md     # readonly: true
│       └── qaithive.md
├── .claude/
│   └── agents/
│       ├── qa-teacher.md     # tools: Read, Grep, Glob
│       └── qaithive.md       # tools: Read, Grep, Glob, Write, Edit
├── Instructions/
├── Modules/
└── ...
```

### 9.1 Отличия синтаксиса

| | opencode | Cursor (`.cursor/agents/`) | Claude Code (`.claude/agents/`) |
|---|---|---|---|
| Обязательные поля | — | `name`, `description` | `name`, `description` |
| Запрет правок | `permission: edit: deny` | `readonly: true` | нет `Write`/`Edit` в `tools` |
| Модель | — | `model: inherit` | `model:` можно не указывать |
| Вызов | `@qa-teacher` | `/qa-teacher` | «Use the qa-teacher subagent» или `@qa-teacher` |

> Cursor читает и `.claude/agents/` (Claude-совместимость), но поле `tools` там
> игнорируется. Поэтому для Cursor лежат отдельные файлы в `.cursor/agents/`
> с `readonly: true` — при совпадении имён `.cursor/` имеет приоритет.

Сами тела агентов общие — различается только frontmatter. Исходные версии для
opencode остались в `obsidian-team-setup/agents/`.

### 9.2 Вариант A — относительный путь (по умолчанию, ничего настраивать не нужно)

В обоих файлах блок «База знаний» указывает на корень репозитория, а все пути
(`00 - Index.md`, `Modules/`, `Instructions/`, `Architecture.md`, `Test Cases/`)
считаются от него.

**Что нужно:** просто открыть папку репозитория — в Cursor как проект, в Claude Code
запустить `claude` из корня. Всё остальное агенты найдут сами.

**Как вызвать:**

```
/qa-teacher как настроить уведомления в HelpDesk?
/qaithive создай чек-лист для проверки создания тикета в HelpDesk
```

В Claude Code — та же формулировка, но через упоминание или просьбу делегировать:

```
@qa-teacher как настроить SLA в HelpDesk?
Use the qaithive subagent to create a checklist for the CSV export feature
```

Этот вариант подходит, если папка базы знаний и есть клон репозитория — тогда
у всех одинаковые файлы и настройка не нужна.

### 9.3 Вариант B — абсолютный путь (если vault лежит отдельно от репозитория)

Если база знаний хранится, например, в `/Users/ИМЯ/Documents/Obsidian`, а агенты
лежат в другом месте (или в глобальной папке `~/.cursor/agents/`), замените блок
«База знаний» в начале каждого файла на абсолютный путь:

```
## База знаний

База знаний: `/Users/ИМЯ/Documents/Obsidian`

Пути ниже считаются от этой папки:
- `00 - Index.md`
- `Modules/Module - {Название}.md`
- `Instructions/{Module} - {Topic}.md`
- `Test Cases/{Module} - {Topic}.md`
- `Architecture.md`
```

- **macOS:** `/Users/ИМЯ/Documents/Obsidian`
- **Windows:** `C:\Users\ИМЯ\Documents\Obsidian`

> Такие правки персональные: не коммитьте их в общий репозиторий, иначе
> перезапишете пути у остальных. Для личного использования проще положить копию
> файлов в `~/.cursor/agents/` или `~/.claude/agents/` и указать там абсолютный путь.

### 9.4 Права субагентов

- **qa-teacher** — только чтение: в Cursor `readonly: true`, в Claude нет `Write`/`Edit`
  среди `tools`. Создавать, менять и удалять файлы он не может, shell-команды не запускает.
- **qaithive** — пишет только в `Test Cases/`. В Claude у него есть `Write`/`Edit`
  (без `Bash`), в Cursor — обычный режим с явным ограничением по папке в промпте.

> **@obsidian-indexer** отдельным субагентом здесь не нужен — индексация
> происходит автоматически раз в сутки в 10:00 UTC.
