<p align="center">
<img src="https://pc.woozooo.com/img/logo2.gif" width="200">
</p>

<h1 align="center">- 蓝奏云API -</h1>

<p align="center">
<img src="https://img.shields.io/badge/version-2.2.1-blue?logo=iCloud">
<img src="https://img.shields.io/badge/support-Windows-blue?logo=Windows">
<img src="https://img.shields.io/badge/support-Linux-yellow?logo=Linux">
<img src="https://github.com/zaxtyson/LanZouCloud-API/workflows/Publish%20to%20PyPI/badge.svg">
</p>

# 简介

- 本库封装了对蓝奏云的基本操作: 登录、列出文件、下载文件、上传文件、删除文件(夹)、
清空回收站、恢复文件、创建文件夹、设置文件(夹)访问密码

- 此外，还解决了蓝奏云的上传格式限制和单文件最大 100MB 的限制，同时增加了批量上传/下载的功能。

- 如果有任何问题或建议，欢迎提 issue。
- 最后，求一个 star (≧∇≦)ﾉ

# `v2.2.2` 更新说明
- 修复下载无提取码文件夹失败的问题
- 修复文件夹、文件链接判断不全的问题
- `get_dir_list()` 函数返回文件夹详细信息
- `get_dir_list2()` 函数返回文件夹"name-id"列表
- 文档转至 wiki 页面

# `v2.2.1` 更新说明
- API 发布到 PyPI ，直接使用 `pip install lanzou-api` 即可安装依赖
 
# `v2.2` 更新说明
- 修复了文件和文件夹 id 冲突的问题(导致部分 API 接口参数变化)
- 修复了蓝奏云网页变化导致文件(夹)无法下载的问题 [#4](https://github.com/zaxtyson/LanZouCloud-CMD/issues/4)
- 修复了上传 rar 分卷文件被 ban 的问题
- 修复了无后缀文件上传出错的问题
- 修复了文件中空白字符导致上传和解压失败的问题
- 修复偶尔出现的 SSL 握手错误

# `v2.1` 更新说明
- 修复了蓝奏云分享链接格式变化导致无法获取直链的问题

# `v2.0` 更新说明
- 修复了登录时 `formhash` 错误的问题
- 解决了多次上传大文件被限制的问题   [#3](https://github.com/zaxtyson/LanZouCloud-CMD/issues/3)
- 细化 API 接口的功能，某些接口被取消、更名
- 操作网盘时会进行检查，屏蔽蓝奏云不合理的设计
- 支持批量上传/下载
- 上传大文件不再直接将数据分段，改用 RAR 分卷压缩    [#2](https://github.com/zaxtyson/LanZouCloud-CMD/issues/2)
- 取消使用`种子文件`下载大文件，自动识别分卷压缩文件并解压
- 上传/下载时支持使用回调函数显示进度  [#1](https://github.com/zaxtyson/LanZouCloud-CMD/issues/1)
- 不再向上抛异常，而是返回错误码

# API 文档请查看 wiki