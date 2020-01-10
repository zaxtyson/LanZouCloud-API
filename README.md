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


# 注册蓝奏云
 [蓝奏云注册](https://pc.woozooo.com/account.php?action=register)

# 安装依赖
```
pip install lanzou-api
```

# 设置压缩工具
为了绕过蓝奏云对上传大文件的限制，本程序使用 RAR 分卷压缩的方式将大文件拆分成 100MB 的小块。

所以，安装依赖后还需要下载解压工具:

- Windows 平台下载项目文件中的 [`/tools/rar.exe`](https://github.com/zaxtyson/LanZouCloud-API/raw/master/tools/rar.exe)
作为解压工具，将它放到你的项目中即可

- Linux 平台使用 `sudo apt install rar` 安装解压工具，然后通过 `whereis rar` 查看可执行文件路径

- 使用 `set_rar_tool()` 设置解压工具路径，详情参考 API 文档


# API 文档

### `.login(username, passwd)`  
> 登录蓝奏云  

|参数|类型|说明|必填|
|:---:|:---:|:---:|:---:|
|username|str|用户名|Y|
|passwd|str|登录密码|Y|

示例 : 
```pydocstring
from lanzou.api import LanZouCloud

lzy = LanZouCloud()
code = lzy.login('username', 'passwd')
if code == LanZouCloud.SUCCESS:
    print('登录成功')
```

返回值 : 
- 成功返回 : `LanZouCloud.SUCCESS`
- 失败返回 : `LanZouCloud.FAILED`

---
### `.logout()`  
> 注销当前账号  

示例 : 
```pydocstring
code = lzy.logout()
if code == LanZouCloud.SUCCESS:
    print('注销成功')
```
返回值 : 
- 成功返回 : `LanZouCloud.SUCCESS`
- 失败返回 : `LanZouCloud.FAILED`

---

### `.get_dir_list(folder_id)`  
> 获取子文件夹name-id列表

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|folder_id|int|文件夹id|N|默认`-1`(根目录)|

示例 :
```pydocstring
# 列出 id 为 1037070 的文件夹的子文件夹
sub_dirs = lzy.get_dir_list(1037070)
print(sub_dirs)
```

返回值：
```pydocstring
{
    "娱乐": 1037080,
    "科幻": 1037083,
    "纪录片": 1037084,
    "游戏改": 1037085
}
```

---

### `.get_file_list(folder_id)`  
> 获取文件详细信息列表

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|folder_id|int|文件夹id|N|默认`-1`(根目录)|

示例 :
```pydocstring
file_list = lzy.get_file_list(1037070)
print(file_list)
```
注意 : 添加了伪装后缀名的文件，伪装后缀会被自动去除 

返回值 : 
```pydocstring
{
    "Valentin - A Little Story.mp3":{
        "id": 12741016,     # 文件 id
        "name": "Valentin - A Little Story.mp3",    # 文件名
        "time": "昨天15:27",      # 上传时间
        "size": "8.0 M",    # 文件大小
        "downs": 6,         # 下载次数
        "has_pwd": False, # 是否设置提取码
        "has_des": True   # 是否设置描述
    },
    "小清水亜美 - 玻璃の空.mp3":{
        "id": 12740874,
        "name": "小清水亜美 - 玻璃の空.mp3",
        "time": "昨天15:24",
        "size": "10.7 M",
        "downs": 0,
        "has_pwd": False,
        "has_des": False
    }
}
```

---

### `.get_file_list2(folder_id)`  
> 获取子文件名-id列表

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|folder_id|int|文件夹id|N|默认`-1`(根目录)|

示例 :
```pydocstring
file_list = lzy.get_file_list2(1037070)
print(file_list)
```

返回值 : 
```pydocstring
{
    "Valentin - A Little Story.mp3": 12741016,
    "小清水亜美 - 玻璃の空.mp3": 12740874
}
```

---

### `.get_full_path(folder_id)`  
> 获取文件夹的绝对路径

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|folder_id|int|文件夹id|N|默认`-1`(根目录)|

示例 : 
```pydocstring
# 路径: /视频/电影/娱乐     "娱乐"文件夹 id 为 1037080
full_path = lzy.get_full_path(1037080)
print(full_path)
```

返回值 : 
```pydocstring
{
    "LanZouCloud": -1,
    "视频": 1033205,
    "电影": 1037070,
    "娱乐": 1037080
}
```

---

### `.delete(fid, is_file=True)`  
> 把网盘的文件(夹)放到回收站

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|fid|int|文件(夹)id|Y|-|
|is_file|bool|是否为文件id|N|默认True|

示例 : 
```pydocstring
code = lzy.delete(12741016)
if code == LanZouCloud.SUCCESS:
    print('删除成功')
```

返回值 : 
- 成功返回 : `LanZouCloud.SUCCESS`
- 失败返回 : `LanZouCloud.FAILED` 

注 : 

- 无法删除**含有子文件夹的文件夹**,但含有文件的可以删除。
- 重复删除同一个 id 仍返回 : `LanZouCloud.SUCCESS`
- 删除不存在的 id 也返回 : `LanZouCloud.SUCCESS`
- 这都是蓝奏云的锅，与我无关 :(

---

### `.move_file(file_id, folder_id)`
> 移动文件到指定文件夹

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|file_id|int|文件id|Y|-|
|folder_id|int|文件夹id|N|默认`-1`(根目录)|

示例 : 
```pydocstring
# 把 id=12741016 的文件移动到 id=1037083 的文件夹
code = lzy.move_file(12741016, 1037083)
if code == LanZouCloud.SUCCESS:
    print('恢复成功')
```
返回值 : 
- 成功返回 : `LanZouCloud.SUCCESS`
- 失败返回 : `LanZouCloud.FAILED`

---

### `.upload_file(file_path, folder_id, call_back)`  
> 上传文件到网盘的指定文件夹  

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|file_path|str|本地文件路径|Y|使用绝对路径|
|folder_id|int|网盘文件夹id|N|默认`-1`(根目录)|
|call_back|func|回调函数|N|默认`None`|

返回值 : 
- 上传成功返回 : `LanZouCloud.SUCCESS` 
- 上传失败返回 : `LanZouCloud.FAILED`
- 压缩过程异常返回 : `LanZouCloud.ZIP_ERROR` 

注意 : 
- 上传一个网盘中已经存在的文件，默认执行覆盖操作
- 不支持的文件会自动添加伪装后缀名，下载时自动去除
- 大文件使用 RAR 分卷压缩，保留 5% 恢复记录
- 上传大文件会自动在网盘创建文件夹以保存分卷

回调函数 : 该函数用于跟踪上传进度  

|参数|类型|说明|
|:---:|:---:|:---:|
|file_name|str|上传文件名|
|total_size|int|文件总字节数|
|now_size|int|已上传字节数|
  

示例:
```pydocstring
# 显示上传进度条的回调函数
def show_progress(file_name, total_size, now_size):
        """显示进度条的回调函数"""
        percent = now_size / total_size
        bar_len = 40  # 进度条长总度
        bar_str = '>' * round(bar_len * percent) + '=' * round(bar_len * (1 - percent))
        print('\r{:.2f}%\t[{}] {:.1f}/{:.1f}MB | {} '.format(
            percent * 100, bar_str, now_size / 1048576, total_size / 1048576, file_name), end='')
        if total_size == now_size:
            print('')  # 下载完成换行

code = lzy.upload_file(r"D:\test\DJ Okawari - Luv Letter.mp3", -1, show_progress)
if code != LanZouCloud.SUCCESS:
    print('上传失败!')
```

结果 : 

![](./img/upload_file.gif)

---

### `.upload_dir(dir_path, folder_id, call_back)`  
> 上传一个文件夹

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|dir_path|str|本地文件夹路径|Y|使用绝对路径|
|folder_id|int|网盘文件夹id|N|默认`-1`(根目录)|
|call_back|func|回调函数|N|默认`None`|

返回值 : 同 `.upload_file()`

注意 : 上传的文件夹中，不能存在子文件夹

回调函数 : 同 `.upload_file()`

示例 :
```pydocstring
code = lzy.upload_dir(r"D:\test\music", -1, show_progress)
if code != LanZouCloud.SUCCESS:
    print('上传失败!')
```

结果 :  
![](./img/upload_dir.gif)

---
### `.is_file_url(share_url)`
> 判断分享链接是否为文件

|参数|类型|说明|必填|
|:---:|:---:|:---:|:---:|
|share_url|str|分享链接|Y|

返回值 : 是文件返回 `True`,否则返回 `False`

---
### `.is_folder_url(share_url)`
> 判断分享链接是否为文件夹

|参数|类型|说明|必填|
|:---:|:---:|:---:|:---:|
|share_url|str|分享链接|Y|

返回值 : 是文件夹返回 `True`,否则返回 `False`

---
### `.set_rar_tool(bin_path)`
> 设置 RAR 压缩工具二进制文件路径

|参数|类型|说明|必填|
|:---:|:---:|:---:|:---:|
|bin_path|str|压缩工具路径|Y|

返回值 : 
- 设置成功返回 : `LanZouCloud.SUCCESS`
- 文件不存在返回 : `LanZouCloud.ZIP_ERROR`

---

### `.download_file(share_url, pwd, save_path, call_back)`  
> 通过分享链接下载文件
  
|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|share_url|str|文件分享链接|Y|-|
|pwd|str|提取码|N|默认空|
|save_path|str|文件保存路径|N|默认当前路径|
|call_back|func|回调函数|N|默认`None`|

返回值 : 
- 链接非法返回 : `LanZouCloud.URL_INVALID`
- 文件已取消返回 : `LanZouCloud.FILE_CANCELLED`
- 全部成功返回 : `LanZouCloud.SUCCESS`
- 下载失败返回 : `LanZouCloud.FAILED`
- 缺少提取码返回 : `LanZouCloud.LACK_PASSWORD`
- 提取码错误返回 : `LanZouCloud.PASSWORD_ERROR`

示例 : 
```pydocstring
code = lzy.download_file('https://www.lanzous.com/i6qxywb', '6666', r'D:\test\download', show_progress)
if code == LanZouCloud.FAILED:
    print('失败!')
```
 
结果 :  
![](./img/download_file.gif)

---

### `.download_file2(fid, save_path, call_back)`  
> 登录用户通过id下载文件
  
|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|fid|int|文件id|Y|-|
|save_path|str|文件保存路径|N|默认当前路径|
|call_back|func|回调函数|N|默认`None`|

返回值 : 
- 成功返回 : `LanZouCloud.SUCCESS`
- 失败返回 : `LanZouCloud.FAILED`

回调函数 : 同 `.download_file()`

---

### `.download_dir(share_url, dir_pwd, save_path, call_back)`  
> 通过分享链接下载文件夹
  
|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|share_url|str|文件夹分享链接|Y|-|
|dir_pwd|str|提取码|N|默认空|
|save_path|str|文件保存路径|N|默认`./down`|
|call_back|func|回调函数|N|默认`None`|

返回值 : 
- 链接非法返回 : `LanZouCloud.URL_INVALID`
- 文件已取消返回 : `LanZouCloud.FILE_CANCELLED`
- 全部成功返回 : `LanZouCloud.SUCCESS`
- 下载失败返回 : `LanZouCloud.FAILED`
- 缺少提取码返回 : `LanZouCloud.LACK_PASSWORD`
- 提取码错误返回 : `LanZouCloud.PASSWORD_ERROR`
- 解压失败返回 : `LanZouCloud.ZIP_ERROR`

注意 :
- 不能下载多级文件夹，只会下载一个文件夹下的所有文件
- 分卷压缩文件下载完成后自动解压出原文件
- 解压异常时不会自动删除分卷文件，可尝试使用解压软件手动修复

示例 : 
```pydocstring
code = lzy.download_dir('https://www.lanzous.com/b0f142z0d/', '6666', r'D:\test\download', show_progress)
if code == LanZouCloud.LACK_PASSWORD:
    print('大人！您没给我没填提取码啊！')
elif code == LanZouCloud.PASSWORD_ERROR:
    print('我好难啊，提取码不对！')
```

结果 :  
![](./img/download_dir.gif)

---
### `.download_dir2(fid, save_path, call_back)`  
> 登录后通过id下载文件夹
  
|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|fid|int|文件夹id|Y|-|
|save_path|str|文件保存路径|N|默认`./down`|
|call_back|func|回调函数|N|默认`None`|

返回值 : 同 `.download_dir()`

示例 : 
```pydocstring
code = lzy.download_dir2(1056513, r'D:\test\download', show_progress)
if code != LanZouCloud.SUCCESS:
    print('艾玛，失败了??不可能!!')
```

---




示例 : 
```pydocstring
code = lzy.mkdir(-1, 'my_music', '音乐分享')
if code == LanZouCloud.SUCCESS:
    print('创建成功')
```

返回值 : 
- 创建成功返回 : `LanZouCloud.SUCCESS`
- 目标已存在返回 : `LanZouCloud.SUCCESS`
- 创建失败返回 : `LanZouCloud.FAILED`



---

### `.mkdir(parent_id, folder_name, description)`  
> 创建文件夹并返回 id  

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|parent_id|int|父文件夹id|Y|`-1` 表根目录|
|folder_name|str|文件夹名|Y|自动删除非法字符|
|description|str|文件夹描述|N|默认无|

示例 : 
```pydocstring
code = lzy.mkdir(-1, 'my_music', '音乐分享')
if code != LanZouCloud.MKDIR_ERROR:
    print('文件夹id:' + str(code))
```

返回值 : 
- 创建成功返回 : `文件夹ID`
- 目标已存在返回 : `文件夹ID`
- 创建失败返回 : `LanZouCloud.MKDIR_ERROR` 

注意 : 蓝奏云支持创建 **同名文件夹** ，但本方法会阻止这种操作，以防出现混淆

---

### `.rename_dir(folder_id, folder_name, description)`  
> 重命名文件夹(和描述)  

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|folder_id|int|文件夹id|N|默认`-1`(根目录)|
|folder_name|str|文件夹名|Y|非法字符自动删除|
|description|str|文件夹描述|N|默认无|

示例 : 
```pydocstring
code = lzy.rename_dir(1037070, 'soft-music', '轻音乐分享')
if code == LanZouCloud.SUCCESS:
    print('修改成功')
```

返回值 : 
- 成功返回 : `LanZouCloud.SUCCESS`
- 失败返回 : `LanZouCloud.FAILED`

---

### `.list_recovery()`  
> 列出回收站文件(夹)

示例 :
```pydocstring
deleted_files = lzy.list_recovery()
print(deleted_files)
```

返回值 :
```pydocstring
{
    "folder_list": {
        "杂物": "1037324",
        "相册": "1037324"
    },
    "file_list": {
        "java模拟器.zip": "1037324",
        "Valentin - A Little Story.mp3": "12741016",
        "小清水亜美 - 玻璃の空.mp3": "12740874"
    }
}
```

---

### `.recovery(fid, is_file=True)`  
> 从回收站恢复文件（夹）

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|fid|int|文件(夹)id|Y|-|
|is_file|bool|是否为文件id|N|默认True|

示例 : 
```pydocstring
code = lzy.recovery(12741016)
if code == LanZouCloud.SUCCESS:
    print('恢复成功')
```

返回值 : 
- 成功返回 : `LanZouCloud.SUCCESS`
- 失败返回 : `LanZouCloud.FAILED`

---

### `.clean_recycle()`  
> 清空回收站

示例 :
```pydocstring
code = lzy.clean_recycle()
if code == LanZouCloud.SUCCESS:
    print('清空成功')
```

返回值 : 
- 成功返回 : `LanZouCloud.SUCCESS`
- 失败返回 : `LanZouCloud.FAILED`

---

### `.get_share_info(fid, is_file=True)`  
> 获取文件(夹)分享信息

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|fid|int|文件(夹)id|Y|-|
|is_file|bool|是否为文件id|N|默认True|

示例 :
```pydocstring
info = lzy.get_share_info(1033203)

if info['code'] == LanZouCloud.SUCCESS:
    print('分享链接:' + info['share_url'])
```

返回值 : 
```pydocstring
{
    "code": 0,      # 状态码
    "share_url": "https://www.lanzous.com/i6q0fli",    # 分享链接
    "passwd": "6666"          # 提取码
}
```

状态码 code:  
- 获取成功 : `LanZouCloud.SUCCESS`
- 获取失败 : `LanZouCloud.FAILED`
- fid参数错误 : `LanZouCloud.ID_ERROR`

---

### `.set_share_passwd(fid, passwd, is_file=True)`  
> 设置文件(夹)分享密码

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|fid|int|文件(夹)id|Y|-|
|passwd|str|分享密码|N|2-6个字符,默认空(无密码)|
|is_file|bool|是否为文件id|N|默认True|

示例 :
```pydocstring
code = lzy.set_share_info(1033203, 'fuck')
if code == LanZouCloud.SUCCESS:
    print('设置成功')
```

返回值 : 
- 成功返回 : `LanZouCloud.SUCCESS`
- 失败返回 : `LanZouCloud.FAILED` 

---

### `.get_direct_url(share_url, pwd)`  
> 获取文件下载直链

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|share_url|str|文件分享链接|Y|-|
|pwd|str|提取码|N|默认空|

示例 :
```pydocstring
info = lzy.get_direct_url('https://www.lanzous.com/i6qxywb', '6666')

if info['code'] == LanZouCloud.SUCCESS:
    print('直链地址:' + info['direct_url'])
elif info['code'] == LanZouCloud.LACK_PASSWD:
    print('缺少提取码')
```

返回值 : 
```pydocstring
{
    "code": 0,
    "name": "Git-2.23.0-64-bit.exe",
    "direct_url": "https://development5.baidupan.com/100420bb/2019/10/03/41c4117570de8c0ce02d7e7ddc838135.mp3?st=o22S3uwv063cbklsDWh50w&e=1570193627&b=CAwBYFA8UzNXbAclADkAagN2WisNLAVCUSIBQFM9B3FTdQ5iUDVYfVVTVHYEOwF3VXkAcgFtA3VSMg_c_c&fi=12741016&up="
}
```
状态码 code :  
- 获取成功 : `LanZouCloud.SUCCESS`
- 分享链接非法 : `LanZouCloud.URL_INVALID`
- 缺少提取码 : `LanZouCloud.LACK_PASSWORD`
- 提取码错误 : `LanZouCloud.PASSWORD_ERROR`
- 文件已取消 : `LanZouCloud.FILE_CANCELLED`

注意 : 
- 本方法会检查分享链接合法性
- 直链有效期约 30 分钟

---
### `.get_direct_url2(fid)`  
> 登录后通过id获取文件下载直链

|参数|类型|说明|必填|备注|  
|:---:|:---:|:---:|:---:|:---:|
|fid|int|文件id|Y|-|

返回值 :  同 `.get_direct_url()`

