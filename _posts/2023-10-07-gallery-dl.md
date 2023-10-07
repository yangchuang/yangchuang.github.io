---
layout: post
title: macOS命令行批量下载Twitter账号的图片及视频
date: 2023-10-07 20:24:00
feature: https://static.ericsky.com/images/2023-09-17/IMG_8425.jpg
summary: 想批量下载某些Twitter账号的图片和视频，试了一些油猴脚本和浏览器插件，都是只能单个视频单张图片下载。后来在github上找到了gallery-dl这个工具，能满足我的批量下载需求。
categories: 工具分享
---

参考 [gallery-dl](https://github.com/mikf/gallery-dl)

### 1. 安装gallery-dl
```
brew install gallery-dl
```
### 2. 安装[Get cookies.txt LOCALLY](https://chromewebstore.google.com/detail/cclelndahbckbenkjhflpdbgdldlbecc) 浏览器插件

### 3. 使用[Get cookies.txt LOCALLY](https://chromewebstore.google.com/detail/cclelndahbckbenkjhflpdbgdldlbecc) 浏览器插件导出X（Twitter）的cookies
![导出cookies](/images/2023-10-07/aa68b602-3e3f-48de-b67d-69d7eac2895d.jpg)

### 4. 使用下面的命令行批量下载X账号的图片及视频
```
gallery-dl --cookies "$HOME/path/to/cookies.txt" "URL"
```
<font color=green>重复的文件会自动跳过，</font><font color=red>但没有验证是否全部下载完该账号下的图片及视频</font>
![下载](/images/2023-10-07/8043026c-cc6a-450a-8e4f-03747fca1be5.jpg)
