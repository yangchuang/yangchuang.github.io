---
layout: post
title: 使用DALL-E3给诗词配图
date: 2023-12-03 10:24:00
summary: 写了个AI小玩具，每天随机一句古诗词，使用DALL-E3给古诗词配图。
feature: https:/.ericsky.com/images/aigc/daily_poetry_logo.jpeg
categories: share
---
## 诗画共赏

“诗画共赏”是一个展示唐诗宋词和DALL-E3 AI配图的微信小程序。每天，你可以在这里欣赏到一首精选的唐诗宋词，以及根据诗句生成的DALL-E3 AI配图。

<img src="https://static.ericsky.com/images/aigc/daily-poetry-mini-program-qr.jpg" alt="诗画共赏" width="300px"/>

### 运行截图

<table>
  <tr>
    <td><img src="/images/aigc/daily-poetry1.png" alt="诗画共赏" /></td>
    <td><img src="/images/aigc/daily-poetry2.png" alt="诗画共赏" /></td>
  </tr>
  <tr>
    <td><img src="/images/aigc/daily-poetry4.png" alt="诗画共赏" /></td>
    <td><img src="/images/aigc/daily-poetry3.png" alt="诗画共赏" /></td>
  </tr>
</table>



## 关键API

### OPENAI的[images generations](https://platform.openai.com/docs/api-reference/images/create)
```shell
curl -X POST https://ai.ericsky.com/api/openai/v1/images/generations  \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-***" \
  -d '{ "model":"dall-e-3", "prompt": "中国水墨画: 醉后不知天在水，满船清梦压星河。", "n": 1, "size": "1024x1024" }'
```

### [古诗词API](https://github.com/yangchuang/gushici)