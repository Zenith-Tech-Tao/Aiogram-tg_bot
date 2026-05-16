# 🤖aiogram-handbook

## О проекте

**aiogram-handbook** — это личный проект-конспект по библиотеке aiogram.

Проект создавался во время изучения разработки Telegram-ботов на Python и используется как:

* практическая база знаний
* шпаргалка
* набор рабочих примеров
* личная документация
* место для экспериментов

Главная цель проекта — сохранить основные механики aiogram, чтобы спустя время можно было быстро вспомнить:

* как работает библиотека
* как строится архитектура ботов
* как писать handlers
* как подключать API
* как использовать FSM
* как работать с базой данных
* как организовывать Telegram-ботов

---

# Важное

Этот репозиторий не является production-проектом.

Он создавался исключительно для:

* обучения
* практики
* экспериментов
* закрепления знаний

Некоторые части кода:

* могут повторяться
* могут быть написаны неидеально
* содержат временные решения
* сделаны как эксперименты
* отражают процесс обучения

И это нормально.

Главная ценность проекта — не «идеальный код», а сохранённый опыт и практические примеры.

---

# Технологии

Проект использует:

* Python 3
* aiogram 3
* asyncio
* aiohttp
* SQLite
* aiosqlite
* Telegram Bot API

---

# Структура проекта

Проект разделён на отдельные папки по темам.

Практически в каждой папке используется одинаковая структура:

```text
main.py
routes.py
config.py
```

Где:

* `main.py` — запуск бота
* `routes.py` — основная логика
* `config.py` — токены и API-ключи

---

# Разделы проекта

## 📁 Базовые команды

Изучение:

* Command handlers
* message handlers
* filters
* parse_mode
* работа с Message
* HTML-разметка Telegram

Что реализовано:

```python
@bot.message(Command("start"))
async def start(message: Message):
```

Функции:

* `/start`
* `/help`
* `/info`
* обработка текста
* получение данных пользователя
* форматирование сообщений

Также изучалось:

* `F.text`
* `message.answer()`
* `parse_mode='HTML'`
* получение username/id

---

## 📁 Интеграция с внешними API

Изучение:

* aiohttp
* async requests
* JSON
* работа с API
* обработка ошибок

Что реализовано:

* API шуток
* погодный бот
* OpenWeather API

Пример:

```python
async with aiohttp.ClientSession() as session:
```

Изучались:

* GET-запросы
* response.json()
* status codes
* try/except
* асинхронные HTTP-запросы

---

## 📁 Клавиатуры ReplyKeyboard и InlineKeyboard

Изучение:

* ReplyKeyboardMarkup
* InlineKeyboardMarkup
* callback_query
* callback_data
* inline buttons
* reply buttons

Что реализовано:

```python
InlineKeyboardButton(text='Мой Github', url='...')
```

Изучались:

* inline-кнопки
* callback handlers
* URL-кнопки
* reply keyboard
* взаимодействие через callback_query

---

## 📁 Машина состояний (FSM)

Изучение:

* FSMContext
* states
* Form
* пошаговые формы
* хранение временных данных
* валидация

Что реализовано:

* анкета пользователя
* проверка возраста
* проверка email
* отмена анкеты
* хранение состояний

Пример:

```python
await state.set_state(Form.name)
```

Изучались:

* state.update_data()
* state.get_data()
* state.clear()
* FSM flow

---

## 📁 Хранение данных SQLite + aiosqlite

Изучение:

* SQLite
* SQL
* async database
* CRUD-операции
* таблицы

Что реализовано:

* создание БД
* регистрация пользователей
* сохранение данных
* получение данных
* вывод пользователей

Пример:

```python
async with aiosqlite.connect(DB) as db:
```

Изучались:

* CREATE TABLE
* INSERT
* SELECT
* commit()
* fetchall()

---

## 📁 Проект — Telegram-бот “Личный трекер привычек”

Небольшой практический проект на основе изученного материала.

Использовалось:

* aiogram
* SQLite
* callback_query
* inline keyboard
* message handlers
* async architecture
* хранение данных

Возможности:

* добавление привычек
* хранение описаний
* просмотр привычек
* взаимодействие через кнопки
* сохранение информации в БД

---

# AI_routes.py

В проекте присутствует файл:

```text
AI_routes.py
```

Это экспериментальная часть проекта.

Часть логики генерировалась ИИ для:

* сравнения архитектуры
* анализа подходов
* экспериментов
* изучения того, как ИИ видит структуру aiogram-проектов

Основная логика проекта всё равно писалась вручную.

---

# Что изучалось в проекте

В ходе проекта затрагивались:

* async/await
* routers
* handlers
* filters
* Telegram Bot API
* FSM
* callback_query
* keyboards
* aiohttp
* SQLite
* aiosqlite
* архитектура aiogram 3
* обработка ошибок
* работа с JSON
* работа с API
* организация проекта

---

# Примеры изученных механик

## Получение данных пользователя

```python
user_id = message.from_user.id
username = message.from_user.username
```

---

## Обработка callback_query

```python
@bot.callback_query(lambda c: c.data == 'history')
```

---

## Работа с FSM

```python
await state.update_data(name=message.text)
```

---

## Работа с БД

```python
await db.execute('''INSERT INTO users ...''')
```

---

## Работа с API

```python
data = await response.json()
```

---

# Безопасность

Файл `config.py` не загружается в GitHub намеренно.

Некоторые токены могут присутствовать в тестовых примерах, но используются исключительно для временных и учебных проектов.

Для реальных проектов рекомендуется:

```python
from dotenv import load_dotenv
import os
```

И использование:

* `.env`
* `.gitignore`
* скрытых API-ключей

---

# Цель репозитория

Этот репозиторий нужен прежде всего самому автору.

Это:

* личный handbook
* база знаний
* архив практики
* коллекция примеров
* способ не забыть изученный материал

Чтобы через время можно было открыть проект и быстро восстановить в памяти:

* архитектуру aiogram
* работу FSM
* клавиатуры
* БД
* API
* async-подход
* структуру Telegram-ботов

---

# Статус проекта

```text
Learning / Practice Project
```

Проект продолжает дополняться по мере изучения новых механик.

---

# Автор

ZenithTech TAO

Изучение:

* Telegram Bot Development
* Python
* aiogram
* async architecture
* databases
* API integration
