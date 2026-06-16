---
title: "Карта офиса - REST API. Служебные методы"
module: "Карта офиса + Бронирование"
type: instruction
version: "8.0.0"
created: 2026-06-16
updated: 2026-06-16
tags:
  - type/instruction
  - module/workplaces
  - type/rest-api
related:
  - "Карта офиса - REST API. Обзор"
  - "Карта офиса - REST API. Бронирования"
---

# Карта офиса - REST API. Служебные методы

**Модуль:** [[Module - Карта офиса + Бронирование]]

## Описание

Служебные REST-методы модуля для AI-агентов и интеграций: контекст пользователя, машиночитаемая схема API и пакетный вызов методов.

## Ключевые функции

### workplaces.currentUser
- **HTTP:** GET
- **Кто может вызывать:** авторизованный пользователь
- **Параметры:** нет
- **Возвращает:** `id`, `login`, `name`, `isSystemAdmin`, `isAdmin`, `isSecretary`, `offices[]` с `role` (admin|secretary|user)
- **Ошибки:** `UNAUTHORIZED`, `INTERNAL_ERROR`
- **Примечание:** метод `workplaces.me` удалён

### workplaces.schema
- **HTTP:** GET
- **Кто может вызывать:** авторизованный пользователь
- **Параметры:** нет
- **Возвращает:** `scope`, `prefix`, `batchMaxCalls`, `methods[]` (method, http, controller, action)
- **Ошибки:** `UNAUTHORIZED`, `INTERNAL_ERROR`

### workplaces.batch
- **HTTP:** POST
- **Кто может вызывать:** авторизованный пользователь
- **Параметры:** `calls` (обяз.) — массив `[{ method, params }]`, до 50 вызовов
- **Возвращает:** массив ответов `ApiResponse`
- **Ошибки:** `BATCH_LIMIT_EXCEEDED` (> 50), `BATCH_NESTED_NOT_ALLOWED` (вложенный batch), `BATCH_INVALID_CALL`, `METHOD_NOT_FOUND`
- **Правила:**
  - В `calls[].method` указывайте полное имя: `workplaces.city.list`
  - Параметры в `calls[].params`
  - Запрос только POST с JSON
  - Вложенный `workplaces.batch` → `BATCH_NESTED_NOT_ALLOWED`
  - Несуществующий метод → `METHOD_NOT_FOUND`
  - Более 50 вызовов → `BATCH_LIMIT_EXCEEDED`
  - Ошибка одного call не отменяет остальные

## Предусловия

- Модуль «Карта офиса + Бронирование» версии 8.0.0+
- Scope `workplaces` у вебхука
- Авторизованный пользователь

## Граничные случаи

- `workplaces.me` устарел и не поддерживается; используйте `workplaces.currentUser`
- В batch максимум 50 вызовов за запрос
- Вложенный batch запрещён
- Ошибка в одном вызове batch не влияет на остальные

## Связанные документы

- [[Module - Карта офиса + Бронирование]]
- [[Карта офиса - REST API. Обзор]]
- [[Карта офиса - REST API. Бронирования]]
