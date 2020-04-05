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

- 本库封装了蓝奏网盘的基础功能: 登录、注销、获取文件(夹)列表、下载文件、上传文件、删除文件(夹)、
移动文件、清空回收站、恢复文件(夹)、创建文件夹、设置文件(夹)访问密码、设置文件(夹)描述

- 解决了蓝奏云的上传格式限制和单文件大小限制，同时增加了以下功能: 批量上传/下载文件、
上传/下载时断点续传、清理"幽灵"文件夹、移动文件夹、获取下载直链

- 本库一直紧跟蓝奏云官方的变动，如果发现 Bug 请提交反馈，以便尽快修复。如果有任何问题或建议，欢迎提 issue。

- 最后，维护不易，求一个 star (\*/ω＼*)

# API 文档
- `dev` 分支用于修复错误，待稳定后再推到 `master` 分支
- `master` 分支将自动发布到 PyPI，使用 `pip install lanzou-api` 即可安装
- API 文档请查看 [wiki](https://github.com/zaxtyson/LanZouCloud-API/wiki) 页面

# 更新日志

## `v2.4.4`
- 修复蓝奏云 js 含有注释导致匹配文件信息错误的问题
- 修复 `is_file_url()`、`is_folder_url()`、 `get_file_info_by_url()` 无法正确处理 VIP 用户分享页面的问题
- 修复上传大文件自动创建文件夹名包含 `mkdir` 字符串后缀的问题(这不是feature，只是测试时无意中写到代码里了－_－)

## `v2.4.3`
- 上传/下载时支持断点续传(包括大文件)
- 降低了下载大文件时出现验证码的可能性(`dwg`、`gho` 等后缀容易触发验证码)
- 调整了数据分段大小的权重，降低数据块平均大小(便于上传时断点续传)
- 修复 `get_file_info_*()` 无法获取某些文件的文件名和日期的问题
- 修复 `get_full_path()` 可能碰到无效数据导致崩溃的问题
- 新增 `clean_ghost_folders()` 用于清理网盘中的"幽灵文件夹"(不在网盘和回收站显示的文件夹,移动文件时可以看见,文件移进去就丢失)
- 新增 `set_captcha_handler()` 用于处理下载时的验证码校验
- 新增 `delete_rec_multi()` 用于批量删除文件(夹)
- 新增 `recovery_multi()` 用于批量恢复文件(夹)
- 新增 `recovery_all()` 用于恢复全部文件(夹)
 
## `v2.4.2`
- 紧急修复了蓝奏云网页端变化导致  `get_full_path()` 和 `get_dir_list()` 失效的 Bug
## `v2.4.1`
- 修复使用 URL 下载时，记录文件被误判为普通文件，导致异常截断的问题
- 修复上传小文件时没有去除文件名中非法字符的问题

## `2.4.0` 更新说明
- 放弃分段压缩，使用更复杂的方式上传大文件。分段数据文件名、文件大小、文件后缀随机，下载时自动处理。
- 放弃使用修改文件名的方式绕过上传格式限制。上传的文件末尾被添加了 512 字节的信息，储存真实文件名，
下载时自动检测并截断，不会影响文件 hash。一般情况下，不截断此信息不影响文件的使用，但纯文本类文件会受影响(比如代码文件)，
建议压缩后上传。
- API 不再返回 `dict`，减少大量使用 `result['attr']` 方式取值，而是返回 `namedtuple`，直接使用 `result.attr` 取值。
- 获取文件(夹)列表不再返回 `list`，而是返回 `FileList` 或 `FolderList` 对象，支持 `list` 的操作，同时支持 `find_by_id()`
`find_by_name()`、`filter()`、`pop_by_id()` 等方法查找和筛选数据。 `get_file_id_list()` 、
`get_dir_id_list()`  废弃，直接访问 `ListObj.name_id` 属性即可。
- `get_folders_id_name()` 、 `get_folders_name_id()` 被废弃，使用 `get_move_folders()` 获取网盘全部文件夹列表(`FolderList`对象)，
使用 `get_move_paths()` 获取网盘全部文件夹的绝对路径列表(排序好的`list`)，因此支持在不同路径下创建同名文件夹
- 上传下载大文件时隐藏更多细节，回调函数只显示一个文件。数据切片由生成器实现，边上传边切片数据，减少等待时间。下载时按顺序写入一个文件，无需再次合并。
- 批量上传下载时，使用回调函数 `failed_callback()` 即时处理失败文件，不再等待全部任务完成后返回失败列表。


## `2.3.5` 更新说明
- 修复发送请求时 `timeout` 无效的问题 [#7](https://github.com/zaxtyson/LanZouCloud-API/issues/7)
- 修复回收站文件夹中文件名过长，导致后缀丢失，程序闪退的问题 [#14](https://github.com/zaxtyson/LanZouCloud-CMD/issues/14)
- 修复回收站存在多个文件重复时，序号添加不合理的问题
- 修复官方启用滑动验证导致无法登录的问题 [#15](https://github.com/zaxtyson/LanZouCloud-CMD/issues/15)

## `2.3.4` 更新说明
- 修复了官方对 `.wtf[0-9]+.rar` 分卷后缀限制 [#11](https://github.com/zaxtyson/LanZouCloud-CMD/issues/11) [#12](https://github.com/zaxtyson/LanZouCloud-CMD/issues/12)
- 新增函数 `move_folder()` 支持移动文件夹
- 新增函数 `set_max_size()` 允许修改单个文件大小限制(会员用户) [#9](https://github.com/zaxtyson/LanZouCloud-CMD/issues/9)
- 新增函数 `rename_file()` 支持修改文件名(会员用户)
- 修复了函数 `get_rec_all()` 在某些情况下崩溃的问题
- 函数 `get_folder_id_list()` 重命名为 `get_folders_name_id()`
- 新增函数 `get_folders_id_name()` 以应对用户手动创建同名文件夹带来的问题
- 上传时不再自动删除文件名中空格, 自动转换 `\xa0`，`\u3000` 为英文空格
- 函数 `down_dir_by_url()` 、 `down_dir_by_id()` 增加参数 `mkdir=True`, 下载时自动创建子文件夹
- 修复文件日期错误 [#8](https://github.com/zaxtyson/LanZouCloud-CMD/issues/8)

## `2.3.3` 更新说明
- 修复上传超过 1GB 的文件时，前 10 个分卷丢失的 Bug [#7](https://github.com/zaxtyson/LanZouCloud-CMD/issues/7)

## `2.3.2` 更新说明
- 修复了文件无法上传的 Bug
- 解除了官方对文件名包含多个后缀的限制
- 允许使用 cookie 登录

## `2.3.1` 更新说明
- 开放了对 `is_file_url()` 和 `is_folder_url()` 两个函数的调用
- 修复了文件夹深度达到 4 层时 `get_full_path()` 报错的问题
- `mkdir()` 创建文件夹时会检查是否有同名文件夹，有的话加上 `_` 后缀
- `get_folder_id_list()` 返回的文件夹中加入了根目录信息 `{LanZouCloud: -1}` 

## `2.3.0` 更新说明
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

## `v2.2.2` 更新说明
- 修复无提取码文件夹无法下载的问题
- 修复文件夹、文件链接判断不完整的问题
- `get_dir_list()` 函数返回文件夹详细信息
- `get_dir_list2()` 函数返回文件夹"name-id"列表
- 文档转至 wiki 页面

## `v2.2.1` 更新说明
- API 发布到 PyPI ，直接使用 `pip install lanzou-api` 即可安装依赖
 
## `v2.2` 更新说明
- 修复了文件和文件夹 id 冲突的问题(导致部分 API 接口参数变化)
- 修复了蓝奏云网页变化导致文件(夹)无法下载的问题 [#4](https://github.com/zaxtyson/LanZouCloud-CMD/issues/4)
- 修复了上传 rar 分卷文件被 ban 的问题
- 修复了无后缀文件上传出错的问题
- 修复了文件中空白字符导致上传和解压失败的问题
- 修复偶尔出现的 SSL 握手错误

## `v2.1` 更新说明
- 修复了蓝奏云分享链接格式变化导致无法获取直链的问题

## `v2.0` 更新说明
- 修复了登录时 `formhash` 错误的问题
- 解决了多次上传大文件被限制的问题   [#3](https://github.com/zaxtyson/LanZouCloud-CMD/issues/3)
- 细化 API 接口的功能，某些接口被取消、更名
- 操作网盘时会进行检查，屏蔽蓝奏云不合理的设计
- 支持批量上传/下载
- 上传大文件不再直接将数据分段，改用 RAR 分卷压缩    [#2](https://github.com/zaxtyson/LanZouCloud-CMD/issues/2)
- 取消使用`种子文件`下载大文件，自动识别分卷压缩文件并解压
- 上传/下载时支持使用回调函数显示进度  [#1](https://github.com/zaxtyson/LanZouCloud-CMD/issues/1)
- 不再向上抛异常，而是返回错误码