---
layout: post
title: Password, Session, Cookie, Token, JWT, SSO, OAuth - 认证机制深度解析 - 第1部分[译]
date: 2024-01-04 10:24:00
feature: https://static.ericsky.com/images/2023-09-17/IMG_8425.jpg
summary: Password, Session, Cookie, Token, JWT, SSO, OAuth - 认证机制深度解析 - 第1部分。
categories: translates
---
原文：[Password, Session, Cookie, Token, JWT, SSO, OAuth - Authentication Explained - Part 1](https://blog.bytebytego.com/p/password-session-cookie-token-jwt)

作者：Alex Xu

当我们使用各种应用程序和网站时，通常有三个核心的安全步骤在持续进行：

- 身份识别
- 身份认证
- 授权许可

下面的示意图展示了这些方法在一个典型的网站架构中的应用范围以及它们的具体含义。

![](https://substack-post-media.s3.amazonaws.com/public/images/ced6562d-3be6-4dd4-a141-fed9e6b02182_1600x1226.png)

在接下来的两篇文章中，我们将深入研究各种认证方式，包括passwords、sessions、Cookies、Tokens、JWTs (JSON Web Tokens)、SSO（单点登录）以及OAuth2协议。我们会讨论每种方式所解决的问题，以及如何根据我们的需要来选择最适合的认证方式。

# 密码认证

密码认证作为一种基本且广泛使用的身份验证方式，对于网站和应用程序来说至关重要。在此方法中，用户通过输入他们独一无二的用户名和密码组合，来获取对受保护资源的访问权限。系统会把输入的凭据与存储在系统中的用户信息进行比对，一旦核对匹配，用户就会被授权进入。

尽管密码认证是一个基本的用户身份验证方式，但是它确实存在一些限制。例如，用户可能忘记密码，多个网站的用户名和密码过于复杂难以管理。此外，如果缺乏足够的安全防护措施，基于密码的系统可能会面临蛮力攻击或字典攻击等威胁。

为了解决这些问题，现代系统通常会实施一些额外的安全措施，如多因素认证，或者利用其他认证机制（例如，基于session-cookie 或 Token的认证）来增强或取代密码认证机制，以便于用户之后能对保护资源进行访问。

在接下来的这一部分，我们将首先详细介绍基于密码的认证机制，以便大家能更好地理解它的发展历程以及具体运作方式。

## HTTP Basic Access Authentication

HTTP基础访问认证是一种网络安全机制，它需要在用户访问受保护资源时提供用户名和密码。这些身份信息会通过Base64算法进行编码，然后放入HTTP的头字段*Authorization: Basic*中。

这个过程可以简单概述为以下几个步骤：

1. 客户端向服务器发送请求，试图访问某项保护资源。
2. 如果客户端第一次请求并未提供有效的身份认证，服务器会返回一个"401 未授权"的状态代码，并附带一个WWW-Authenticate: Basic的头字段，以告知客户端必须进行基础认证。
3. 客户端随后会提示用户输入用户名和密码，并以"username:password"的格式将它们整合成一串字符串。
4. 这个字符串然后会被Base64编码，放入后续请求的“Authorization: Basic”字段中，比如"Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ="。
5. 当服务器收到含有认证信息的请求后，会解码提供的Base64编码的身份信息，并提取出用户名和密码。服务器此后会将这些信息与存储在自身的用户数据库或者认证服务中的信息进行比对。
6. 如果客户端提供的身份信息与服务器进行的核对相符，服务器会授权访问被请求的资源；反之，服务器会返回"401 未授权"的状态代码。

然而，HTTP基础访问认证并非完美无缺，它存在一些明显的局限性。例如，使用Base64编码的用户名和密码能够被轻易解码。尽管现今大部分的网站会采用TLS(传输层安全协议)对浏览器和服务器间的数据进行加密以提升安全性，但用户的身份信息仍有可能面临被窃取或中间人攻击的风险。

再者，虽然在HTTP基础访问认证中，浏览器会在每次请求同一域名下的保护资源时都发送带有身份信息的Authorization头，从而避免用户反复输入用户名和密码，但由于每个网站都维护着各自独特的用户名和密码，用户可能会觉得难以记住这些信息。

综上所述，这种认证机制在现今的环境下已经相对过时，不再适用于许多现代网站。

![](https://substack-post-media.s3.amazonaws.com/public/images/10e83d0a-8fb5-42f6-abeb-a5e8980450c3_1600x1275.png)

## Session-Cookie 认证

Session-Cookie认证可以解决 HTTP 基础访问认证无法追踪用户登录状态的问题。为了追踪用户在访问期间的状态，会生成一个session ID。这个session ID 会被记录在服务器和客户的cookie中，所以它可以作为一种认证机制。之所以被称为session-cookie，是因为它是一片内部储存有session ID 的cookie。用户在首次访问时需要提供用户名和密码，之后，服务器会为用户的访问建立一个session。后续的请求会包含cookie，这样服务器就可以比较客户端和服务器端的session ID 了。

下面我们看看它是如何工作的：

1. 客户端发送请求要访问服务器上的某个受保护资源。如果客户端还未进行过认证，服务器会返回一个登录提示。此时客户端会向服务器提交他们的用户名和密码。

2. 服务器会根据自己的用户数据库或者身份验证服务核实提供的登陆凭证是否正确。如果凭证正确，服务器会生成一个唯一的session ID，并在服务器端的存储（比如，服务器内存、数据库或session服务器）中创建一个相应的session。

3. 服务器会将session ID 以cookie的形式发送给客户端，通常会设置到cookie header里。

4. 客户端会保存这个session cookie。

5. 对于后续的请求，客户端会将cookie放在request headers中一并发送。

6. 服务器会根据存储的session数据检查cookie中的session ID，以此来认证用户的身份。

7. 如果认证成功，服务器会授权用户访问请求的资源。当用户退出登录，或者到了设定的过期时间，服务器便会使这个session失效，客户端也会删除这个session cookie。

![](https://substack-post-media.s3.amazonaws.com/public/images/9b3002be-d4f2-489c-99cd-f789012d76dc_1600x1173.png)