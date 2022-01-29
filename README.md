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
employee_name,user_id,O,C,E,A,N,authority,insider_prob,best_response
Nishio-kun,MCN0973,44,30,11,16,23,Strong,0.42452056587254794,Warn
Yagawa-kun,NSC0622,38,35,25,33,35,Strong,0.2794394698324557,Keep
Kathleen Audrey Vargas,KAV0428,37,35,31,18,31,Strong,0.30371847399181184,Keep
Taiyaki-kun,AJM0772,44,30,36,20,25,Strong,0.3084107354132066,Keep
Nicole Maris Valentine,NMV0507,39,30,21,11,36,Strong,0.36657089568005496,Warn
Tsujinaga-kun,CMW0297,50,43,25,36,33,Strong,0.40026980184457717,Warn
Christian James Rutledge,CJR0414,44,17,26,48,24,Normal,0.19886751398813107,Keep
Keefe Darius Duran,KDD0511,43,26,24,40,26,Normal,0.2556122995901057,Keep
Shimizu-san,ABH0821,15,35,37,26,30,Normal,0.13165916782510434,Keep
Kashiwazaki-sensei,BAG0190,41,10,14,39,31,Normal,0.22103301744733617,Keep
Blake Chadwick Vaughan,BCV0304,22,23,27,39,28,Normal,0.12672646717034863,Keep
Nemo-nyan-kun,GCB0638,42,14,37,16,32,Normal,0.24365090902562292,Keep
Willa Pearl Kidd,WPK0074,42,46,24,43,32,Weak,0.3214171057746834,Keep
Aoki-kun,ITG0649,10,43,38,29,31,Weak,0.12143661681448548,Keep
Hanada-paisen,SMB0012,40,39,30,26,31,Weak,0.3176515334912968,Keep
Cassady Mercedes Bentley,CMB0645,32,30,15,20,28,Weak,0.2940818284047161,Keep
Eagan Chase Pratt,ECP0997,27,30,23,17,29,Weak,0.2417116473386921,Keep
Yakiniku-paisen,KCS0524,33,41,40,45,27,Weak,0.18206870437321598,Keep
```
