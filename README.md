<p align="center">
<img src="https://pc.woozooo.com/img/logo2.gif" width="200">
</p>

<h1 align="center">- 蓝奏云API -</h1>

<p align="center">
<img src="https://img.shields.io/github/v/release/zaxtyson/LanZouCloud-API.svg?logo=iCloud">
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

# API 文档
 API 文档请查看 [wiki](https://github.com/zaxtyson/LanZouCloud-API/wiki) 页面

# `2.3.3` 更新说明
- 修复上传超过 1GB 的文件时，前 10 个分卷丢失的 Bug [#7](https://github.com/zaxtyson/LanZouCloud-CMD/issues/7)

# `2.3.2` 更新说明
- 修复了文件无法上传的 Bug
- 解除了官方对文件名包含多个后缀的限制
- 允许使用 cookie 登录

# `2.3.1` 更新说明
- 开放了对 `is_file_url()` 和 `is_folder_url()` 两个函数的调用
- 修复了文件夹深度达到 4 层时 `get_full_path()` 报错的问题
- `mkdir()` 创建文件夹时会检查是否有同名文件夹，有的话加上 `_` 后缀
- `get_folder_id_list()` 返回的文件夹中加入了根目录信息 `{LanZouCloud: -1}` 

# `2.3.0` 更新说明
- 重新封装了 `_get()`、`_post()`方法，防止弱网环境炸出一堆网络异常导致程序崩溃

- 文件的上传时间统一为 `%Y-%m-d` 格式，不再使用蓝奏云显示的 `N小时前`、`N天前`、`前天` 之类词语

- 变更的函数
    - `get_dir_list()` 返回的信息增多，格式 `dict` -> `list`
    - `get_file_list()` 返回的信息增多，格式 `dict` -> `list`
    - `get_share_info()` 返回的信息增多
    - `list_recovery()` 被移除
    - `rename_dir()` 功能减少，仅用作重命名文件夹

 - 更名的函数
    - `get_file_list2()` -> `get_file_id_list()`
    - `get_dir_list2()` -> `get_dir_id_list()`
    - `get_direct_url()` -> `get_durl_by_url()`
    - `get_direct_url2()` -> `get_durl_by_id()`
    - `download_file()` -> `down_file_by_url()`
    - `download_file2()` -> `down_file_by_id()`
    - `set_share_passwd()` -> `set_passwd()`
    - `clean_recovery()` -> `clean_rec()`

- 新增的函数
    - `get_rec_dir_list()` 获取回收站文件夹信息列表
    - `get_rec_file_list()` 获取回收站文件信息列表
    - `get_rec_all()` 获取整理后的回收站全部信息
    - `delete_rec()` 彻底删除回收站文件(夹)
    - `get_folder_id_list()` 获取全部文件夹 id 列表
    - `get_folder_info_by_url()` 获取文件夹及其文件信息
    - `get_folder_info_by_id()` 获取文件夹及其文件信息
    - `get_file_info_by_url()` 获取文件信息
    - `get_file_info_by_id()` 获取文件信息
    - `set_desc()` 设置文件(夹)描述信息
    
- 本次更新内容较多，其它诸多细节不再列举，具体变更请查看 wiki 页的 API 文档

# `v2.2.2` 更新说明
- 修复无提取码文件夹无法下载的问题
- 修复文件夹、文件链接判断不完整的问题
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