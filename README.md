# InsiderSignalingGame

## デモの起動

```
$ git clone https://github.com/melonattacker/InsiderSignalingGame.git
$ cd InsiderSignalingGame
$ make upnet
$ docker-compose up -d --build
```

## デモの利用
デモは `http://localhost:3000` から利用可能.

サンプルデータは `./data` にある.

curlを使用しても計算することができる.

```
$ curl -X POST -F file=@./data/test1.csv http://localhost:8080
```
