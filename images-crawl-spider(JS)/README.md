
images-crawl-spider(JS)
---
images logo & icons, 爬虫批量下载

## 准备工作

- 使用 mongodb 创建一叫spider的数据库， redis ???
- 硬盘空间-根据实际资源的大小来确定！
- 使用`node.js`

## clone repo

```sh
git clone git@github.com:xgqfrms/spider.git
cd spider
npm i
# npm install
node crawl
```

## Note

没有处理意外中断,继续抓取下载的逻辑,可以自己改进吧.

## 自定义 base URL

var homeUrl = https://rollbar.com/docs/'
var BASE = 'https://rollbar.com'

https://rollbar.com/assets/docs/images/logos

.svg  
.png  
.gif
.jpeg
.webp

## 不同 格式图片的处理 ？？？
 
https://rollbar.com/assets/docs/images/logos/ruby.svg
https://rollbar.com/assets/docs/images/logos/php.gif
https://rollbar.com/assets/docs/images/logos/node.png
https://rollbar.com/assets/docs/images/logos/golang.png
https://rollbar.com/assets/docs/images/logos/perl.png



分析 图片资源 URL path

拼接 path
