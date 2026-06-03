# QA База знаний — iThive

База знаний для QA-тестирования модулей iThive. Obsidian + opencode AI + авто-индексация.

## Как работает

Яна пушит `.md` инструкции в свой GitLab → раз в сутки (или вручную) GitHub Actions запускает нейросеть → она анализирует изменения и обновляет базу.

```
Яна (GitLab)          GitHub Actions            QA База (GitHub)
     │                      │                        │
     ├── git push ──────────┤                        │
     │                      │  ┌──────────────────┐  │
     │                      ├──│ schedule / manual │  │
     │                      │  └──────────────────┘  │
     │                      │          │             │
     │                      │  ┌───────▼──────────┐  │
     │                      │  │ git ls-remote    │  │
     │                      │  │ GitLab API diff  │  │
     │                      │  │ download changes │  │
     │                      │  └───────┬──────────┘  │
     │                      │          │             │
     │                      │  ┌───────▼──────────┐  │
     │                      │  │ opencode AI      │  │
     │                      │  │ deepseek-v4-flash│  │
     │                      │  └───────┬──────────┘  │
     │                      │          │             │
     │                      │  ┌───────▼──────────┐  │
     │                      │  │ git commit+push  │──┤
     │                      │  └──────────────────┘  │
     │                      │                        │
```

## Как запустить вручную

1. Actions → Index from Yana → Run workflow
2. Или склонировать репо и запустить fetch.py с opеncode

## Безопасность

Репозиторий публичный, но запустить workflow могут только владельцы.
Ключи (GitLab, нейросеть) хранятся в GitHub Secrets — их никто не видит.

## Файлы

- `Instructions/` — 223 инструкции по 16 модулям
- `Modules/` — 16 файлов модулей
- `MOC - Инструкции.md` — оглавление
- `fetch.py` — Python-скрипт для GitLab API
- `prompt.txt` — промпт для нейросети
- `.github/workflows/index.yml` — workflow CI
- `.yana_last_commit` — хеш последнего обработанного коммита Яны
