# Введение в sql

## Представление данных в SQL

Данные в SQL представлены в виде связанных таблиц

## Структура запроса SQL

- SELECT -какие поля запрашиваем
- FROM - из какой таблицы берем данные
- WHERE - условия на записи
- GROUP BY - группировка данных
- HAVING - фильтрация данных
- ORDER BY - порядок записи
- LIMIT - ограничение на количество записей

## Операторы SELECT и FROM

- Оператор SELECT отвечает за то, какие поля мы хотим получить в результате запроса.
- Оператор FROM - за то, к каким таблицам мы обращаемся
- Операторы SELECT и FROM обязательны в любом запросе
- Запрашиваемые поля после SELECT отделяются запятыми
- `SELECT *` выведет все поля таблицы
- Связка операторов SELECT DISTINCT позволяют вывести все уникальные записи (удаляет дубли)

Пример:

```sql
SELECT client_id, last_name
FROM client_base;
```

## Оператор JOIN

- Оператор JOIN позволяет объединять таблицы по совпадающему ключу
- Это необходимо, когда нужно собрать данные, распределенные по разным таблицам
- Для соединения используется конструкция

```sql
SELECT...FROM t1 JOIN t2
ON (BOOLEAN EXPRESSION);
```

### Типы оператора JOIN

- INNER JOIN - оставляет только записи обеих таблиц, удовлетворяющие условию
- LEFT JOIN - оставляет строки первой таблицы, даже если совпадения по ключу нет
- RIGHT JOIN - аналогично LEFT JOIN, но для второй таблицы
- FULL OUTER JOIN - оставляет все строки обеих таблиц, даже если совпадений по ключу нет
- CROSS JOIN - полное декартово произведение, не требуется доп условий

Пример:

```sql
SELECT client_id, last_name, transaction_id, transactoin_dt
FROM client_base
         INNER JOIN transactions
                    ON client_base.client_id = transactions.client_id;
```

## Оператор WHERE

- Оператор WHERE отвечает за то, какие условия мы накладываем на поля
- Выведены будут только поля, удовлетворяющие логическому условию оператора WHERE
- Можно использовать AND, OR

## Оператора GROUP BY

Оператор GROUP BY отвечает за группировку данных по выделенным полям
Пример:

```sql
SELECT registration_year COUNT(client_id) as client_amount
GROUP BY registation_year;
```

## Оператор HAVING

- Оператор HAVING позволяет фильтровать данные по уже сгруппированным полям
- Стобцы в условиях оператора HAVING нужно называть так, как они были названы в SELECT, даже если в SELECT их
  переименовали с помощью AS

## Оператор ORDER BY

- Оператор ORDER BY позволяет сортировать щаписи результирубщего запроса по нужным полям.
- Указывать поля после оператора ORDER BY нужно через запятую в том порядке, в котором нужна сортировка
- По умолчанию сортировка производится по возрастанию значений, для сортировки по убыванию после указанных полей нужно
  дописать команду DESC

## Оператор LIMIT

- Оператор LIMIT позволяет вручную задать количество записей в результирующем запросе
- На практике это нужно для проверки содержимого таблиц и доступа к ним. Запрос с использованием LIMIT заставит
  хранилище выгружать большие объемы

## Операторы DROP и CREATE

- Оператор CREATE позволяет создавать таблицы в базе данных
- При попытке создать уже существующую таблицу, запрос выдаст ошибку
- Оператор DROP позволяет удалять таблицы из базы данных
- При попытке удалить несуществующую таблицу, запрос выдаст ошибку
- DROP IF EXIST позволяет проверять, существует ли таблица, и если существует - удалить

## Оператор WITH

- Позволяет создавать обобщенные таблицы выражения (CTE)
- Обобщённые табличные выражения используются для создания подзапросов, которые можно использовать в более сложных
  запросов

```sql
WITH common_table AS (SELECT * FROM table...)
SELECT ... FROM common_table
```



## Задания с лекции
### Задание 1. 
Получить список товаров продавцов с датами первой и последней продажи.
```sql
SELECT user_id,
       SUM(gmv - psp_commission) as gmv_no_com
FROM fact_purchases
GROUP BY user_id
ORDER BY gmv_no_com DESC limit 10;
```

### Задание 2
Получить список товаров продавцов с датами первой и последней продажи для продавцов, которые пришли в 02.2019
```sql
SELECT dim_sellers.seller_id,
       fact_purchases.product_id,
       MIN(fact_purchases.ds) as first_purchase,
       MAX(fact_purchases.ds) as last_purchase
FROM dim_sellers
       JOIN fact_purchases
            ON dim_sellers.seller_id = fact_purchases.seller_id
WHERE DATE_TRUNC('month', dim_sellers.date_joined):: date = '2019-02-01'
GROUP BY dim_sellers.seller_id, fact_purchases.product_id
```

### Задание 3
Необходимо получить список товаров, которые были куплены минимум 10 раз за май 2019 года.
```sql
SELECT product_id
FROM fact_purchases
WHERE date_trunc('month', ds) = '01may2019'
GROUP BY product_id
HAVING count(*) >= 10
```

### Задание 4
Получить пользователей, которые сменили страну использования сервиса
```sql
SELECT user_id
FROM dim_users
GROUP BY user_id
HAVING COUNT(DISTINCT country) > 1
```

### Задание 5
Найти товары, которые наиболее часто продавались у продавцов из когорты (апрель 19)
```sql
WITH a AS (SELECT seller_id,
                  product_id,
                  COUNT(*) AS cnt
           FROM fact_purchases
           GROUP BY seller_id,
                    product_id)
SELECT DISTINCT 
ON (a.seller_id)
    a.seller_id, a.product_id
FROM a
    JOIN dim_sellers ds
ON a.seller_id = ds.seller_id
WHERE to_char(ds.ds, 'yyyy-mm') = '2019-04'
ORDER BY seller_id, cnt DESC
```