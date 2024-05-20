# Movie Catalog

* Flaskの勉強のために、ChatGPTすべて作らせた

## ChatGPTでの作成手順

* 認証画面を経由して表示されるランディングページを作成させる
* 認証画面をリッチにするためにStyleを作らせる
* ランディングページをダッシュボードにして、画面上部にメニューを作らせて、page1~3を作らせる
* page1をmongoDBのmoviesコレクションの情報を取得し、サイドバーにタイトル、コンテンツエリアに詳細情報を表示させる。
* 以下のmoviesコレクションのスキーマと、mongoDBへのログインの仕方もいっしょに教えておく。

```
{"_id":{"$oid":"573a1390f29313caabcd42e8"},"plot":"A group of bandits stage a brazen train hold-up, only to find a determined posse hot on their heels.","genres":["Short","Western"],"runtime":{"$numberInt":"11"},"cast":["A.C. Abadie","Gilbert M. 'Broncho Billy' Anderson","George Barnes","Justus D. Barnes"],"poster":"https://m.media-amazon.com/images/M/MV5BMTU3NjE5NzYtYTYyNS00MDVmLWIwYjgtMmYwYWIxZDYyNzU2XkEyXkFqcGdeQXVyNzQzNzQxNzI@._V1_SY1000_SX677_AL_.jpg","title":"The Great Train Robbery","fullplot":"Among the earliest existing films in American cinema - notable as the first film that presented a narrative story to tell - it depicts a group of cowboy outlaws who hold up a train and rob the passengers. They are then pursued by a Sheriff's posse. Several scenes have color included - all hand tinted.","languages":["English"],"released":{"$date":{"$numberLong":"-2085523200000"}},"directors":["Edwin S. Porter"],"rated":"TV-G","awards":{"wins":{"$numberInt":"1"},"nominations":{"$numberInt":"0"},"text":"1 win."},"lastupdated":"2015-08-13 00:27:59.177000000","year":{"$numberInt":"1903"},"imdb":{"rating":{"$numberDouble":"7.4"},"votes":{"$numberInt":"9847"},"id":{"$numberInt":"439"}},"countries":["USA"],"type":"movie","tomatoes":{"viewer":{"rating":{"$numberDouble":"3.7"},"numReviews":{"$numberInt":"2559"},"meter":{"$numberInt":"75"}},"fresh":{"$numberInt":"6"},"critic":{"rating":{"$numberDouble":"7.6"},"numReviews":{"$numberInt":"6"},"meter":{"$numberInt":"100"}},"rotten":{"$numberInt":"0"},"lastUpdated":{"$date":{"$numberLong":"1439061370000"}}},"num_mflix_comments":{"$numberInt":"0"}}
```

## .env

| 設定値 | 記入内容 |
| ----- | ------- |
| SECRET_KEY | セッション符号化のためのランダムな文字列。例：4e3c9d1ab8b2d82b3f8f95d7e3a3c7e8f3e5d2b4a1e7d9a1f2a8b3c4d5e6f7a8 |
| USER_USERNAME | 認証で使うユーザー名 |
| USER_PASSWORD | 認証で使うパスワード |
| MONGODB_USERNAME | mongoDB AtlasのDB接続用ユーザー名 |
| MONGODB_PASSWORD | mongoDB AtlasのDB接続用パスワード |
