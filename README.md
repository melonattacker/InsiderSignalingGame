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

デモ動画は[こちら](https://vimeo.com/678975412).

サンプルデータは `./data` にある.

curlを使用しても計算することができる.

```
$ curl -X POST -F file=@./data/test.csv http://localhost:8080
Nishio-kun,MCN0973,Strong,0.08941,Keep
Yagawa-kun,NSC0622,Strong,0.12183,Keep
Kathleen Audrey Vargas,KAV0428,Strong,0.65622,Warn
Taiyaki-kun,AJM0772,Strong,0.90699,Revoke
Nicole Maris Valentine,NMV0507,Strong,0.036,Keep
Tsujinaga-kun,CMW0297,Strong,0.44754,Warn
Christian James Rutledge,CJR0414,Normal,0.01017,Keep
Keefe Darius Duran,KDD0511,Normal,0.86425,Revoke
Shimizu-san,ABH0821,Normal,0.62587,Warn
Kashiwazaki-sensei,BAG0190,Normal,0.27737,Keep
Blake Chadwick Vaughan,BCV0304,Normal,0.0011,Keep
Nemo-nyan-kun,GCB0638,Normal,0.00127,Keep
Willa Pearl Kidd,WPK0074,Weak,0.96821,Warn
Aoki-kun,ITG0649,Weak,0.16046,Keep
Hanada-paisen,SMB0012,Weak,0.50539,Keep
Cassady Mercedes Bentley,CMB0645,Weak,0.17695,Keep
Eagan Chase Pratt,ECP0997,Weak,0.04616,Keep
Yakiniku-paisen,KCS0524,Weak,0.01416,Keep
```
