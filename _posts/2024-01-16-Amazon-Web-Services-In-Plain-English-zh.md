---
layout: post
title: Amazon 云服务（Amazon Web Services）浅显易懂的解释
date: 2024-01-16 10:24:00
feature: https://static.ericsky.com/images/translates/AWS-In-Plain-Text.jpeg
summary: Amazon 云服务（Amazon Web Services）浅显易懂的解释
categories: study
---

嘿，你有听说过Amazon 云服务下的新产品：ContainerCache、ElastiCast和QR72吗？你当然不会听说过，因为它们是我刚刚编的😄。

但面对Amazon 50多个名称晦涩难懂的服务，我们决定真的不能再忍了，需要用一些通俗的语言来解释一下。

## 运行应用服务

无论你如何使用 AWS，你可能都会用到这些服务，因为它们是所有其他服务的交互点。

### EC2(Elastic Compute Cloud)

**更贴切的名字**  Amazon 虚拟服务器  
**用途是**  托管你视为电脑的那些部分。  
**类似于**  这听起来有点模糊，但 EC2 实例类似于你在 Linode、DigitalOcean 或 Rackspace 上使用的虚拟私有服务器。  

### IAM(Identity and Access Management)

**更贴切的名字**  用户、密钥和证书  
**用途是**  添加新用户，创建新的 AWS 密钥和策略。  

### S3(Simple Storage Service)

**更贴切的名字**  Amazon 无限 FTP 服务器  
**用途是**  存储网站的图片和其他资源，备份和在各服务间共享文件，托管静态网站。另外，许多其它 AWS 服务也会在 S3 中读写数据。[通俗易懂的 S3](https://expeditedsecurity.com/aws-in-plain-english/s3)  

### VPC(Virtual Private Cloud)

**更贴切的名字**  Amazon 虚拟租用机架  
**用途是**  通过增加额外的安全层，来打消 "所有数据都在互联网上！" 的顾虑。它让你所有的 AWS 服务看起来如同在同一个小网络上，而不是互联网的一小部分。  
**类似于**  如果你懂计算机网络：和 VLAN 是类似的。  

### Lambda

**更贴切的名字**  AWS 应用脚本  
**用途是**  运行小型的、自包含的 JS、Java 或 Python 脚本来完成特定任务。它既是队列又是执行的集合，用于存储然后执行你的 AWS 设置的变更，或响应 S3 或 DynamoDB 的事件。 [通俗易懂的 Lambda](https://expeditedsecurity.com/aws-in-plain-english/lambda)  

## 网页开发者服务

如果你正在搭建一个网页应用，那么主要可能会用到以下这些服务。这些与你在Heroku的插件市场里所能找到的很相似。

### API Gateway

**更贴切的名字**  API 代理  
**用途是**  让你的应用API经过此处代理，这样就可以限制不良的客户端流量，试验新的版本，且更直观地展示各种方法。  
**类似于**  3Scale  

### RDS(Relational Database Service)

**更贴切的名字**  Amazon SQL  
**用途是**  作为你的应用的Mysql、Postgres及Oracle数据库。  
**类似于**  Heroku Postgres  

### Route53

**更贴切的名字**  Amazon DNS + 域名  
**用途是**  购买新的域名并为该域名设置DNS记录。  
**类似于**  DNSimple, GoDaddy, Gandi  

### SES(Simple Email Service)

**更贴切的名字**  Amazon 的事务性邮件  
**用途是**  发送一次性的邮件，如重设密码、通知等。如果你自己写了所有的代码的话，你或许可以使用它发送通讯，不过这个想法并不是特别好。  
**类似于**  SendGrid, Mandrill, Postmark  

### CloudFront

**更贴切的名字**  Amazon CDN  
**用途是**  通过让静态文件的分发更接近你的用户，从而让你的网站加载得更快。  
**类似于**  MaxCDN, Akamai  

### CloudSearch

**更贴切的名字**  Amazon 全文搜索  
**用途是**  浏览在S3或RDS上的数据，并查找‘Jimmy’的每一个实例。  
**类似于**  Sphinx, Solr, ElasticSearch  

### DynamoDB

**更贴切的名字**  Amazon NoSQL  
**用途是**  作为你的应用的无差别存储的大规模可缩放的键-值存储。  
**类似于**  MongoLab  

### Elasticache

**更贴切的名字**  Amazon Memcached  
**用途是**  充任你的应用的 Memcached 或 Redis。  
**类似于**  Redis to Go, Memcachier  

### Elastic Transcoder

**更贴切的名字**  Amazon 初级剪辑  
**用途是**  解决视频格式的问题（如转换格式、压缩等）。  

### SQS(Simple Queue Service)

**更贴切的名字**  Amazon 队列  
**用途是**  在队列里存储未来需处理的数据。此处的"消息"指的是需保存的数据，跟电子邮件或者短信没关系。SQS 只是一个存取数据的地方，而没有其他功能。  
**类似于**  RabbitMQ, Sidekiq  

### WAF(Web Application Firewall)

**更贴切的名字**  AWS 防火墙  
**用途是**  屏蔽对Cloudfront保护的网站的恶意请求（也就是阻止黑客对/wp-admin试验10000个密码的行为）。  
**类似于**  Sophos, Kapersky  

## 移动应用开发者服务

以下服务是专门为移动应用开发者设计的。

### Cognito

**更贴切的名字**  Amazon 的OAuth服务  
**用途是**  让用户（非AWS用户）能通过如Google、Facebook等账号进行登录。  
**类似于**  OAuth.io  

### Device Farm

**更贴切的名字**  Amazon 的旧Android设备储藏室  
**用途是**  同时在多款iOS和Android设备上进行应用测试。  
**类似于**  MobileTest、iOS模拟器  

### Mobile Analytics

**更贴切的名字**  符合实际，Amazon 产品经理应该注意一下  
**用途是**  跟踪用户在你的应用内部都做了些什么。  
**类似于**  Flurry  

### SNS(Simple Notification Service)

**更贴切的名字**  Amazon 信使（Messenger）  
**用途是**  发送移动通知、电子邮件或者SMS短信。  
**类似于**  UrbanAirship, Twilio  

## 运营和代码部署服务

以下服务主要帮助你自动化操作和部署代码到其他服务器上。

### CodeCommit

**更贴切的名字**  Amazon 版Github  
**用途是**  对你的代码进行版本管理 - 托管在Git上。  
**类似于**  Github、BitBucket  

### Code Deploy

**更贴切的名字**  (这个名字OK)  
**用途是**  以合理的方式从你的 CodeCommit 仓库（或Github）将代码部署到多个 EC2 实例上。  
**类似于**  Heroku、Capistrano  

### CodePipeline

**更贴切的名字**  Amazon 的持续集成服务  
**用途是**  对代码进行自动化测试，然后根据测试结果进行相应处理。  
**类似于**  CircleCI、Travis  

### ECS(Elastic Container Service)

**更贴切的名字**  Amazon 的Docker服务  
**用途是**  把Docker文件放入EC2实例，然后就可以运行网站了。  

### Elastic Beanstalk

**更贴切的名字**  Amazon 的服务平台  
**用途是**  当你的应用在Heroku上的开销过大时，可以将其搬迁至AWS。  
**类似于**  Heroku、BlueMix、Modulus  

## 企业/公司级服务

专为企业和网络提供的服务。

### AppStream

**更贴切的名字**  Amazon Citrix  
**用途是**  将应用程序的副本放在一个远程访问的 Windows 服务器上。  
**类似于**  Citrix、RDP  

### Direct Connect

**更贴切的名字**  直连服务  
**用途是**  付费给你的电信运营商和AWS，从你的数据中心或网络获得一条直达 AWS 的专属线路。对于数据流量，这比公网更为经济。  
**类似于**  宛如一条绕过拥堵的收费高速公路。  

### Directory Service

**更贴切的名字**  目录服务  
**用途是**  将所有需要 Microsoft Active Directory 操控的应用集成在一起。  

### WorkDocs

**更贴切的名字**  Amazon 无结构文件存储  
**用途是**  与同事共享 Word 文档。  
**类似于**  Dropbox，DataAnywhere  

### WorkMail

**更贴切的名字**  Amazon 公司邮箱服务  
**用途是**  赋予公司所有员工统一的邮箱系统和日历。  
**类似于**  Google Apps for Domains  

### Workspaces

**更贴切的名字**  Amazon 远程计算机  
**用途是**  获得一个可以远程控制的标准 Windows 桌面。  

### Service Catalog

**更贴切的名字**  Amazon 预设  
**用途是**  让你的团队中的其他 AWS 用户访问你已经建立的应用，这样他们就无需阅读复杂的指南了。  

### Storage Gateway

**更贴切的名字**  将其伪装为你公司网络的S3  
**用途是**  不再需要购买额外的存储空间用于保存Word文档。让从你的公司网络将文件自动迁移到S3变得更加简单。  

## 大数据服务

提供摄取、处理和调整数据以达到你的要求的服务。

### Data Pipeline

**更贴切的名字**  Amazon ETL  
**用途是**  从AWS的其他部分提取、转化和加载数据。你可以设定执行的时间，并在执行失败时接收警报。  

### Elastic Map Reduce

**更贴切的名字**  Amazon Hadooper  
**用途是**  对保存在S3的大量原始数据文本文件进行迭代处理。  
**类似于**  Treasure Data  

### Glacier

**更贴切的名字**  运行速度缓慢的Amazon S3  
**用途是**  对存储在S3上的备份数据进行备份。注意，如果匆忙取出数据，可能会产生较高的成本。适合长期存档。  

### Kinesis

**更贴切的名字**  Amazon 高吞吐量  
**用途是**  快速摄取大量数据（例如分析数据，或者是人们转发Kanye的推文等），然后使用其他的AWS服务进行分析。  
**类似于**  Kafka  

### RedShift

**更贴切的名字**  Amazon 数据仓库  
**用途是**  存储大量的分析数据，进行一些处理，然后将其数据清空。  

### Machine Learning

**更贴切的名字**  Skynet  
**用途是**  根据现有的数据预测未来的行为，例如欺诈检测，或者是“购买x的人也买了y”。  

### SWF(Simple Workflow Service)

**更贴切的名字**  Amazon EC2队列  
**用途是**  在EC2的基础上建立一个由“deciders”和“workers”组成的服务以完成特定任务。与SQS不同的是，它在服务内建立逻辑来确定什么应该发生以及如何发生。  
**类似于**  IronWorker  

### Snowball

**更贴切的名字**  AWS超大型便携式存储  
**用途是**  获得一堆可以链接到你网络的硬盘驱动器，让（TB级别的）大量数据在AWS之间的传输更加简易。  
**类似于**  将网络连接存储设备发送至AWS  

## Amazon 云服务管理工具

因为Amazon 云服务的管理有时候会复杂难懂，所以他们创造出一套帮助你管理的服务并出售。

### CloudFormation

**更贴切的名字**  Amazon 云服务设置  
**用途是**  一次性地设置一整套互联的Amazon 云服务。  

### CloudTrail

**更贴切的名字**  Amazon 日志记录  
**用途是**  Log who is doing what in your AWS stack（如API调用等）。  

### CloudWatch

**更贴切的名字**  Amazon 状态通知器  
**用途是**  在Amazon 云服务出问题或者断开连接时，接收警告提醒。  
**类似于**  PagerDuty，Statuspage  

### Config

**更贴切的名字**  Amazon 配置管理  
**用途是**  如果你的Amazon 云服务设置较大，且有你想要追踪的变化发生，使用它可以有助于你保持理智。  

### OpsWorks

**更贴切的名字**  Amazon Chef  
**用途是**  管理像自动扩展等运行你的应用程序的事宜。  

### Trusted Advisor

**更贴切的名字**  Amazon 省钱顾问  
**主要功能是**  帮你找出在Amazon 云服务设置中哪里支付过多（例如，未使用的 EC2 实例等）。  

### Inspector

**更贴切的名字**  Amazon 审计员  
**用途是**  扫描你的Amazon 云服务设置，看你是否有不安全的配置  
**类似于**  Alert Logic  

原文地址: https://expeditedsecurity.com/aws-in-plain-english