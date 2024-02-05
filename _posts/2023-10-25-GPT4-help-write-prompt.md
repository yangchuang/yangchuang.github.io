---
layout: post
title: 使用GPT-4帮你写高质量的Prompt
date: 2023-10-25 10:24:00
summary: 许多人由于不知道如何撰写高质量的提示（Prompt）而感到困惑，特别是要用英语表达更加困难，很难准确地表达。可以尝试让ChatGPT来帮你写，尤其是GPT-4，它生成的内容质量相当不错。
feature: https:/.ericsky.com/images/aigc/daily_poetry_logo.jpeg
categories: share
---
<a id="prompt"></a>

Prompt参考宝玉老师的推文：https://twitter.com/dotey/status/1716700422763618653

```text
现在你是一个Prompt Engineer，擅长写 GPT-4 能理解并输出高质量结果的，撰写设计Prompt时，优先考虑：
1. Chain of Thought，think step by step，Split complex tasks into simpler subtasks，Tactic: Specify the steps required to complete a task
2. Strategy: Give GPTs time to "think"
3. Tactic: Provide examples

Prompt的结构：
1. 设定一个角色，例如你是一个擅长翻译的助手
2. 设定任务目标
3. 限定输出格式，方便程序解析，例如JSON，或者特殊字符隔开的文本，没有无关信息

我将在接下来的消息中提出需要你帮助设计和撰写的Prompt。
```

### 案例

最近在上传一些航拍视频到Adobe Stock和Pond5等microstock网站。然而，给视频起标题和撰写关键字感到困扰，不知道该如何写得更好。当可以识别图片的GPT-4V发布时，想到可以利用GPT-4V来帮助我写标题和关键字。

可惜没有ChatGPT Plus账号，无法直接使用GPT-4V。所幸的是，可以通过Bing间接使用GPT-4V。

#### 1. 我自己写的prompt

```text
I'm a new Adobe contributor, please help me make an attractive title, detail description and 15 most related suitable keywords for this picture.  
Plese use comma to split keywords. Then translate the title, description and keywords to Chinese. Please output in json formart directly.  
```

<img src="/images/aigc/uploadtobing1.png"  alt="山下的乡村"/>

Bing的输出

```json
Sure, I’d be happy to help. Here’s my suggestion in JSON format:
{
  "title": "Cityscape Serenity: A Vibrant Urban Jungle Nestled in Nature's Embrace",
  "description": "This photorealistic image captures a bustling cityscape nestled against the backdrop of lush green mountains. The city, densely populated with buildings of various colors and sizes, exudes a vibrant urban energy. The low-rise buildings, predominantly residential, are bathed in the soft glow of daylight under a blue sky dotted with white clouds.",
  "keywords": "cityscape, mountains, urban jungle, residential buildings, blue sky, white clouds, greenery, nature's embrace, vibrant, bustling city, low-rise buildings, daylight, photorealistic image, urban energy, lush green mountains",
  "Chinese": {
    "title": "城市景观宁静：一个充满活力的城市丛林坐落在大自然的怀抱中",
    "description": "这张逼真的照片捕捉到了一个繁华的城市景观，背靠着郁郁葱葱的绿山。这个城市，密集的各种颜色和大小的建筑物，散发出充满活力的城市能量。低层建筑，主要是住宅，沐浴在白天的柔和光线下，蓝天上点缀着白云。",
    "keywords": "城市景观，山脉，城市丛林，住宅建筑，蓝天，白云，绿色植被，大自然的怀抱，充满活力，繁华的城市，低层建筑，白天，逼真的图像，城市能量，郁郁葱葱的绿山"
  }
}
```

<img src="/images/aigc/bingai.png"  alt="Bing识图描述"/>

#### 2. [使用GPT-4帮写prompt](#prompt)

输入：

```text
Please design and write a prompt for a new Adobe contributor. When contributor upload a picture, GPT-4 can make an attractive title, detail description and 15 most related suitable keywords for this picture. keywords are splitted by comma, including title, description and keywords Chinese translation, output the them in json format.
```

输出：

```text
Prompt:

You are an artistic assistant AI specialized in analyzing and generating descriptive context for photographs. Here is a link to an uploaded photo: "{photo_link}". Please study the photograph carefully and create an appealing title, a detailed description. Also, provide 15 keywords that are most relevant to the photo for tagging purposes. Remember, we need both the English version and its Chinese translation for each: the title, description, and the keywords. Please organize your output in a JSON format.

Example:
If given a picture of the Eiffel Tower at dusk, you could produce something like this:

{
  "title": {
    "en": "Evening Elegance at Eiffel",
    "cn": "艾菲尔在夜幕下的优雅"
  },
  "description": {
    "en": "A captivating panorama of the Eiffel Tower basking in the warm hues of a Parisian sunset. The dwindling day casts long shadows, presenting a beautiful interplay of light and structure.",
    "cn": "艾菲尔铁塔在巴黎黄昏的暖色调中沉醉的迷人全景。落日留下了长长的阴影，呈现了光线和结构之间美丽的互动。"
  },
  "keywords": {
    "en": "Eiffel Tower, Paris, sunset, evening, dusk, landmark, architecture, travel, tourism, panorama, scenic, silhouette, shadows, light, structure",
    "cn": "艾菲尔铁塔，巴黎，日落，晚上，黄昏，地标，建筑，旅行，旅游，全景，风景，剪影，阴影，光，结构"
  }
}

Please generate the title, description, and keywords for the provided photo link accordingly.
```

<img src="/images/aigc/gpt4writeprompt.png"  alt="GPT4帮写Prompt"/>

#### 3. GPT-4帮写的Prompt的效果(稍微有做修改)

输入：
```text
You are an artistic assistant AI specialized in analyzing and generating descriptive context for photographs. I will upload a photo for you. Please study the photograph carefully and create an appealing title, a detailed description. Also, provide 15 keywords that are most relevant to the photo for tagging purposes. Remember, we need both the English version and its Chinese translation for each: the title, description, and the keywords. Please organize your output in a JSON format.

Example:
If given a picture of the Eiffel Tower at dusk, you could produce something like this:

{
  "title": {
    "en": "Evening Elegance at Eiffel",
    "cn": "艾菲尔在夜幕下的优雅"
  },
  "description": {
    "en": "A captivating panorama of the Eiffel Tower basking in the warm hues of a Parisian sunset. The dwindling day casts long shadows, presenting a beautiful interplay of light and structure.",
    "cn": "艾菲尔铁塔在巴黎黄昏的暖色调中沉醉的迷人全景。落日留下了长长的阴影，呈现了光线和结构之间美丽的互动。"
  },
  "keywords": {
    "en": "Eiffel Tower, Paris, sunset, evening, dusk, landmark, architecture, travel, tourism, panorama, scenic, silhouette, shadows, light, structure",
    "cn": "艾菲尔铁塔，巴黎，日落，晚上，黄昏，地标，建筑，旅行，旅游，全景，风景，剪影，阴影，光，结构"
  }
}

Please generate the title, description, and keywords for the provided photo accordingly.

Here is the photo:
```

<img src="/images/aigc/uploadtobing.png"  alt="乡村高速"/>

输出：

```text
Here is the description for the provided photo:
{
  "title": {
    "en": "Aerial View of a Highway in the Countryside",
    "cn": "乡村高速公路的航拍视角"
  },
  "description": {
    "en": "An aerial view of a highway cutting through the lush green countryside. The highway is flanked by fields and houses, presenting a beautiful contrast of urban development and rural landscape.",
    "cn": "高速公路穿过郁郁葱葱的乡村的航拍视角。高速公路两侧是田野和房屋，呈现出城市发展和乡村景观之间的美丽对比。"
  },
  "keywords": {
    "en": "highway, countryside, aerial view, fields, houses, urban development",
    "cn": "高速公路，乡村，航拍视角，田野，房屋，城市发展"
  }
}
```

<img src="/images/aigc/bingai1.png"  alt="Bing使用GPT4写的prompt识图描述"/>

### 总结

虽然我自己写的prompt也可以达到识图起标题撰写关键字的目标，跟GPT-4帮写的prompt最终效果差不多。但很明显的GPT-4帮写的prompt更加清晰明了。