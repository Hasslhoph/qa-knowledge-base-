---
title: "Карта офиса - REST API. Бронирования"
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
  - "Карта офиса - REST API. Служебные методы"
  - "Карта офиса - Бронирование рабочих мест"
---

# Карта офиса - REST API. Бронирования

**Модуль:** [[Module - Карта офиса + Бронирование]]

## Описание

REST-методы для работы с бронированиями рабочих мест: создание, получение, список, обновление, отмена, подтверждение и удаление броней.

## Ключевые функции

### workplaces.reservation.add
- **HTTP:** POST
- **Кто может вызывать:** право брони на место; за другого — администратор офиса
- **Параметры:** `workplaceId` (обяз.), `dateFrom` (обяз.), `dateTo` (обяз.), `userId`, `reservationType` (hourly|workDay|tolkRoom), `active`
- **Возвращает:** `{ id }`
- **Ошибки:** `WORKPLACE_NOT_FOUND`, `RESERVATION_CONFLICT`, `LIMIT_EXCEEDED`, `INVALID_DATE_RANGE`
- **Побочные эффекты:** уведомления; при `USE_CONFIRM=Y` — ожидание подтверждения

### workplaces.reservation.get
- **HTTP:** GET
- **Кто может вызывать:** владелец, админ или секретарь офиса
- **Параметры:** `id` (обяз.)
- **Возвращает:** объект брони: `id`, `userId`, `workplaceId`, `dateFrom`, `dateTo`, `active`, `typeOfReservationId`, `reservationType`, `dateConfirmed`, `dateCanceled`, `cancelTypeId`, `createdBy`, `workplaceName`

### workplaces.reservation.list
- **HTTP:** GET
- **Кто может вызывать:** владелец, админ или секретарь офиса
- **Параметры:** `limit`, `offset`, `fetchAll`, `filter` (Mongo), `workplaceId`, `userId`, `officeId`, `dateRangeFrom`, `dateRangeTo`, `status`
- **Ярлыки:** `workplaceId`, `userId`, `officeId`, `dateRangeFrom`, `dateRangeTo`, `status` (confirmed|pending|cancelled)
- **Фильтр (Mongo):** `DATE_FROM`, `DATE_TO`, `STATUS` (confirmed|pending|cancelled), `WORKPLACE_ID`, `USER_ID`
- **Ошибки:** `INVALID_FILTER` (неизвестное поле), `VALIDATION_ERROR` (неверный статус)

### workplaces.reservation.update
- **HTTP:** POST
- **Кто может вызывать:** владелец; за другого — секретарь/админ
- **Параметры:** `id` (обяз.), `workplaceId`, `userId`, `dateFrom`, `dateTo`, `reservationType`, `active`
- **Примечание:** при подтверждённой брони `dateFrom` не меняется
- **Ошибки:** `RESERVATION_CONFLICT`, `LIMIT_EXCEEDED`, `INVALID_DATE_RANGE`

### workplaces.reservation.cancel
- **HTTP:** POST
- **Кто может вызывать:** владелец или секретарь офиса
- **Параметры:** `id` (обяз.), `cancelType` (employee|manager|unlimited|auto), `type` (синоним cancelType), `reasonId`, `otherReason`
- **Побочные эффекты:** смена статуса брони, запись причины отмены
- **Ошибки:** `INVALID_CANCEL_TYPE`

### workplaces.reservation.confirm
- **HTTP:** POST
- **Кто может вызывать:** только владелец брони
- **Параметры:** `id` (обяз.)
- **Побочные эффекты:** запись `UF_DATE_CONFIRMATION`

### workplaces.reservation.confirm.status
- **HTTP:** GET
- **Кто может вызывать:** авторизованный пользователь с доступом к брони
- **Параметры:** `id` (обяз.)
- **Возвращает:** `reservationId`, `isConfirmed`, `isInValidConfirmationPeriod`, `canCancel`

### workplaces.reservation.delete
- **HTTP:** POST
- **Кто может вызывать:** админ офиса или администратор портала
- **Параметры:** `id` (обяз.)
- **Побочные эффекты:** физическое удаление записи HL

### workplaces.reservation.cancelType.list
- **HTTP:** GET
- **Кто может вызывать:** авторизованный пользователь
- **Параметры:** нет
- **Возвращает:** массив `{ id, xmlId, value }` (employee, manager, auto)

### workplaces.employee.inOffice.list
- **HTTP:** GET
- **Кто может вызывать:** право чтения офиса
- **Параметры:** `officeId` (обяз.)
- **Возвращает:** массив сотрудников в офисе: `userId`, `name`, `workplaceId`, `reservationId`, `dateFrom`, `dateTo`
- **Условие:** активные брони (`UF_BEGIN <= now <= UF_END`)

## Предусловия

- Модуль «Карта офиса + Бронирование» версии 8.0.0+
- Scope `workplaces` у вебхука
- Соответствующие права на выполнение методов

## Граничные случаи

- При подтверждённой брони `dateFrom` не меняется через `update`
- `filter[STATUS]` в `list` принимает только `confirmed`, `pending`, `cancelled` (не `0`/`1`)
- Неверный статус → `VALIDATION_ERROR` с `details.allowed`
- Вложенный `batch` в `cancel` не поддерживается
- Типы бронирования: hourly, workDay, tolkRoom

## Связанные документы

- [[Module - Карта офиса + Бронирование]]
- [[Карта офиса - REST API. Обзор]]
- [[Карта офиса - REST API. Служебные методы]]
- [[Карта офиса - Бронирование рабочих мест]]
