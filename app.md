# App Exam

表. ユーザの体温
| idx | user_id |      measuring_date | body_temperature |   registration_date |
| --- | ------- | ------------------- | ---------------- | ------------------- |
|   1 |     111 | '22-07-01 00:00:00' |             36.5 | '22-07-15 00:00:00' |
|   2 |     111 | '22-08-01 00:00:00' |             36.5 | '22-09-15 00:00:00' |
|   3 |     111 | '22-09-01 00:00:00' |             38.5 | '22-09-15 00:00:00' |
|   4 |     222 | '22-07-01 00:00:00' |             36.5 | '22-07-15 00:00:00' |
|   5 |     222 | '22-08-01 00:00:00' |             36.5 | '22-08-15 00:00:00' |
|   6 |     222 | '22-09-01 00:00:00' |             37.5 | '22-09-15 00:00:00' |

// '22-07-01 00:00:00', 'YY-MM-DD HH24:MI:SS'


### table の作成

1. `test_user_body_temperature` DB の作成
   ```sql
   create database test;
   use test;
   ```
2. `user_body_temperature` table の作成とデータの挿入
   ```sql
   create table user_body_temperature(idx int not null auto_increment primary key, user_id int, measuring_date date, body_temperature float, registration_date date);
   insert user_body_temperature(idx, user_id, measuring_date, body_temperature, registration_date) value
   (1, 111, '22-07-01 00:00:00', 36.5, '22-07-15 00:00:00'),
   (2, 111, '22-08-01 00:00:00', 36.5, '22-09-15 00:00:00'),
   (3, 111, '22-09-01 00:00:00', 38.5, '22-09-15 00:00:00'),
   (4, 222, '22-07-01 00:00:00', 36.5, '22-07-15 00:00:00'),
   (5, 222, '22-08-01 00:00:00', 36.5, '22-08-15 00:00:00'),
   (6, 222, '22-09-01 00:00:00', 37.5, '22-09-15 00:00:00');
   ```
