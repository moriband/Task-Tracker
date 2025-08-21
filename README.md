
# Task Tracker CLI

**Task Tracker CLI** — простой инструмент для управления задачами через командную строку.  
Позволяет добавлять, обновлять, удалять задачи и отслеживать их статус: `todo`, `in-progress`, `done`.  

Все задачи сохраняются в JSON-файле `tasks.json`.

---

## Установка

1. Скачайте проект или клонируйте репозиторий.
2. Убедитесь, что установлен Python 3.x.
3. Запускайте скрипт через командную строку:
```bash
python task_tracker.py <command> [arguments]
````

---

## Команды и использование

| Команда            | Аргументы                        | Описание                                                          | Пример                                                           |
| ------------------ | -------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------- |
| `add`              | `"Описание"` `[status]`          | Добавить задачу. Статус по умолчанию `todo`.                      | `python task_tracker.py add "Купить продукты"`                   |
| `update`           | `<id> "Новое описание" <status>` | Обновить описание и статус задачи                                 | `python task_tracker.py update 1 "Приготовить ужин" in-progress` |
| `delete`           | `<id>`                           | Удалить задачу по ID                                              | `python task_tracker.py delete 1`                                |
| `delete_all`       | —                                | Удалить все задачи                                                | `python task_tracker.py delete_all`                              |
| `mark-in-progress` | `<id>`                           | Отметить задачу как выполняемую                                   | `python task_tracker.py mark-in-progress 1`                      |
| `mark-done`        | `<id>`                           | Отметить задачу как выполненную                                   | `python task_tracker.py mark-done 1`                             |
| `list`             | `[status]`                       | Вывести все задачи или по статусу (`todo`, `in-progress`, `done`) | `python task_tracker.py list in-progress`                        |

---

## Формат задачи

Каждая задача хранится с полями:

* `id` — уникальный идентификатор
* `description` — описание задачи
* `status` — статус (`todo`, `in-progress`, `done`)
* `createdAt` — дата и время создания
* `updatedAt` — дата и время последнего изменения

---

## Примеры использования

```bash
# Добавление задач
python task_tracker.py add "Купить продукты"
python task_tracker.py add "Приготовить ужин"

# Просмотр всех задач
python task_tracker.py list

# Обновление задачи
python task_tracker.py update 1 "Купить продукты и напитки" in-progress

# Отметить задачу как выполненную
python task_tracker.py mark-done 1

# Удалить задачу
python task_tracker.py delete 2

# Удалить все задачи
python task_tracker.py delete_all
```

---

## Примечания

* Все команды используют **позиционные аргументы**.
* Статусы должны быть точными: `todo`, `in-progress`, `done`.
* JSON-файл `tasks.json` не удаляйте вручную, иначе данные будут потеряны.

