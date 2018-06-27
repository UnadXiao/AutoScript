# AutoStorePDB

#### GetGitHash

获取git最新提交的hash值，并写入文件。

#### StorePdb

将路径下的pdb文件拷贝到指定目录，同时该pdb文件名会被改写为带GUID信息。

#### LookGUID

查看当前路径下exe/dll文件的GUID。

注：只有VS编译出的文件才带有GUID信息。

### LookHash

查看文件的Hash(md5)值。python脚本

### SetProgramInfo

设置文件版本信息。python脚本

### StorePDB

将路径下的pdb文件拷贝到指定目录，同时该pdb文件名会被改写为带hash值。python脚本