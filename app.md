# App Exam

ここでは，サンプルデータに対する SQL クエリの例を示す．

## サンプルデータ

表. ユーザの体温
| idx | user_id |      measuring_date | body_temperature | heart_rate |   registration_date |
| --- | ------- | ------------------- | ---------------- | ---------- | ------------------- |
|   1 |     111 | '22-07-01 00:00:00' |             36.5 |        120 | '22-07-15 00:00:00' |
|   2 |     111 | '22-08-01 00:00:00' |             36.5 |         65 | '22-09-15 00:00:00' |
|   3 |     111 | '22-09-01 00:00:00' |             38.5 |        120 | '22-09-15 00:00:00' |
|   4 |     222 | '22-07-01 00:00:00' |             36.5 |         65 | '22-07-15 00:00:00' |
|   5 |     222 | '22-08-01 00:00:00' |             36.5 |         65 | '22-08-15 00:00:00' |
|   6 |     222 | '22-09-01 00:00:00' |             37.5 |         65 | '22-09-15 00:00:00' |
|   6 |     333 | '22-09-01 00:00:00' |             37.5 |         65 | '22-09-15 00:00:00' |
|   6 |     333 | '22-09-06 00:00:00' |             37.5 |         65 | '22-09-15 00:00:00' |

// '22-07-01 00:00:00', 'YY-MM-DD HH24:MI:SS'

### カラムの説明

- idx: インデックス
- user_id: ユーザ ID
- measuring_date: ユーザデータの測定日
- body_temperature: ユーザの体温
- registration_date: ユーザデータをデータベースに同期した日付

## table の管理

### table の作成

1. `test_user_body_temperature` DB の作成
   ```sql
   create database test;
   use test;
   ```
2. `user_body_temperature` table の作成とデータの挿入
   ```sql
   create table user_body_temperature(idx int not null auto_increment primary key, user_id int, measuring_date date, body_temperature float, heart_rate int, registration_date date);
   insert user_body_temperature(idx, user_id, measuring_date, body_temperature, heart_rate, registration_date) value
   (1, 111, '22-07-01 00:00:00', 36.5, 120, '22-07-15 00:00:00'),
   (2, 111, '22-08-01 00:00:00', 36.5,  65, '22-09-15 00:00:00'),
   (3, 111, '22-09-01 00:00:00', 38.5, 120, '22-09-15 00:00:00'),
   (4, 222, '22-07-01 00:00:00', 36.5,  65, '22-07-15 00:00:00'),
   (5, 222, '22-08-01 00:00:00', 36.5,  65, '22-08-15 00:00:00'),
   (6, 222, '22-09-01 00:00:00', 37.5,  65, '22-09-15 00:00:00'),
   (7, 333, '22-09-01 00:00:00', 37.5,  65, '22-09-15 00:00:00'),
   (8, 333, '22-09-06 00:00:00', 37.5,  65, '22-09-15 00:00:00');
   ```

### table の削除

```sql
drop table user_body_temperature;
```

## クエリ例

### 新規に追加されたレコード (最新の registration_date のレコード) を取得して，body_temperature を評価する

1. 最新の日付を取得する
   - クエリ
     ```sql
     select max(registration_date) from user_body_temperature;
     ```
   - 実行結果
     ```console
     +------------------------+
     | max(registration_date) |
     +------------------------+
     | 2022-09-15             |
     +------------------------+
     ```
2. 「1.」で取得した日付のレコード一覧を取得する
   - クエリ
     ```sql
     select * from user_body_temperature
     where registration_date = (select max(registration_date) from user_body_temperature);
     ```
   - 実行結果
     ```console
     +-----+---------+----------------+------------------+-------------------+
     | idx | user_id | measuring_date | body_temperature | registration_date |
     +-----+---------+----------------+------------------+-------------------+
     |   2 |     111 | 2022-08-01     |             36.5 | 2022-09-15        |
     |   3 |     111 | 2022-09-01     |             38.5 | 2022-09-15        |
     |   6 |     222 | 2022-09-01     |             37.5 | 2022-09-15        |
     |   7 |     333 | 2022-09-01     |             37.5 | 2022-09-15        |
     |   8 |     333 | 2022-09-06     |             37.5 | 2022-09-15        |
     +-----+---------+----------------+------------------+-------------------+
     ```
3. 「2.」で取得したクエリの内，体温が 38 ℃を超える高熱のユーザのレコードを取得する
   - クエリ
     ```sql
     select * from user_body_temperature
     where (
        registration_date = (select max(registration_date) from user_body_temperature)
        and body_temperature >= 38
     );
     ```
   - 実行結果
     ```console
     +-----+---------+----------------+------------------+-------------------+
     | idx | user_id | measuring_date | body_temperature | registration_date |
     +-----+---------+----------------+------------------+-------------------+
     |   3 |     111 | 2022-09-01     |             38.5 | 2022-09-15        |
     +-----+---------+----------------+------------------+-------------------+
     ```

### 前回値との diff

1. 最新の日付を取得する
   - クエリ
     ```sql
     select max(registration_date) from test.user_body_temperature;
     ```
   - 実行結果
     ```console
     +------------------------+
     | max(registration_date) |
     +------------------------+
     | 2022-09-15             |
     +------------------------+
     ```
2. 「1.」で取得した日付のレコード一覧を取得する
   - クエリ
     ```sql
     select * from test.user_body_temperature
     where registration_date = (select max(registration_date) from test.user_body_temperature);
     ```
   - 実行結果
     ```console
     +-----+---------+----------------+------------------+-------------------+
     | idx | user_id | measuring_date | body_temperature | registration_date |
     +-----+---------+----------------+------------------+-------------------+
     |   2 |     111 | 2022-08-01     |             36.5 | 2022-09-15        |
     |   3 |     111 | 2022-09-01     |             38.5 | 2022-09-15        |
     |   6 |     222 | 2022-09-01     |             37.5 | 2022-09-15        |
     |   7 |     333 | 2022-09-01     |             37.5 | 2022-09-15        |
     |   8 |     333 | 2022-09-06     |             37.5 | 2022-09-15        |
     +-----+---------+----------------+------------------+-------------------+
     ```
3. 最新レコードの内，各 user_id の measuring_date が「1番新しいもの」を取得する
   - クエリ
     ```sql
     select * from (
         select *, row_number() over (partition by user_id order by measuring_date desc) row_num
         from test.user_body_temperature
         where registration_date = (select max(registration_date) from test.user_body_temperature)
     ) row_num
     where row_num = 1;
     ```
     - 解説：各 user_id ごとに partition で分割してソートする．ソートしたレコードの内，1番目の物を `where row_num = 1` で指定して取得する．
     - メモ：最新の registration_date かつ，measuring_date が「2番新しいもの」や「3番新しいもの」を取得する場合は，row_num を調整する．結果がなくなるまでループを回す．
   - 実行結果
     ```console
     +-----+---------+----------------+------------------+-------------------+---------+
     | idx | user_id | measuring_date | body_temperature | registration_date | row_num |
     +-----+---------+----------------+------------------+-------------------+---------+
     |   3 |     111 | 2022-09-01     |             38.5 | 2022-09-15        |       1 |
     |   6 |     222 | 2022-09-01     |             37.5 | 2022-09-15        |       1 |
     |   8 |     333 | 2022-09-06     |             37.5 | 2022-09-15        |       1 |
     +-----+---------+----------------+------------------+-------------------+---------+
     ```
3. 最新レコードの内，各 user_id の measuring_date が「2番新しいもの」を取得する
   - クエリ
     ```sql
     select * from (
         select *, row_number() over (partition by user_id order by measuring_date desc) row_num
         from test.user_body_temperature
         where registration_date = (select max(registration_date) from test.user_body_temperature)
     ) row_num
     where row_num = 2;
     ```
   - 実行結果
     ```console
     +-----+---------+----------------+------------------+-------------------+---------+
     | idx | user_id | measuring_date | body_temperature | registration_date | row_num |
     +-----+---------+----------------+------------------+-------------------+---------+
     |   2 |     111 | 2022-08-01     |             36.5 | 2022-09-15        |       2 |
     |   7 |     333 | 2022-09-01     |             37.5 | 2022-09-15        |       2 |
     +-----+---------+----------------+------------------+-------------------+---------+
     ```
4. 「2.」と「3.」の結果を inner join する（前回値の無いものは無視する）
   - クエリ
     ```sql
     select
        user_id,
        measuring_date,
        body_temperature,
        measuring_date_prev,
        body_temperature_prev,
        registration_date
     from (
        select 
            user_id,
            measuring_date,
            body_temperature,
            registration_date
        from (
            select *, row_number() over (partition by user_id order by measuring_date desc) row_num
            from test.user_body_temperature
            where registration_date = (select max(registration_date) from test.user_body_temperature)
        ) row_num where row_num = 1
     ) lhs
     join (
        select 
            user_id as user_id_prev,
            measuring_date as measuring_date_prev,
            body_temperature as body_temperature_prev,
            registration_date as registration_date_prev
        from (
            select *, row_number() over (partition by user_id order by measuring_date desc) row_num
            from test.user_body_temperature
            where registration_date = (select max(registration_date) from test.user_body_temperature)
        ) row_num where row_num = 2
     ) rhs
     on lhs.user_id = rhs.user_id_prev;
     ```
   - 実行結果
     ```console
     +---------+----------------+------------------+---------------------+-----------------------+-------------------+
     | user_id | measuring_date | body_temperature | measuring_date_prev | body_temperature_prev | registration_date |
     +---------+----------------+------------------+---------------------+-----------------------+-------------------+
     |     111 | 2022-09-01     |             38.5 | 2022-08-01          |                  36.5 | 2022-09-15        |
     |     333 | 2022-09-06     |             37.5 | 2022-09-01          |                  37.5 | 2022-09-15        |
     +---------+----------------+------------------+---------------------+-----------------------+-------------------+
     ```
5. 前回値との差分を計算する
   - クエリ
     ```sql
     select
        user_id,
        measuring_date,
        body_temperature,
        measuring_date_prev,
        body_temperature_prev,
        (body_temperature - body_temperature_prev) as diff,
        registration_date
     from (
        select 
            user_id,
            measuring_date,
            body_temperature,
            registration_date
        from (
            select *, row_number() over (partition by user_id order by measuring_date desc) row_num
            from test.user_body_temperature
            where registration_date = (select max(registration_date) from test.user_body_temperature)
        ) row_num where row_num = 1
     ) lhs
     join (
        select 
            user_id as user_id_prev,
            measuring_date as measuring_date_prev,
            body_temperature as body_temperature_prev,
            registration_date as registration_date_prev
        from (
            select *, row_number() over (partition by user_id order by measuring_date desc) row_num
            from test.user_body_temperature
            where registration_date = (select max(registration_date) from test.user_body_temperature)
        ) row_num where row_num = 2
     ) rhs
     on lhs.user_id = rhs.user_id_prev;
     ```
   - 実行結果
     ```console
     +---------+----------------+------------------+---------------------+-----------------------+------+-------------------+
     | user_id | measuring_date | body_temperature | measuring_date_prev | body_temperature_prev | diff | registration_date |
     +---------+----------------+------------------+---------------------+-----------------------+------+-------------------+
     |     111 | 2022-09-01     |             38.5 | 2022-08-01          |                  36.5 |    2 | 2022-09-15        |
     |     333 | 2022-09-06     |             37.5 | 2022-09-01          |                  37.5 |    0 | 2022-09-15        |
     +---------+----------------+------------------+---------------------+-----------------------+------+-------------------+
     ```

### body_temperature と heart_rate の 2 つがしきい値を超える新規レコードの取得

1. 最新の日付を取得する
   - クエリ
     ```sql
     select max(registration_date) from user_body_temperature;
     ```
   - 実行結果
     ```console
     +------------------------+
     | max(registration_date) |
     +------------------------+
     | 2022-09-15             |
     +------------------------+
     ```
2. 「1.」で取得した日付のレコード一覧を取得する
   - クエリ
     ```sql
     select * from user_body_temperature
     where registration_date = (select max(registration_date) from user_body_temperature);
     ```
   - 実行結果
     ```console
     +-----+---------+----------------+------------------+------------+-------------------+
     | idx | user_id | measuring_date | body_temperature | heart_rate | registration_date |
     +-----+---------+----------------+------------------+------------+-------------------+
     |   2 |     111 | 2022-08-01     |             36.5 |         65 | 2022-09-15        |
     |   3 |     111 | 2022-09-01     |             38.5 |        120 | 2022-09-15        |
     |   6 |     222 | 2022-09-01     |             37.5 |         65 | 2022-09-15        |
     |   7 |     333 | 2022-09-01     |             37.5 |         65 | 2022-09-15        |
     |   8 |     333 | 2022-09-06     |             37.5 |         65 | 2022-09-15        |
     +-----+---------+----------------+------------------+------------+-------------------+
     ```
3. 「2.」の内，しきい値を超えた項目の数を集計する
   - クエリ
     ```sql
     select
         user_id,
         measuring_date,
         body_temperature,
         heart_rate,
         (body_temperature >= 37.0) as BT_TF,
         (heart_rate >= 120) as HR_TF,
         ((body_temperature >= 37.0) + (heart_rate >= 120)) as sum_conditions
     from (
         select * from test.user_body_temperature
         where registration_date = (select max(registration_date) from test.user_body_temperature)
     ) as ret;
     ```
   - 実行結果
     ```console
     +---------+----------------+------------------+------------+-------+-------+----------------+
     | user_id | measuring_date | body_temperature | heart_rate | BT_TF | HR_TF | sum_conditions |
     +---------+----------------+------------------+------------+-------+-------+----------------+
     |     111 | 2022-08-01     |             36.5 |         65 |     0 |     0 |              0 |
     |     111 | 2022-09-01     |             38.5 |        120 |     1 |     1 |              2 |
     |     222 | 2022-09-01     |             37.5 |         65 |     1 |     0 |              1 |
     |     333 | 2022-09-01     |             37.5 |         65 |     1 |     0 |              1 |
     |     333 | 2022-09-06     |             37.5 |         65 |     1 |     0 |              1 |
     +---------+----------------+------------------+------------+-------+-------+----------------+
     ```
4. 「3.」の内，しきい値を超えた項目を取得する
   - クエリ
     ```sql
     select * from (
         select
             user_id,
             measuring_date,
             body_temperature,
             heart_rate,
             (body_temperature >= 37.0) as BT_TF,
             (heart_rate >= 120) as HR_TF,
             ((body_temperature >= 37.0) + (heart_rate >= 120)) as sum_conditions
         from (
             select * from test.user_body_temperature
             where registration_date = (select max(registration_date) from test.user_body_temperature)
         ) as dummy1
     ) as dummy2 where sum_conditions >= 2;
     ```
   - 実行結果
     ```console
     +---------+----------------+------------------+------------+-------+-------+----------------+
     | user_id | measuring_date | body_temperature | heart_rate | BT_TF | HR_TF | sum_conditions |
     +---------+----------------+------------------+------------+-------+-------+----------------+
     |     111 | 2022-08-01     |             36.5 |         65 |     0 |     0 |              0 |
     |     111 | 2022-09-01     |             38.5 |        120 |     1 |     1 |              2 |
     |     222 | 2022-09-01     |             37.5 |         65 |     1 |     0 |              1 |
     |     333 | 2022-09-01     |             37.5 |         65 |     1 |     0 |              1 |
     |     333 | 2022-09-06     |             37.5 |         65 |     1 |     0 |              1 |
     +---------+----------------+------------------+------------+-------+-------+----------------+
     ```

## 参考文献

- [【SQL】グループごとに最大の値を持つレコードを取得する方法3選](https://takakisan.com/sql-max-in-each-group/)
