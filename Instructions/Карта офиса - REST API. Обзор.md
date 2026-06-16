---
title: "Карта офиса - REST API. Обзор"
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
  - "Карта офиса - REST API. Бронирования"
  - "Карта офиса - REST API. Служебные методы"
  - "Карта офиса - История версий"
---

# Карта офиса - REST API. Обзор

**Модуль:** [[Module - Карта офиса + Бронирование]]

## Описание

Справочник REST-методов модуля «Карта офиса + бронирование рабочих мест» для интеграций, входящих вебхуков и AI-агентов. Всего 44 метода: структура офиса (city, office, room — 18 методов), рабочие места (7 методов), бронирования (11 методов), настройки и доступ (7 методов), служебные/AI (3 метода).

## Ключевые функции

### Базовый URL
- `https://{портал}/rest/{user_id}/{webhook_code}/{method}.json`
- Альтернатива: `/bitrix/services/main/ajax.php?action=ithive.workplaces.{method}`

### Scope и аутентификация
- Scope: `workplaces`
- Аутентификация: входящий вебхук Bitrix24 или сессия авторизованного пользователя
- Почти все методы требуют авторизации

### Формат ответа
- Внутренний конверт модуля: `result`, `total`, `next`, `error`
- При успехе: `error` = `null`, данные в `result.result`
- При ошибке: `error` = `{ code, message, details }`

### Коды ошибок
- **Общие:** `UNAUTHORIZED`, `ACCESS_DENIED`, `VALIDATION_ERROR`, `INTERNAL_ERROR`, `NOT_FOUND`, `INVALID_LIMIT`, `INVALID_OFFSET`, `INVALID_FILTER`, `INVALID_FILTER_OPERATOR`, `FETCH_ALL_LIMIT_EXCEEDED`
- **Структура офиса:** `CITY_HAS_OFFICES`, `OFFICE_HAS_CHILDREN`, `OFFICE_HAS_WORKPLACES`, `ROOM_HAS_WORKPLACES`, `INVALID_SVG`, `FILE_TOO_LARGE`
- **Рабочие места:** `WORKPLACE_NOT_FOUND`, `USER_NOT_FOUND`
- **Бронирования:** `RESERVATION_NOT_FOUND`, `RESERVATION_CONFLICT`, `LIMIT_EXCEEDED`, `INVALID_DATE_RANGE`, `INVALID_CANCEL_TYPE`
- **Batch:** `BATCH_LIMIT_EXCEEDED`, `BATCH_NESTED_NOT_ALLOWED`, `BATCH_INVALID_CALL`, `METHOD_NOT_FOUND`

### Пагинация (list-методы)
- `limit` — по умолчанию 50, максимум 500
- `offset` — по умолчанию 0
- `fetchAll` — все страницы; лимит из `rest_fetch_all_max` (по умолчанию 5000)

### Фильтрация
- Параметр `filter` — объект в стиле MongoDB
- Операторы: `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$nin`
- В POST — JSON в теле; в GET — JSON-строка в query

### Формат дат
- В `reservation.add/update`: `Y-m-d H:i:s`, `Y-m-d H:i`, `d.m.Y H:i:s`, `d.m.Y H:i`
- В ответе API: `Y-m-d H:i:s`
- В Mongo filter: рекомендуется `d.m.Y H:i:s`

### Иерархия структуры офиса
Город (depth 1) → офис (2) → комната (3) → рабочие места (элементы инфоблока)

## Предусловия

- Установленный модуль «Карта офиса + Бронирование» версии 8.0.0+
- Входящий вебхук Bitrix24 с scope `workplaces`
- Права в модуле «Карта офиса» для выполнения методов

## Связанные документы

- [[Module - Карта офиса + Бронирование]]
- [[Карта офиса - REST API. Бронирования]]
- [[Карта офиса - REST API. Служебные методы]]
- [[Карта офиса - История версий]]
