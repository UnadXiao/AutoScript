# 批处理工具集

## 目录

- [AutoStorePDB](#autostorepdb)
  - [GetGitHash](#getgithash) 获取Git提交hash值
  - [StorePdb](#storepdb) 存储pdb文件
  - [LookGUID](#lookguid) 查看exe/dll文件GUID

###AutoStorePDB

意在解决pdb找不到问题，提供一个解决思路。

#### GetGitHash

获取git最新提交的hash值，并写入文件。

#### StorePdb

将路径下的pdb文件拷贝到指定目录，同时该pdb文件名会被改写为带GUID信息。

#### LookGUID

查看当前路径下exe/dll文件的GUID。

注：只有VS编译出的文件才带有GUID信息。

