# docker-mysql-with-python-data-analysis-sample

## server
### コンテナの取り扱い
- 起動
  ```
  ./docker_srv/docker_run_mysql.sh
  ```
  ※ ログ情報など，起動中のメッセージを取得したい場合は，shell の -d オプションを外すこと．
- 起動中コンテナの確認
  ```
  docker ps
  ```
- コンテナの削除
  ```
  docker rm -f <CONTAINER ID>
  ```

## client
起動したコンテナは様々なアプリケーションから接続できる．
例えば，GUI アプリなら MySQL Workbench，
コマンドラインなら mysql-client，
プログラムで Python のライブラリから接続するなら `mysql.connector` がある．

アプリケーションでの接続は `docker/docker_run_with_console.sh` に記載の通り，
下記の設定で接続できる．

- ログインユーザ
  - root user で接続する場合
    ```
    user name: root
    pass: rootpass
    port: 3306
    ```
  - test user で接続する場合
    ```
    user name: testuser
    pass: testpass
    port: 3306
    ```

### MySQL Workbench での接続
MySQL Workbench をインストールして，
上記のログインユーザでログインする．

### mysql-client での接続
#### system の mysql-client を使う場合
1. 事前に mysql-client を install する
   ```
   sudo apt-get -y install mysql-client
   ```
2. 接続する
   ```
   mysql -uroot -prootpass -hlocalhost -P3306 --protocol=tcp
   ```

#### docker を使う場合
```
./docker_client/docker_run_mysql_client.sh
```
※ host ネットワークを共有するか，
`docker create network` で作成したネットワークを共有するか，
docker compose でネットワークを疎通する必要がある．
ここでは host ネットワークを共有している．

## 付録
### docker image
- [mysql - dockerhub](https://hub.docker.com/_/mysql)
### 作成工程
#### docker image と起動オプションの調整
- [Dockerでいつでも作り直せるローカルDB(mysql)作ってみた]()
- [docker run するときにUID,GIDを指定する](https://qiita.com/manabuishiirb/items/83d675afbf6b4eea90e4)
- [【Docker】コンテナ間をネットワークで連携する](https://pointsandlines.jp/server-infra/docker/container-network-link)

