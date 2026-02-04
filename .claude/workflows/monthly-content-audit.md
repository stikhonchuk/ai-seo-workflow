# Monthly Workflow: Content Audit Integration

## Когда запускать

**Последний день месяца** - перед созданием monthly report

## Команда

```bash
cd /home/serge/Sites/[YOUR-PROJECT]
venv/bin/python scripts/content_audit/main.py --full
```

⏱️ Время: ~10 минут для 585 страниц

## Что произойдёт

1. **Парсинг sitemap.xml** → найдёт все страницы блога и категорий
2. **Скрейпинг страниц** → соберёт title, H1, meta, word count
3. **Извлечение ключей** → топ-10 keywords для каждой страницы
4. **Обогащение GSC** → добавит клики, показы, позиции
5. **Генерация отчётов** → создаст CSV, JSON, Markdown

## Выходные файлы

```
research/content-audit/
├── site-content-audit-2026-01-31.csv   ← Датированный отчёт (архивируется)
├── site-content-audit-latest.csv       ← Symlink на последний (использовать)
├── content-gaps-2026-01-31.md          ← Датированный анализ
├── content-gaps-latest.md              ← Symlink на последний
└── audit-log.txt                       ← Лог выполнения
```

**Примечание:** Используйте файлы `*-latest.*` для работы - они всегда указывают на самый свежий отчёт. Датированные файлы сохраняются для истории.

## Как использовать результаты

### 1. Для Monthly Report

#### Данные для отчёта

**Таблица опубликованного контента:**
- Откройте `site-content-audit-latest.csv`
- Фильтр по датам: `lastmod` за отчётный месяц
- Используйте колонки: `title`, `word_count`, `url`

**Таблица "Текущая эффективность контента":**
- Откройте `content-gaps-latest.md`
- Скопируйте секцию "Top 10 Performing Pages (by clicks)"
- Это уже готовая таблица с топ-10 страниц по трафику

**Метрики для анализа:**
- `yandex_clicks` - клики Yandex Webmaster
- `yandex_impressions` - показы Yandex
- `yandex_position` - средняя позиция Yandex
- `gsc_clicks` - клики Google Search Console
- `word_count` - объём контента

**Шаблон отчёта:** [`.claude/workflows/MONTHLY_REPORT_TEMPLATE.md`](MONTHLY_REPORT_TEMPLATE.md)

### 2. Для планирования следующего месяца

Откройте `site-content-audit-latest.csv`:
- Колонка `top_keywords` - уже используемые темы
- Проверьте перед планированием новых статей
- Избегайте дублирования ключевых слов

**Пример:**
```bash
# Найти все статьи про лоферы
grep -i "лоферы" research/content-audit/site-content-audit.csv

# Найти статьи про Premiata
grep -i "premiata" research/content-audit/site-content-audit.csv
```

### 3. Для выявления content gaps

Откройте `content-gaps.md`:
- Раздел "Content Gaps (Low Word Count Pages)"
- Страницы с <300 словами
- Кандидаты для расширения/доработки

### 4. Для отслеживания прогресса

Сравните с предыдущим месяцем:
```bash
# Посмотреть статистику
cat research/content-audit/site-content-audit.json | grep -A 10 "summary"
```

## Обновление только GSC данных (опционально)

Если нужно обновить только метрики без повторного скрейпинга:

```bash
venv/bin/python scripts/content_audit/main.py --update-webmaster
```

⏱️ Время: ~30 секунд (использует кэш страниц)

## Частота запуска

| Режим | Когда | Зачем |
|-------|-------|-------|
| `--full` | Конец месяца | Monthly report + планирование |
| `--update-webmaster` | Середина месяца (опц.) | Обновить только GSC метрики |
| `--sitemap-only` | По необходимости | Быстрый просмотр структуры |

## Интеграция с Monthly Report Skill

При запуске `/monthly-report`:
1. Сначала запустить `--full` аудит
2. Затем использовать свежие данные из CSV для отчёта
3. Включить insights из `content-gaps.md`

## Troubleshooting

**Ошибка "Module not found":**
```bash
# Переустановить зависимости
venv/bin/pip install -r scripts/content_audit/requirements.txt
```

**Ошибка "Permission denied":**
```bash
# Сделать main.py исполняемым
chmod +x scripts/content_audit/main.py
```

**Слишком медленно:**
- Нормально: ~10 минут для 585 страниц
- Delay 0.5 сек между запросами (вежливость к серверу)
- Используйте `--update-webmaster` для быстрого обновления GSC

## Хранение результатов

- Все отчёты перезаписываются при каждом запуске
- Если нужна история - сохраните CSV с датой:
  ```bash
  cp research/content-audit/site-content-audit.csv \
     research/content-audit/archive/audit-2026-01-31.csv
  ```
