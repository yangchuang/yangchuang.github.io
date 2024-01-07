---
layout: post
title: Password, Session, Cookie, Token, JWT, SSO, OAuth - 认证机制深度解析 - 第2部分[译]
date: 2024-01-05 10:24:00
feature: https://static.ericsky.com/images/2023-09-17/IMG_8425.jpg
summary: Password, Session, Cookie, Token, JWT, SSO, OAuth - 认证机制深度解析 - 第2部分。
categories: translates
---

原文：[Password, Session, Cookie, Token, JWT, SSO, OAuth - Authentication Explained - Part 2](https://blog.bytebytego.com/p/password-session-cookie-token-jwt-ec1)

作者：Alex Xu

# 无需密码的身份验证

到现在为止，我们已经研究了三种身份验证方式：HTTP基础验证、session-cookie验证和基于token的验证。所有这些方式都需要一个密码。然而，我们还有其它方法可以在不需要密码的情况下证明身份。

提到身份验证，我们要考虑到三方面的因素：

- 知识因素：你知道的东西，例如密码
- 所有权因素：你拥有的东西，例如设备或电话号码
- 内在因素：你特有的东西，例如你的生物特征

密码是属于“你知道的东西”类别。一次性密码（OTP）证明用户拥有一个手机或设备，而生物特征验证则证明了“你独有的东西”。

## 一次性密码（OTP）

一次性密码（OTP）被广泛应用为更安全的身份验证方式。与静态密码（可重复使用）不同, OTP仅在有限的时间内有效, 通常只有几分钟。也就是说, 即使有人窃取了OTP，他们也无法在之后使用它进行登录。此外，OTP需要在验证时结合“你拥有的东西”以及“你知道的东西”。这个“你拥有的东西”可以是用户能接收到的电话号码或电子邮件地址，这增加了黑客窃取的难度。

然而，必须注意的是，使用短信作为OTP传达方式可能比其他方式更不安全。这是因为黑客可能截取或重定向短信，尤其是在用户的电话号码已经被窃取的情况下。有时，攻击者通过说服移动服务提供商把号码转移到一张新的SIM卡上，就能够接管这个电话号码。一旦攻击者掌控了这个电话号码，他们就能拦截任何通过短信发送的OTP。因此，一般建议尽可能使用其它传送方式，例如电子邮件或手机应用。

下面是一次性密码如何工作的详细说明：

步骤1：用户希望登录一个网站，会被问及用户名、电话号码或电子邮件地址。
步骤2：服务器产生一个有过期时间的OTP。
步骤3：服务器把OTP通过短信或电子邮件的方式，发送给用户的设备。
步骤4：用户在登录区域输入接收到的OTP。
步骤5-6：服务器比较产生的OTP和用户输入的OTP。如果两者相符，那么系统就允许用户登录。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb27865df-e833-47c8-9340-cba5510a90a0_1600x1069.png)

同样，我们也可以使用硬件或软件密钥来生成一次性密码，以实现多因素认证（MFA）。比如说，Google的二次认证（2FA）就使用了一个能够在每30秒生成一次新的一次性密码的软件密钥。在用户登陆的时候，他们需要输入密码以及设备上显示的即时一次性密码。这样的做法增加了一层额外的安全保障，毕竟黑客要想盗取一次性密码，必须先要能够接触到用户的设备。关于多因素认证，我们后面会再详细讲解。

## 单点登录（SSO）

单点登录，简称SSO，是一种用户认证机制，只需一套登录凭证，用户就可以登录并使用多个系统或应用。SSO极大地简化了登录流程，让用户在各个平台上的体验变得无缝衔接。

SSO主要依赖于一个重要的节点，那就是中央认证服务（CAS）服务器。以下是SSO流程的详尽分解：

- 当我们试图登录一个应用，比如Gmail，我们首先会被引导到CAS服务器。

- CAS服务器核对我们的登录信息，并生成一个准证发放票据（TGT）。这个TGT随后会以一个准证发放Cookie（TGC）的形式，保存在我们的浏览器中，这代表了我们的全局会话。

- CAS会为我们访问Gmail的行为生成一张服务票据（ST），然后带着这张ST，我们被引导回到了Gmail。

- Gmail会使用这张ST，在CAS服务器那里进行登录验证。确认无误后，我们就可以正常使用Gmail了。

当我们想要访问其他的应用，比如YouTube，流程就更为简便了：

- 由于我们在登录Gmail的时候已经得到了一个TGC，CAS服务器可以识别出我们的登录状态。

- CAS服务器会再为我们访问YouTube生成一张新的ST，这样我们就可以在不用再次输入凭证的情况下，直接使用YouTube了。

这样一来，我们就无需记住并输入多套登录信息了。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff52780c-e94e-4d80-a083-7c9cbead8b6f_1600x1473.png)

实现SSO功能，有多种协议可供选择：

- SAML（安全断言标记语言），在企业应用中广泛使用。SAML所传输的认证和授权数据，是以XML的格式呈现。
  
- OIDC（OpenID Connect），在用户应用中深受喜爱。OIDC利用JSON Web Tokens（JWT）完成认证操作，并以此为基础建立在OAuth 2.0框架之上。这方面的细节，我们将会在下一小节进行讲解。

对于新开发的应用，OIDC通常是首选。它支持各种类型的客户端，包括基于网页的、移动端，还有[基于JavaScript的客户端](https://openid.net/connect/)。

SSO提供了一种高效又安全的认证方法，只要一套凭证，就可以让用户在各种应用间畅游。这种方法通过使用复杂且唯一的密码，降低了被欺诈的风险，从而提升了安全性。同时，此举也大幅度减轻了IT部门的管理工作量。

## OAuth 2.0和OpenID Connect（OIDC）

虽然OAuth 2.0主要是一个授权框架，但它也可以和OpenID Connect（OIDC）结合起来，共同进行身份验证。OIDC实际上是建立在OAuth 2.0之上的一个身份验证层，它能实现用户身份的验证，并控制受保护资源的访问。

当使用“通过Google登录”或者类似的功能时，OAuth 2.0与OIDC携手共同简化了身份验证流程。OIDC用标准化的JSON Web Token（JWT）的格式提供用户身份数据。这个token包含了已认证用户的信息，让第三方的应用能够在无需单独注册的情况下，创建用户的个人档案。

在这个机制中，[OAuth 2.0](https://oauth.net/2/)通过发放短期token，而不使用密码，实现了“安全的授权访问”，让第三方服务在得到资源所有者的允许后，能访问受保护的资源。这样做的好处是，第三方服务无需直接处理或者存储用户的密码，提高了安全性。

下面的这张图，解释了在“通过 Google 登录”的情景中，这个协议是怎样起作用的。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75a1f3e9-7bad-410a-b059-66ccd6189f6b_1600x998.png)

举“通过Google登录”这个例子来说，OAuth 2.0定义了四个角色：

1. 资源所有者：最终的用户，他们在掌握自己的个人数据。

2. 资源服务器：托管用户个人档案的受保护资源的Google服务器。通过使用访问token，响应受保护资源的请求，确保只有获得授权的服务能获取这些数据。

3. 客户端：代表资源所有者发起请求的设备（PC或者智能手机）。这个设备代表着寻求访问用户数据的第三方应用。

4. 授权服务器：Google的授权服务器，他们负责向客户端发放token，管理资源服务器和客户端之间的token的安全流转。

为了适应不同的情况，OAuth 2.0提供了四种类型的授权：

1. 授权码授权：最完整且通用的模式，适用于大部分类型的应用程序。后续还会有更详细的解释。

2. Implicit grant：为那些仅有前端的应用而设计，比如单页应用或者手机应用。但这种方式已经不再推荐了。后续还会有更详细的解释。

3. 资源所有者密码凭证授权：用户很信任某个第三方应用，完全可以把凭证交给他们保管，比如一个值得信任的手机应用。

4. 客户端凭证授权：适用于那些没有前端的情况，比如命令行工具，或者服务器与服务器之间的沟通，无需资源所有者介入即可。

这个标准提供了多种模式，以适应不同的应用场景和需求，确保了在面对多样化的情境时，依然能灵活适应。

授权码授权是一个值得详述的例子。关于其他三种授权类型的具体规格，可以在[RFC-6749](https://www.rfc-editor.org/rfc/rfc6749)内找到。

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce0b4f94-1fae-4d70-a71e-1f82ef93220c_1600x1257.png)